---
title: 3-D LiDAR-Aided GNSS NLOS Mitigation for Reliable GNSS-RTK Positioning in Urban Canyons
authors:
- Xikun Liu
- Weisong Wen
- Feng Huang
- Han Gao
- Yongliang Wang
- Li-Ta Hsu
publisher: IEEE Transactions on Instrumentation and Measurement
date: '2025-01-01'
doi: https://doi.org/hccr4h
image: images/papers/cards/2025-liu-3d-lidaraided-gnss.jpg
citation_id: doi:10.1109/TIM.2025.3629836
---

## Abstract

GNSS real-time kinematic (RTK) and LiDAR odometry are complementary, offering global and local positioning capabilities, respectively. 
GNSS-RTK/LiDAR integration primarily focuses on two aspects: (1) 3D LiDARaided (3DLA) GNSS non-line-of-sight (NLOS) mitigation using point cloud data. (2) State estimation via tightly-coupled 
GNSS/LiDAR integration, which improves GNSS geometry, yielding better float solutions and lower estimation uncertainty. 
Combining 3DLA NLOS mitigation with tightly-coupled integration can thus enhance urban positioning reliability. 
However, the current 3DLA GNSS-RTK system remains limited in terms of 
NLOS detection reliability, tightly-coupled integration effectiveness, and computational efficiency. This paper proposes a tightly-coupled 
GNSS-RTK/LiDAR/INS integration system with 3DLA NLOS mitigation. We focus on improving the robustness of 3DLA NLOS detection, the efficiency and effectiveness of the tightly-coupled GNSSRTK/LiDAR integration. Evaluations on the challenging 
UrbanNav dataset show over 70% improvement in positioning accuracy compared to conventional GNSS-RTK, achieving submeter to meter-level precision. Runtime analysis confirms the system supports real-time optimization and ambiguity resolution with an average computation time of 70 ms.

## Problem Addressed

GNSS-RTK degrades in urban canyons due to NLOS receptions and poor satellite geometry, and current 3D LiDAR-aided GNSS-RTK systems remain limited in NLOS detection reliability, tightly-coupled integration effectiveness, and computational efficiency.

## Key Contributions

- Drift-free 3D sliding-window point cloud map-based NLOS detection and exclusion, with drift corrected by pose graph optimization
- Tightly-coupled GNSS-RTK/LiDAR/INS factor graph integration using virtual satellites from sparse LiDAR landmarks
- Efficiency-oriented design using fewer LiDAR observations with balanced LiDAR/GNSS weighting
- Extensive evaluation on three challenging urban canyon sequences in Hong Kong

## Conclusions

On the challenging UrbanNav dataset, the system achieves over 70% improvement in positioning accuracy compared to conventional GNSS-RTK, reaching submeter to meter-level precision with commercial-grade receivers. Runtime analysis confirms real-time optimization and ambiguity resolution with an average computation time of 70 ms.
