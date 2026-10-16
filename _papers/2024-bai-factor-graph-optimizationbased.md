---
title: Factor Graph Optimization-Based Smartphone IMU-Only Indoor SLAM With Multihypothesis Turning Behavior Loop Closures
authors:
- Shiyu Bai
- Weisong Wen
- Li-Ta Hsu
- Peiwen Yang
publisher: IEEE Transactions on Aerospace and Electronic Systems
date: '2024-12-01'
doi: https://doi.org/g8t54q
image: images/papers/cards/2024-bai-factor-graph-optimizationbased.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/BaiShiyu2024Factor_Graph_Optimization-Based_Smartphone_IMU-Only_Indoor_SLAM_With_Multihypothesis_Turning_Behavior_Loop_Closures.pdf
tags:
- Pedestrian dead reckoning
- simultaneous localization and mapping (SLAM)
citation_id: doi:10.1109/TAES.2024.3430256
---

## Abstract

Pedestrian dead reckoning (PDR) using smartphones is a popular method for indoor localization. However, it encounters challenges due to the drift of position errors. While external resources like Wi-Fi, Bluetooth, and indoor maps can correct the drift, they require the preinstallation of facilities or information, limiting their application. Inspired by the recent advancement of the simultaneous localization and mapping (SLAM), such as the visual SLAM, this article proposes a factor graph optimization (FGO)-based smartphone inertial measurement unit (IMU)-only indoor SLAM with multihypothesis turning behavior loop closures. In this article, the turning behavior that can be observed repetitively is regarded as landmarks, which are like the visual landmarks in visual SLAM. FGO is employed, wherein the motion deduced from PDR is used to establish relative constraints between consecutive variable nodes. Meanwhile, the robust loop closure constraint inferred from the multihypothesis behavior data association is formed to correct the drift of the PDR. Experimental tests in different scenarios are done to evaluate the localization performance, and the time consumption of the proposed method is given.

## Problem Addressed

Smartphone pedestrian dead reckoning suffers from cumulative position drift, while corrections from Wi-Fi, Bluetooth, or indoor maps require pre-installed facilities or prior information that limit deployment.

## Key Contributions

- Factor graph optimization-based IMU-only indoor SLAM treating repetitive turning behavior as landmarks, analogous to visual landmarks
- Multihypothesis turning behavior loop closures maintaining multiple factor graphs for reliable data association
- Turning behavior sequence classification to exclude improper loop closures and avoid losing valid associations
- Confidence ellipse construction and detailed PDR scheme improving turning-behavior data association

## Conclusions

Experiments in an office building and an underground car park show the method outperforms compared filter-based methods in instantaneous localization and produces smoother, more accurate trajectories. The approach transfers across smartphones because low-cost IMUs perform similarly, though it requires structured environments with corners or corridors and frequent revisits; it can be extended to a map-matching mode for distant goals.
