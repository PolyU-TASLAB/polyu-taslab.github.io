---
title: Fisheye Camera Aided GNSS NLOS Detection and Learning-Based Pseudorange Bias Correction for Intelligent Vehicles in Urban Canyons
authors:
- Runzhi Hu
- Weisong Wen
- Li–Ta Hsu
publisher: 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)
date: '2023-09-24'
doi: https://doi.org/g8t66b
image: images/papers/cards/2023-hu-fisheye-camera-aided-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Fisheye_Camera_Aided_GNSS_NLOS_Detection_and_Learning-Based_Pseudorange_Bias_Correction_for_Intelligent_Vehicles_in_Urban_Canyons.pdf
tags:
- simultaneous localization and mapping (SLAM)
- factor graph optimization (FGO)
- smart phone
- human activity
citation_id: 10.1109/ITSC57777.2023.10422540
---

## Abstract

The global navigation satellite system (GNSS) is low-cost and is highly expected by intelligent vehicles, which can provide reliable absolute positioning service in open areas. Unfortunately, the performance of the GNSS positioning is significantly degraded in urban canyons, due to the notorious non-line-of-sight (NLOS) receptions and multipath interference caused by signal reflections. To fill this gap, this paper proposed a fisheye camera-based GNSS NLOS detection method, where the state-of-the-art Swin Transformer model is employed to segment the sky and non-sky view areas within the image. Instead of directly excluding the detected GNSS NLOS receptions that would significantly degrade the geometry of satellite distribution, this paper proposed to directly estimate the bias of the NLOS receptions and multipath by a tightly-coupled integration model of GNSS least square and the deep neural network (DNN). The effectiveness of the proposed method was validated on multiple datasets from urban canyons in Hong Kong. In particular, a GNSS NLOS detection accuracy of more than 99.0% is achieved in the evaluated dataset. By correcting the bias involved from the GNSS NLOS and multipath, improved positioning accuracy about 5% is obtained using the proposed method. To benefit the research community, we open-source a library, the pyRTKLIB, which can serve as an important bridge between the DNN and the conventional GNSS processing tools, the RTKLIB.

## Problem Addressed

GNSS positioning in urban canyons is significantly degraded by NLOS receptions and multipath from signal reflections, while directly excluding detected NLOS satellites further deteriorates satellite geometry.

## Key Contributions

- Fisheye camera-based GNSS NLOS detection using Swin Transformer sky/non-sky segmentation
- DNN architecture estimating pseudorange bias of NLOS and multipath, considering chosen and master satellites
- Tightly coupled integration of GNSS least squares with the DNN instead of excluding NLOS receptions
- Open-sourced pyRTKLIB library bridging deep neural networks and the RTKLIB processing tools

## Conclusions

The method achieves NLOS detection accuracy, precision, and recall of approximately 99% on the evaluated datasets, and correcting pseudorange bias improves positioning accuracy by about 5%. Evaluation on three distinct datasets without data leakage demonstrates generalization potential. Future work should verify whether image-based NLOS corresponds to physical NLOS and incorporate time-sequence information.
