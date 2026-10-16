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
date: '2025-12-23'
doi: https://arxiv.org/abs/2512.20224
image: images/papers/cards/2025-qin-urbanv2x-multisensory-vehicleinfrastructure-3.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2512.20224v1.pdf
- type: source
  text: code
  link: https://polyu-taslab.github.io/UrbanV2X/
tags:
- Multisensor Fusion
- Roadside Infrastructure
- SLAM
- Autonomous Driving
citation_id: arXiv:2512.20224
---

## Abstract

Due to the limitations of a single autonomous vehicle, Cellular Vehicle-to-Everything (C-V2X) technology opens a new window for achieving fully autonomous driving through sensor information sharing. However, real-world datasets supporting vehicle–infrastructure cooperative navigation in complex urban environments remain rare. To address this gap, we present UrbanV2X, a comprehensive multisensory dataset collected from vehicles and roadside infrastructure in the Hong Kong C-V2X testbed, designed to support research on smart mobility applications in dense urban areas. Our onboard platform provides synchronized data from multiple industrial cameras, LiDARs, 4D radar, Ultra-wideband (UWB), IMU, and high-precision GNSS-RTK/INS navigation systems. Meanwhile, our roadside infrastructure provides LiDAR, GNSS, and UWB measurements. The entire vehicle–infrastructure platform is synchronized using the Precision Time Protocol (PTP), with sensor calibration data provided. We also benchmark various navigation algorithms to evaluate the collected cooperative data. The dataset is publicly available at: https://polyu-taslab. github.io/UrbanV2X/.

## Problem Addressed

Real-world datasets supporting vehicle-infrastructure cooperative navigation in complex urban environments remain rare, hindering research on C-V2X-enabled autonomous driving and smart mobility.

## Key Contributions

- UrbanV2X, a comprehensive real-world vehicle-infrastructure dataset collected in Hong Kong's dense urban C-V2X testbed.
- Time-synchronized and calibrated data from onboard cameras, LiDARs, 4D radar, UWB, IMU, and GNSS-RTK/INS, plus roadside LiDAR, GNSS, and UWB.
- Whole vehicle-infrastructure platform synchronized via Precision Time Protocol, with sensor calibration data provided.
- Benchmarked multiple state-of-the-art positioning algorithms, publicly releasing the dataset and benchmark results.

## Conclusions

Preliminary evaluations using state-of-the-art SLAM and positioning algorithms demonstrate that incorporating infrastructure sensing improves robustness and accuracy for cooperative navigation. The dataset provides a unique testbed under real-world constraints such as dynamic objects, GNSS degradation, and occlusions, supporting research in V2X perception, multi-agent navigation, and smart city applications. Future work will enrich the data, extend evaluations with collaborative SLAM methods, and add annotations.
