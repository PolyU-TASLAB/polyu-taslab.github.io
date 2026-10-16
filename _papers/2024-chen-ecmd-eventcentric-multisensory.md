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
image: images/papers/cards/2024-chen-ecmd-eventcentric-multisensory.jpg
citation_id: doi:10.1109/TIV.2023.3339144
---

## Abstract

Leveraging multiple sensors enhances complex environmental perception and increases resilience to varying luminance conditions and high-speed motion patterns, achieving precise localization and mapping. This paper proposes, ECMD, an event-centric multisensory dataset containing 81 sequences and covering over 200 km of various challenging driving scenarios including high-speed motion, repetitive scenarios, dynamic objects, etc. ECMD provides data from two sets of stereo event cameras with different resolutions (640×480,
346×260), stereo industrial cameras, an infrared camera, a top-installed mechanical LiDAR with two slanted LiDARs, two consumer-level GNSS receivers, and an onboard IMU.
Meanwhile, the ground-truth of the vehicle was obtained using a centimeter-level high-accuracy GNSS-RTK/INS navigation system. All sensors are well-calibrated and temporally synchronized at the hardware level, with recording data simultaneously. We additionally evaluate several state-of-the-art
SLAM algorithms for benchmarking visual and LiDAR SLAM and identifying their limitations. The dataset is available at https://arclab-hku.github.io/ecmd/.

## Problem Addressed

SLAM research lacks multisensory driving datasets that combine event cameras with conventional sensors across challenging conditions such as varying luminance, high-speed motion, repetitive scenes, and dynamic objects.

## Key Contributions

- ECMD dataset with 81 sequences covering over 200 km of challenging driving scenarios
- Rich sensor suite: two stereo event camera sets (640x480 and 346x260), stereo industrial cameras, infrared camera, three LiDARs including two slanted, consumer GNSS receivers, and onboard IMU
- Hardware-level temporal synchronization and careful calibration of all sensors, with centimeter-level GNSS-RTK/INS ground truth
- Benchmark evaluation of state-of-the-art visual and LiDAR SLAM algorithms identifying their limitations

## Conclusions

All sensors are meticulously calibrated and hardware-synchronized, with centimeter-level ground truth from a GNSS-RTK/INS system. Benchmarking of state-of-the-art visual and LiDAR SLAM algorithms reveals their constraints, and the dataset is publicly released to support SLAM development, with future expansion planned for semantics, optical flow, and depth estimation.
