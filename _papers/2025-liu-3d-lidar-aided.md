---
title: 3D LiDAR Aided GNSS NLOS Correction by Direction-of-Arrival Estimation Using Doppler Measurements in Urban Canyons
authors:
- Xikun Liu
- Weisong Wen
- Liyuan Zhang
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Transportation Systems
date: '2025-08-19'
doi: https://doi.org/g92s6v
image: images/papers/cards/2025-liu-3d-lidar-aided.jpg
tags:
- 3D LiDAR
- global navigation satellite system (GNSS)
- perception-aided integration
- NLOS correction
- Doppler measurement model
- geometry distribution
- urban canyons
citation_id: doi:10.1109/TITS.2025.3596582
---

## Abstract

Global navigation satellite system (GNSS) positioning in urban environments suffers from significant accuracy degradation due to non-line-of-sight (NLOS) signal receptions.
Existing correction methods, such as 3D model-aided and
3D LiDAR-aided GNSS, lack signal direction information and typically construct candidate reflection paths by exhaustively searching over possible reflection surfaces or azimuth angles, and selecting the final path based on the shortest-path assumption.
However, this assumption is often invalid in dense urban canyons.
To address this limitation, we propose a novel GNSS NLOS correction method that uses Doppler shift measurements to infer signal directional information, which is integrated with real-time point cloud mapping to reconstruct the actual signal reflection path actively. This approach allows us to directly track signal reflection, eliminating the need for exhaustive candidate generation and the shortest-path assumption. Experiments conducted on datasets collected in urban canyons demonstrate the effectiveness of the proposed method. Results show that the method achieves over 90% correction availability for NLOS signals, leading to more than 50% improvement in 3D GNSS positioning accuracy.

## Problem Addressed

GNSS positioning in urban environments suffers significant degradation from NLOS receptions, and existing 3D model- or LiDAR-aided correction methods lack signal direction information, relying on exhaustive candidate reflection path searches and a shortest-path assumption that is often invalid in dense urban canyons.

## Key Contributions

- 3D LiDAR-aided GNSS signal direction-of-arrival estimation using Doppler measurements, with accuracy analysis of LiDAR-derived prior velocity
- NLOS correction framework integrating DOA estimation with real-time point cloud mapping via multi-ray tracking and residual evaluation
- First integration of 3D LiDAR and GNSS Doppler to actively track NLOS signal paths, handling signal penetration, mapping inaccuracies, and DOA error

## Conclusions

Evaluated on two challenging urban canyon sequences in Hong Kong, the method achieves over 90% correction availability for NLOS signals. Integrated into a GNSS/LiDAR/INS framework, it reduces 3D positioning errors from 9.8 to 4.3 m in Urban Canyon 1 and from 5.1 to 3.7 m in Urban Canyon 2, an improvement of more than 50% in 3D GNSS positioning accuracy. Residual meter-level errors remain due to unmodeled multipath and multi-reflection effects, motivating future multi-reflection path modeling.
