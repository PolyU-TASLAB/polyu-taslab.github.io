---
title: An Improved Inertial Preintegration Model in Factor Graph Optimization for High Accuracy Positioning of Intelligent Vehicles
authors:
- Liang Zhang
- Weisong Wen
- Li-Ta Hsu
- Tao Zhang
publisher: IEEE Transactions on Intelligent Vehicles
date: '2024-01-01'
doi: https://doi.org/g8xprc
image: images/papers/cards/2024-zhang-improved-inertial-preintegration.jpg
citation_id: doi:10.1109/TIV.2023.3282623
---

## Abstract

Accurate and reliable positioning is of great importance for the realization of intelligent vehicles (IV). Factor graph optimization (FGO) has been popularized in the field of robotics for state estimation. As a ubiquitous sensor, the IMU is widely used for vehicular positioning based on the preintegration theory using FGO. However, the existing preintegration model fails to consider the earth's rotation, which challenges the attitude and positioning performance of vehicles equipped with high-precision inertial measurement units (IMU). To fill this gap, an accurate IMU factor that accounts for the earth's rotation rate is designed in this article. First, an exact preintegration measurement model is derived based on a high-precision inertial navigation system (INS) mechanization. The proposed factor is more accurate and it enables the application of the FGO more suitable for inertial-based integrated navigation with different precision IMUs. In both simulation and field tests, the INS/ Global Navigation Satellite System (GNSS) integration, as a representative of inertial-based integrated navigation, is used to verify the performance of the proposed preintegration factor. The navigation results using our experimental car reveal that the proposed model leads to a more accurate estimation, outperforming the traditional preintegration models, especially in the aspect of attitude estimation.

## Problem Addressed

Existing IMU preintegration models ignore the Earth's rotation, restricting factor graph optimization to low-precision IMUs and degrading attitude and positioning performance for vehicles equipped with high-precision IMUs.

## Key Contributions

- Exact IMU preintegration measurement model accounting for Earth's rotation, derived from high-precision INS mechanization
- Unified mathematical formulation applicable to inertial-based integrated navigation with IMUs of different precision levels
- Accurate IMU factor design making FGO suitable for high-grade inertial sensors
- Validated in simulation and automotive field tests with INS/GNSS integration

## Conclusions

Simulation and field tests with INS/GNSS integration show that the proposed preintegration model yields more accurate estimation than traditional preintegration models, with especially clear advantages in attitude estimation, broadening the application of FGO in inertial-based integrated navigation.
