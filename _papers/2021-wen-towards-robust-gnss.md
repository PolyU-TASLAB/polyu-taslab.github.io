---
title: Towards Robust GNSS Positioning and Real-time Kinematic Using Factor Graph Optimization
authors:
- Weisong Wen
- Li-Ta Hsu
publisher: 2021 IEEE International Conference on Robotics and Automation (ICRA)
date: '2021-05-30'
doi: https://doi.org/gprd6g
image: images/papers/cards/2021-wen-towards-robust-gnss.jpg
citation_id: doi:10.1109/icra48506.2021.9562037
---

## Abstract

Global navigation satellite systems (GNSS) are one of the utterly popular sources for providing globally referenced positioning for autonomous systems. However, the performance of the GNSS positioning is significantly challenged in urban canyons, due to the signal reflection and blockage from buildings. Given the fact that the GNSS measurements are highly environmentally dependent and time-correlated, the conventional filtering-based method for GNSS positioning cannot simultaneously explore the time-correlation among historical measurements. As a result, the filtering-based estimator is sensitive to unexpected outlier measurements. In this paper, we present a factor graph-based formulation for 
GNSS positioning and real-time kinematic (RTK). The formulated factor graph framework effectively explores the time-correlation of pseudorange, carrier-phase, and doppler measurements, and leads to the non-minimal state estimation of the GNSS receiver. The feasibility of the proposed method is evaluated using datasets collected in challenging urban canyons of Hong Kong and significantly improved positioning accuracy is obtained, compared with the filtering-based estimator.

## Problem Addressed

GNSS measurements are highly environment-dependent and time-correlated, but conventional filtering-based estimators cannot exploit the time correlation among historical measurements, making them sensitive to unexpected outliers in urban canyons.

## Key Contributions

- Factor graph formulation for GNSS positioning and RTK exploring time correlation of pseudorange, carrier-phase, and Doppler measurements.
- Non-minimal state estimation of the GNSS receiver with easy integration of additional sensors such as LiDAR odometry.
- First open-source FGO implementation for GNSS positioning and RTK, with accompanying datasets released.
- Evaluated on challenging datasets collected in Hong Kong urban canyons.

## Conclusions

The factor graph-based framework effectively mitigates the effects of GNSS outlier measurements, yielding significantly improved accuracy for both GNSS positioning and GNSS-RTK compared with filtering-based estimators. Future work targets cycle slip detection and adding more sensors to increase the RTK fixed rate.
