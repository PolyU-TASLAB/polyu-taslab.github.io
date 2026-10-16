---
title: 3D LiDAR Aided GNSS NLOS Mitigation in Urban Canyons
authors:
- Weisong Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Transportation Systems
date: '2022-10-01'
doi: https://doi.org/gqhp38
image: images/papers/cards/2022-wen-3d-lidar-aided.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/3D_LiDAR_Aided_GNSS_NLOS_Mitigation_in_Urban_Canyons.pdf
tags:
- GNSS
- 3D LiDAR
- GNSS NLOS detection
- NLOS correction and remodeling
- automobile-level GNSS
- receiver
- urban canyons
citation_id: doi:10.1109/TITS.2022.3167710
---

## Abstract

This paper proposes a 3D LiDAR aided global navigation satellite system (GNSS) non-line-of-sight (NLOS) mitigation method due to both static buildings and dynamic objects.
A sliding window map describing the environment of the egovehicle is first generated, based on real-time 3D point clouds from a 3D LiDAR sensor. Subsequently, the NLOS receptions are detected based on the sliding window map using a proposed quick searching method which eliminates the reliance on the initial guessing of the position of the GNSS receiver. Instead of directly excluding the detected NLOS satellites from further estimating the position, this paper rectifies the pseudo-range measurement model by (1) correcting the pseudo-range measurements if the reflecting point of the NLOS signals is detected within the sliding window map, and (2) remodeling the uncertainty in the NLOS pseudo-range measurement using a novel weighting scheme.
The performance of the proposed model was experimentally evaluated in several typical urban canyons in Hong Kong using an automobile-level GNSS receiver. Furthermore, the potential of the proposed NLOS mitigation method in GNSS and the integration of inertial navigation systems were evaluated via factor graph optimization.

## Problem Addressed

GNSS positioning in urban canyons suffers severely from NLOS receptions caused by both static buildings and dynamic objects, while 3D building model-based methods cannot describe the real-time environment.

## Key Contributions

- Real-time sliding window map from 3D LiDAR point clouds enlarging the effective field of view for NLOS detection
- Quick searching method for NLOS detection eliminating reliance on initial position guesses
- Pseudorange correction when the NLOS reflection point is detected within the sliding window map
- Novel weighting scheme remodeling uncertainty of NLOS pseudorange measurements instead of excluding satellites

## Conclusions

Experiments in typical Hong Kong urban canyons with an automobile-level GNSS receiver show that potential NLOS receptions caused by static buildings, dynamic objects, and semi-static infrastructure can be detected, remodeled, and corrected. The method also benefits GNSS and inertial integration via factor graph optimization and can be adapted to multi-LiDAR systems. Since the remaining positioning error was still about 17 meters in the dense Urban Canyon 2, future work will integrate LiDAR odometry and improve orientation accuracy.
