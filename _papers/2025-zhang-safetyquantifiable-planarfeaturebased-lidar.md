---
title: Safety-Quantifiable Planar-Feature-Based LiDAR Localization With a Prior Map for Intelligent Vehicles in Urban Scenarios
authors:
- Jiachen Zhang
- Xikun Liu
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Vehicles
date: '2025-07-01'
doi: https://doi.org/g8t5zc
image: images/papers/cards/2025-zhang-safetyquantifiable-planarfeaturebased-lidar.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/Jiachen2024Safety-Quantifiable_Planar-Feature-based_LiDAR_Localization.pdf
tags:
- 3D LiDAR
- Non-convexity
- Planar features
- Safety-quantifiable Localization
- Urban canyons
citation_id: doi:10.1109/TIV.2024.3467115
---

## Abstract

Safety-quantifiable and accurate localization is of great importance for safety-critical applications with navigation requirements, such as intelligent vehicles (IV). LiDAR-based localization with the prior map is highly expected due to its high accuracy. However, how to reliably quantify the safety (quantify the maximum potential localization error) of LiDAR localization is still an open challenge. Integrity monitoring (IM) is one of the most stringent existing solutions to quantify the safety of satellite navigation, where usually tens of measurements are involved and interpreted by an almost locally linear model. Differently, the number of measurements involved in the LiDAR localization problem is significantly larger (e.g. 2000). Moreover, the LiDAR measurement model is highly non-linear. The convexity of the 
LiDAR localization is still to be quantified. To fill these gaps, this paper proposes a safety-quantifiable planar feature-based LiDAR localization method with a prior map. Specifically, the LiDAR localization framework utilizing representative planar features with maximum spectral attributes is proposed. The cardinality restriction facilitates feasible safety quantification regardless of thousands of measurements. To quantify the convexity of the 
LiDAR localization problem, the Hessian matrix of the planar feature measurement model is analytically derived. The local convex property during non-linear optimization of the localization model is quantified from dual perspectives. Additionally, different from existing methods, the protection level of the derived LiDAR localization is estimated for both translation and rotation to quantify the safety. The feasibility of the proposed method is validated using the datasets collected in typical urban canyons of 
Hong Kong.

## Problem Addressed

Reliably quantifying the safety—the maximum potential error—of prior-map LiDAR localization is an open challenge, because the problem involves thousands of measurements and a highly nonlinear measurement model whose convexity has yet to be quantified, unlike the nearly linear models of satellite navigation integrity monitoring.

## Key Contributions

- Safety-quantifiable planar feature-based LiDAR localization framework using representative features with maximum spectral attributes
- Measurement cardinality reduction enabling feasible fault detection and exclusion despite thousands of raw measurements
- Analytical Hessian derivation quantifying local convexity of the nonlinear localization optimization from dual perspectives
- Protection levels estimated for both translation and rotation of the 6-DoF pose via the parity space approach

## Conclusions

Experiments on datasets collected in typical urban canyons of Hong Kong show that localization with representative planar features achieves accuracy comparable to the state-of-the-art pipeline using all available features, with hardly any accuracy compromise. Convexity quantification through positive-definiteness analysis of the Hessian certifies that the subsequent safety quantification is credible, and the residual-based protection level outperforms the conventional 3-sigma approach for safety awareness. Future work will combine fault detection with weight matrix estimation for tighter protection levels and study intractable real-world faults via simulation.
