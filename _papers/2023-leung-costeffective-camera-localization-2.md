---
title: COST-EFFECTIVE CAMERA LOCALIZATION AIDED BY PRIOR POINT CLOUDS MAPS FOR LEVEL 3 AUTONOMOUS DRIVING VEHICLES
authors:
- Y.-T. Leung
- X. Zheng
- H.-Y. Ho
- W. Wen
- L.-T. Hsu
publisher: The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences
date: '2023-05-25'
doi: https://doi.org/g8xprb
image: images/papers/cards/2023-leung-costeffective-camera-localization-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/isprs-archives-XLVIII-1-W1-2023-227-2023.pdf
tags:
- Autonomous Driving Vehicles
- Visual localization
- 3D LiDAR maps
- Image reconstruction
- Matching geometry
citation_id: 10.5194/isprs-archives-XLVIII-1-W1-2023-227-2023
---

## Abstract

Precise and robust localization is critical for many navigation tasks, especially autonomous driving systems. The most popular localization approach is global navigation satellite systems (GNSS). However, it has several shortcomings such as multipath and non-line-of-sight reception. Vision-based localization is one of the approaches without using GNSS which is based on vision. This paper used visual localization with a prior 3D LiDAR map. Compared to common methods for visual localization using camera-acquired maps, this paper used the method that tracks the image feature and poses of a monocular camera to match with prior 3D LiDAR maps. This paper reconstructs the image feature to several sets of 3D points by a local bundle adjustment-based visual odometry system. Those 3D points matched with the prior 3D point cloud map to track the globe pose of the user. The visual localization approach has several advantages. (1) Since it only relies on matching geometry, it is robust to changes in ambient luminosity appearance. (2) Also, it uses the prior 3D map to provide viewpoint invariance. Moreover, the proposed method only requires users to use low-cost and lightweight camera sensors.

## Problem Addressed

GNSS-based localization suffers from multipath and non-line-of-sight reception, so autonomous driving systems need accurate alternatives; a cost-effective approach using only a low-cost camera remains desirable for Level 3 autonomous vehicles.

## Key Contributions

- Monocular visual localization against a prior 3D LiDAR point cloud map instead of camera-acquired maps
- Local bundle-adjustment visual odometry reconstructing image features into 3D point sets matched with the prior map
- Continuous 6-DoF global camera pose tracking from the local-to-prior map transformation
- Geometry-only matching providing robustness to lighting changes and viewpoint invariance with low-cost sensors

## Conclusions

The method combines the benefits of LiDAR and camera to estimate the transformation between the local point map and the prior 3D map, continuously tracking the 6-DoF camera pose. Real-world experiments on open-source data demonstrated the accuracy of the system. Highly dynamic urban environments remain challenging, and future work will improve the method in more dynamic and complex scenarios.
