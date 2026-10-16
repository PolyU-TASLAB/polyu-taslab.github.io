---
title: 'FGO-MFI: factor graph optimization-based multi-sensor fusion and integration for reliable localization'
authors:
- Jiaqi Zhu
- Guirong Zhuo
- Xin Xia
- Weisong Wen
- Lu Xiong
- Bo Leng
- Wei Liu
publisher: Measurement Science and Technology
date: '2024-05-08'
doi: https://doi.org/g8t54v
image: images/papers/cards/2024-zhu-fgomfi-factor-graph.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/Zhu_2024_Meas._Sci._Technol._35_086303.pdf
tags:
- Vehicle localization
- Multi-sensor fusion
- IMU/dynamics pre-integration
citation_id: doi:10.1088/1361-6501/ad440a
---

## Abstract

Reliable and precise information pertaining to the position, velocity, and attitude is essential for automated driving. This paper proposes FGO-MFI, a cost-effective and robust multi-sensor fusion and integration localization framework that utilizes factor graph optimization. Firstly, a tightly coupled Global Navigation Satellite Systems (GNSS)/on-board sensor fusion localization framework is established to estimate vehicle states, including position, velocity, and attitude. To address the large drift rate of the Inertial Measurement Unit (IMU), this study introduces a novel IMU/Dynamics pre-integration method based on the vehicle dynamics model. We establish a two-degree-of-freedom vehicle dynamics model utilizing measurements from the wheel speed sensor and steering wheel angle sensor. The IMU/Dynamics factor is devised through a close integration of the model output and IMU pre-integration, enabling the construction of precise odometry with low-cost on-board sensors. Then, to address the issue of the non-Gaussian distribution of GNSS pseudorange error, this paper employs a Gaussian
Mixture Model (GMM) to characterize the pseudorange noise, which is then applied to further sensor fusion. Given the time-varying nature of pseudorange noise, the expectation maximization algorithm is utilized to estimate GMM parameters online, leveraging the pseudorange residuals within a sliding window. Comprehensive experiments, inclusive of challenging scenarios such as urban canyons, tunnels, and wooded areas, have been carried out.
They affirm the superior performance of the proposed method. Experiments have shown that our method demonstrates reliable localization across different statuses of GNSS signal, exhibiting a
39.4% improvement in the root mean square error of position error when compared to the state-of-the-art. Additionally, this FGO-MFI is a general sensor data fusion framework and is able to incorporate diverse sensor measurements, for example, from cameras and LiDARs to provide more reliable and accurate localization information.

## Problem Addressed

Automated driving requires reliable position, velocity, and attitude estimation, but low-cost IMUs drift rapidly and GNSS pseudorange errors are non-Gaussian and time-varying, challenging robust multi-sensor fusion.

## Key Contributions

- Cost-effective tightly coupled GNSS/on-board sensor fusion localization framework based on factor graph optimization
- Novel IMU/Dynamics pre-integration based on a two-degree-of-freedom vehicle dynamics model with wheel-speed and steering-angle sensors
- Gaussian mixture model characterization of pseudorange noise with online EM estimation over sliding-window residuals
- Reliable localization demonstrated across urban canyons, tunnels, and wooded areas

## Conclusions

Comprehensive experiments in challenging scenarios including urban canyons, tunnels, and wooded areas confirm reliable localization under varying GNSS signal conditions. The method improves position RMSE by 39.4% over the state of the art, and the framework generalizes to additional sensors such as cameras and LiDARs.
