---
title: Low‐cost solid‐state LiDAR/inertial‐based localization with prior map for autonomous systems in urban scenarios
authors:
- Yihan Zhong
- Feng Huang
- Jiachen Zhang
- Weisong Wen
- Li‐Ta Hsu
publisher: IET Intelligent Transport Systems
date: '2022-09-20'
doi: https://doi.org/g8t577
image: images/papers/cards/2022-zhong-lowcost-solidstate-lidarinertialbased.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Zhong_Low_cost_Lidar.pdf
tags:
- 3D LiDAR
- weighting estimation
- dynamic objects
- urban areas
- autonomous driving
citation_id: doi:10.1049/itr2.12273
---

## Abstract

A low-cost and accurate positioning solution is significant for the massive deployment of fully autonomous driving vehicles (ADV). Conventional mechanical LiDAR has proven its performance, but its high cost hinders the massive production of autonomous vehicles. This paper proposes a low-cost LiDAR/inertial-based localization solution for autonomous systems with prior maps in urban areas. Instead of relying on the costly mechanical LiDAR, this paper proposes to utilize the solid-state LiDAR (SSL) with the prior map to estimate the position of the vehicle by matching the real-time point clouds from the SSL and the prior map using the normal distribution transformation (NDT) algorithm. However, the field of view (FOV) of the SSL is signifcantly smaller than the conventional mechanical LiDAR, which can easily lead to failure during the NDT map matching. To fill this gap, this paper proposes to exploit the complementariness of the inertial measurement unit (IMU) and the SSL, where the IMU pre-integration provides a coarse but high-frequency initial guess to the map matching. To evaluate the effectiveness of the proposed method in this paper, the authors collect the dataset in two typical urban scenarios through a pedestrian hand-hold and a vehicle driving condition. The results reveal that the SSL-only-based localization is significantly challenged in dynamic scenarios. With the help of the IMU, the robustness of the proposed method is significantly improved, achieving an accuracy of within 0.5 m. To show the sensitivity of the SSL-based map matching against the initial guess of the state, this paper also presents the convergence results of the map matching under different levels of accuracy in terms of the initial guess.

## Problem Addressed

Mechanical LiDAR delivers proven localization performance but its high cost hinders mass production of autonomous vehicles, while low-cost solid-state LiDAR has a much smaller field of view that easily causes NDT map-matching failure when localizing against a prior map.

## Key Contributions

- Solid-state LiDAR localization with a prior map via NDT matching for drift-free positioning in urban canyons
- IMU pre-integration providing a coarse but high-frequency initial guess to compensate for the small SSL field of view
- Sensitivity analysis of SSL map matching against initial-guess accuracy and NDT grid size
- Step-by-step validation on hand-held pedestrian and vehicle-driving datasets in two urban scenarios

## Conclusions

SSL-only localization is significantly challenged in dynamic scenarios, but with IMU assistance the proposed method achieved robust performance with accuracy within 0.5 m. The paper also quantifies how map-matching convergence depends on the accuracy of the initial guess. Future work includes combining multiple low-cost SSLs to approach the field of view of mechanical LiDAR and using them to keep the HD map fresh.
