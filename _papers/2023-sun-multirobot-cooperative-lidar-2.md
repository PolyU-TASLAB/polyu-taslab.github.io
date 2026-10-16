---
title: MULTI-ROBOT COOPERATIVE LIDAR SLAM FOR EFFICIENT MAPPING IN URBAN SCENES
authors:
- Y. Sun
- F. Huang
- W. Wen
- L.-T. Hsu
- X. Liu
publisher: The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences
date: '2023-05-25'
doi: https://doi.org/g8t57z
image: images/papers/cards/2023-sun-multirobot-cooperative-lidar-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/isprs-archives-XLVIII-1-W1-2023-473-2023.pdf
tags:
- Factor graph optimization (FGO)
- geospatial information
- global navigation satellite system (GNSS)
- map
- navigation
citation_id: doi:10.5194/isprs-archives-XLVIII-1-W1-2023-473-2023
---

## Abstract

We first use the multi-robot SLAM framework DiSCo-SLAM to evaluate the performance of cooperative SLAM based on the complicated dataset in urban scenes. Besides, we perform comparisons of single-robot SLAM and multi-robot SLAM to explore whether the cooperative framework can noticeably improve robot localization performance and the influence of inter-robot constraints in local pose graph, utilizing an identical dataset generated via the Carla simulator. Our findings indicate that under specific conditions, the integration of inter-robot constraints may effectively mitigate drift in local pose estimation. The extent to which inter-robot constraints affect the correction of local SLAM is related to various factors, such as the confidence level of the constraints and the range of keyframes imposed by the constraint.

## Problem Addressed

Whether cooperative multi-robot SLAM noticeably improves robot localization over single-robot SLAM in complicated urban scenes, and how inter-robot constraints influence local pose graph estimation, remains insufficiently explored.

## Key Contributions

- First use of the DiSCo-SLAM framework to compare single-robot and cooperative multi-robot LiDAR SLAM on an identical Carla-simulated urban dataset
- Analysis of how inter-robot constraints are transformed into intra-pose constraints within local SLAM
- Study of factors governing constraint effectiveness, including confidence level and keyframe range

## Conclusions

The experiments show good collaborative mapping and localization results in large urban environments, and under specific conditions inter-robot constraints can effectively mitigate drift in local pose estimation. The extent of correction depends on factors such as the confidence level of the constraints and the range of keyframes they span. Proper task allocation between robots and route design strategies can leverage the benefits of inter-robot constraints.
