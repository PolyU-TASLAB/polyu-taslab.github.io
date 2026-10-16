---
title: Degeneration-Aware Outlier Mitigation for Visual Inertial Integrated Navigation System in Urban Canyons
authors:
- Xiwei Bai
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Instrumentation and Measurement
date: '2021-01-01'
doi: https://doi.org/gsk25m
image: images/papers/cards/2021-bai-degenerationaware-outlier-mitigation.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Degeneration-Aware_Outlier_Mitigation_for_Visual_Inertial_Integrated_Navigation_System_in_Urban_Canyons.pdf
tags:
- GNC
- navigation
- optimizaiton method
- outlier measurement
- urban canyons
- VINS
- Visual odometry
citation_id: doi:10.1109/TIM.2021.3126010
---

## Abstract

In this article, we proposed a graduated nonconvexity (GNC) aided outlier mitigation method for the improvement of the visual-inertial integrated navigation system (VINS) to face the challenge of dynamic environments with numerous unexpected outlier measurements. A GNC optical flow algorithm was proposed for the detection of the outliers of feature tracking in the front-end of VINS by iteratively estimating the optical
flow and the optimal weightings of feature correspondences.
Then the feature correspondences with small weightings were excluded. However, excessive outlier exclusion may cause insufficient constraints on the state, causing degeneration of VINS.
To solve the problem, this article proposed to detect the potential degeneration based on the degree of constraint in different directions of the pose estimation. Then the number of features being considered was intelligently adapted based on the degeneration level to improve the geometry constraint in the coming epochs.
We evaluated the effectiveness of the proposed method by using two challenging datasets (including challenging night scenarios) collected in urban canyons of Hong Kong. The results show that the proposed method can effectively reject the potential outlier visual measurements, and alleviate the degeneration, leading to improved positioning performance in both evaluated datasets.

## Problem Addressed

Visual-inertial navigation systems in dynamic urban environments face numerous unexpected outlier visual measurements. Aggressively excluding outliers can leave insufficient constraints and cause degeneration of the pose estimation.

## Key Contributions

- Graduated nonconvexity (GNC) optical flow detects feature-tracking outliers by iteratively estimating flow and optimal correspondence weightings.
- Degeneration detection based on the degree of constraint along different directions of pose estimation.
- Number of considered features intelligently adapted to the degeneration level to maintain geometry constraints.
- Evaluated on two challenging Hong Kong urban canyon datasets, including night scenarios.

## Conclusions

The proposed method effectively rejects outlier visual measurements while detecting and alleviating the resulting degeneration, leading to improved positioning performance on both evaluated urban canyon datasets.
