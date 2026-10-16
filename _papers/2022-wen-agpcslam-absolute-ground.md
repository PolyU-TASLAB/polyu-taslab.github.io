---
title: 'AGPC-SLAM: Absolute Ground Plane Constrained 3D Lidar SLAM'
authors:
- Weisong Wen
- Li-Ta Hsu
publisher: 'NAVIGATION: Journal of the Institute of Navigation'
date: '2022-01-01'
doi: https://doi.org/gsk2zv
image: images/papers/cards/2022-wen-agpcslam-absolute-ground.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/AGPC-SLAM.pdf
tags:
- dynamic object
- ground plane constraint
- lidar SLAM
- urban canyons
citation_id: 10.33012/navi.527
---

## Abstract

3D lidar-based simultaneous localization and mapping (SLAM) is a well-recognized solution for mapping and localization applications. However, the typical 3D lidar sensor (e.g., Velodyne HDL-32E) only provides a very limited field of view vertically. As a result, the vertical accuracy of pose estimation suffers. This paper aims to alleviate this problem by detecting the absolute ground plane to constrain vertical pose estimation. Different from the conventional relative plane constraint, this paper employs the absolute plane distance to refine the position in the z-axis and the norm vector of the ground plane to constrain the attitude drift. Finally, relative positioning from lidar odometry, constraint from ground plane detection, and loop closure are integrated under a proposed factor graph-based 3D lidar SLAM framework (AGPC-SLAM). The effectiveness is verified using several data sets collected in Hong Kong.
Keywords dynamic object, ground plane constraint, lidar SLAM, urban canyons

WEN and HSU
     positioning from the front-end, positioning from the global navigation satellite system (GNSS; Dow et al., 2009; Shetty & Gao, 2019), and loop closure (Magnusson et al., 2009). 
The accuracy of point cloud registration, which is the major part of the front-end, dominates the performance of 3D lidar SLAM. Therefore, numerous works have been studied to improve the point cloud registration process, such as the iterative closest point (ICP; Kuramachi et al., 2015), the normal distribution transform (NDT; Magnusson et al., 2007), and lidar odometry and mapping (LOAM; Zhang & 
Singh, 2017). The LOAM algorithm obtained top accuracy in the KITTI data set odometry benchmark (Geiger et al., 2012) until December 2020 due to its feature extraction and impressive data association structure. Unlike the point-wise registration methods (e.g., ICP and NDT), the LOAM algorithm extracts meaningful edge and planar features from raw 3D point clouds, leading to lower computational load and decreased sensitivity to the local minimums. Instead of simply relying on finding the transformation between consecutive frames of point clouds (Low, 
2004; Pang et al., 2019; Saarinen et al., 2013) v

## Problem Addressed

Typical 3D LiDAR sensors provide only a limited vertical field of view, so vertical pose estimation in 3D LiDAR SLAM suffers from accumulated drift; existing relative plane constraints cannot bound this error over time.

## Key Contributions

- Absolute ground plane constraint using absolute plane distance and normal vector to constrain z-axis position and attitude drift
- General factor-graph 3D LiDAR SLAM framework integrating LiDAR odometry, ground plane constraint, and loop closure
- Framework readily extensible to additional sensors such as GNSS and magnetometers
- Validation on two challenging large-scale datasets collected in Hong Kong

## Conclusions

AGPC-SLAM achieved improved accuracy over the state-of-the-art LeGO-LOAM, effectively mitigating z-axis drift in both evaluated scenarios; better-constrained vertical states also improved x- and y-axis positioning. With loop closure it reached 0.43 m translation RMSE, 0.64 degree rotation RMSE, and 0.13 m altitude error. A limitation is the requirement of a flat ground plane; slopes or ground occlusion by dynamic vehicles can cause misidentification, which future work will address.
