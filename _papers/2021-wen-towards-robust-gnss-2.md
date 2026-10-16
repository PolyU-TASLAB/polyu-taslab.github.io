---
title: Towards Robust GNSS Positioning and Real-time Kinematic Using Factor Graph Optimization
authors:
- Weisong Wen
- Li-Ta Hsu
publisher: 2021 IEEE International Conference on Robotics and Automation (ICRA)
date: '2021-05-30'
doi: https://doi.org/gprd6g
image: images/papers/cards/2021-wen-towards-robust-gnss-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Towards_Robust_GNSS_Positioning_and_Real-time_Kinematic_Using_Factor_Graph_Optimization.pdf
tags:
- GNSS
- GNSS-RTK
- Localization
- urban canyons
- mapping
- Autonomous vehicle
- FGO
citation_id: doi:10.1109/ICRA48506.2021.9562037
---

## Abstract

Global navigation satellite systems (GNSS) are one of the utterly popular sources for providing globally referenced positioning for autonomous systems. However, the performance of the GNSS positioning is significantly challenged in urban canyons, due to the signal reflection and blockage from buildings. Given the fact that the GNSS measurements are highly environmentally dependent and time-correlated, the conventional filtering-based method for GNSS positioning cannot simultaneously explore the time-correlation among historical measurements. As a result, the filtering-based estimator is sensitive to unexpected outlier measurements. In this paper, we present a factor graph-based formulation for 
GNSS positioning and real-time kinematic (RTK). The formulated factor graph framework effectively explores the time-correlation of pseudorange, carrier-phase, and doppler measurements, and leads to the non-minimal state estimation of the GNSS receiver. The feasibility of the proposed method is evaluated using datasets collected in challenging urban canyons of Hong Kong and significantly improved positioning accuracy is obtained, compared with the filtering-based estimator.

## Problem Addressed

GNSS positioning is significantly challenged in urban canyons by signal reflection and blockage, and filtering-based estimators cannot exploit the time-correlation among historical measurements, making them sensitive to outlier measurements.

## Key Contributions

- Formulates GNSS positioning and RTK within a factor graph optimization framework
- Exploits time-correlation of pseudorange, carrier-phase, and Doppler measurements for non-minimal state estimation
- Enables easy integration of additional sensors such as LiDAR odometry into the framework
- Releases the first open-source FGO implementation for GNSS positioning and RTK with datasets

## Conclusions

Evaluation on datasets collected in the urban canyons of Hong Kong shows the factor graph based formulation effectively mitigates the effects of GNSS outlier measurements. It derives improved accuracy in both GNSS positioning and GNSS-RTK positioning compared with filtering-based estimators. Future work includes cycle slip detection for ambiguity resolution and adding more sensors to increase the RTK fixed rate.
