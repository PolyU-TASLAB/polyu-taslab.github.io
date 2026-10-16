---
title: 'GLIO: Tightly-Coupled GNSS/LiDAR/IMU Integration for Continuous and Drift-Free State Estimation of Intelligent Vehicles in Urban Areas'
authors:
- Xikun Liu
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Vehicles
date: '2024-01-01'
doi: https://doi.org/g8t655
image: images/papers/cards/2024-liu-glio-tightlycoupled-gnsslidarimu-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/GLIO_Tightly-Coupled_GNSS_LiDAR_IMU_Integration_for_Continuous_and_Drift-Free_State_Estimation_of_Intelligent_Vehicles_in_Urban_Areas.pdf
- type: website
  link: https://github.com/XikunLiu-huskit/GLIO
tags:
- Robotics
- Tightly-Coupled
- GNSS
- LiDAR
- IMU
repo: https://github.com/XikunLiu-huskit/GLIO
citation_id: 10.1109/TIV.2023.3323648
---

## Abstract

Intelligent vehicles demand reliable, continuous, and accurate positioning capability. Light Detection and Ranging (LiDAR)-inertial odometry (LIO) provides precise continuous relative pose estimation but suffers from drift over large-scale operations. Global navigation satellite system (GNSS) offers drift-free absolute positioning capability but the accuracy is strongly affected by non-line-of-sight (NLOS) receptions and multipath effects arising from the reflections of the surrounding environments. The tightly-coupled integration of the GNSS and LIO is highly complementary. However, how to fully utilize the complementariness of LiDAR measurements and the GNSS model is still an open question. More importantly, an open-sourced implementation of their integration is highly expected. To fill these gaps, this article proposes the GLIO, a GNSS/LiDAR/IMU integrated estimator that tightly fuses GNSS pseudorange, Doppler, LiDAR, and IMU measurements using factor graph optimization (FGO). In particular, the corrections from the reference station are adopted to remove the systematic errors involved in the GNSS pseudorange measurements. To fully exploit the complementariness of the LiDAR and GNSS measurements, two stages of the optimization scheme are utilized to achieve global consistent and continuous pose estimation. In the first stage of optimization, the sliding-window-based FGO is employed to integrate the GNSS-related factors, IMU pre-integration factor, and scan-to-map-based LiDAR factor for efficient odometry estimation. In the second stage of optimization, the LiDAR factor is employed as a scan-to-multiscan scheme to maintain global consistency and improve the robustness of the system to the GNSS outlier by large-scale batch optimization. We evaluate the proposed method and verify its effectiveness through the challenge dataset UrbanNav involving highly urbanized areas. The proposed system achieves more than 70% improvement in positioning accuracy compared with the traditional GNSS positioning method and LIO standalone system.

## Problem Addressed

LiDAR-inertial odometry drifts over large-scale operations while GNSS absolute positioning is degraded by NLOS receptions and multipath in urban areas; fully exploiting their complementarity, with an open-source implementation, remains an open question.

## Key Contributions

- GLIO: factor graph optimization tightly fusing GNSS pseudorange, Doppler, LiDAR, and IMU measurements
- Reference-station corrections adopted to remove systematic errors in GNSS pseudorange measurements
- Two-stage optimization: sliding-window FGO odometry plus batch scan-to-multiscan fusion for global consistency
- Evaluated on challenging UrbanNav sequences using commercial-level GNSS receivers and a LiDAR/IMU kit

## Conclusions

Experiments on challenging Hong Kong sequences achieve more than 70% improvement, demonstrating reliable accuracy and robustness in urban environments. A maximum error of nearly 10 meters remains because unhealthy GNSS observations are not fully mitigated and healthy ones are insufficient to correct the trajectory. Future work targets point-cloud-based correction of biased GNSS signals, integration with 3D LiDAR-aided RTK for centimeter-level positioning, and extension to PPP.
