---
title: Perception-aided Visual-Inertial Integrated Positioning in Dynamic Urban Areas
authors:
- Xiwei Bai
- Bo Zhang
- Weisong Wen
- Li-Ta Hsu
- Huiyun Li
publisher: 2020 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2020-04-01'
doi: https://doi.org/gkzh9d
image: images/papers/cards/2020-bai-perceptionaided-visualinertial-integrated.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Perception_aided_Visual-Inertial_Integrated_Positioning_in_Dynamic_Urban_Areas.pdf
tags:
- Visual Odometry
- INS
- VINS
- Navigation
- Positioning
- Urban Areas
citation_id: doi:10.1109/PLANS46316.2020.9109963
---

## Abstract

Visual-inertial navigation systems (VINS) have been extensively studied in the past decades to provide positioning services for autonomous systems, such as autonomous driving vehicles (ADV) and unmanned aerial vehicles (UAV). Decent performance can be obtained by VINS in indoor scenarios with stable illumination and texture information. Unfortunately, applying the VINS in dynamic urban areas is still a challenging problem, due to the excessive dynamic objects which can significantly degrade the performance of VINS. Detecting and removing the features inside an image using the deep neural network (DNN) that belongs to unexpected objects, such as moving vehicles and pedestrians, is a straightforward idea to mitigate the impacts of dynamic objects on VINS. However, excessive exclusion of features can significantly distort the geometry distribution of visual features. Even worse, excessive removal can cause the unobservability of the system states. Instead of directly excluding the features that possibly belong to dynamic objects, this paper proposes to remodel the uncertainty of dynamic features. Then both the healthy and dynamic features are applied in the VINS. The experiment in a typical urban canyon is conducted to validate the performance of the proposed method. The result shows that the proposed method can effectively mitigate the impacts of the dynamic objects and improved accuracy is obtained.

## Problem Addressed

Visual-inertial navigation systems degrade in dynamic urban areas where numerous moving objects corrupt feature tracking. Directly excluding features of dynamic objects can distort feature geometry and even cause unobservability of the system states.

## Key Contributions

- Remodel the uncertainty of dynamic feature points instead of directly excluding them from VINS.
- Dynamic features assigned smaller weightings than static visual features within factor graph optimization.
- Both healthy and dynamic features retained for state estimation.
- Experiment conducted in a typical urban canyon to validate the method.

## Conclusions

Remodeling dynamic features with reduced weighting effectively mitigates the impact of dynamic objects and improves accuracy. Excessive removal of dynamic features is not recommended because it distorts the geometry distribution of features, while the fixed weighting used in the experiments remains a limitation.
