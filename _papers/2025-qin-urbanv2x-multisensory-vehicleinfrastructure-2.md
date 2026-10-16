---
title: 'UrbanV2X: A Multisensory Vehicle-Infrastructure Dataset for Cooperative Navigation in Urban Areas'
authors:
- Qijun Qin
- Ziqi Zhang
- Yihan Zhong
- Feng Huang
- Xikun Liu
- Runzhi Hu
- Hang Chen
- Wei Hu
- Dongzhe Su
- Jun Zhang
- Hoi-Fung Ng
- Weisong Wen
publisher: arXiv
date: '2025-01-01'
doi: https://doi.org/hccr4p
image: images/papers/cards/2025-qin-urbanv2x-multisensory-vehicleinfrastructure-2.jpg
citation_id: doi:10.48550/arXiv.2512.20224
---

## Abstract

Due to the limitations of a single autonomous vehicle, Cellular Vehicle-to-Everything (C-V2X) technology opens a new window for achieving fully autonomous driving through sensor information sharing. However, real-world datasets supporting vehicle-infrastructure cooperative navigation in complex urban environments remain rare. To address this gap, we present UrbanV2X, a comprehensive multisensory dataset collected from vehicles and roadside infrastructure in the Hong Kong C-V2X testbed, designed to support research on smart mobility applications in dense urban areas. Our onboard platform provides synchronized data from multiple industrial cameras, LiDARs, 4D radar, ultra-wideband (UWB), IMU, and high-precision GNSS-RTK/INS navigation systems. Meanwhile, our roadside infrastructure provides LiDAR, GNSS, and UWB measurements. The entire vehicle-infrastructure platform is synchronized using the Precision Time Protocol (PTP), with sensor calibration data provided. We also benchmark various navigation algorithms to evaluate the collected cooperative data. The dataset is publicly available at https://polyu-taslab.github.io/UrbanV2X/.

## Problem Addressed

Real-world datasets supporting vehicle-infrastructure cooperative navigation in complex urban environments remain rare, limiting research on C-V2X-enabled fully autonomous driving.

## Key Contributions

- UrbanV2X dataset collected from vehicles and roadside infrastructure in the Hong Kong C-V2X testbed
- Synchronized, calibrated onboard data from cameras, LiDARs, 4D radar, UWB, IMU, and GNSS-RTK/INS
- Roadside infrastructure providing LiDAR, GNSS, and UWB measurements, synchronized via Precision Time Protocol
- Benchmarks of state-of-the-art positioning algorithms, with dataset and results publicly released

## Conclusions

Benchmark evaluations using state-of-the-art SLAM and positioning algorithms demonstrate that incorporating infrastructure sensing enhances robustness and accuracy. UrbanV2X provides a unique testbed for cooperative autonomy under real-world constraints such as dynamic objects, GNSS degradation, and occlusions, and the dataset is publicly available to support reproducible research.
