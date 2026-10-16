---
title: Performance Analysis of NDT-based Graph SLAM for Autonomous Vehicle in Diverse Typical Driving Scenarios of Hong Kong
authors:
- Weisong Wen
- Li-Ta Hsu
- Guohao Zhang
publisher: Sensors
date: '2018-11-14'
doi: https://doi.org/ggrgr2
image: images/papers/cards/2018-wen-performance-analysis-ndtbased.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/PANG.pdf
tags:
- Localization
- NDT
- Graph SLAM
- LiDAR
- Autonomous Vehicle
citation_id: doi:10.3390/s18113928
---

## Abstract

Robust and lane-level positioning is essential for autonomous vehicles. As an irreplaceable sensor, Light detection and ranging (LiDAR) can provide continuous and high-frequency pose estimation by means of mapping, on condition that enough environment features are available. The error of mapping can accumulate over time. Therefore, LiDAR is usually integrated with other sensors. In diverse urban scenarios, the environment feature availability relies heavily on the traffic (moving and static objects) and the degree of urbanization. Common LiDAR-based simultaneous localization and mapping (SLAM) demonstrations tend to be studied in light traffic and less urbanized area. However, its performance can be severely challenged in deep urbanized cities, such as Hong Kong, Tokyo, and New York with dense traffic and tall buildings. This paper proposes to analyze the performance of standalone NDT-based graph SLAM and its reliability estimation in diverse urban scenarios to further evaluate the relationship between the performance of LiDAR-based SLAM and scenario conditions. The normal distribution transform (NDT) is employed to calculate the transformation between frames of point clouds. Then, the LiDAR odometry is performed based on the calculated continuous transformation. The state-of-the-art graph-based optimization is used to integrate the LiDAR odometry measurements to implement optimization. The 3D building models are generated and the definition of the degree of urbanization based on Skyplot is proposed. Experiments are implemented in different scenarios with different degrees of urbanization and traffic conditions. The results show that the performance of the LiDAR-based SLAM using NDT is strongly related to the traffic condition and degree of urbanization. The best performance is achieved in the sparse area with normal traffic and the worse performance is obtained in dense urban area with 3D positioning error (summation of horizontal and vertical) gradients of 0.024 m/s and 0.189 m/s, respectively. The analyzed results can be a comprehensive benchmark for evaluating the performance of standalone NDT-based graph SLAM in diverse scenarios which is significant for multi-sensor fusion of autonomous vehicle.

## Problem Addressed

LiDAR-based SLAM is usually demonstrated in light traffic and less urbanized areas, so its performance in deep urbanized cities with dense traffic and tall buildings is poorly understood. Mapping error accumulates over time and feature availability varies strongly with the scenario.

## Key Contributions

- Implements NDT-based graph SLAM with LiDAR odometry and graph-based optimization
- Generates 3D building models and defines a Skyplot-based degree of urbanization for scenario classification
- Evaluates SLAM performance across scenarios with different urbanization degrees and traffic conditions
- Analyzes the relationship between NDT-based SLAM performance, traffic, and urbanization

## Conclusions

Experiments show the performance of NDT-based LiDAR SLAM is strongly related to traffic conditions and the degree of urbanization. The best performance is achieved in sparse areas with normal traffic, while the worst performance occurs in dense urban areas, with a reported 3D positioning error gradient of 0.024 m/s. The findings provide a basis for mitigating traffic and urbanization effects on LiDAR positioning.
