---
title: Coarse-to-Fine Loosely-Coupled LiDAR-Inertial Odometry for Urban Positioning and Mapping
authors:
- Jiachen Zhang
- Weisong Wen
- Feng Huang
- Xiaodong Chen
- Li-Ta Hsu
publisher: Remote Sensing
date: '2021-06-17'
doi: https://doi.org/gkzjdq
image: images/papers/cards/2021-zhang-coarsetofine-looselycoupled-lidarinertial.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/remotesensing-13-02371-v2-1.pdf
tags:
- LiDAR-inertial odometry
- loosely-coupled integration
- adaptive covariance estimation
- urban canyons
- mapping
- Autonomous system
citation_id: doi:10.3390/rs13122371
---

## Abstract

Accurate positioning and mapping are significant for autonomous systems with navigation requirements. In this paper, a coarse-to-fine loosely-coupled (LC) LiDAR-inertial odometry (LC-LIO) that could explore the complementariness of LiDAR and inertial measurement unit (IMU) was proposed for the real-time and accurate pose estimation of a ground vehicle in urban environments.
Different from the existing tightly-coupled (TC) LiDAR-inertial fusion schemes which directly use all the considered ranges and inertial measurements to optimize the vehicle pose, the method proposed in this paper performs loosely-couped integrated optimization with the high-frequency motion prediction, which was produced by IMU integration based on optimized results, employed as the initial guess of LiDAR odometry to approach the optimality of LiDAR scan-to-map registration. As one of the prominent contributions, thorough studies were conducted on the performance upper bound of the TC LiDAR-inertial fusion schemes and LC ones, respectively. Furthermore, the experimental verification was performed on the proposition that the proposed pipeline can fully relax the potential of the LiDAR measurements (centimeter-level ranging accuracy) in a coarse-to-fine way without being disturbed by the unexpected IMU bias. Moreover, an adaptive covariance estimation method employed during LC optimization was proposed to explain the uncertainty of LiDAR scan-to-map registration in dynamic scenarios. Furthermore, the effectiveness of the proposed system was validated on challenging real-world datasets. Meanwhile, the process that the proposed pipelines realized the coarse-to-fine LiDAR scan-to-map registration was presented in detail. Comparing with the existing state-of-the-art TC-LIO, the focus of this study would be placed on that the proposed
LC-LIO work could achieve similar or better accuracy with a reduced computational expense.

## Problem Addressed

Tightly coupled LiDAR-inertial fusion optimizes all range and inertial measurements jointly, so unexpected IMU bias can disturb pose estimation and limit the potential of centimeter-level LiDAR ranging. A loosely coupled alternative that fully exploits LiDAR accuracy is underexplored.

## Key Contributions

- Proposes a coarse-to-fine loosely coupled LiDAR-inertial odometry using IMU prediction as scan-matching initial guess
- Studies the performance upper bounds of tightly coupled and loosely coupled LiDAR-inertial fusion schemes
- Introduces adaptive covariance estimation to model scan-to-map registration uncertainty in dynamic scenarios
- Validates the system on challenging real-world urban datasets

## Conclusions

The proposed loosely coupled LiDAR-inertial odometry fully relaxes the potential of LiDAR measurements in a coarse-to-fine manner without being disturbed by IMU bias. It achieves similar or better accuracy than existing state-of-the-art tightly coupled LiDAR-inertial odometry with reduced computational expense on challenging real-world datasets.
