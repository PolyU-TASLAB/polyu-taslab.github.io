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
image: images/papers/cards/2024-huang-dynamic-objectaware-lidar-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Dynamic_Object-Aware_LiDAR_Odometry_Aided_by_Joint_Weightings_Estimation_in_Urban_Areas.pdf
- type: website
  link: https://github.com/DarrenWong/code_for_dynaLO
tags:
- 3D LiDAR
- weighting estimation
- dynamic objects
- urban areas
- autonomous driving
repo: https://github.com/DarrenWong/code_for_dynaLO
citation_id: 10.1109/TIV.2023.3338141
---

## Abstract

Dynamic object detection from point clouds has been widely studied in recent years to achieve accurate and robust LiDAR odometry for autonomous driving. Satisfactory accuracy can be achieved by dynamic object detection from point clouds has been widely studied in recent years to achieve accurate and robust LiDAR odometry for autonomous driving. Satisfactory accuracy can be achieved by detecting and removing the object points in the urban environment. However, it is still not clear how dynamic objects numerically affect the performance of LiDAR odometry. In addition, the existing solutions tended to directly remove the LiDAR features belonging to the dynamic object, which can lead to the degradation of the geometry constraints of the surrounding features. This paper aims to give answers to these problems by evaluating the effects of dynamic objects as well as reweighting both dynamic objects and static objects. Three factors affecting the performance of LiDAR odometry in highly dynamic scenarios, including the number, geometry distribution, and velocity of the dynamic objects, are first extensively studied using generated scenarios by leveraging real data. Instead of brutely removing the dynamic features, this paper proposes to adaptively assign weightings to the dynamic features. Then both the dynamic and static features are employed to estimate the LiDAR odometry. The effectiveness of the proposed method is verified using UrbanNav and nuScenes datasets that include numerous dynamic and static objects. To benefit the community, the implementation of the dynamic vehicle simulator and the code for the proposed method are both open-sourced.

## Problem Addressed

Dynamic objects degrade LiDAR odometry in urban areas, yet their numerical impact is unclear, and directly removing dynamic features weakens the geometric constraints of surrounding static features.

## Key Contributions

- Extensive numerical analysis of how number, geometric distribution, and velocity of dynamic objects affect LiDAR odometry
- Dynamic vehicle simulator leveraging real data to generate highly dynamic evaluation scenarios
- Adaptive joint weighting of dynamic and static features instead of brute-force removal of dynamic points
- Validation on UrbanNav and nuScenes datasets; simulator and code open-sourced

## Conclusions

The proposed joint weighting approach improves state estimation in both highly dynamic and adverse scenes, outperforming the traditional method and the prior dynamic-object-removal method. Future directions include generative AI for LiDAR scene generation, exploiting LiDAR-GNSS complementarity, and leveraging intelligent roadside infrastructure.
