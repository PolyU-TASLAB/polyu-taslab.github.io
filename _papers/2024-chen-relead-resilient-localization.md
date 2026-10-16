---
title: 'RELEAD: Resilient Localization with Enhanced LiDAR Odometry in Adverse Environments'
authors:
- Zhiqiang Chen
- Hongbo Chen
- Yuhua Qi
- Shipeng Zhong
- Dapeng Feng
- Jin Wu
- Weisong Wen
- Ming Liu
publisher: 2024 IEEE International Conference on Robotics and Automation (ICRA)
date: '2024-05-13'
doi: https://doi.org/g8t54t
image: images/papers/cards/2024-chen-relead-resilient-localization.jpg
citation_id: doi:10.1109/icra57147.2024.10611074
---

## Abstract

LiDAR-based localization is valuable for applications like mining surveys and underground facility maintenance. However, existing methods can struggle when dealing with uninformative geometric structures in challenging scenarios. This paper presents RELEAD, a LiDAR-centric solution designed to address scan-matching degradation. Our method enables degeneracy-free point cloud registration by solving constrained ESIKF updates in the front end and incorporates multisensor constraints, even when dealing with outlier measurements, through graph optimization based on Graduated
Non-Convexity (GNC). Additionally, we propose a robust Incremental Fixed Lag Smoother (rIFL) for efficient GNC-based optimization. RELEAD has undergone extensive evaluation in degenerate scenarios and has outperformed existing state-ofthe-art LiDAR-Inertial odometry and LiDAR-Visual-Inertial odometry methods.

## Problem Addressed

LiDAR-based localization for applications such as mining surveys and underground facility maintenance struggles when uninformative geometric structures cause scan-matching degradation in challenging scenarios.

## Key Contributions

- Degeneracy-eliminated LiDAR-inertial odometry analyzing 6-DOF alignment strength with a degradation detection module
- Constrained error-state iterated Kalman filter providing drift-free pose updates along ill-conditioned directions
- Failure-tolerant multi-sensor fusion via graph optimization based on Graduated Non-Convexity robust to outliers
- Robust incremental fixed-lag smoother enabling efficient GNC-based optimization
- Outperforms state-of-the-art LiDAR-inertial and LiDAR-visual-inertial odometry in degenerate scenarios

## Conclusions

RELEAD identifies environmental degradation and achieves precise, drift-free pose estimation along degradation directions through constrained optimization, while GNC factors robustly integrate multi-sensor constraints under outlier measurements. Its resilience is demonstrated through extensive experiments in degenerate scenarios.
