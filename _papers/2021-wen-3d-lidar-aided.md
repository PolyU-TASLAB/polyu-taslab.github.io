---
title: 3D LiDAR Aided GNSS Real-time Kinematic Positioning
authors:
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2021-10-13'
doi: https://doi.org/g7vx59
image: images/papers/cards/2021-wen-3d-lidar-aided.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Wen_3D_Lidar_Aided.pdf
tags:
- FGO
- 3D LiDAR
- NLOS
- RTK
- 3DMA GNSS
citation_id: doi:10.33012/2021.18072
---

## Abstract

Global navigation satellite system real-time kinematic (GNSS-RTK) positioning is an indispensable source for providing absolute positioning for autonomous driving vehicles (ADV), due to its high accuracy when a fixed solution is achieved. 
Satisfactory accuracy can be obtained in open areas. However, the performance of GNSS-RTK can be significantly degraded by signal reflections from buildings, causing multipath effects and non-line-of-sight (NLOS) receptions. To fill this gap, this paper proposed a novel method to exclude the potential GNSS NLOS receptions, aided by the local environment description generated with 3D LiDAR and inertial sensor, to further improve the GNSS-RTK. The local environment description, the 3D point cloud map, is built via LiDAR/inertial integration using factor graph optimization. Then the potential GNSS NLOS receptions are detected and remove using the 3D point cloud maps before the GNSS-RTK positioning. Finally, the improved GNSS-RTK positioning is adopted to correct the drift of the 3D point cloud map derived from LiDAR/inertial integration. The effectiveness of the proposed method is verified through a challenging dataset collected in urban canyons of Hong Kong using the automobilelevel low-cost GNSS receiver.

## Problem Addressed

GNSS-RTK provides absolute positioning for autonomous driving vehicles but is significantly degraded in urban canyons by multipath effects and NLOS receptions caused by signal reflections from buildings.

## Key Contributions

- First work enabling GNSS NLOS exclusion for GNSS-RTK positioning using LiDAR/inertial integration.
- Real-time 3D point cloud map built via LiDAR/inertial factor graph optimization as local environment description.
- Potential NLOS receptions detected and removed against the point cloud map before GNSS-RTK positioning.
- Improved GNSS-RTK solutions used to correct drift of the LiDAR/inertial point cloud map.

## Conclusions

On a challenging Hong Kong urban canyon dataset with a low-cost automobile-level receiver, GNSS-RTK accuracy improved from 2.43 to 1.95 meters with the proposed NLOS exclusion. The RTK fixed rate remains limited by poor satellite geometry after exclusion, motivating future use of perceived environmental features and multiple LiDARs.
