---
title: Dynamic Object-Aware LiDAR Odometry Aided by Joint Weightings Estimation in Urban Areas
authors:
- Feng Huang
- Weisong Wen
- Jiachen Zhang
- Chaoqun Wang
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Vehicles
date: '2024-02-01'
doi: https://doi.org/g5w4mt
image: images/papers/cards/2024-huang-dynamic-objectaware-lidar.jpg
citation_id: doi:10.1109/TIV.2023.3338141
---

## Abstract

Dynamic object detection from point clouds has been widely studied in recent years to achieve accurate and robust
LiDAR odometry for autonomous driving. Satisfactory accuracy can be achieved by dynamic object detection from point clouds has been widely studied in recent years to achieve accurate and robust
LiDAR odometry for autonomous driving. Satisfactory accuracy can be achieved by detecting and removing the object points in the urban environment. However, it is still not clear how dynamic objects numerically affect the performance of LiDAR odometry.
In addition, the existing solutions tended to directly remove the
LiDAR features belonging to the dynamic object, which can lead to the degradation of the geometry constraints of the surrounding features. This paper aims to give answers to these problems by evaluating the effects of dynamic objects as well as reweighting both dynamic objects and static objects. Three factors affecting the performance of LiDAR odometry in highly dynamic scenarios, including the number, geometry distribution, and velocity of the dynamic objects, are first extensively studied using generated scenariosbyleveragingrealdata.Insteadofbrutelyremovingthedynamic features, this paper proposes to adaptively assign weightings to the dynamic features. Then both the dynamic and static features are employed to estimate the LiDAR odometry. The effectiveness of the proposed method is verified using UrbanNav and nuScenes datasets that include numerous dynamic and static objects. To benefit the community, the implementation of the dynamic vehicle simulator and the code for the proposed method are both open-sourced.

## Problem Addressed

Dynamic objects degrade LiDAR odometry in urban areas, yet their numerical impact is unclear, and directly removing dynamic features can weaken the geometric constraints provided by surrounding features.

## Key Contributions

- Extensive numerical analysis of how dynamic object number, geometric distribution, and velocity degrade LiDAR odometry
- Adaptive joint weighting of dynamic and static features instead of brute-force dynamic feature removal
- Dynamic vehicle simulator generating controllable evaluation scenarios from real point cloud data
- Validated on UrbanNav and nuScenes datasets; simulator and method code open-sourced

## Conclusions

Experiments on the UrbanNav and nuScenes datasets show that reweighting dynamic objects improves state estimation in both highly dynamic and adverse scenes, outperforming the traditional method and the dynamic-object-removal approach.
