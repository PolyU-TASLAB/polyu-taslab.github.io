---
title: Uncertainty estimation of LiDAR matching aided by dynamic vehicle detection and high definition map
authors:
- W. Wen
- X. Bai
- W. Zhan
- M. Tomizuka
- L.-T. Hsu
publisher: Electronics Letters
date: '2019-03-01'
doi: https://doi.org/ggtk78
image: images/papers/cards/2019-wen-uncertainty-estimation-lidar.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/UELM.pdf
tags:
- 3D LiDAR
- Uncertainty estimation
- dynamic detection
citation_id: doi:10.1049/el.2018.8075
---

## Abstract

LiDAR matching between real-time point clouds and pre-built points map is a popular approach to provide accurate localisation service for autonomous vehicles. However, the performance is severely deteriorated in dense traffic scenes. Unavoidably, dynamic vehicles introduce additional uncertainty to the matching result. The main cause is that the pre-built map can be blocked by the surrounding dynamic vehicles from the view of LiDAR of ego vehicle. A novel uncertainty of LiDAR matching (ULM) estimation method aided by the dynamic vehicle (DV) detection and high definition map is proposed in this Letter. Compared to the conventional Hessian matrix-based ULM estimation approach, the proposed method innovatively estimates the ULM by modelling surrounding DV. Then the authors propose to correlate the ULM with the detected DV and convergence feature of matching algorithm. From the evaluated real-data in an intersection area with dense traffic, the proposed method has exhibited the feasibility of estimating the ULM accurately.

## Problem Addressed

LiDAR matching against pre-built point cloud maps deteriorates severely in dense traffic, because surrounding dynamic vehicles block the map from the ego vehicle's LiDAR view and introduce additional localization uncertainty that conventional Hessian-based estimation does not capture.

## Key Contributions

- Uncertainty of LiDAR matching estimation method aided by dynamic vehicle detection and a high-definition map
- Modeling of surrounding dynamic vehicles to estimate matching uncertainty beyond the Hessian-based approach
- Correlation of the estimated uncertainty with detected dynamic vehicles and convergence features of the matching algorithm

## Conclusions

Evaluation on real data collected at an intersection with dense traffic demonstrates the feasibility of accurately estimating the uncertainty of LiDAR matching, showing that explicitly modeling dynamic vehicles improves uncertainty estimation over the conventional Hessian-based method.
