---
title: 'RTT-LIO: A Wi-Fi RTT-Aided LiDAR-Inertial Odometry via Tightly-Coupled Factor Graph Optimization in Complex Scenes'
authors:
- Ruijie Xu
- Xikun Liu
- Xin Wang
- Weisong Wen
- Yulong Huang
publisher: IEEE Internet of Things Journal
date: '2026-03-25'
doi: https://doi.org/hcb4mj
image: images/papers/cards/2026-xu-rttlio-wifi-rttaided.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/RTT-LIO_A_Wi-Fi_RTT-Aided_LiDAR-Inertial_Odometry_via_Tightly-Coupled_Factor_Graph_Optimization_in_Complex_Scenes.pdf
tags:
- Factor graph optimization (FGO)
- LiDAR inertial odometry (LIO)
- sensor fusion
- Wi-Fi round-trip-time (RTT).
citation_id: doi:10.1109/JIOT.2026.3677365
---

## Abstract

The pursuit of reliable and high-precision indoor positioning has become increasingly critical with the widespread deployment of unmanned autonomous systems (UASs) across smart cities. While Wi-Fi round-trip-time (RTT) technology offers promising absolute positioning capabilities, it faces challenges from signal interference and processing delays. Similarly,
LiDAR-inertial odometry (LIO) systems provide accurate relative positioning, but suffer from cumulative drift over time. Although existing methods have explored loosely coupled technologies, they process sensor data separately, failing to fully exploit the complementary strengths of different sensors. This research pioneered a tightly- coupled RTT/LIO framework, encompassing novel factor graph formulations that ensure consistency between
RTT and LiDAR observations, alongside LiDAR-aided RTT outlier detection and exclusion. Furthermore, we developed an innovative approach to estimate the positions of unknown access points (APs) using prior trajectory and RTT observations. AP position estimation is based on kernel density estimation (KDE) and geometric diversity constraints (GDCs) with the help of an adaptive RANSAC-based fault detection algorithm. Compared to RTT-only implementations, state-of-the-art LIO systems, and conventional loosely coupled approaches, our method demonstrated error reductions of 20-80% in extensive experiments. The implementation of our proposed methodology has been made publicly available on GitHub. The video Bilibili is also shared to display our research.

## Problem Addressed

Wi-Fi RTT offers absolute indoor positioning but suffers from signal interference and processing delays, while LiDAR-inertial odometry provides accurate relative positioning yet drifts over time; existing loosely coupled methods process sensors separately and fail to exploit their complementary strengths.

## Key Contributions

- First tightly coupled RTT/LiDAR/IMU integration at raw measurement level via factor graph optimization
- Factor graph formulations ensuring consistency between RTT and LiDAR observations, with progressive fault detection for RTT outliers
- Unknown access point position estimation combining kernel density estimation and geometric diversity constraints with adaptive RANSAC
- Open-sourced code, datasets, and demonstration video

## Conclusions

Real-world experiments in challenging indoor environments achieve an RMSE of 0.76 m, versus 2.08 m for traditional least squares and 0.98 m for state-of-the-art LIO—a 22.4% improvement over LIO and a 63.5% reduction versus least squares, with error reductions of 20-80% across comparisons. The RANSAC-based KDE and GDC method estimates unknown AP positions at sub-meter accuracy for well-observed APs. The approach requires a minimum number of visible Wi-Fi APs, which may limit performance in sparse connectivity environments.
