---
title: '3DIO: Low-Drift 3-D Deep-Inertial Odometry for Indoor Localization Using an IMU'
authors:
- Shiyu Bai
- Weisong Wen
- Chuang Shi
publisher: IEEE Internet of Things Journal
date: '2024-12-23'
doi: https://doi.org/g9hrnm
image: images/papers/cards/2024-bai-3dio-lowdrift-3d.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/3DIO_Low-Drift_3-D_Deep-Inertial_Odometry_for_Indoor_Localization_Using_an_IMU.pdf
tags:
- 3-D space
- deep learning
- indoor localization
- inertial measurement unit (IMU)
- inertial odometry
- Invariant extended Kalman filter (InEKF).
citation_id: doi:10.1109/JIOT.2024.3521404
---

## Abstract

The use of mobile devices for indoor localization has proven to be a convenient solution for pedestrians in Internet of Things (IoTs) applications. Radiofrequency (RF) signals, including Wi-Fi, Bluetooth, and others, are among the most commonly used sources. However, their availability cannot be guaranteed in all scenarios. Although pedestrian dead reckoning (PDR) using an inertial measurement unit (IMU) provides a self-contained positioning solution, it is susceptible to error accumulation due to heading uncertainties and varying motions.
This article presents a low-drift 3-D deep-inertial odometry (DIO) method for indoor pedestrian localization using an IMU.
The proposed approach employs a neural network to regress speeds within the human body frame, ensuring that the speeds are unaffected by absolute heading. These regressed speeds are integrated with inertial navigation to determine position. To enhance accuracy, the method incorporates an invariant extended
Kalman filter (InEKF)-based integration for state estimation.
Additionally, a learned height is included in the filter to improve
3-D position estimation. The performance of the proposed method is validated through real-world tests in various environments.
Results demonstrate that the proposed method outperforms traditional PDR, robust neural inertial navigation (RONIN), and
EKF-based techniques. Furthermore, this article examines the method from multiple perspectives, highlighting its strengths in addressing heading drift and varying motions, as well as the impact of height constraints and behavior-based position corrections. The video (YouTube) or (BiliBili) is shared to showcase our work.

## Problem Addressed

RF-based indoor localization (Wi-Fi, Bluetooth) cannot be guaranteed in all scenarios, while IMU-based pedestrian dead reckoning is self-contained but suffers error accumulation from heading uncertainties and varying motions.

## Key Contributions

- Deep learning regression of forward and vertical speeds in the body frame, independent of absolute heading
- 3-D deep-inertial odometry (3DIO) using an invariant extended Kalman filter to fuse learned speeds with strapdown inertial navigation
- Learned height constraint incorporated into the filter to reduce vertical errors
- Real-world validation across various environments, outperforming PDR, RONIN, and EKF-based techniques

## Conclusions

Field tests across various environments show that 3DIO effectively mitigates error drift in 3-D scenarios using only an IMU and significantly outperforms traditional IMU-only localization methods, including PDR, RONIN, and EKF-based techniques. A stated limitation is the assumption that the smartphone is held relatively static with respect to the human body, which future work will address with learned rotation compensation.
