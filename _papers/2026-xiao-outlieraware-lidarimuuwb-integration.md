---
title: Outlier-Aware LiDAR–IMU–UWB Integration with NLOS Mitigation and Anchor Self-Calibration in Complex Scenarios
authors:
- Naigui Xiao
- Weisong Wen
- Lu Bai
- Xiangru Wang
- Jiahao Hu
- Qi Zhang
- Jianhao Jiao
- Zhen Lyu
- Feng Huang
publisher: IEEE Transactions on Instrumentation and Measurement
date: '2026-01-01'
doi: https://doi.org/hcm4md
citation_id: doi:10.1109/TIM.2026.3742091
---

## Abstract

LiDAR-inertial odometry (LIO) is susceptible to long-term drift in global navigation satellite system (GNSS)-challenged environments, limiting accurate state estimation for unmanned aerial vehicles (UAVs), mobile robots, and autonomous ground vehicles. Ultra-wideband (UWB) infrastructure can provide ranging constraints to mitigate this drift. However, its practical utility is limited by two critical bottlenecks: the labor-intensive requirement for precise anchor pre-calibration and measurement degradation caused by non-line-of-sight (NLOS) propagation. To address these challenges, we propose a UWB-aided continuous-time fusion framework that tightly couples LiDAR, IMU, and UWB data using non-uniform B-splines on Lie groups within a factor graph optimization (FGO) structure. First, to reduce the reliance on precise anchor positions, we formulate UWB anchor positions as static anchor states and jointly optimize them with the continuous-time vehicle trajectory under rough prior initialization. This design enables asynchronous range measurements to jointly constrain the spline trajectory and anchor position. Second, a map-aware NLOS mitigation strategy based on geometric penetration depth (GPD) is developed. GPD estimates physical obstructions along UWB propagation paths from the LiDAR-generated map and converts them into continuous measurement uncertainty, thereby avoiding residual-based robust kernels that suppress measurements only after large residuals emerge. The proposed method is evaluated on a public vehicle-infrastructure urban dataset and multiple self-collected datasets covering complex urban and controlled indoor environments. Experimental results demonstrate that the proposed method outperforms LiDAR-inertial, UWB-inertial, and discrete-time UWB-LiDAR-inertial baselines in both localization accuracy and robustness, while achieving long-term drift-bounded localization in GNSS-challenged environments. To facilitate further research, our implementation and data...

## Problem Addressed

LiDAR-inertial odometry accumulates long-term drift in GNSS-challenged environments. UWB ranging can bound this drift, but its utility is limited by labor-intensive precise anchor pre-calibration and measurement degradation from non-line-of-sight propagation.

## Key Contributions

- UWB-aided continuous-time fusion framework tightly coupling LiDAR, IMU, and UWB via non-uniform B-splines on Lie groups within factor graph optimization
- Anchor self-calibration treating anchor positions as static states jointly optimized with the trajectory under rough priors
- Map-aware NLOS mitigation using geometric penetration depth estimated from the LiDAR map
- Continuous measurement uncertainty modeling that avoids residual-based robust kernels reacting only after large errors emerge

## Conclusions

Evaluated on a public vehicle-infrastructure urban dataset and multiple self-collected urban and indoor datasets, the method outperforms LiDAR-inertial, UWB-inertial, and discrete-time UWB-LiDAR-inertial baselines in both localization accuracy and robustness. It achieves long-term drift-bounded localization in GNSS-challenged environments, and the implementation and data are released for further research.
