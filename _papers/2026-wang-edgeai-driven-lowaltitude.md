---
title: 'Edge-AI Driven Low-Altitude Security: A Robust UAV Tracking System With Multi-Scale Attention And Adaptive Motion Modeling'
authors:
- Jiale Wang
- Jingyi Cai
- Ming Xia
- Weisong Wen
- Fanchen Meng
- Wu Chen
- Chuang Shi
publisher: IEEE Transactions on Vehicular Technology
date: '2026-01-01'
doi: https://doi.org/hcncbh
citation_id: doi:10.1109/TVT.2026.3743336
---

## Abstract

Unmanned aerial vehicles (UAVs) are becoming increasingly prevalent in low-altitude airspace, posing significant safety challenges and demanding robust detection and tracking systems that can operate in complex, dynamic environments. This paper proposes a novel edge-deployed autonomous tracking system that integrates a customized lightweight detector (DT-YOLOv5s) with an adaptive tracking algorithm (KF-OCSORT) on a gimbal-based control platform. To address the challenge of detecting small, high-speed targets under stringent computational constraints, we redesign the detection architecture by introducing a high-resolution P2 feature level, incorporating the gradient-efficient C2f module, and proposing a Dual Coordinate Attention (DCA) mechanism. These enhancements substantially improve feature representation for tiny objects. Comparative experiments demonstrate that the proposed model outperforms state-of-the-art baselines, including YOLOv8 and YOLOv11, in detection accuracy on a UAV dataset.For the tracking stage, to mitigate trajectory fragmentation caused by occlusions and camera jitter, we develop the KF-OCSORT algorithm. By fusing Kalman filter prediction with an observation-centric SORT framework, the system maintains trajectory continuity during short-term target loss or IoU degradation. Field tests validate that the proposed closed-loop “sense-aim-control” system achieves high-precision tracking and strong robustness across diverse scenarios, providing a practical solution for low-altitude airspace surveillance and border defense.

## Problem Addressed

The rapid spread of UAVs in low-altitude airspace creates safety risks, while detecting small, fast-moving targets on edge platforms under tight compute budgets and maintaining trajectories through occlusion and camera jitter remains difficult.

## Key Contributions

- Edge-deployed closed-loop sense-aim-control tracking system combining DT-YOLOv5s detector and KF-OCSORT tracker on a gimbal platform
- Lightweight detector redesign with a high-resolution P2 feature level for tiny-object detection
- Gradient-efficient C2f module and Dual Coordinate Attention mechanism improving feature representation
- KF-OCSORT tracker fusing Kalman filter prediction with observation-centric SORT to preserve trajectories during short-term target loss

## Conclusions

The proposed detector outperforms state-of-the-art baselines including YOLOv8 and YOLOv11 in detection accuracy on a UAV dataset. Field tests confirm that the closed-loop system achieves high-precision tracking and strong robustness across diverse scenarios, offering a practical solution for low-altitude airspace surveillance and border defense.
