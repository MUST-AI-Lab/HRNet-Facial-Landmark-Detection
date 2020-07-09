# Performance
## HRNet-SE
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

## HRNet-SE + residual
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

## HRNet-SE + residual + seed
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

## HRNet-SE + residual + feature fusion
| Model | reduction | *common*| *challenge* | *full* | *test*| seed | stage |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |4| 2.96 | 5.21 | 3.40 | 3.94 | 111 | 3+4 |
|HRNetV2-W18 |4| 2.97 | 5.27 | 3.42 | 3.95 | 111 | 2+3+4 |
|HRNetV2-W18 |4| 2.96 | 5.18 | 3.39 | 4.02 | 111 | 1+2+3+4 |

## HRNet-NonLocal
| Model | f | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-NonLocal |Gaussian, embed| 2.95 | 5.18 | 3.38 | 3.96 | 111 |
|HRNetV2-W18-NonLocal |Gaussian| 2.92 | 5.19 | 3.36 | 4.00 | 111 |
|HRNetV2-W18-NonLocal |dot-product| 2.95 | 5.25 | 3.40 | 3.96 | 111 |
|HRNetV2-W18-NonLocal |concatenation| - | - | - | - | - |

## HRNet-CBAM/BAM
| Model | reduction | *common*| *challenge* | *full* | *test*| seed |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|HRNetV2-W18 |-| 2.91 | 5.11 | 3.34 | 3.85 | - |
|HRNetV2-W18-CBAM |4| 2.98 | 5.25 | 3.42 | 3.93 | 111 |
|HRNetV2-W18-BAM |4| 2.92 | 5.18 | 3.36 | 3.98 | 111 |
|HRNetV2-W18-CBAM |8| 2.96 | 5.21 | 3.40 | 3.95 | 111 |
|HRNetV2-W18-BAM |8| 2.97 | 5.20 | 3.40 | 3.97 | 111 |
|HRNetV2-W18-CBAM |16| 2.92 | 5.20 | 3.37 | 3.93 | 111 |
|HRNetV2-W18-BAM |16| 2.94 | 5.20 | 3.38 | 3.96 | 111 |

## Integrating in resdiual unit
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
