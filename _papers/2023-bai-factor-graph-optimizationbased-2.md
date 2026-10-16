---
title: Factor Graph Optimization-based Indoor Pedestrian SLAM with Probabilistic Exact Activity Loop Closures using Smartphone
authors:
- Shiyu Bai
- Weisong Wen
- Li-Ta Hsu
- Yue Yu
publisher: 2023 13th International Conference on Indoor Positioning and Indoor Navigation (IPIN)
date: '2023-09-25'
doi: https://doi.org/g8t656
image: images/papers/cards/2023-bai-factor-graph-optimizationbased-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Factor_Graph_Optimization-based_Indoor_Pedestrian_SLAM_with_Probabilistic_Exact_Activity_Loop_Closures_using_Smartphone.pdf
tags:
- indoor localization
- simultaneous localization and mapping (SLAM)
- factor graph optimization (FGO)
- smart phone
- human activity
citation_id: 10.1109/IPIN57070.2023.10332510
---

## Abstract

Indoor localization by smartphones has indicated its promising application prospect in daily life. Smartphonebased pedestrian dead reckoning (PDR) is a common method to obtain the locations. However, PDR suffers from position error accumulation. Although radio frequency (RF) and indoor map can be utilized to restrain the error drift, it requires the prior deployment of facilities or information, which is unsuitable for unknown environments. This paper proposes a factor graph optimization (FGO)-based indoor pedestrian simultaneous localization and mapping (SLAM) with probabilistic exact activity loop closures using a smartphone. In this paper, the smartphone built-in inertial measurement unit (IMU) is solely used to achieve
SLAM, in which the human turning activity is regarded as the landmark. Repeatedly observed activities are then used to form loop closures to restrain the drift. FGO is first utilized to formulate pedestrian IMU-only SLAM, which achieves better estimation accuracy than the filter-based method. Moreover, multi-hypothesis tracking is employed to deal with ambiguous data association. During the turning, key points are defined and mutually matched to form exact loop closures to improve estimation accuracy. Simulations and experimental tests are both done to evaluate the performance of the proposed method.

## Problem Addressed

Smartphone-based pedestrian dead reckoning accumulates position error, and radio-frequency or map-based corrections require prior facility deployment or information unsuitable for unknown indoor environments.

## Key Contributions

- FGO-based indoor pedestrian SLAM using only smartphone IMU, treating human turning activity as landmarks
- Probabilistic exact activity loop closures to restrain cumulative error
- Multi-hypothesis data association maintaining trajectories under ambiguous loop closures
- Key points during turning defined and mutually matched to form exact loop closures

## Conclusions

Simulations and experiments show the method effectively restrains position error accumulation of smartphone PDR using only IMU data. It achieves better estimation accuracy than filter-based methods and runs faster than the particle filter, even with multiple factor graphs.
