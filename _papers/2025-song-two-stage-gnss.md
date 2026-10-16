---
title: Two stage GNSS outlier detection for factor graph optimization based GNSS-RTK/INS/odometer fusion
authors:
- Baoshan Song
- Penggao Yan
- Xiao Xia
- Yihan Zhong
- Weisong Wen
- Li-Ta Hsu
publisher: arXiv
date: '2025-10-01'
doi: https://arxiv.org/abs/2510.00524
image: images/papers/cards/2025-song-two-stage-gnss.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2510.00524v1.pdf
tags: []
citation_id: arxiv:2510.00524
---

## Abstract

Reliable GNSS positioning in complex environments remains a critical challenge due to non-line-of-sight (NLOS) propagation, multipath effects, and frequent signal blockages. These effects can easily introduce large outliers into the raw pseudo-range measurements, which significantly degrade the performance of global navigation satellite system (GNSS) real-time kinematic (RTK) positioning and limit the effectiveness of tightly coupled GNSS-based integrated navigation system. To address this issue, we propose a two-stage outlier detection method and apply the method in a tightly coupled GNSS-RTK, inertial navigation system (INS), and odometer integration based on factor graph optimization (FGO). In the first stage, Doppler measurements are employed to detect pseudo-range outliers in a GNSS-only manner, since Doppler is less sensitive to multipath and NLOS effects compared with pseudo-range, making it a more stable reference for detecting sudden inconsistencies. In the second stage, pre-integrated inertial measurement units (IMU) and odometer constraints are used to generate predicted double-difference pseudo-range measurements, which enable a more refined identification and rejection of remaining outliers. By combining these two complementary stages, the system achieves improved robustness against both gross pseudo-range errors and degraded satellite measuring quality. To ensure real-time feasibility, the high-frequency IMU and odometer measurements are processed through a pre-integration scheme, while a marginalization-based sliding window maintains computational efficiency. The proposed method was validated using several real-world datasets collected in GNSS-challenging conditions. The experimental results demonstrate that the two-stage detection framework significantly reduces the impact of pseudo-range outliers, and leads to improved positioning accuracy and consistency compared with representative baseline approaches. In the deep urban canyon test, the outlier mitigation method has limits the RMSE of GNSS-RTK/INS/odometer fusion from 0.52 m to 0.30 m, with 42.3% improvement.

## Problem Addressed

NLOS propagation, multipath effects, and frequent signal blockages introduce large outliers into raw pseudorange measurements, significantly degrading GNSS-RTK positioning and tightly coupled GNSS-based integrated navigation.

## Key Contributions

- Two-stage GNSS outlier detection framework enhancing measurement reliability
- First stage uses Doppler measurements, less sensitive to multipath and NLOS, for GNSS-only pseudorange outlier detection
- Second stage refines detection using predicted double-difference pseudoranges from pre-integrated IMU and odometer constraints
- Embedded in an FGO-based tightly coupled GNSS-RTK/INS/odometer system with pre-integration and sliding-window marginalization

## Conclusions

Validation on several real-world datasets collected in GNSS-challenging conditions shows the two-stage framework significantly reduces the impact of pseudorange outliers and improves positioning accuracy and consistency compared with representative baselines. The framework is robust to limited satellite geometry and measurement outliers, providing a foundation for practical deployment in autonomous ground vehicles.
