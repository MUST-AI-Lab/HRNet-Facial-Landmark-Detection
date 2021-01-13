# Performance
## Attention Mechanism
### HRNet-SE
| Model | reduction | *common*| *challenge* | *full* | *test*|
|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |1| 2.95 | 5.11 | 3.38 | 3.93 | 
|HRNetV2-W18 |2| 2.96 | 5.16 | 3.39 | 3.94 | 
|HRNetV2-W18 |3| 2.95 | 5.25 | 3.40 | 3.98 | 
|HRNetV2-W18 |4| 2.93 | 5.27 | 3.39 | 4.02 | 
|HRNetV2-W18 |5| 2.96 | 5.19 | 3.40 | 3.95 | 
|HRNetV2-W18 |6| 3.14 | 5.56 | 3.39 | 4.29 | 
|HRNetV2-W18 |7| 3.12 | 5.66 | 3.39 | 4.22 | 
|HRNetV2-W18 |8| 2.91 | 5.18 | 3.36 | 4.01 | 
|HRNetV2-W18 |9| 2.94 | 5.22 | 3.39 | 3.93 | 
|HRNetV2-W18 |10| 2.93 | 5.23 | 3.38 | 3.96 | 
|HRNetV2-W18 |11| 2.96 | 5.13 | 3.39 | 3.97 | 
|HRNetV2-W18 |12| 2.96 | 5.22 | 3.40 | 3.95 |
|HRNetV2-W18 |13| 2.97 | 5.24 | 3.42 | 3.96 | 
|HRNetV2-W18 |14| 2.94 | 5.22 | 3.38 | 3.98 | 
|HRNetV2-W18 |15| 3.00 | 5.27 | 3.45 | 3.99 | 
|HRNetV2-W18 |16| 2.92 | 5.29 | 3.39 | 3.94 | 

### HRNet-SE + residual
| Model | reduction | *common*| *challenge* | *full* | *test*|
|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |1| 2.94 | 5.20 | 3.39 | 3.95 | 
|HRNetV2-W18 |2| 2.95 | 5.31 | 3.42 | 3.94 | 
|HRNetV2-W18 |3| 2.95 | 5.32 | 3.41 | 4.00 | 
|HRNetV2-W18 |4| 2.93 | 5.11 | 3.36 | 3.93 | 
|HRNetV2-W18 |5| 2.93 | 5.22 | 3.37 | 3.90 | 
|HRNetV2-W18 |6| 2.95 | 5.28 | 3.40 | 3.94 | 
|HRNetV2-W18 |7| 2.93 | 5.19 | 3.38 | 3.93 | 
|HRNetV2-W18 |8| 2.95 | 5.18 | 3.39 | 3.98 | 
|HRNetV2-W18 |9| 2.93 | 5.14 | 3.36 | 3.94 | 
|HRNetV2-W18 |10| 2.95 | 5.27 | 3.41 | 3.97 | 
|HRNetV2-W18 |11| 2.96 | 5.19 | 3.40 | 3.94 | 
|HRNetV2-W18 |12| 2.95 | 5.17 | 3.39 | 3.94 |
|HRNetV2-W18 |13| 2.92 | 5.18 | 3.36 | 4.00 | 
|HRNetV2-W18 |14| 2.95 | 5.19 | 3.39 | 4.00 | 
|HRNetV2-W18 |15| 2.94 | 5.31 | 3.40 | 3.95 | 
|HRNetV2-W18 |16| 2.94 | 5.26 | 3.40 | 3.96 |

### HRNet-SE + residual + seed
| Model | reduction | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |4| 2.93 | 5.16 | 3.37 | 3.97 | 111 |
|HRNetV2-W18 |4| 2.93 | 5.15 | 3.36 | 3.94 | 111 |
|HRNetV2-W18 |4| 2.95 | 5.16 | 3.39 | 3.97 | 222 |
|HRNetV2-W18 |4| 2.94 | 5.26 | 3.40 | 3.93 | 333 |
|HRNetV2-W18 |8| 2.93 | 5.29 | 3.39 | 3.94 | 111 |
|HRNetV2-W18 |8| 2.96 | 5.23 | 3.40 | 4.00 | 222 |
|HRNetV2-W18 |8| 2.96 | 5.26 | 3.41 | 4.00 | 333 |
|HRNetV2-W18 |16| 2.95 | 5.30 | 3.39 | 3.95 | 111 |
|HRNetV2-W18 |16| 2.94 | 5.20 | 3.39 | 3.96 | 222 |
|HRNetV2-W18 |16| 2.94 | 5.26 | 3.39 | 3.94 | 333 |

### HRNet-SE + residual + feature fusion
| Model | reduction | *common*| *challenge* | *full* | *test*| seed | stage |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |4| 2.96 | 5.21 | 3.40 | 3.94 | 111 | 3+4 |
|HRNetV2-W18 |4| 2.97 | 5.27 | 3.42 | 3.95 | 111 | 2+3+4 |
|HRNetV2-W18 |4| 2.96 | 5.18 | 3.39 | 4.02 | 111 | 1+2+3+4 |

### HRNet-NonLocal
| Model | f | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-NonLocal |Gaussian, embed| 2.95 | 5.18 | 3.38 | 3.96 | 111 |
|HRNetV2-W18-NonLocal |Gaussian| 2.92 | 5.19 | 3.36 | 4.00 | 111 |
|HRNetV2-W18-NonLocal |dot-product| 2.95 | 5.25 | 3.40 | 3.96 | 111 |
|HRNetV2-W18-NonLocal |concatenation| - | - | - | - | - |

### HRNet-CBAM/BAM
| Model | reduction | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-CBAM |4| 2.98 | 5.25 | 3.42 | 3.93 | 111 |
|HRNetV2-W18-BAM |4| 2.92 | 5.18 | 3.36 | 3.98 | 111 |
|HRNetV2-W18-CBAM |8| 2.96 | 5.21 | 3.40 | 3.95 | 111 |
|HRNetV2-W18-BAM |8| 2.97 | 5.20 | 3.40 | 3.97 | 111 |
|HRNetV2-W18-CBAM |16| 2.92 | 5.20 | 3.37 | 3.93 | 111 |
|HRNetV2-W18-BAM |16| 2.94 | 5.20 | 3.38 | 3.96 | 111 |

### Integrating in resdiual unit
| Model | reduction | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-SE |16| 2.97 | 5.23 | 3.41 | 3.98 | 111 |
|HRNetV2-W18-CBAM |16| 2.96 | 5.28 | 3.42 | 4.06 | 111 |
|HRNetV2-W32-SE |16| 2.98 | 5.21 | 3.41 | 4.01 | 111 |
|HRNetV2-W32-CBAM |16| 2.98 | 5.24 | 3.42 | 4.02 | 111 |

## Train from scratch
| Model | Initialization | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18 |normal| 2.99 | 5.21 | 3.43 | 4.08 | 111 |
|HRNetV2-W18 |Xavier| 28.57 | 48.20 | 32.42 | 36.85 | 111 |
|HRNetV2-W18 |kaiming| 82.42 | 94.87 | 84.86 | 84.79 | 111 |

## Darts pretrained on CIFAR-10
| Model | Input/Output Size | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |256/64| 2.91 | 5.11 | 3.34 | 3.85 | - |
|Darts-Layer8 |256/64| 4.76 | 13.00 | 6.37 | 9.22 | 111 |
|Darts-Layer8 |128/32| 3.61 | 6.19 | 4.11 | 4.91 | 111 |
|Darts-Layer20 |128/32| 3.45 | 5.85 | 3.92 | 4.69 | 111 |
|HRNetV2-W18 |128/32| 3.35 | 5.53 | 3.78 | 4.23 | 111 |

## Densenas
| Stack Num | search space | search NME | *common*| *challenge* | *full* | *test*| seed | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|original| DenseNAS          | 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
|4       | DenseNAS          | 20.90 | 3.38 | 5.98 | 3.89 | 4.70 | 111 |
|4       | modified DenseNAS | 21.68 | 3.65 | 6.82 | 4.27 | 5.24 | 111 |
|7       | modified DenseNAS | 20.87 | 3.67 | 6.93 | 4.31 | 5.29 | 111 |
|4       | HRNet             | 20.12 | 5.72 | 9.41 | 6.44 | 7.59 | 111 |
|7       | HRNet             | 21.50 | 4.30 | 7.62 | 4.95 | 6.00 | 111 |

### Original DenseNAS search space (downsample 16x)(Initialized by normal)
Detailed Config: [experiments/300w/config_search_space.txt](https://github.com/MUST-AI-Lab/HRNet-Facial-Landmark-Detection/blob/master/experiments/300w/config_search_space.txt#L1)
| Stack Num | stem |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|original | densenas | 21.78 | 3.41| 6.04 | 3.92 | 4.71 | 111 |
|original | hrnet    | 23.33 | 4.57| 7.47 | 5.14 | 6.06 | 111 |
| 4       | densenas | 20.90 | 3.38| 5.98 | 3.89 | 4.70 | 111 |
| 4       | hrnet    | 21.78 | 4.77| 7.97 | 5.40 | 6.38 | 111 |

| channel reduction |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 2 | 21.79 | 3.50| 6.12 | 4.01 | 4.88 | 111 |
| 4 | 20.71 | 3.65| 6.47|  4.20| 5.13| 111 |
| 8 | 21.54 | 3.93| 7.29 | 4.59 | 5.68 | 111 |

| Stack Num |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| +2 |22.32 | 3.43| 6.03 | 3.94 | 4.75 | 111 |
| +4 |21.78 | 3.40 | 5.98 | 3.90 | 4.69 | 111 |
| +6 |22.37 | 3.38 | 5.98| | 3.89 | 4.69 | 111 |
| +8 | 21.54 | 3.40| 5.98 | 3.91 | 4.73 | 111 |

| blcok Num |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| -2 |21.50 | 3.44 | 6.05 | 3.95 | 4.73 | 111 |
| -4 |21.78 | 3.43 | 6.01 | 3.94 | 4.76| 111 |
| -6 |22.37 | 3.56 | 6.48| 4.14 | 5.10 | 111 |
| -8 | 21.54 | 3.38| 5.98 | 4.18 | 5.13 | 111 |

| transition |search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | 21.78 | 3.41 | 6.04 | 3.92 | 4.71 | 111 |
| 2 | 21.62 | 3.35| 5.85|  3.84| 4.60| 111 |

### Modified Search Space
#### Search Space: Modified DenseNAS(Initialize by kaiming normal)
Detailed Config: [experiments/300w/config_search_space.txt](https://github.com/MUST-AI-Lab/HRNet-Facial-Landmark-Detection/blob/master/experiments/300w/config_search_space.txt#L27)
| Stack Num | Stage | channel expansion | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 |1+2    | x1 | 111.06| 125.06 | 113.81 | 112.67 | 111 |
|4 |1+2+3  | x1 | 105.77| 119.47 | 108.45 | 108.38 | 111 |
|4 |1+2+3+4| x1 | 70.09 | 81.21 | 72.27  | 72.96 | 111 |
|4 |1+2    | x2 | 129.13| 143.38 | 131.92 | 130.53 | 111 |
|4 |1+2+3  | x2 | 93.51 | 105.61 | 95.88  | 94.59 | 111 |
|4 |1+2+3+4| x2 | 57.70 | 66.88 | 59.50  | 62.89 | 111 |
|4 |1+2    | x4 | 103.93| 116.22 | 106.34 | 105.04 | 111 |
|4 |1+2+3  | x4 | 110.37| 120.28 | 112.31 | 111.50 | 111 |
|4 |1+2+3+4| x4 | 46.99 | 59.10 | 49.36  | 50.64 | 111 |
|7 |1+2    | x1 | 116.10| 131.02| 119.03 | 117.95 | 111 |
|7 |1+2+3  | x1 | 120.93| 136.14| 123.91 | 122.42 | 111 |
|7 |1+2+3+4| x1 | 63.33 | 73.49 | 65.32  | 65.79 | 111 |
|7 |1+2    | x2 | 125.80| 140.72 | 128.72 | 128.77 | 111 |
|7 |1+2+3  | x2 | 94.86 | 105.82 | 97.01  | 95.34 | 111 |
|7 |1+2+3+4| x2 | 51.31 | 62.37 | 53.48  | 54.20 | 111 |
|7 |1+2    | x4 | 104.33| 118.74| 107.15 | 106.93 | 111 |
|7 |1+2+3  | x4 | 81.59 | 92.87 | 83.80  | 84.06 | 111 |
|7 |1+2+3+4| x4 | 31.98 | 47.18 | 34.96  | 37.26 | 111 |
|10|1+2    | x1 | 118.96 | 134.75 | 122.05 | 120.14 | 111 |
|10|1+2+3  | x1 | 127.07| 126.21| 114.84 | 114.37 | 111 |
|10|1+2+3+4| x1 | 62.47 | 74.81 | 64.88  | 65.93 | 111 |
|10|1+2    | x2 | 132.40| 147.19| 135.30 | 133.41 | 111 |
|10|1+2+3  | x2 | 102.96| 116.80| 105.67 | 105.36 | 111 |
|10|1+2+3+4| x2 | 46.87 | 56.01 | 48.65  | 51.09 | 111 |
|10|1+2    | x4 | 108.02| 119.09| 110.19 | 112.71| 111 |
|10|1+2+3  | x4 | 75.77 | 87.81 | 78.13  | 79.08 | 111 |
|10|1+2+3+4| x4 | 31.09 | 43.82 | 33.58  | 36.36 | 111 |

#### Search Space: Modified DenseNAS (Stage 4)
| Stack Num | Initialization | channel expansion | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 |kaiming| x1 | 70.09 | 81.21 | 72.27  | 72.96 | 111 |
|4 |kaiming| x2 | 57.70 | 66.88 | 59.50  | 62.89 | 111 |
|4 |kaiming| x4 | 46.99 | 59.10 | 49.36  | 50.64 | 111 |
|7 |kaiming| x1 | 63.33 | 73.49 | 65.32  | 65.79 | 111 |
|7 |kaiming| x2 | 51.31 | 62.37 | 53.48  | 54.20 | 111 |
|7 |kaiming| x4 | 31.98 | 47.18 | 34.96  | 37.26 | 111 |
|10|kaiming| x1 | 62.47 | 74.81 | 64.88  | 65.93 | 111 |
|10|kaiming| x2 | 46.87 | 56.01 | 48.65  | 51.09 | 111 |
|10|kaiming| x4 | 31.09 | 43.82 | 33.58  | 36.36 | 111 |
|4 |normal | x1 | 3.65 | 6.82 | 4.27 | 5.24 | 111 |
|4(down16x) |normal | x1 | 4.60 | 7.51 | 5.17 | 6.10 | 111 |
|7 |normal | x1 | 3.67 | 6.93 | 4.31 | 5.29 | 111 |
|10|normal | x1 | 4.12 | 6.74 | 4.63 | 5.51 | 111 |
|10|normal | x2 | 3.47 | 6.01 | 3.96 | 4.79 | 111 |
|10|normal | x4 | 3.38 | 5.94 | 3.88 | 4.63 | 111 |

#### Search Space: Modified DenseNAS(Initialize by normal)
| Stack Num | update alpha(epoch) | transition| search NME | *common*| *challenge* | *full* | *test*| seed | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 |0-20  | 1 | 21.68 | 3.65| 6.82 | 4.27 | 5.24 | 111 |
|7 |0-20  | 1 | 20.87 | 3.67| 6.93 | 4.31 | 5.29 | 111 |
|7 |0-20  | 2 | 26.09 | 3.50| 6.15 | 4.02 | 4.83 | 111 |
|7 |10-30 | 2 | 24.28 | 3.48| 6.11 | 4.00 | 4.80 | 111 |

#### Search Space: HRNet (Initialize by normal)
Detailed Config: [experiments/300w/config_search_space.txt](https://github.com/MUST-AI-Lab/HRNet-Facial-Landmark-Detection/blob/master/experiments/300w/config_search_space.txt#L52)
| Stack Num | +noise | search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 |-          | 20.12 | 5.72 | 9.41 | 6.44 | 7.59 | 111 |
|7 |-          | 21.50 | 4.30 | 7.62 | 4.95 | 6.00 | 111 |
|7 |smoothdarts| 12.67 | 4.69| 7.65 | 5.27 | 6.24 | 111 |
|7 |noisydarts(step)| 29.38 | 4.46| 7.78 | 5.11 | 6.06 | 111 |
|7 |noisydarts(epoch)| 28.82 | 4.46| 7.78 | 5.11 | 6.06 | 111 |

#### Search Space: HRNet + darts cell based
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
| 0-40 | 0.15 | 21.20 | 3.40 | 5.98 | 3.94 | 4.61 | 111 |
|10-30 | 0.15 | 21.49 | 3.38 | 5.90 | 3.87 | 4.66 | 111 |
|20-40 | 0.15 | 21.33 | 3.41 | 5.97 | 3.91 | 4.73 | 111 |
|0-20  | 0 | 21.53 | 3.38 | 5.93 | 3.88 | 4.64 | 111 | 
|0-30  | 0 | 21.55 | 3.87 | 6.89 | 4.46 | 5.37 | 111 | 
|0-40  | 0 | 21.13 | 3.40 | 5.98 | 3.91 | 4.61 | 111 | 
|10-30 | 0 | 21.48 | 3.64 | 6.35 | 4.17 | 4.95 | 111 | 
|20-40 | 0 | 21.16 | 3.73 | 6.66 | 4.30 | 6.37 | 111 |

#### Search Space: HRNet + DARTS ops (Initialize by kmnormal_fanout)
| Stack Num | transition | search NME | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 | 1 | 100.88 | 93.51| 107.42 | 96.23 | 95.36 | 111 |
|7 | 1 | 156.61  | 102.26| 117.01 | 105.15 | 105.65 | 111 |
|4 | 2 | 160.19 | 84.96| 97.96 | 87.50 | 88.26 | 111 |
|7 | 2 | 140.24 | 94.74| 106.02 | 96.95 | 96.63 | 111 |

#### Multi-Scale( Search Space: 带红线的HRNet)
| Stack Num |Initialization| Transition | channel expansion | *common*| *challenge* | *full* | *test*| seed | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|4 | normal |1 | x1 | 4.04 | 6.88 | 4.59 | 5.51 | 111 |
|7 | normal |1 | x1 | 4.38 | 7.05 | 4.90 | 5.70 | 111 |
|4 | normal |2 | x1 | 3.88 | 6.88 | 4.47 | 5.36 | 111 |
|7 | normal |2 | x1 | 4.21 | 7.15 | 4.78 | 5.65 | 111 |
|4 | normal |2 | x2 | 3.58 | 6.21 | 4.09 | 4.89 | 111 |
|7 | normal |2 | x2 | 3.56 | 6.34 | 4.10 | 4.94 | 111 |

