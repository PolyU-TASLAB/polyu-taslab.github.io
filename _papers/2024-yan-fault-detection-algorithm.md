---
title: A Fault Detection Algorithm for LiDAR/IMU Integrated Localization Systems with Non-Gaussian Noises
authors:
- Penggao Yan
- Weisong Wen
- Feng Huang
- Li-Ta Hsu
publisher: The International Technical Meeting of the The Institute of Navigation
date: '2024-02-14'
doi: https://doi.org/g8t65n
image: images/papers/cards/2024-yan-fault-detection-algorithm.jpg
citation_id: doi:10.33012/2024.19564
---

## Abstract

Fault detection for localization systems with non-Gaussian measurement noises is a challenging task. This paper investigates the impacts of noise modeling on fault detection performance in the inertial measurement units (IMU) and light detection and ranging (LiDAR) integrated localization system based on the extended Kalman filter (EKF). Specifically, we model the noise distribution of LiDAR range measurements as a Gaussian mixture model (GMM) and establish a clear relationship between the measurement noise and the measurement residual in EKF through error propagation. After proving that the measurement residual is also GMM distributed, a test statistic is constructed by transforming the measurement residual to a variable that approximates a standard multivariate normal (MVN) distribution based on the law of total covariance. Then, a Chi-squared test is performed based on the constructed test statistic to detect potential faults. The performance of the proposed method is evaluated in the simulated environment regarding two types of measurement failures, including the step failure and the slope failure. Compared to the method that adopts Gaussian noise modeling, the proposed method demonstrates its superiority in detecting small faults and the improved sensitivity to slowly increasing faults.

## Problem Addressed

Fault detection for LiDAR/IMU integrated localization systems is challenging when measurement noises follow non-Gaussian distributions, and conventional Gaussian noise modeling limits detection sensitivity for small or slowly growing faults.

## Key Contributions

- Fault detection algorithm for EKF-based localization modeling non-Gaussian measurement noise as a Gaussian mixture model
- Proof that the EKF measurement residual is GMM-distributed, transformed to an approximate standard normal variable
- Chi-squared test statistic constructed from the transformed residual via the law of total covariance
- CARLA-based simulated urban environment enabling controlled fault injection and fair algorithm comparison

## Conclusions

In step-failure experiments, the proposed method achieves over 85% fault detection rate across all three GMM noise settings, significantly outperforming the Gaussian method. In slope-failure experiments, detection delay is reduced by 17-23% compared with the Gaussian method, demonstrating greater sensitivity to slowly increasing faults.
