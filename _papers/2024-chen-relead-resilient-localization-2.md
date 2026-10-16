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
image: images/papers/cards/2024-chen-relead-resilient-localization-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/ChenZhiqiang2024ICRARELEAD.pdf
tags:
- ESIKF
- Graduated Non-Convexit
- Cremental Fixed Lag Smoothe
citation_id: 10.1109/ICRA57147.2024.10611074
---

## Abstract

LiDAR-based localization is valuable for applications like mining surveys and underground facility maintenance. However, existing methods can struggle when dealing with uninformative geometric structures in challenging scenarios. This paper presents RELEAD, a LiDAR-centric solution designed to address scan-matching degradation. Our method enables degeneracy-free point cloud registration by solving constrained ESIKF updates in the front end and incorporates multisensor constraints, even when dealing with outlier measurements, through graph optimization based on Graduated
Non-Convexity (GNC). Additionally, we propose a robust Incremental Fixed Lag Smoother (rIFL) for efficient GNC-based optimization. RELEAD has undergone extensive evaluation in degenerate scenarios and has outperformed existing state-ofthe-art LiDAR-Inertial odometry and LiDAR-Visual-Inertial odometry methods.

## Problem Addressed

LiDAR-based localization for applications such as mining surveys and underground facility maintenance struggles when geometric structures are uninformative, causing scan-matching degradation. Existing methods fail to maintain robust pose estimation in such adverse environments.

## Key Contributions

- Proposes degeneracy-eliminated LiDAR-inertial odometry with a constrained error-state iterated Kalman filter
- Analyzes alignment strength for 6 DOF to detect ill-conditioned directions for drift-free pose updates
- Integrates multisensor constraints robustly via graph optimization based on Graduated Non-Convexity
- Introduces a robust incremental fixed-lag smoother for efficient GNC-based optimization

## Conclusions

RELEAD is extensively evaluated in degenerate scenarios and outperforms existing state-of-the-art LiDAR-inertial odometry and LiDAR-visual-inertial odometry methods. It identifies environmental degradation and achieves precise pose estimation in degradation directions while robustly handling outlier measurements. Future work will implement real-time estimation of measurement covariance in the backend fusion.
