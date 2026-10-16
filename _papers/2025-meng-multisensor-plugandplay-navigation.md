---
title: Multisensor Plug-and-Play Navigation Based on Resilient Information Filter
authors:
- Qian Meng
- Chang Su
- Yingying Jiang
- Weisong Wen
- Xiaolin Meng
publisher: IEEE Sensors Journal
date: '2025-02-26'
doi: https://doi.org/g9hrnp
image: images/papers/cards/2025-meng-multisensor-plugandplay-navigation.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Multisensor_Plug-and-Play_Navigation_Based_on_Resilient_Information_Filter.pdf
tags:
- Asynchronous information
- information filter (IF)
- multisensor integration
- plug and play
- resilient navigation
citation_id: doi:10.1109/JSEN.2025.3540790
---

## Abstract

To improve the positioning accuracy and resilience of the multisensor integration, a resilient plug-andplay navigation method based on information filter (IF) is proposed in this article. As the dual form of Kalman filter (KF), IF turns the likelihood product into a sum, which can fully utilize asynchronous sensor measurements for fusion and realize plug-and-play navigation flexibly. Furthermore, a resilient factor based on the principle of chi-square test is implemented to adjust the sensor information, aiming to reduce the impact of faulty measurements under challenging scenarios. By conducting and analyzing the vehicle experiments in the urban environment, the proposed method shows better performance over traditional KF, with the root mean square (rms) error reduced from 9.13 to 3.28 m. Plug-and-play navigation achieves a 51.37% improvement in positioning accuracy by utilizing more suitable sensor measurements and propagation intervals, which can decrease the sensitivity to measurement noise and faults. The resilient factor directly addresses the faults themselves and improves the positioning performance by 26.13%, further enhancing the system's resilience and robustness to faulty information. This resilient IF method is fully validated as effective for multisensor plug-and-play navigation.

## Problem Addressed

Multisensor integration needs higher positioning accuracy and resilience, but Kalman filter-based fusion cannot flexibly exploit asynchronous sensor measurements and remains vulnerable to faulty measurements in challenging scenarios.

## Key Contributions

- Multisensor plug-and-play navigation based on the information filter, exploiting its additive/subtractive fusion structure
- Resilient factor derived from the chi-square test principle to dynamically adjust sensor information online
- Validation in urban canyon vehicle experiments with INS/GNSS/LiDAR using open-sourced data

## Conclusions

The proposed method outperforms the traditional Kalman filter, with RMS error reduced from 9.13 to 3.28 m. Plug-and-play navigation yields a 51.37% improvement in positioning accuracy through more suitable sensor measurements and propagation intervals, and the resilient factor adds a further 26.13% improvement by directly addressing faulty measurements.
