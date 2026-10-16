---
title: 'ECMD: An Event-Centric Multisensory Driving Dataset for SLAM'
authors:
- Peiyu Chen
- Weipeng Guan
- Feng Huang
- Yihan Zhong
- Weisong Wen
- Li-Ta Hsu
- Peng Lu
publisher: IEEE Transactions on Intelligent Vehicles
date: '2024-01-01'
doi: https://doi.org/g8t488
image: images/papers/cards/2024-chen-ecmd-eventcentric-multisensory-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2311.02327v1.pdf
- type: website
  link: https://arclab-hku.github.io/ecmd/
tags:
- Event-based Vision
- Multi-sensor Fusion
- SLAM
- Autonomous Driving
- Dataset
repo: https://arclab-hku.github.io/ecmd/
citation_id: 10.1109/TIV.2023.3339144
---

## Abstract

Leveraging multiple sensors enhances complex environmental perception and increases resilience to varying lu-minance conditions and high-speed motion patterns, achieving precise localization and mapping. This paper proposes, ECMD, an event-centric multisensory dataset containing 81 sequences and covering over 200 km of various challenging driving scenarios including high-speed motion, repetitive scenarios, dynamic objects, etc. ECMD provides data from two sets of stereo event cameras with different resolutions (640×480, 346×260), stereo industrial cameras, an infrared camera, a top-installed mechanical LiDAR with two slanted LiDARs, two consumer-level GNSS receivers, and an onboard IMU. Meanwhile, the ground-truth of the vehicle was obtained using a centimeter-level high-accuracy GNSS-RTK/INS navigation system. All sensors are well-calibrated and temporally synchronized at the hardware level, with recording data si-multaneously. We additionally evaluate several state-of-the-art SLAM algorithms for benchmarking visual and LiDAR SLAM and identifying their limitations. The dataset is available at https://arclab-hku.github.io/ecmd/.

## Problem Addressed

SLAM in challenging driving conditions such as high-speed motion, repetitive scenarios, dynamic objects, and varying luminance demands resilient multisensory perception, which existing datasets centered on event cameras do not adequately support.

## Key Contributions

- Event-centric multisensory driving dataset with 81 sequences covering over 200 km of challenging scenarios
- Two stereo event camera sets (640x480, 346x260), stereo industrial and infrared cameras, three LiDARs, GNSS receivers, and IMU
- Hardware-level temporal synchronization and calibration with centimeter-level GNSS-RTK/INS ground truth
- Benchmark evaluation of state-of-the-art visual and LiDAR SLAM algorithms, identifying their limitations

## Conclusions

The dataset provides meticulously calibrated, hardware-synchronized multisensory data with centimeter-level ground truth for SLAM development. Evaluations of state-of-the-art visual and LiDAR SLAM algorithms reveal their constraints. Future work will expand the dataset to additional tasks including semantics, optical flow, and depth estimation.
