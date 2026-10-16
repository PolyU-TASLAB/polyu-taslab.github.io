---
title: LiDAR Feature Outlier Mitigation Aided by Graduated Non-convexity Relaxation for Safety-critical Localization in Urban Canyons
authors:
- Jiachen Zhang
- Weisong Wen
- Li-Ta Hsu
- Zheng Gong
- Zhongzhe Su
publisher: 2023 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2023-04-24'
doi: https://doi.org/g8t574
image: images/papers/cards/2023-zhang-lidar-feature-outlier.jpg
citation_id: doi:10.1109/plans53410.2023.10139983
---

## Abstract

Safety-critical localization is essential for unmanned autonomous systems. LiDAR localization gains great popularity in urban canyons due to its high ranging accuracy. 
Inheriting from the integrity monitoring theory for GNSS, safety-certifiable LiDAR localization first consists in fault detection and exclusion (FDE). In face of numerous LiDAR measurements, conventional chi-square test for FDE is computationally intractable. What's more, inliers could be mistakenly excluded without reconsideration. This paper proposes a computationally tractable and flexible FDE method. 
It's realized via outlier mitigation aided by graduated nonconvexity (GNC) relaxation. The two novel loss functions truncated least square (TLS) and the Geman McClure (GM) are combined respectively. The outlier-mitigated planar-featurebased LiDAR localization is formulated with GNC and TLS or 
GM. More importantly, a triple-layer optimization method is proposed to solve the localization formulation. Besides the typical GNC relaxation, the control parameter is taken into consideration for tuning the outliers resistance degree. The outlier mitigated pose estimation and the weightings ranging from 0 to 1 for the exploited LiDAR measurements are finally produced. Extensive experiments of the proposed method is conducted on urban dataset. What's more, considering that TSL and GM provides distinct outlier mitigation patterns, the performances from them are investigated and compared.

## Problem Addressed

Safety-certifiable LiDAR localization requires fault detection and exclusion, but the conventional chi-square test is computationally intractable with numerous LiDAR measurements, and inliers can be mistakenly excluded without reconsideration.

## Key Contributions

- Computationally tractable and flexible FDE via outlier mitigation with graduated non-convexity relaxation
- Combination of truncated least squares and Geman-McClure loss functions
- Outlier-mitigated planar-feature-based LiDAR localization formulated with GNC and TLS or GM
- Triple-layer optimization with a control parameter tuning outlier resistance, yielding pose estimates and measurement weights

## Conclusions

Extensive experiments on an urban dataset evaluate the proposed outlier mitigation method for planar-feature-based LiDAR localization. The distinct outlier mitigation patterns provided by the TLS and GM loss functions are investigated and compared.
