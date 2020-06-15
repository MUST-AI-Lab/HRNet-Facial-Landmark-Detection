# High-resolution networks (HRNets) for facial landmark detection
## Introduction 
This is the official code of [High-Resolution Representations for Facial Landmark Detection](https://arxiv.org/pdf/1904.04514.pdf). 
We extend the high-resolution representation (HRNet) [1] by augmenting the high-resolution representation by aggregating the (upsampled) 
representations from all the parallel convolutions, leading to stronger representations. The output representations are fed into
classifier. We evaluate our methods on four datasets, COFW, AFLW, WFLW and 300W.

<div align=center>

![](images/hrnet.jpg)

</div>

## Performance
### ImageNet pretrained models
HRNetV2 ImageNet pretrained models are now available! Codes and pretrained models are in [HRNets for Image Classification](https://github.com/HRNet/HRNet-Image-Classification)


We adopt **HRNetV2-W18**(#Params=9.3M, GFLOPs=4.3G) for facial landmark detection on COFW, AFLW, WFLW and 300W.

### COFW

The model is trained on COFW *train* and evaluated on COFW *test*.

| Model | NME | FR<sub>0.1</sub>|pretrained model|model|
|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18  | 3.45 | 0.20 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | [HR18-COFW.pth](https://1drv.ms/u/s!AiWjZ1LamlxzdFIsEUQl8jgUaMk)|
|HRNetV2-W18(reproduced) | 3.45 | 0.20 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | HR18-COFW.pth|
|HRNetV2-W18-SE(reduction=16) | 3.45 | 0.39 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | HR18-COFW-SE.pth|


### AFLW
The model is trained on AFLW *train* and evaluated on AFLW *full* and *frontal*.

| Model | NME<sub>*full*</sub> | NME<sub>*frontal*</sub> | pretrained model|model|
|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 | 1.57 | 1.46 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | [HR18-AFLW.pth](https://1drv.ms/u/s!AiWjZ1Lamlxzc7xumEw810iBLTc)|
|HRNetV2-W18(reproduced) | 1.57 | 1.45 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | HR18-AFLW.pth|

### WFLW

| NME |  *test* | *pose* | *illumination* | *occlution* | *blur* | *makeup* | *expression* | pretrained model|model|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 | 4.60 | 7.86 | 4.57 | 5.42 | 5.36 | 4.26 | 4.78 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | [HR18-WFLW.pth](https://1drv.ms/u/s!AiWjZ1LamlxzdTsr_9QZCwJsn5U)|
|HRNetV2-W18(reproduced) | 4.60 | 7.88 | 5.38 | 5.44 | 5.38 | 4.28 | 4.77 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | HR18-WFLW.pth|
|HRNetV2-W18-SE(reduction=16) | 4.63 | 7.85 | 4.56 | 5.41 | 5.31 | 4.32 | 4.89 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | HR18-WFLW-SE.pth|


### 300W

| NME | *common*| *challenge* | *full* | *test*|  pretrained model|model|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 | 2.91 | 5.11 | 3.34 | 3.85 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | [HR18-300W.pth](https://1drv.ms/u/s!AiWjZ1LamlxzeYLmza1XU-4WhnQ)|
|HRNetV2-W18(reproduced) | 2.95 | 5.12 | 3.37 | 3.96 | [HRNetV2-W18](https://1drv.ms/u/s!Aus8VCZ_C_33cMkPimlmClRvmpw) | HR18-300W.pth|
|HRNetV2-W32(reproduced) | 2.98 | 5.14 | 3.40 | 3.96 | [HRNetV2-W32](https://onedrive.live.com/?authkey=%21AEwfaSueYurmSRA&id=56B9F9C97F261712%2111776&cid=56B9F9C97F261712) | HR32-300W.pth|

#### Train from scratch
| Model | Initialization | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18 |normal| 2.99 | 5.21 | 3.43 | 4.08 | 111 |
|HRNetV2-W18 |Xavier| 28.57 | 48.20 | 32.42 | 36.85 | 111 |
|HRNetV2-W18 |kaiming| 82.42 | 94.87 | 84.86 | 84.79 | 111 |

#### Integrating in resdiual unit
| Model | reduction | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-SE |16| 2.97 | 5.23 | 3.41 | 3.98 | 111 |
|HRNetV2-W18-CBAM |16| 2.96 | 5.28 | 3.42 | 4.06 | 111 |
|HRNetV2-W32-SE |16| 2.98 | 5.21 | 3.41 | 4.01 | 111 |
|HRNetV2-W32-CBAM |16| 2.98 | 5.24 | 3.42 | 4.02 | 111 |

#### HRNet-SE + residual
| Model | reduction | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-SE |4| 2.93 | 5.16 | 3.37 | 3.97 | 111 |
|HRNetV2-W18-SE |4| 2.93 | 5.15 | 3.36 | 3.94 | 111 |
|HRNetV2-W18-SE |4| 2.95 | 5.16 | 3.39 | 3.97 | 222 |
|HRNetV2-W18-SE |4| 2.94 | 5.26 | 3.40 | 3.93 | 333 |
|HRNetV2-W18-SE |8| 2.93 | 5.29 | 3.39 | 3.94 | 111 |
|HRNetV2-W18-SE |8| 2.96 | 5.23 | 3.40 | 4.00 | 222 |
|HRNetV2-W18-SE |8| 2.96 | 5.26 | 3.41 | 4.00 | 333 |
|HRNetV2-W18-SE |16| 2.95 | 5.30 | 3.39 | 3.95 | 111 |
|HRNetV2-W18-SE |16| 2.94 | 5.20 | 3.39 | 3.96 | 222 |
|HRNetV2-W18-SE |16| 2.94 | 5.26 | 3.39 | 3.94 | 333 |

#### HRNet-SE + residual + feature fusion
| Model | reduction | *common*| *challenge* | *full* | *test*| seed | stage |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - | 4 |
|HRNetV2-W18-SE |4| 2.93 | 5.15 | 3.36 | 3.94 | 111 | 4 |
|HRNetV2-W18-SE |4| 2.96 | 5.21 | 3.40 | 3.94 | 111 | 3+4 |
|HRNetV2-W18-SE |4| 2.97 | 5.27 | 3.42 | 3.95 | 111 | 2+3+4 |
|HRNetV2-W18-SE |4| 2.96 | 5.18 | 3.39 | 4.02 | 111 | 1+2+3+4 |

#### HRNet-NonLocal
| Model | f | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-NonLocal |Gaussian, embed| 2.95 | 5.18 | 3.38 | 3.96 | 111 |
|HRNetV2-W18-NonLocal |Gaussian| 2.92 | 5.19 | 3.36 | 4.00 | 111 |
|HRNetV2-W18-NonLocal |dot-product| 2.95 | 5.25 | 3.40 | 3.96 | 111 |
|HRNetV2-W18-NonLocal |concatenation| - | - | - | - | - |

#### HRNet-CBAM/BAM
| Model | reduction | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-CBAM |4| 2.98 | 5.25 | 3.42 | 3.93 | 111 |
|HRNetV2-W18-BAM |4| 2.92 | 5.18 | 3.36 | 3.98 | 111 |
|HRNetV2-W18-CBAM |8| 2.96 | 5.21 | 3.40 | 3.95 | 111 |
|HRNetV2-W18-BAM |8| 2.97 | 5.20 | 3.40 | 3.97 | 111 |
|HRNetV2-W18-CBAM |16| 2.92 | 5.20 | 3.37 | 3.93 | 111 |
|HRNetV2-W18-BAM |16| 2.94 | 5.20 | 3.38 | 3.96 | 111 |


![](images/face.png)

## Quick start
#### Environment
This code is developed using on Python 3.6 and PyTorch 1.0.0 on Ubuntu 16.04 with NVIDIA GPUs. Training and testing are 
performed using 1 NVIDIA P40 GPU with CUDA 9.0 and cuDNN 7.0. Other platforms or GPUs are not fully tested.

#### Install
1. Install PyTorch 1.0 following the [official instructions](https://pytorch.org/)
2. Install dependencies
````bash

pip install -r requirements.txt
````
3. Clone the project
````bash 
git clone https://github.com/HRNet/HRNet-Facial-Landmark-Detection.git
````

#### HRNetV2 pretrained models
```bash
cd HRNet-Facial-Landmark-Detection
# Download pretrained models into this folder
mkdir hrnetv2_pretrained
```
#### Data

1. You need to download the annotations files which have been processed from [OneDrive](https://1drv.ms/u/s!AiWjZ1LamlxzdmYbSkHpPYhI8Ms), [Cloudstor](https://cloudstor.aarnet.edu.au/plus/s/m9lHU2aJId8Sh8l), and [BaiduYun(Acess Code:ypxg)](https://pan.baidu.com/s/1Yg1IEp3l2IpGPolpUsWdfg).

2. You need to download images (300W, AFLW, WFLW) from official websites and then put them into `images` folder for each dataset.

Your `data` directory should look like this:

````
HRNet-Facial-Landmark-Detection
-- lib
-- experiments
-- tools
-- data
   |-- 300w
   |   |-- face_landmarks_300w_test.csv
   |   |-- face_landmarks_300w_train.csv
   |   |-- face_landmarks_300w_valid.csv
   |   |-- face_landmarks_300w_valid_challenge.csv
   |   |-- face_landmarks_300w_valid_common.csv
   |   |-- images
   |-- aflw
   |   |-- face_landmarks_aflw_test.csv
   |   |-- face_landmarks_aflw_test_frontal.csv
   |   |-- face_landmarks_aflw_train.csv
   |   |-- images
   |-- cofw
   |   |-- COFW_test_color.mat
   |   |-- COFW_train_color.mat  
   |-- wflw
   |   |-- face_landmarks_wflw_test.csv
   |   |-- face_landmarks_wflw_test_blur.csv
   |   |-- face_landmarks_wflw_test_expression.csv
   |   |-- face_landmarks_wflw_test_illumination.csv
   |   |-- face_landmarks_wflw_test_largepose.csv
   |   |-- face_landmarks_wflw_test_makeup.csv
   |   |-- face_landmarks_wflw_test_occlusion.csv
   |   |-- face_landmarks_wflw_train.csv
   |   |-- images

````

#### Train
Please specify the configuration file in `experiments` (learning rate should be adjusted when the number of GPUs is changed).
````bash
python tools/train.py --cfg <CONFIG-FILE>
# example:
python tools/train.py --cfg experiments/wflw/face_alignment_wflw_hrnet_w18.yaml
````

#### Test
````bash
python tools/test.py --cfg <CONFIG-FILE> --model-file <MODEL WEIGHT> 
# example:
python tools/test.py --cfg experiments/wflw/face_alignment_wflw_hrnet_w18.yaml --model-file HR18-WFLW.pth
````

 
## Other applications of HRNets (codes and models):
* [Human pose estimation](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch)
* [Semantic segmentation](https://github.com/HRNet/HRNet-Semantic-Segmentation)
* [Object detection](https://github.com/HRNet/HRNet-Object-Detection)
* [Image classification](https://github.com/HRNet/HRNet-Image-Classification)
 
## Citation
If you find this work or code is helpful in your research, please cite:
````
@inproceedings{SunXLW19,
  title={Deep High-Resolution Representation Learning for Human Pose Estimation},
  author={Ke Sun and Bin Xiao and Dong Liu and Jingdong Wang},
  booktitle={CVPR},
  year={2019}
}

@article{WangSCJDZLMTWLX19,
  title={Deep High-Resolution Representation Learning for Visual Recognition},
  author={Jingdong Wang and Ke Sun and Tianheng Cheng and 
          Borui Jiang and Chaorui Deng and Yang Zhao and Dong Liu and Yadong Mu and 
          Mingkui Tan and Xinggang Wang and Wenyu Liu and Bin Xiao},
  journal   = {TPAMI}
  year={2019}
}
````

## Reference
[1] Deep High-Resolution Representation Learning for Visual Recognition. Jingdong Wang, Ke Sun, Tianheng Cheng, 
    Borui Jiang, Chaorui Deng, Yang Zhao, Dong Liu, Yadong Mu, Mingkui Tan, Xinggang Wang, Wenyu Liu, Bin Xiao. Accepted by TPAMI.  [download](https://arxiv.org/pdf/1908.07919.pdf)
