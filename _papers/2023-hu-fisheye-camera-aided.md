---
title: Fisheye Camera Aided GNSS NLOS Detection and Learning-Based Pseudorange Bias Correction for Intelligent Vehicles in Urban Canyons
authors:
- Runzhi Hu
- Weisong Wen
- Li–Ta Hsu
publisher: 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)
date: '2023-09-24'
doi: https://doi.org/g8t66b
image: images/papers/cards/2023-hu-fisheye-camera-aided.jpg
citation_id: doi:10.1109/itsc57777.2023.10422540
---

## Abstract

The global navigation satellite system (GNSS) is lowcost and is highly expected by intelligent vehicles, which can provide reliable absolute positioning service in open areas. 
Unfortunately, the performance of the GNSS positioning is significantly degraded in urban canyons, due to the notorious non-line-of-sight (NLOS) receptions and multipath interference caused by signal reflections. To fill this gap, this paper proposed a fisheye camera-based GNSS NLOS detection method, where the state-of-the-art Swin Transformer model is employed to segment the sky and non-sky view areas within the image. Instead of directly excluding the detected GNSS NLOS receptions that would significantly degrade the geometry of satellite distribution, this paper proposed to directly estimate the bias of the NLOS receptions and multipath by a tightlycoupled integration model of GNSS least square and the deep neural network (DNN). The effectiveness of the proposed method was validated on multiple datasets from urban canyons in Hong Kong. In particular, a GNSS NLOS detection accuracy of more than 99.0% is achieved in the evaluated dataset. By correcting the bias involved from the GNSS NLOS and multipath, improved positioning accuracy about 5% is obtained using the proposed method. To benefit the research community, we open-source a library, the pyRTKLIB, which can serve as an important bridge between the DNN and the conventional GNSS processing tools, the RTKLIB.

## Problem Addressed

GNSS positioning for intelligent vehicles is significantly degraded in urban canyons by NLOS receptions and multipath interference caused by signal reflections.

## Key Contributions

- Fisheye camera-based GNSS NLOS detection using Swin Transformer to segment sky and non-sky areas
- DNN-based pseudorange bias estimation for NLOS and multipath, avoiding satellite exclusion and geometry degradation
- Tightly coupled integration of GNSS least squares and the deep neural network
- Open-source pyRTKLIB library bridging deep neural networks and conventional RTKLIB GNSS processing

## Conclusions

The method achieves NLOS detection accuracy, precision, and recall of approximately 99% on the evaluated dataset. The DNN bias correction, evaluated on three distinct datasets without data leakage, outperforms traditional approaches and improves positioning accuracy by about 5%. Whether image-based NLOS detection corresponds to physical NLOS requires further study, and the single-satellite DNN design should be extended with additional information and time sequences.
