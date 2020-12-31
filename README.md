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

#### DenseNAS
| Stack Num | search space | search NME | *common*| *challenge* | *full* | *test*| seed | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|original| DenseNAS          | 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
|4       | DenseNAS          | 20.90 | 3.38 | 5.98 | 3.89 | 4.70 | 111 |
|4       | modified DenseNAS | 21.68 | 3.65 | 6.82 | 4.27 | 5.24 | 111 |
|7       | modified DenseNAS | 20.87 | 3.67 | 6.93 | 4.31 | 5.29 | 111 |
|4       | HRNet             | 20.12 | 5.72 | 9.41 | 6.44 | 7.59 | 111 |
|7       | HRNet             | 21.50 | 4.30 | 7.62 | 4.95 | 6.00 | 111 |
|4       | modified HRNet    | 21.30 | 4.04 | 6.88 | 4.59 | 5.51 | 111 |
|7       | modified HRNet    | 21.13 | 4.38 | 7.05 | 4.90 | 5.70 | 111 |

##### Original DenseNAS search space (downsample 16x)(Initialized by normal)
Detailed Config: [experiments/300w/config_search_space.txt](https://github.com/MUST-AI-Lab/HRNet-Facial-Landmark-Detection/blob/master/experiments/300w/config_search_space.txt#L1)
| Stack Num | stem | pretrained |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|original | densenas |False| 21.78 | 3.41| 6.04 | 3.92 | 4.71 | 111 |
|original | densenas |True | 21.78 | 3.40| 5.92 | 3.89 | 4.64 | 111 |
|original | hrnet    |False| 23.33 | 4.57| 7.47 | 5.14 | 6.06 | 111 |
| 4       | densenas |False| 20.90 | 3.38| 5.98 | 3.89 | 4.70 | 111 |
| 4       | hrnet    |False| 21.78 | 4.77| 7.97 | 5.40 | 6.38 | 111 |

on batch size and seed
|batch size|search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|16| 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
|16| 22.09| 3.42| 6.03 |  3.93 | 4.72 | 111 |
|16| 21.74 | 3.38| 5.89 | 3.88 | 4.64 | 222 |
|16| 21.91 | 3.40| 5.90 | 3.89 | 4.67 | 333 |
|32| 22.58| 3.43| 6.02 |  3.93 | 4.74 | 111 |

on the epoch updating alpha 
|update a(epoch)| loss factor |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0-20 | 0.15 |21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
|10-30 | 0.15 |21.55 | 3.39 | 5.96 | 3.90 | 4.69 | 111 |
|20-40 | 0.15 |21.73 | 3.39 | 6.00 | 3.90 | 4.69 | 111 |
|0-20  | 0 | 21.59 | 3.48 | 6.10 | 3.99 | 4.79 | 111 |
|0-30  | 0 | 21.53 | 3.37 | 5.86 | 3.86 | 4.64 | 111 |
|0-40  | 0 | 21.52 | 3.39 | 5.84 | 3.87 | 4.65 | 111 |
|10-30 | 0 | 21.58 | 3.47 | 6.08 | 3.99 | 4.83 | 111 |
|20-40 | 0 | 21.32 | 3.43 | 5.90 | 3.91 | 4.67 | 111 |

on channel size
| channel reduction |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
| 2 | 21.79 | 3.50| 6.12 | 4.01 | 4.88 | 111 |
| 4 | 20.71 | 3.65| 6.47|  4.20| 5.13| 111 |
| 8 | 21.54 | 3.93| 7.29 | 4.59 | 5.68 | 111 |

on the number of basic layer
| Stack Num |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| +0 | 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
| +2 |22.32 | 3.43| 6.03 | 3.94 | 4.75 | 111 |
| +4 |21.78 | 3.40 | 5.98 | 3.90 | 4.69 | 111 |
| +6 |22.37 | 3.38 | 5.98| 3.89 | 4.69 | 111 |
| +8 | 21.54 | 3.40| 5.98 | 3.91 | 4.73 | 111 |

on the number of routing block
| block Num |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| -0 |21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
| -2 |21.50 | 3.44 | 6.05 | 3.95 | 4.73 | 111 |
| -4 |21.78 | 3.43 | 6.01 | 3.94 | 4.76| 111 |
| -6 |22.37 | 3.56 | 6.48| 4.14 | 5.10 | 111 |
| -8 | 21.54 | 3.38| 5.98 | 4.18 | 5.13 | 111 |

on multi-branch
| transition |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
| 2 | 21.62 | 3.35| 5.85|  3.84| 4.60| 111 |

adding noise
| +noise | search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|-               | 21.78 | 3.41| 6.04 | 3.92 | 4.71 | 111 |
|smoothdarts     | 22.29 | 3.40| 5.92 | 3.90 | 4.70 | 111 |
|noisydarts(step)| 34.69 | 3.40| 6.04 | 3.92 | 4.70 | 111 |
|noisydarts(epoch)| 34.69 | 3.40| 6.04 | 3.92 | 4.70 | 111 |

adding operations from darts search space
| +ops |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|     -       | 21.78 | 3.41| 6.04 | 3.92 | 4.71 | 111 |
| sep conv3x3 | 24.74 | 3.47 | 6.15 | 4.00 | 4.85 | 111 |
| dil conv3x3 | 24.10 | 3.43 | 6.07 | 3.95 | 4.73 | 111 |
| sep conv5x5 | 25.33 | 3.43 | 6.15 | 3.96 | 4.81 | 111 |
| dil conv5x5 | 27.85 | 3.47 | 6.09 | 3.98 | 4.83 | 111 |

on the factor of loss function to control model size
| loss factor |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0.15   | 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
| 0      | 21.59 | 3.48 | 6.10 | 3.99 | 4.79 | 111 |

##### Search Space: Modified DenseNAS (Stage 4)
Detailed Config: [experiments/300w/config_search_space.txt](https://github.com/MUST-AI-Lab/HRNet-Facial-Landmark-Detection/blob/master/experiments/300w/config_search_space.txt#L27)
| Stack Num | Initialization |downsample| channel expansion | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 |kaiming|8x| x1 | 70.09 | 81.21 | 72.27  | 72.96 | 111 |
|4 |kaiming|8x| x2 | 57.70 | 66.88 | 59.50  | 62.89 | 111 |
|4 |kaiming|8x| x4 | 46.99 | 59.10 | 49.36  | 50.64 | 111 |
|7 |kaiming|8x| x1 | 63.33 | 73.49 | 65.32  | 65.79 | 111 |
|7 |kaiming|8x| x2 | 51.31 | 62.37 | 53.48  | 54.20 | 111 |
|7 |kaiming|8x| x4 | 31.98 | 47.18 | 34.96  | 37.26 | 111 |
|10|kaiming|8x| x1 | 62.47 | 74.81 | 64.88  | 65.93 | 111 |
|10|kaiming|8x| x2 | 46.87 | 56.01 | 48.65  | 51.09 | 111 |
|10|kaiming|8x| x4 | 31.09 | 43.82 | 33.58  | 36.36 | 111 |
|4 |normal |8x| x1 | 3.65 | 6.82 | 4.27 | 5.24 | 111 |
|4 |normal |16x| x1 | 4.60 | 7.51 | 5.17 | 6.10 | 111 |
|7 |normal |8x| x1 | 3.67 | 6.93 | 4.31 | 5.29 | 111 |
|10|normal |8x| x1 | 4.12 | 6.74 | 4.63 | 5.51 | 111 |
|10|normal |8x| x2 | 3.47 | 6.01 | 3.96 | 4.79 | 111 |
|10|normal |8x| x4 | 3.38 | 5.94 | 3.88 | 4.63 | 111 |

##### Search Space: Modified DenseNAS(Initialized by normal)
| Stack Num | update alpha(epoch) | transition| search NME | *common*| *challenge* | *full* | *test*| seed | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 |0-20  | 1 | 21.68 | 3.65| 6.82 | 4.27 | 5.24 | 111 |
|7 |0-20  | 1 | 20.87 | 3.67| 6.93 | 4.31 | 5.29 | 111 |
|7 |0-20  | 2 | 26.09 | 3.50| 6.15 | 4.02 | 4.83 | 111 |
|7 |10-30 | 2 | 24.28 | 3.48| 6.11 | 4.00 | 4.80 | 111 |

##### Search Space: HRNet (Initialized by normal)
Detailed Config: [experiments/300w/config_search_space.txt](https://github.com/MUST-AI-Lab/HRNet-Facial-Landmark-Detection/blob/master/experiments/300w/config_search_space.txt#L52)
| Stack Num | +noise | search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 |-          | 20.12 | 5.72 | 9.41 | 6.44 | 7.59 | 111 |
|7 |-          | 21.50 | 4.30 | 7.62 | 4.95 | 6.00 | 111 |
|7 |smoothdarts| 12.67 | 4.69| 7.65 | 5.27 | 6.24 | 111 |
|7 |noisydarts(step)| 29.38 | 4.46| 7.78 | 5.11 | 6.06 | 111 |
|7 |noisydarts(epoch)| 28.82 | 4.46| 7.78 | 5.11 | 6.06 | 111 |

##### Search Space: Darts cell based
| Sum/Concat | Search Space |Initialization |pretrained| Search NME | *common*| *challenge* | *full* | *test*| seed | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|-     | DenseNAS | normal|False| 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
|Sum   |HRNet   |kaiming|False| 130.38 |111.13 |126.08 | 114.06 | 114.00| 111 |
|Concat|HRNet   |kaiming|False| 108.76 | 51.07 | 68.33 | 54.45  | 55.87 | 111 |
|Sum   |modified DenseNAS|kaiming|False| 107.53 | 61.52 | 74.65 | 64.09  | 67.44 | 111 |
|Concat|modified DenseNAS|kaiming|False| 111.99 | 56.74 | 75.94 | 60.50  | 61.90 | 111 |
|Sum   | DenseNAS |kaiming|False| 110.66 | 39.91| 60.43 | 43.93 | 47.25 | 111 |
|Concat| DenseNAS |kaiming|False| 109.36 | 66.14| 79.80 | 68.82 | 70.18 | 111 |
|Sum   | DenseNAS (head:basic block) |normal|False| 21.54 | 3.40| 5.93 | 3.89 | 4.71 | 111 |
|Sum   | DenseNAS (head:basic block) |normal|True| 21.54 | 3.38| 5.98 | 3.89 | 4.67 | 111 |
|Concat| DenseNAS (head:basic block) |normal|False| 21.69  | 3.51| 6.23 | 4.04 | 4.93 | 111 |

on the DenseNAS with head:basic block
|update a(epoch)| loss factor | search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 0-20 | 0.15 | 21.54 | 3.40 | 5.93 | 3.89 | 4.71 | 111 |
| 0-30 | 0.15 | 21.51 | 3.41 | 5.97 | 3.91 | 4.67 | 111 | 
| 0-40 | 0.15 | 21.20 |  |  |  |  |  |
|10-30 | 0.15 | 21.49 | 3.38 | 5.90 | 3.87 | 4.66 | 111 |
|20-40 | 0.15 | 21.33 | 3.41 | 5.97 | 3.91 | 4.73 | 111 |
|0-20  | 0 | 21.53 | 3.38 | 5.93 | 3.88 | 4.64 | 111 | 
|0-30  | 0 | 21.55 | 3.87 | 6.89 | 4.46 | 5.37 | 111 | 
|0-40  | 0 | 21.13 | 3.40 | 5.98 | 3.91 | 4.61 | 111 | 
|10-30 | 0 | 21.48 | 3.64 | 6.35 | 4.17 | 4.95 | 111 | 
|20-40 | 0 | 21.16 |  |  |  |  |  |

##### Search Space: HRNet + DARTS ops (Initialized by kmnormal_fanout)
| Stack Num | transition | search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 | 1 | 100.88 | 93.51| 107.42 | 96.23 | 95.36 | 111 |
|7 | 1 | 156.61  | 102.26| 117.01 | 105.15 | 105.65 | 111 |
|4 | 2 | 160.19 | 84.96| 97.96 | 87.50 | 88.26 | 111 |
|7 | 2 | 140.24 | 94.74| 106.02 | 96.95 | 96.63 | 111 |

##### Multi-Scale(Search Space: 带红线的HRNet)
| Stack Num |Initialization| Transition | channel expansion | *common*| *challenge* | *full* | *test*| seed | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 | normal |1 | x1 | 4.04 | 6.88 | 4.59 | 5.51 | 111 |
|7 | normal |1 | x1 | 4.38 | 7.05 | 4.90 | 5.70 | 111 |
|4 | normal |2 | x1 | 3.88 | 6.88 | 4.47 | 5.36 | 111 |
|7 | normal |2 | x1 | 4.21 | 7.15 | 4.78 | 5.65 | 111 |
|4 | normal |2 | x2 | 3.58 | 6.21 | 4.09 | 4.89 | 111 |
|7 | normal |2 | x2 | 3.56 | 6.34 | 4.10 | 4.94 | 111 |

#### Darts pretrained on CIFAR-10
| Model | Input/Output Size | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |256/64| 2.91 | 5.11 | 3.34 | 3.85 | - |
|Darts-Layer8 |256/64| 4.76 | 13.00 | 6.37 | 9.22 | 111 |
|Darts-Layer8 |128/32| 3.61 | 6.19 | 4.11 | 4.91 | 111 |
|Darts-Layer20 |128/32| 3.45 | 5.85 | 3.92 | 4.69 | 111 |
|HRNetV2-W18 |128/32| 3.35 | 5.53 | 3.78 | 4.23 | 111 |

#### Train from scratch
| Model | Initialization | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18 |normal| 2.99 | 5.21 | 3.43 | 4.08 | 111 |
|HRNetV2-W18 |Xavier| 28.57 | 48.20 | 32.42 | 36.85 | 111 |
|HRNetV2-W18 |kaiming| 82.42 | 94.87 | 84.86 | 84.79 | 111 |


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
