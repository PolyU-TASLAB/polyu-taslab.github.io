---
title: Graph-Based Indoor 3D Pedestrian Location Tracking With Inertial-Only Perception
authors:
- Shiyu Bai
- Weisong Wen
- Dongzhe Su
- Li-Ta Hsu
publisher: IEEE Transactions on Mobile Computing
date: '2025-01-06'
doi: https://doi.org/g9gh5g
image: images/papers/cards/2025-bai-graphbased-indoor-3d.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Graph-Based_Indoor_3D_Pedestrian_Location_Tracking_With_Inertial-Only_Perception.pdf
tags:
- Indoor localization
- pedestrians
- inertial perception
- SLAM
- factor graph optimization
citation_id: doi:10.1109/TMC.2025.3526196
---

## Abstract

Pedestrian location tracking in emergency responses and environmental surveys of indoor scenarios tend to rely only on their own mobile devices, reducing the usage of external services. Low-cost and small-sized inertial measurement units (IMU) have been widely distributed in mobile devices. However, they suffer from high-level noises, leading to drift in position estimation over time. In this work, we present a graph-based indoor
3D pedestrian location tracking with inertial-only perception. The proposed method uses onboard inertial sensors in mobile devices alone for pedestrian state estimation in a simultaneous localization and mapping (SLAM) mode. It starts with a deep vertical odometry-aided 3D pedestrian dead reckoning (PDR) to predict the position in 3D space. Environment-induced behaviors, such as corner-turning and stair-taking, are regarded as landmarks.
Multi-hypothesis loop closures are formed using statistical methods to handle ambiguous data association. A factor graph optimization fuses 3D PDR and behavior loop closures for state estimation. Experiments in different scenarios are performed using a smartphone to evaluate the performance of the proposed method, which can achieve better location tracking than current learning-based and
filtering-based methods. Moreover, the proposed method is also discussed in different aspects, including the accuracy of offline optimization and proposed height regression, and the reliability of the multi-hypothesis behavior loop closures. The video (YouTube) or (BiliBili) is also shared to display our research.

## Problem Addressed

Low-cost IMUs in mobile devices exhibit high noise levels that cause position drift over time, limiting inertial-only indoor pedestrian tracking. Existing behavior-based SLAM approaches additionally suffer compromised estimation accuracy and ambiguous data association.

## Key Contributions

- Inertial-perception-only indoor 3D pedestrian SLAM operating on smartphones
- Deep vertical odometry-aided 3D pedestrian dead reckoning for 3D position prediction
- Environment-induced behaviors such as corner-turning and stair-taking exploited as landmarks
- Multi-hypothesis loop closures formed with statistical methods to resolve ambiguous data association
- Factor graph optimization fusing 3D PDR with behavior loop closures for state estimation

## Conclusions

Experiments with a smartphone in different scenarios show that the proposed method suppresses drift and achieves better location tracking than current learning-based and filtering-based methods. Batch (offline) factor graph optimization yields a better solution than filtering-based estimation, and the accuracy of the proposed height regression and the reliability of the multi-hypothesis behavior loop closures are confirmed.
