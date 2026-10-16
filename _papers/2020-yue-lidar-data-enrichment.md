---
title: 'LiDAR Data Enrichment Using Deep Learning Based on High-Resolution Image: An Approach to Achieve High-Performance LiDAR SLAM Using Low-cost LiDAR'
authors:
- Jiang Yue
- Weisong Wen
- Jing Han
- Li-Ta Hsu
publisher: arXiv
date: '2020-01-01'
doi: https://doi.org/g8t489
image: images/papers/cards/2020-yue-lidar-data-enrichment.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/LDEUDL.pdf
tags:
- LiDAR
- Point Clouds
- Depth Completion
- Convolutional Neural Network
- NDT
- SLAM
citation_id: doi:10.48550/arXiv.2008.03694
---

## Abstract

LiDAR-based simultaneous localization and mapping (SLAM) algorithms are extensively studied to providing robust and accurate positioning for autonomous driving vehicles (ADV) in the past decades. Satisfactory performance can be obtained using high-grade 3D LiDAR with 64 channels, which can provide dense point clouds. Unfortunately, the high price significantly prevents its extensive commercialization in ADV. The cost-effective 3D LiDAR with 16 channels is a promising replacement. However, only limited and sparse point clouds can be provided by the 16 channels LiDAR, which cannot guarantee sufficient positioning accuracy for ADV in challenging dynamic environments. The high-resolution image from the low-cost camera can provide ample information about the surroundings. However, the explicit depth information is not available from the image. Inspired by the complementariness of 3D LiDAR and camera, this paper proposes to make use of the high-resolution images from a camera to enrich the raw 3D point clouds from the low-cost 16 channels LiDAR based on a state-of-the-art deep learning algorithm. An ERFNet is firstly employed to segment the image with the aid of the raw sparse 3D point clouds. Meanwhile, the sparse convolutional neural network (SCNN) is employed to predict the dense point clouds based on raw sparse 3D point clouds. Then, the predicted dense point clouds are fused with the segmentation outputs from ERFnet using a novel multi-layer convolutional neural network (MCNN) to refine the predicted 3D point clouds. Finally, the enriched point clouds are employed to perform LiDAR SLAM based on the state-of-the-art normal distribution transform (NDT). We tested our approach on the re-edited KITTI datasets: (1) the sparse 3D point clouds are significantly enriched with a mean square error of 1.1m MSE. (2) the map generated from the LiDAR SLAM is denser which includes more details without significant accuracy loss.

## Problem Addressed

High-grade 64-channel LiDAR that enables satisfactory SLAM is too expensive for widespread commercialization in autonomous driving, while low-cost 16-channel LiDAR provides only sparse point clouds that cannot guarantee sufficient positioning accuracy in challenging dynamic environments.

## Key Contributions

- Enriches sparse 16-channel LiDAR point clouds using high-resolution camera images via deep learning
- Uses ERFNet for image segmentation aided by the raw sparse point clouds
- Predicts dense point clouds with a sparse convolutional neural network (SCNN)
- Refines predictions by fusing segmentation and predicted clouds with a multi-layer CNN (MCNN)
- Performs NDT-based LiDAR SLAM on the enriched point clouds and tests on re-edited KITTI datasets

## Conclusions

On re-edited KITTI datasets, the sparse 3D point clouds are significantly enriched with a mean square error of 1.1 m, and the SLAM maps generated from the enriched data are denser and include more details without significant accuracy loss. Future work will collect challenging urban on-road datasets in Hong Kong and explore using the denser point clouds to detect or correct GNSS NLOS.
