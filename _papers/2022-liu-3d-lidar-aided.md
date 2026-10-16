---
title: 3D LiDAR Aided GNSS Real-time Kinematic Positioning via Coarse-to-fine Batch Optimization for High Accuracy Mapping in Dense Urban Canyons
authors:
- Xikun Liu
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2022-10-20'
doi: https://doi.org/g8t5rz
image: images/papers/cards/2022-liu-3d-lidar-aided.jpg
buttons:
- type: manubot
  text: paper
  link: https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/publications/papers/xxx.pdf
tags: []
citation_id: doi:10.33012/2022.18545
---

## Abstract

Global navigation satellite system real-time kinematic (GNSS-RTK) positioning is an indispensable source for providing absolute positioning for autonomous driving vehicles (ADV), due to its high accuracy when a fixed solution is achieved. 
Satisfactory accuracy can be obtained in open areas. However, the performance of GNSS-RTK can be significantly degraded by signal reflections from buildings, causing multipath effects and non-line-of-sight (NLOS) receptions. To fill this gap, this paper proposed a novel method to exclude the potential GNSS NLOS receptions, aided by the local environment description generated with 3D LiDAR and inertial sensor, to further improve the GNSS-RTK. The local environment description, the 3D point cloud map, is built via LiDAR/inertial integration using factor graph optimization. Then the potential GNSS NLOS receptions are detected and remove using the 3D point cloud maps before the GNSS-RTK positioning. Finally, the improved GNSS-RTK positioning is adopted to correct the drift of the 3D point cloud map derived from LiDAR/inertial integration. The effectiveness of the proposed method is verified through a challenging dataset collected in urban canyons of Hong Kong using the automobile-level low-cost GNSS receiver.

## Problem Addressed

GNSS-RTK positioning, an indispensable absolute positioning source for autonomous driving, is significantly degraded in dense urban canyons by multipath and NLOS receptions caused by building reflections. Reliable high-accuracy mapping in these environments requires removing such corrupted measurements.

## Key Contributions

- First work enabling GNSS NLOS exclusion for RTK positioning using LiDAR/inertial integration
- Local 3D point cloud map built via LiDAR/inertial factor graph optimization to detect and remove NLOS before RTK
- Improved RTK solutions fed back to correct drift of the LiDAR/inertial point cloud map
- Evaluation on challenging Hong Kong urban-canyon data with a low-cost automobile GNSS receiver

## Conclusions

With the proposed NLOS exclusion, GNSS-RTK accuracy improved from 2.43 m to 1.95 m on the evaluated urban-canyon dataset. The RTK fixed rate remains limited by poor satellite geometry after NLOS exclusion. Future work will use perceived environmental features to improve geometry constraints and employ multiple 3D LiDARs to widen the field of view of environment reconstruction.
