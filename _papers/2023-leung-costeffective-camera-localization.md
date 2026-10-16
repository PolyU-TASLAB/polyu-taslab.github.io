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
image: images/papers/cards/2023-leung-costeffective-camera-localization.jpg
citation_id: doi:10.5194/isprs-archives-xlviii-1-w1-2023-227-2023
---

## Abstract

Precise and robust localization is critical for many navigation tasks, especially autonomous driving systems. The most popular localization approach is global navigation satellite systems (GNSS). However, it has several shortcomings such as multipath and nonline-of-sight reception. Vision-based localization is one of the approaches without using GNSS which is based on vision. This paper used visual localization with a prior 3D LiDAR map. Compared to common methods for visual localization using camera-acquired maps, this paper used the method that tracks the image feature and poses of a monocular camera to match with prior 3D LiDAR maps. 
This paper reconstructs the image feature to several sets of 3D points by a local bundle adjustment-based visual odometry system. 
Those 3D points matched with the prior 3D point cloud map to track the globe pose of the user. The visual localization approach has several advantages. (1) Since it only relies on matching geometry, it is robust to changes in ambient luminosity appearance. (2) Also, it uses the prior 3D map to provide viewpoint invariance. Moreover, the proposed method only requires users to use low-cost and lightweight camera sensors.

## Problem Addressed

Precise and robust localization is critical for autonomous driving, but GNSS suffers from multipath and non-line-of-sight reception. Vision-based localization with camera-acquired maps is a GNSS-free alternative that remains challenging with low-cost sensors.

## Key Contributions

- Monocular visual localization matching reconstructed image features against a prior 3D LiDAR point cloud map
- Local bundle adjustment-based visual odometry reconstructing image features into 3D point sets
- Continuous 6-DoF camera pose tracking via local-to-prior map registration
- Low-cost solution requiring only lightweight camera sensors, robust to luminosity changes

## Conclusions

The method combines the benefits of LiDAR and the camera to estimate the transformation between the local point map and the prior 3D map, continuously tracking the 6-DoF camera pose. Real-world experiments on open-source data demonstrate the accuracy of the system with notable outcomes. Handling more dynamic and challenging urban environments remains future work.
