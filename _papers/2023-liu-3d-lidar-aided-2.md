---
title: 3D LiDAR Aided GNSS NLOS Correction with Direction of Arrival Estimation Using Doppler Measurements
authors:
- Xikun Liu
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2023-10-05'
doi: https://doi.org/g8t66d
image: images/papers/cards/2023-liu-3d-lidar-aided-2.jpg
buttons:
- type: manubot
  text: paper
  link: https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/publications/papers/navi.590.full.pdf
tags:
- 3D vision
- autonomous system
- GNSS-RTK
- urban canyons
- NLOS
citation_id: 10.33012/2023.19447
---

## Abstract

Global navigation satellite system (GNSS) positioning in urban environments suffers from significant accuracy degradation due to non-line-of-sight (NLOS) signal receptions.
Existing correction methods, such as 3D model-aided and
3D LiDAR-aided GNSS, lack signal direction information and typically construct candidate reflection paths by exhaustively searching over possible reflection surfaces or azimuth angles, and selecting the final path based on the shortest-path assumption.
However, this assumption is often invalid in dense urban canyons.
To address this limitation, we propose a novel GNSS NLOS correction method that uses Doppler shift measurements to infer signal directional information, which is integrated with real-time point cloud mapping to reconstruct the actual signal reflection path actively. This approach allows us to directly track signal reflection, eliminating the need for exhaustive candidate generation and the shortest-path assumption. Experiments conducted on datasets collected in urban canyons demonstrate the effectiveness of the proposed method. Results show that the method achieves over 90% correction availability for NLOS signals, leading to more than 50% improvement in 3D GNSS positioning accuracy.

## Problem Addressed

Existing 3D model-aided and 3D LiDAR-aided GNSS NLOS correction methods lack signal direction information and rely on exhaustive candidate searches with a shortest-path assumption that is often invalid in dense urban canyons.

## Key Contributions

- 3D LiDAR-aided GNSS direction-of-arrival estimation using Doppler measurements, with accuracy analysis against velocity bias
- NLOS correction framework integrating DOA estimation with real-time point cloud mapping
- Multi-ray tracking and residual evaluation accounting for signal penetration, mapping inaccuracies, and DOA estimation error
- First attempt to actively track NLOS signal reflection paths by integrating 3D LiDAR and GNSS Doppler measurements

## Conclusions

The method achieves over 90% NLOS correction availability and more than 50% improvement in 3D positioning accuracy. Integrated into a GNSS/LiDAR/INS framework, it reduces 3D positioning errors from 9.8 to 4.3 meters in Urban Canyon 1 and from 5.1 to 3.7 meters in Urban Canyon 2. Residual meter-level errors remain due to unmodeled multipath and multi-reflection effects, which future work will address.
