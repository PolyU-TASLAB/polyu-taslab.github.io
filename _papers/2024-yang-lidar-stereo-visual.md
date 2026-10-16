---
title: LiDAR Stereo Visual Inertial Pose Estimation Based on Feedforward and Feedbacks
authors:
- Wenyu Yang
- Haochen Hu
- Kwai-wa Tse
- Shengyang Chen
- Weisong Wen
- Chih-yung Wen
publisher: 2024 International Conference on Unmanned Aircraft Systems (ICUAS)
date: '2024-06-04'
doi: https://doi.org/hcc4r2
image: images/papers/cards/2024-yang-lidar-stereo-visual.jpg
citation_id: doi:10.1109/icuas60882.2024.10556962
---

## Abstract

In this paper, we present a LiDAR Visual Inertial Odometry (LVIO) based on feedforward and feedbacks. Compared to traditional Kalman filter-based methods or optimization-based methods for sensor fusion, the proposed system achieves sensor fusion through feedforward and feedbacks. This system, named Feedforward-feedback LiDAR
Visual Inertial System (FLiVIS) consists of a Visual Inertial
Odometry (VIO) subsystem and a LiDAR Inertial Odometry (LIO) subsystem, these two subsystems are coupled through complementary filters. Instead of directly integrating gyroscope data and accelerometer data, our framework leverages the complementary nature of gyroscope and accelerometer measurements. FLiVIS is evaluated on public datasets, it achieves a relative translation error of 0.68% on the KITTI dataset and
0.138 m absolute translation error on the NTU-Viral dataset, respectively. The experiment results demonstrate the accuracy and robustness of FLiVIS with respect to other state-of-the-art counterparts. FLiVIS is capable of accommodating both multiline spinning LiDARs and emerging solid-state LiDARs, which employ distinct scanning patterns. Additionally, it can perform real-time operations on a range of platforms, from laptops to upboard processors.

## Problem Addressed

Accurate and robust pose estimation by fusing LiDAR, visual, and inertial measurements remains challenging for traditional Kalman filter-based and optimization-based sensor fusion schemes.

## Key Contributions

- FLiVIS framework fusing LiDAR, visual, and inertial measurements through designed feedforward and feedbacks
- Complementary filters coupling VIO and LIO subsystems, exploiting complementary gyroscope and accelerometer characteristics
- Supports multi-line spinning and solid-state LiDARs with real-time operation from laptops to embedded processors
- Benchmarked on KITTI and NTU-Viral datasets with accuracy comparable to top-ranked algorithms

## Conclusions

FLiVIS achieves a relative translation error of 0.68% on the KITTI dataset and an absolute translation error of 0.138 m on the NTU-Viral dataset, competitive with other state-of-the-art algorithms.
