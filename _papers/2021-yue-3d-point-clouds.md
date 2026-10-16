---
title: 3D Point Clouds Data Super Resolution-Aided LiDAR Odometry for Vehicular Positioning in Urban Canyons
authors:
- Jiang Yue
- Weisong Wen
- Jin Han
- Li-Ta Hsu
publisher: IEEE Transactions on Vehicular Technology
date: '2021-05-01'
doi: https://doi.org/g8tzct
image: images/papers/cards/2021-yue-3d-point-clouds.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/3D_Point_Clouds_Data_Super_Resolution-Aided_LiDAR_Odometry_for_Vehicular_Positioning_in_Urban_Canyons.pdf
tags:
- LiDAR
- NDT
- sparse point clouds
- superresolution
- convolutional neural network
- LiDAR odometry
- vehicular positioning
citation_id: doi:10.1109/TVT.2021.3069212
---

## Abstract

LiDAR odometry algorithms are extensively studied for vehicular positioning. However, achieving high-precision positioning using low-cost 16-channel LiDAR in urban canyons remains a challenging problem due to the limited point cloud density from low-cost LiDAR and excessive dynamic surrounding objects. To fill this gap, this paper proposes enriching sparse 3D point clouds to denser clouds via a novel deep learning-based superresolution (SR) algorithm before its utilization in 3D LiDAR odometry. We validate the effectiveness of the proposed method using the KITTI dataset and a challenging dataset collected in an urban canyon (with complex environmental structures and dynamic objects) of Hong Kong. We conclude that significantly denser point clouds are achieved with considerable accuracy. In addition, significantly improved performance of 3D LiDAR odometry is obtained in the evaluated dataset collected in an urban canyon of Hong Kong.

## Problem Addressed

High-precision vehicular positioning with a low-cost 16-channel LiDAR in urban canyons remains difficult because of the limited point cloud density of low-cost LiDAR and excessive dynamic surrounding objects.

## Key Contributions

- Deep learning-based super-resolution algorithm enriches sparse 3D point clouds before LiDAR odometry.
- LiDAR-only design explicitly exploits discontinuity between objects, removing the camera reliance of prior work.
- Sparsity and edge-detection analysis demonstrates feasibility of LiDAR standalone point cloud super-resolution.
- Validated on the KITTI dataset and a challenging Hong Kong urban canyon dataset.

## Conclusions

Significantly denser point clouds are achieved with considerable accuracy, comparable to state-of-the-art super-resolution methods. The enriched point clouds significantly improve 3D LiDAR odometry performance on the evaluated Hong Kong urban canyon dataset.
