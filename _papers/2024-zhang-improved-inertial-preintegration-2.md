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
image: images/papers/cards/2024-zhang-improved-inertial-preintegration-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/An_Improved_Inertial_Preintegration_Model_in_Factor_Graph_Optimization_for_High_Accuracy_Positioning_of_Intelligent_Vehicles.pdf
tags:
- Factor graph optimization
- IMU preintegration
- inertial navigation
- integrated navigation
- vehicle navigation
citation_id: 10.1109/TIV.2023.3282623
---

## Abstract

Accurate and reliable positioning is of great importance for the realization of intelligent vehicles (IV). Factor graph optimization (FGO) has been popularized in the field of robotics for state estimation. As a ubiquitous sensor, the IMU is widely used for vehicular positioning based on the preintegration theory using
FGO. However, the existing preintegration model fails to consider the earth's rotation, which challenges the attitude and positioning performance of vehicles equipped with high-precision inertial measurement units (IMU). To fill this gap, an accurate IMU factor that accounts for the earth's rotation rate is designed in this article.
First, an exact preintegration measurement model is derived based on a high-precision inertial navigation system (INS) mechanization.
The proposed factor is more accurate and it enables the application of the FGO more suitable for inertial-based integrated navigation with different precision IMUs. In both simulation and field tests, the INS/ Global Navigation Satellite System (GNSS) integration, as a representative of inertial-based integrated navigation, is used to verify the performance of the proposed preintegration factor.
The navigation results using our experimental car reveal that the proposedmodelleadstoamoreaccurateestimation,outperforming the traditional preintegration models, especially in the aspect of attitude estimation.

## Problem Addressed

Existing IMU preintegration models in factor graph optimization ignore the Earth's rotation, which limits attitude and positioning performance for vehicles equipped with high-precision IMUs.

## Key Contributions

- Exact IMU preintegration measurement model derived from high-precision INS mechanization accounting for Earth's rotation rate
- Unified mathematical expressions applicable to inertial-based integrated navigation with IMUs of different precision grades
- Accurate IMU factor making FGO suitable for high-grade IMU applications
- Verified through INS/GNSS integration in both simulation and field tests

## Conclusions

Simulations and field tests show the proposed model yields more accurate estimation than traditional preintegration models, especially in attitude estimation, broadening the application of FGO in inertial-based integrated navigation. Future work includes long-term navigation for autonomous underwater and aerial vehicles with high-grade inertial sensors, and robust optimization under complex environmental interference.
