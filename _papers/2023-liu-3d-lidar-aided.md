---
title: 3D LiDAR Aided GNSS NLOS Correction with Direction of Arrival Estimation Using Doppler Measurements
authors:
- Xikun Liu
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2023-10-05'
doi: https://doi.org/g8t66d
image: images/papers/cards/2023-liu-3d-lidar-aided.jpg
citation_id: doi:10.33012/2023.19447
---

## Abstract

Global navigation satellite system (GNSS) positioning in urban environments suffers from significant accuracy degradation due to non-line-of-sight (NLOS) signal receptions.
Existing correction methods, such as 3D model-aided and
3D LiDAR-aided GNSS, lack signal direction information and typically construct candidate reflection paths by exhaustively searching over possible reflection surfaces or azimuth angles, and selecting the final path based on the shortest-path assumption.
However, this assumption is often invalid in dense urban canyons.
To address this limitation, we propose a novel GNSS NLOS correction method that uses Doppler shift measurements to infer signal directional information, which is integrated with real-time point cloud mapping to reconstruct the actual signal reflection path actively. This approach allows us to directly track signal reflection, eliminating the need for exhaustive candidate generation and the shortest-path assumption. Experiments conducted on datasets collected in urban canyons demonstrate the effectiveness of the proposed method. Results show that the method achieves over 90% correction availability for NLOS signals, leading to more than 50% improvement in 3D GNSS positioning accuracy.

## Problem Addressed

GNSS positioning in urban environments suffers significant accuracy degradation from NLOS signal receptions. Existing 3D model-aided and 3D LiDAR-aided correction methods lack signal direction information and rely on exhaustive candidate searches and a shortest-path assumption that is often invalid in dense urban canyons.

## Key Contributions

- 3D LiDAR-aided GNSS signal direction-of-arrival estimation using Doppler measurements, with accuracy analysis
- NLOS correction framework integrating signal DOA with LiDAR point cloud mapping
- Multi-ray tracking and residual evaluation to robustly determine reflection points
- First integration of 3D LiDAR and GNSS Doppler measurements to track NLOS signal paths

## Conclusions

The method achieves over 90% correction availability for NLOS signals on two challenging urban sequences in Hong Kong, with substantial improvements in NLOS observation accuracy. Integrated into a GNSS/LiDAR/INS framework, it reduces 3D positioning errors from 9.8 to 4.3 meters in Urban Canyon 1 and from 5.1 to 3.7 meters in Urban Canyon 2. Residual errors remain at the meter level due to unmodeled multipath and multi-reflection effects, motivating future multi-reflection path modeling.
