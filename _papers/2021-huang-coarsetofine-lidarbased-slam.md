---
title: A Coarse-to-Fine LiDAR-Based SLAM with Dynamic Object Removal in Dense Urban Areas
authors:
- Feng Huang
- Donghui Shen
- Weisong Wen
- Jiachen Zhang
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2021-10-13'
doi: https://doi.org/gsk2vg
image: images/papers/cards/2021-huang-coarsetofine-lidarbased-slam.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Huang_Coarse-To-Fine_Lidar-Based_Slam.pdf
tags:
- SLAM
- Lidar
- Localization
- DNN
- Dynamic object removal
citation_id: doi:10.33012/2021.18083
---

## Abstract

Robust and precise localization and mapping are essential for autonomous systems. Light detection and ranging (LiDAR) odometry is extensively studied in the past decades to achieve this goal. However, almost all the LiDAR-based approaches are built on top of the static world assumption. The performance of the LiDAR-based method is significantly degraded in urban canyons with enormous dynamic objects. To tackle this challenge, we propose a coarse-to-fine LiDAR-based solution with dynamic object removal. Both instant-level deep neural network (DNN) and point-wise discrepancy images are adopted to deal with the dynamic points. The evaluation results show that a 19.1% improvement of the LiDAR-based method in a highly urbanized area can be achieved by distinguishing dynamic objects from LiDAR scan while generating clean maps for real-world representation.

## Problem Addressed

LiDAR-based SLAM methods are built on the static world assumption, so their localization and mapping performance degrades significantly in urban canyons crowded with dynamic objects.

## Key Contributions

- Coarse-to-fine LiDAR-based SLAM pipeline with dynamic object removal.
- Instance-level deep neural network coarsely detects dynamic objects in urban scenes.
- Point-wise discrepancy images refine dynamic point labeling before fine-stage mapping.
- Evaluation on challenging datasets collected in typical urban canyons of Hong Kong.

## Conclusions

Distinguishing dynamic objects from LiDAR scans improves the odometry of the LiDAR-based method by 19.1% in a highly urbanized area. The pipeline also generates cleaner point cloud maps that better represent the real world.
