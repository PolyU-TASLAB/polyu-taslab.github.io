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
image: images/papers/cards/2024-yan-fault-detection-algorithm-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/A-Fault-Detection-Algorithm-for-LiDAR-IMU-Integrated-Localization-Systems-with-Non-Gaussian-Noises.pdf
tags:
- Smartphone
- IO
- Ubiquitous
- Perdestrian Positioning
- Sensor Integration
- VINS
- 3DMA
- GNSS
- FGO
citation_id: 10.33012/2024.19564
---

## Abstract

Fault detection for localization systems with non-Gaussian measurement noises is a challenging task. This paper investigates the impacts of noise modeling on fault detection performance in the inertial measurement units (IMU) and light detection and ranging (LiDAR) integrated localization system based on the extended Kalman filter (EKF). Specifically, we model the noise distribution of LiDAR range measurements as a Gaussian mixture model (GMM) and establish a clear relationship between the measurement noise and the measurement residual in EKF through error propagation. After proving that the measurement residual is also GMM distributed, a test statistic is constructed by transforming the measurement residual to a variable that approximates a standard multivariate normal (MVN) distribution based on the law of total covariance. Then, a Chi-squared test is performed based on the constructed test statistic to detect potential faults. The performance of the proposed method is evaluated in the simulated environment regarding two types of measurement failures, including the step failure and the slope failure. Compared to the method that adopts Gaussian noise modeling, the proposed method demonstrates its superiority in detecting small faults and the improved sensitivity to slowly increasing faults.

## Problem Addressed

Fault detection in localization systems with non-Gaussian measurement noises is challenging, and conventional approaches built on Gaussian noise modeling perform poorly for LiDAR/IMU integrated systems whose range noise is not Gaussian.

## Key Contributions

- Gaussian mixture model noise modeling for LiDAR range measurements in an EKF-based LiDAR/IMU localization system
- Proof that the EKF measurement residual is GMM-distributed, transformed via the law of total covariance into a near-standard normal test variable
- Chi-squared fault detection test built on the constructed test statistic
- CARLA-based simulated urban environment enabling controlled step- and slope-failure injection for fair comparison

## Conclusions

In the step-failure experiment, the proposed method achieved over 85% fault detection rate under all three GMM noise settings, significantly outperforming the Gaussian-modeling method. In the slope-failure experiment, detection delay was reduced by 17 to 23%, demonstrating greater sensitivity to slowly increasing faults. The results indicate that GMM-based noise modeling benefits fault detection in localization systems with non-Gaussian noises.
