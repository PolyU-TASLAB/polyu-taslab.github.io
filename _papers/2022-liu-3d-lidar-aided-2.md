---
title: 3D LiDAR Aided GNSS NLOS Mitigation for Reliable GNSS-RTK Positioning in Urban Canyons
authors:
- Xikun Liu
- Weisong Wen
- Feng Huang
- Han Gao
- Yongliang Wang
- Li-Ta Hsu
publisher: arXiv
date: '2022-01-01'
doi: https://doi.org/g8t6kn
image: images/papers/cards/2022-liu-3d-lidar-aided-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2212.05477v1.pdf
tags:
- 3D LiDAR
- GNSS-RTK
- Perception-aided integration
- NLOS exclusion
- Geometry distribution
- Urban canyons
citation_id: doi:10.48550/arXiv.2212.05477
---

## Abstract

GNSS and LiDAR odometry are complementary as they provide absolute and relative positioning, respectively. Their integration in a loosely-coupled manner is straightforward but is challenged in urban canyons due to the GNSS signal reflections. 
Recent proposed 3D LiDAR-aided (3DLA) GNSS methods employ the point cloud map to identify the non-line-of-sight (NLOS) reception of GNSS signals. This facilitates the GNSS receiver to obtain improved urban positioning but not achieve a sub-meter level. GNSS real-time kinematics (RTK) uses carrier phase measurements to obtain decimeter-level positioning. In urban areas, the GNSS RTK is not only challenged by multipath and 
NLOS-affected measurement but also suffers from signal blockage by the building. The latter will impose a challenge in solving the ambiguity within the carrier phase measurements. In the other words, the model observability of the ambiguity resolution (AR) is greatly decreased. This paper proposes to generate virtual satellite (VS) measurements using the selected LiDAR landmarks from the accumulated 3D point cloud maps (PCM). These LiDAR-PCMmade VS measurements are tightly-coupled with GNSS pseudorange and carrier phase measurements. Thus, the VS measurements can provide complementary constraints, meaning providing low-elevation-angle measurements in the across-street directions. As a result, the model observability of the AR is improved. The implementation is done using factor graph optimization to solve an accurate float solution of the ambiguity before it is fed into LAMBDA. The effectiveness of the proposed method has been validated by the evaluation conducted on our recently open-sourced challenging dataset, UrbanNav. The result shows the fix rate of the proposed 3DLA GNSS RTK is about 30% while the conventional GNSS-RTK only achieves about 14%. In addition, the proposed method achieves sub-meter positioning accuracy in most of the data collected in challenging urban areas.

## Problem Addressed

GNSS-RTK can reach decimeter-level positioning but in urban canyons it is degraded by multipath and NLOS measurements and by building blockage that reduces the model observability of ambiguity resolution; existing 3D LiDAR-aided GNSS methods improve positioning but do not reach sub-meter level.

## Key Contributions

- Drift-free 3D sliding-window point cloud map for GNSS NLOS detection and exclusion, with map drift corrected by improved RTK
- Virtual satellite measurements generated from selected LiDAR landmarks to improve satellite geometry in across-street directions
- Tightly coupled factor graph optimization of GNSS pseudorange/carrier phase, IMU, and virtual satellite measurements before LAMBDA
- Mathematical derivation of geometry improvement and evaluation on the open-sourced UrbanNav dataset

## Conclusions

The proposed 3D LiDAR-aided GNSS-RTK raised the fix rate to about 30% compared with about 14% for conventional GNSS-RTK, and achieved sub-meter positioning accuracy on most of the challenging urban data. On evaluated Hong Kong sequences, 2D mean error was reduced from 1.81 m (GNSS-RTK) to 0.61 m and 0.49 m by the 3DLA variants, with fixed rates of 12.93% and 19.19% versus 3.45%. Remaining errors are mainly attributed to multipath receptions, which are harder to identify; future work targets multipath detection and joint optimization over more epochs.
