import argparse
import cv2
import numpy as np
import torch
from torch.autograd import Function
from torchvision import models
import torch.nn as nn
import torch.nn.functional as F
import torch.backends.cudnn as cudnn

import lib.models as models
from lib.config import config, update_config
from lib.utils import utils
import pprint
import matplotlib.pyplot as plt


class FeatureExtractor():
    """ Class for extracting activations and
    registering gradients from targetted intermediate layers """

    def __init__(self, model, target_layers):
        self.model = model
        self.target_layers = target_layers
        self.gradients = []

    def save_gradient(self, grad):
        self.gradients.append(grad)

    def __call__(self, x):
        outputs = []
        self.gradients = []
        # for name, module in self.model._modules.items():
        #     x = module(x)
        #     print('name=', name)
        #     print('x.size()=', x.size())
        #
        #     if name in self.target_layers:
        #         x.register_hook(self.save_gradient)
        #         outputs += [x]
        x = self.model.conv1(x)
        x = self.model.bn1(x)
        x = self.model.relu(x)
        x = self.model.conv2(x)
        x = self.model.bn2(x)
        x = self.model.relu(x)
        x = self.model.layer1(x)

        # stage1
        # x.register_hook(self.save_gradient)
        # outputs += [x]

        x_list = []
        for i, m in enumerate(self.model.transition1):
            if m is not None:
                x_list.append(m(x))
            else:
                x_list.append(x)
        y_list = self.model.stage2(x_list)

        # stage2
        # y_list[0].register_hook(self.save_gradient)
        # y_list[1].register_hook(self.save_gradient)
        # outputs += [y_list[0]]
        # outputs += [y_list[1]]

        x_list = []
        for i, m in enumerate(self.model.transition2):
            if m is not None:
                x_list.append(m(y_list[-1]))
            else:
                x_list.append(y_list[i])
        y_list = self.model.stage3(x_list)

        # stage3
        y_list[0].register_hook(self.save_gradient)
        y_list[1].register_hook(self.save_gradient)
        y_list[2].register_hook(self.save_gradient)
        outputs += [y_list[0]]
        outputs += [y_list[1]]
        outputs += [y_list[2]]

        x_list = []
        for i, m in enumerate(self.model.transition3):
            if m is not None:
                x_list.append(m(y_list[-1]))
            else:
                x_list.append(y_list[i])
        x = self.model.stage4(x_list)

        height, width = x[0].size(2), x[0].size(3)
        x1 = F.interpolate(x[1], size=(height, width), mode='bilinear', align_corners=False)
        x2 = F.interpolate(x[2], size=(height, width), mode='bilinear', align_corners=False)
        x3 = F.interpolate(x[3], size=(height, width), mode='bilinear', align_corners=False)
        x = torch.cat([x[0], x1, x2, x3], 1)

        # se
        residual = x
        x = self.model.se(x)
        x += residual

        # stage4
        # x.register_hook(self.save_gradient)
        # outputs += [x]

        return outputs, x


class ModelOutputs():
    """ Class for making a forward pass, and getting:
    1. The network output.
    2. Activations from intermeddiate targetted layers.
    3. Gradients from intermeddiate targetted layers. """

    def __init__(self, head, model, target_layers):
        self.model = model
        self.head = head
        # self.feature_extractor = FeatureExtractor(self.model.features, target_layers)
        self.feature_extractor = FeatureExtractor(self.model, target_layers)

    def get_gradients(self):
        return self.feature_extractor.gradients

    def __call__(self, x):
        target_activations, output = self.feature_extractor(x)
        # output = output.view(output.size(0), -1)
        print('output=', output.size())

        #modify the target model
        # output = resnet.fc(output)
        # output = se_resnet50.fc(output)
        # output = self.model.output(output)

        # output = cbam_resnet50.module.fc(output)
        # output = resnet50_cbam1.fc(output)

        output = self.head(output)

        print('classfier=', output.size())
        return target_activations, output


def preprocess_image(img):
    means = [0.485, 0.456, 0.406]
    stds = [0.229, 0.224, 0.225]

    preprocessed_img = img.copy()[:, :, ::-1]
    for i in range(3):
        preprocessed_img[:, :, i] = preprocessed_img[:, :, i] - means[i]
        preprocessed_img[:, :, i] = preprocessed_img[:, :, i] / stds[i]
    preprocessed_img = \
        np.ascontiguousarray(np.transpose(preprocessed_img, (2, 0, 1)))
    preprocessed_img = torch.from_numpy(preprocessed_img)
    preprocessed_img.unsqueeze_(0)
    input = preprocessed_img.requires_grad_(True)
    return input


def show_cam_on_image(img, mask):
    heatmap = cv2.applyColorMap(np.uint8(255 * mask), cv2.COLORMAP_JET)
    heatmap = np.float32(heatmap) / 255
    cam = heatmap + np.float32(img)
    cam = cam / np.max(cam)
    cv2.imwrite("../examples/sum_cam_se4_stage3_.jpg", np.uint8(255 * cam))


class GradCam:
    def __init__(self, model, target_layer_names, use_cuda):
        self.head = model.head
        del model.head
        self.model = model
        self.model.eval()
        self.cuda = use_cuda
        if self.cuda:
            self.model = model.cuda()

        self.extractor = ModelOutputs(self.head, self.model, target_layer_names)

    def forward(self, input):
        return self.model(input)

    def __call__(self, input, index=None):
        if self.cuda:
            features, output = self.extractor(input.cuda())
        else:
            features, output = self.extractor(input)

        if index == None:
            index = np.argmax(output[0][60].cpu().data.numpy())
            # index = list()
            # for i in output[0]:
            #     index.append(i.argmax())

        one_hot = np.zeros((1, output.view(output.size(1), -1).size()[-1]), dtype=np.float32)
        one_hot[0][index] = 1

        # one_hot = np.zeros((68, output.view(output.size(1), -1).size()[-1]), dtype=np.float32)
        # for i, idx in enumerate(index):
        #     one_hot[i][idx] = 1

        one_hot = torch.from_numpy(one_hot).requires_grad_(True)
        if self.cuda:
            one_hot = torch.sum(one_hot.cuda() * output[0][60].view(1, -1))
            # one_hot = torch.sum((one_hot.cuda().data * output.view(output.size(1), -1)), 1)
            # weights0 = torch.from_numpy(np.ones(68, dtype=np.float32)).cuda()
        else:
            one_hot = torch.sum((one_hot.data * output.view(output.size(1), -1)), 1)
            # weights0 = torch.from_numpy(np.ones(68, dtype=np.float32))

        # self.model.features.zero_grad()
        # self.model.output.zero_grad()
        #
        self.model.zero_grad()
        self.head.zero_grad()
        one_hot.backward(retain_graph=True)

        # one_hot.backward(weights0, retain_graph=True)

        # stage4/stage1
        # grads_val = self.extractor.get_gradients()[-1].cpu().data.numpy()

        # stage3
        grad_stage3_x1 = F.interpolate(self.extractor.get_gradients()[1], size=(64, 64), mode='bilinear',
                                       align_corners=False)
        grad_stage3_x2 = F.interpolate(self.extractor.get_gradients()[0], size=(64, 64), mode='bilinear',
                                       align_corners=False)
        grad_stage3_x = torch.cat([self.extractor.get_gradients()[2], grad_stage3_x1, grad_stage3_x2], 1)
        grad_stage3_x = grad_stage3_x.cpu().data.numpy()

        # stage2
        # grad_stage2_x1 = F.interpolate(self.extractor.get_gradients()[0], size=(64, 64), mode='bilinear',
        #                                align_corners=False)
        # grad_stage2_x = torch.cat([self.extractor.get_gradients()[1], grad_stage2_x1], 1)
        # grad_stage2_x = grad_stage2_x.cpu().data.numpy()

        # stage4/stage1
        # target = features[-1]
        # target = target.cpu().data.numpy()[0, :]

        # stage3
        stage3_x1 = features[1]
        stage3_x2 = features[2]
        stage3_x1 = F.interpolate(stage3_x1, size=(64, 64), mode='bilinear', align_corners=False)
        stage3_x2 = F.interpolate(stage3_x2, size=(64, 64), mode='bilinear', align_corners=False)
        stage3_x = torch.cat([features[0], stage3_x1, stage3_x2], 1)

        target = stage3_x.cpu().data.numpy()[0, :]

        # stage2
        # stage2_x1 = features[1]
        #
        # stage2_x1 = F.interpolate(stage2_x1, size=(64, 64), mode='bilinear', align_corners=False)
        # stage2_x = torch.cat([features[0], stage2_x1], 1)
        #
        # target = stage2_x.cpu().data.numpy()[0, :]

        # element-wise
        # stage4/stage1
        # cam = grads_val[0] * target
        # cam = np.sum(cam, axis=0)

        # modify the target stage
        cam = grad_stage3_x[0] * target
        cam = np.sum(cam, axis=0)

        # mean
        # weights = np.mean(grads_val, axis=(2, 3))[0, :]
        # cam = np.zeros(target.shape[1:], dtype=np.float32)

        # for i, w in enumerate(weights):
        #     cam += w * target[i, :, :]

        #argmax
        # weights = np.max(grads_val, axis=(2, 3))[0, :]
        # cam = np.zeros(target.shape[1:], dtype=np.float32)

        # i_w = weights.argmax()
        # cam = weights[i_w] * target[i_w, :, :]

        cam = np.maximum(cam, 0)
        cam = cv2.resize(cam, (256, 256))
        cam = cam - np.min(cam)
        cam = cam / np.max(cam)
        return cam


class GuidedBackpropReLU(Function):

    @staticmethod
    def forward(self, input):
        positive_mask = (input > 0).type_as(input)
        output = torch.addcmul(torch.zeros(input.size()).type_as(input), input, positive_mask)
        self.save_for_backward(input, output)
        return output

    @staticmethod
    def backward(self, grad_output):
        input, output = self.saved_tensors
        grad_input = None

        positive_mask_1 = (input > 0).type_as(grad_output)
        positive_mask_2 = (grad_output > 0).type_as(grad_output)
        grad_input = torch.addcmul(torch.zeros(input.size()).type_as(input),
                                   torch.addcmul(torch.zeros(input.size()).type_as(input), grad_output,
                                                 positive_mask_1), positive_mask_2)

        return grad_input


class GuidedBackpropReLUModel:
    def __init__(self, model, use_cuda):
        self.model = model
        self.model.eval()
        self.cuda = use_cuda
        if self.cuda:
            self.model = model.cuda()

        # replace ReLU with GuidedBackpropReLU
        # for idx, module in self.model.features._modules.items():
        for idx, module in self.model._modules.items():
            if module.__class__.__name__ == 'ReLU':
                # self.model.features._modules[idx] = GuidedBackpropReLU.apply
                self.model._modules[idx] = GuidedBackpropReLU.apply

    def forward(self, input):
        return self.model(input)

    def __call__(self, input, index=None):
        if self.cuda:
            output = self.forward(input.cuda())
        else:
            output = self.forward(input)

        if index == None:
            index = np.argmax(output.cpu().data.numpy())

        one_hot = np.zeros((1, output.size()[-1]), dtype=np.float32)
        one_hot[0][index] = 1
        one_hot = torch.from_numpy(one_hot).requires_grad_(True)
        if self.cuda:
            one_hot = torch.sum(one_hot.cuda() * output)
        else:
            one_hot = torch.sum(one_hot * output)

        # self.model.features.zero_grad()
        # self.model.classifier.zero_grad()
        one_hot.backward(retain_graph=True)

        output = input.grad.cpu().data.numpy()
        output = output[0, :, :, :]

        return output


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--use-cuda', action='store_true', default=False,
                        help='Use NVIDIA GPU acceleration')
    parser.add_argument('--image-path', type=str, default='./examples/both.png',
                        help='Input image path')
    parser.add_argument('--cfg', help='experiment configuration filename',
                        required=True, type=str)
    parser.add_argument('--model-file', help='model parameters', required=True, type=str)
    args = parser.parse_args()
    args.use_cuda = args.use_cuda and torch.cuda.is_available()
    if args.use_cuda:
        print("Using GPU for acceleration")
    else:
        print("Using CPU for computation")

    update_config(config, args)

    return args


def deprocess_image(img):
    """ see https://github.com/jacobgil/keras-grad-cam/blob/master/grad-cam.py#L65 """
    img = img - np.mean(img)
    img = img / (np.std(img) + 1e-5)
    img = img * 0.1
    img = img + 0.5
    img = np.clip(img, 0, 1)
    return np.uint8(img*255)


if __name__ == '__main__':
    """ python grad_cam.py <path_to_image>
    1. Loads an image with opencv.
    2. Preprocesses it for VGG19 and converts to a pytorch variable.
    3. Makes a forward pass to find the category index with the highest score,
    and computes intermediate activations.
    Makes the visualization. """

    args = get_args()

    logger, final_output_dir, tb_log_dir = \
        utils.create_logger(config, args.cfg, 'grad-cam')

    logger.info(pprint.pformat(args))
    logger.info(pprint.pformat(config))

    cudnn.benchmark = config.CUDNN.BENCHMARK
    cudnn.determinstic = config.CUDNN.DETERMINISTIC
    cudnn.enabled = config.CUDNN.ENABLED

    config.defrost()
    config.MODEL.INIT_WEIGHTS = False
    config.freeze()

    # Can work with any model, but it assumes that the model has a
    # feature method, and a classifier method,
    # as in the VGG models in torchvision.

    #VGG19
    # grad_cam = GradCam(model=models.vgg19(pretrained=True), \
    #                    target_layer_names=["35"], use_cuda=args.use_cuda)

    #ResNet
    # model_res = models.resnet50(pretrained=True)
    # # print(model_res)
    # del model_res.fc
    #
    # grad_cam = GradCam(model_res, target_layer_names=["layer4"], use_cuda=args.use_cuda)

    #SENet
    # hub_model = torch.hub.load('moskomule/senet.pytorch', 'se_resnet50', pretrained=True)
    # del hub_model.fc
    # print(hub_model)
    #
    # grad_cam = GradCam(hub_model, target_layer_names=["layer4"], use_cuda=args.use_cuda)

    #CBAM
    # model = ptcv_get_model("cbam_resnet50", pretrained=True)
    # print(model)
    #
    # grad_cam = GradCam(model, target_layer_names=["stage4"], use_cuda=args.use_cuda)

    # HRNetV2
    model = models.get_face_alignment_net(config)
    model = nn.DataParallel(model).cuda()

    # load model
    state_dict = torch.load(args.model_file)
    if 'state_dict' in state_dict.keys():
        state_dict = state_dict['state_dict']
        model.load_state_dict(state_dict)
    else:
        model.module.load_state_dict(state_dict)

    grad_cam = GradCam(model.module, target_layer_names=["stage4"], use_cuda=args.use_cuda)

    img = cv2.imread(args.image_path, 1)
    img = np.float32(cv2.resize(img, (256, 256))) / 255
    input = preprocess_image(img)

    # # If None, returns the map for the highest scoring category.
    # # Otherwise, targets the requested index.
    target_index = None
    mask = grad_cam(input, target_index)

    show_cam_on_image(img, mask)



    # # gb_model = GuidedBackpropReLUModel(model=models.vgg19(pretrained=True), use_cuda=args.use_cuda)
    # # gb_model = GuidedBackpropReLUModel(model=se_resnet50, use_cuda=args.use_cuda)
    # # gb_model = GuidedBackpropReLUModel(model=resnet, use_cuda=args.use_cuda)
    # gb_model = GuidedBackpropReLUModel(model=cbam_resnet50, use_cuda=args.use_cuda)
    #
    # gb = gb_model(input, index=target_index)
    # gb = gb.transpose((1, 2, 0))
    # cam_mask = cv2.merge([mask, mask, mask])
    # cam_gb = deprocess_image(cam_mask*gb)
    # gb = deprocess_image(gb)
    #
    # cv2.imwrite('gb.jpg', gb)
    # cv2.imwrite('cam_gb.jpg', cam_gb)