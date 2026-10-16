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
image: images/papers/cards/2023-sun-multirobot-cooperative-lidar.jpg
citation_id: doi:10.5194/isprs-archives-xlviii-1-w1-2023-473-2023
---

## Abstract

We first use the multi-robot SLAM framework DiSCo-SLAM to evaluate the performance of cooperative SLAM based on the complicated dataset in urban scenes. Besides, we perform comparisons of single-robot SLAM and multi-robot SLAM to explore whether the cooperative framework can noticeably improve robot localization performance and the influence of inter-robot constraints in local pose graph, utilizing an identical dataset generated via the Carla simulator. Our findings indicate that under specific conditions, the integration of inter-robot constraints may effectively mitigate drift in local pose estimation. The extent to which inter-robot constraints affect the correction of local SLAM is related to various factors, such as the confidence level of the constraints and the range of keyframes imposed by the constraint.

## Problem Addressed

Whether cooperative multi-robot SLAM noticeably improves robot localization performance over single-robot SLAM, and how inter-robot constraints influence the local pose graph, remains insufficiently explored in complex urban scenes.

## Key Contributions

- Evaluation of the DiSCo-SLAM multi-robot framework on a complex urban dataset generated with the Carla simulator
- Systematic comparison of single-robot and multi-robot LiDAR SLAM on identical data
- Analysis of how inter-robot constraints, transformed into intra-pose constraints, affect local SLAM correction

## Conclusions

Collaborative SLAM yields good mapping and localization results in large urban environments. Under specific conditions, inter-robot constraints effectively mitigate drift in local pose estimation, with effectiveness depending on factors such as constraint confidence and the range of keyframes constrained. Proper task allocation between robots and route design strategies may better leverage the benefits of inter-robot constraints.
