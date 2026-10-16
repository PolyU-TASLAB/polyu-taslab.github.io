---
title: 3D LiDAR Aided GNSS and Its Tightly Coupled Integration with INS Via Factor Graph Optimization
authors:
- Weisong Wen
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2020-10-28'
doi: https://doi.org/g8tzcv
image: images/papers/cards/2020-wen-3d-lidar-aided.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/3D_LiDAR_Aided_GNSS_and_Its_Tightly_Coupled_Integration_with_INS_Via_FGO.pdf
tags:
- FGO
- 3D LiDAR
- NLOS
- 3DMA GNSS
citation_id: doi:10.33012/2020.17557
---

## Abstract

Global navigation satellite system (GNSS) positioning is an indispensable source of data for providing absolute positioning for autonomous driving vehicles (ADV). Satisfactory accuracy can be obtained in sparse areas. However, the performance of GNSS can be significantly degraded by signal reflections from buildings, causing multipath effects and non-line-of-sight (NLOS) receptions. State-of-the-art 3D mapping aided (3DMA) GNSS can significantly mitigate the effects of signal reflections caused by static buildings. However, this approach relies heavily on an initial guess of the GNSS receiver, and on the availability of 3D building models. Moreover, the NLOS reception caused by surrounding dynamic objects, such as double-decker buses, cannot be mitigated. To fill this gap, in this paper we propose a novel 3D LiDAR aided GNSS positioning method which makes use of an onboard 3D LiDAR sensor to detect and correct NLOS reception caused by both static buildings and dynamic objects. A novel sliding window map surrounding the ego-vehicle is first generated, based on real-time 3D point clouds from a 3D LiDAR sensor. Then, NLOS receptions are detected based on a real-time sliding window map using a proposed fast searching method. 
The proposed NLOS detection method does not rely on the initial guess of the GNSS receiver. Instead of directly excluding the detected NLOS satellites from further positioning estimation, the algorithm reported in this paper rectifies the pseudorange measurement model by (1) correcting the pseudorange measurements if the reflecting point of NLOS signals is detected inside the sliding window map, and (2) remodeling the uncertainty of the NLOS pseudorange measurement using a new weighting scheme. Finally, both the corrected and healthy pseudorange measurements are tightly integrated with an inertial navigation system (INS) using factor graph optimization (FGO). We evaluated the performance of the proposed method in two typical urban canyons in Hong Kong and found that improved accuracy is obtained even in such environments.

## Problem Addressed

State-of-the-art 3D mapping aided GNSS relies heavily on an initial guess of the receiver and the availability of 3D building models, and cannot mitigate NLOS receptions caused by surrounding dynamic objects such as double-decker buses.

## Key Contributions

- Onboard 3D LiDAR detects and corrects NLOS receptions from both static buildings and dynamic objects.
- Sliding-window map from real-time point clouds with a fast NLOS searching method independent of initial guess.
- Pseudorange correction when the NLOS reflecting point is found, plus a new weighting scheme remodeling NLOS uncertainty.
- Tight integration of corrected and healthy pseudorange measurements with INS via factor graph optimization.

## Conclusions

NLOS receptions caused by static buildings, dynamic objects, and even semi-static infrastructure can be detected, remodeled, and corrected without reliance on an initial guess or 3D building models. Remaining positioning error still reaches about 10 meters in the densest urban canyon evaluated, motivating future integration of LiDAR odometry.
