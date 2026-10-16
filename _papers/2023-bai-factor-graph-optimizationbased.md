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
image: images/papers/cards/2023-bai-factor-graph-optimizationbased.jpg
citation_id: doi:10.1109/ipin57070.2023.10332510
---

## Abstract

Indoor localization by smartphones has indicated its promising application prospect in daily life. Smartphone-based pedestrian dead reckoning (PDR) is a common method to obtain the locations. However, PDR suffers from position error accumulation. Although radio frequency (RF) and indoor map can be utilized to restrain the error drift, it requires the prior deployment of facilities or information, which is unsuitable for unknown environments. This paper proposes a factor graph optimization (FGO)-based indoor pedestrian simultaneous localization and mapping (SLAM) with probabilistic exact activity loop closures using a smartphone. In this paper, the smartphone built-in inertial measurement unit (IMU) is solely used to achieve SLAM, in which the human turning activity is regarded as the landmark. Repeatedly observed activities are then used to form loop closures to restrain the drift. FGO is first utilized to formulate pedestrian IMU-only SLAM, which achieves better estimation accuracy than the filter-based method. Moreover, multi-hypothesis tracking is employed to deal with ambiguous data association. During the turning, key points are defined and mutually matched to form exact loop closures to improve estimation accuracy. Simulations and experimental tests are both done to evaluate the performance of the proposed method.

## Problem Addressed

Smartphone-based pedestrian dead reckoning suffers from position error accumulation. Radio frequency signals and indoor maps can restrain the drift but require prior deployment of facilities or information, which is unsuitable for unknown environments.

## Key Contributions

- Graph-based indoor pedestrian SLAM framework using only smartphone IMU, with human turning activity as landmarks
- First use of factor graph optimization instead of particle filter for activity-landmark pedestrian SLAM
- Probabilistic exact activity loop closures with multi-hypothesis data association
- Key location points during turning defined and matched to form exact loop closures

## Conclusions

The proposed FGO-based pedestrian SLAM achieves better estimation accuracy than filter-based methods and effectively restrains position error accumulation of smartphone-based PDR using only IMU data. Exact loop closures from key turning points and multiple hypotheses further improve trajectory accuracy. The method also runs faster than the particle filter despite maintaining multiple factor graphs.
