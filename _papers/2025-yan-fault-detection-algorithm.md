---
title: 'Fault Detection Algorithm for Gaussian Mixture Noises: An Application in Lidar/IMU Integrated Localization Systems'
authors:
- Penggao Yan
- Zhengdao Li
- Feng Huang
- Weisong Wen
- Li-Ta Hsu
publisher: 'NAVIGATION: Journal of the Institute of Navigation'
date: '2025-03-19'
doi: https://doi.org/g9hrnr
image: images/papers/cards/2025-yan-fault-detection-algorithm.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/navi.684.full.pdf
tags:
- 2D lidar/IMU-based localization
- chi-squared test
- EKF, fault detection
- Gaussian mixture model
- non-Gaussian noise
citation_id: doi:10.33012/navi.684
---

## Abstract

Fault detection is crucial to ensurethe reliability of localization systems. However, conventional fault detection methods usually assume that noises in the system have a Gaussian distribution, limiting their effectiveness in real-world applica­ tions. This study proposes a fault detection algorithm for an extended Kalman filter (EKF)-based localization system by modeling non-Gaussian noises as a Gaussian mixture model (GMM). The relationship between GMM-distributed noises and the measurement residual is rigorously established through error propagation, which is utilized to construct the test statistic for a chi-squared test. The proposed method is applied to an EKF-based two-dimensional light detection and ranging/inertial measurement unit integrated localization sys­ tem. Experimental results in a simulated urban environment show that the pro­ posed method exhibits a 30% improvement in the detection rate and a 17%–23% reduction in the detection delay, compared with the conventional method with Gaussian noise modeling.

## Problem Addressed

Conventional fault detection methods for localization systems assume Gaussian noise distributions, which limits their effectiveness in real-world applications where noises are non-Gaussian.

## Key Contributions

- Fault detection algorithm for EKF-based localization modeling non-Gaussian noises as a Gaussian mixture model
- Rigorous error propagation establishing the relationship between GMM-distributed noises and the measurement residual
- Chi-squared test statistic built from a residual transformed toward a standard multivariate normal distribution
- Application to a 2D lidar/IMU integrated system with reproducible CARLA-based simulated urban evaluation

## Conclusions

Experiments in a simulated urban environment show the proposed method achieves a 30% improvement in detection rate and a 17%-23% reduction in detection delay compared with the conventional method based on Gaussian noise modeling.
