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
image: images/papers/cards/2023-zhang-lidar-feature-outlier-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Lidar_Feature_outlier.pdf
tags:
- 3D  LiDAR
- satety-critical  localization
- urban canyons
- fault detection and exclusion
- graduated non-convexity relaxation
citation_id: doi:10.1109/PLANS53410.2023.10139983
---

## Abstract

Safety-critical localization is essential for unmanned autonomous systems. LiDAR localization gains great popularity in urban canyons due to its high ranging accuracy. Inheriting from the integrity monitoring theory for GNSS, safety-certifiable LiDAR localization first consists in fault detection and exclusion (FDE). In face of numerous LiDAR measurements, conventional chi-square test for FDE is computationally intractable. What's more, inliers could be mistakenly excluded without reconsideration. This paper proposes a computationally tractable and flexible FDE method. It's realized via outlier mitigation aided by graduated non-convexity (GNC) relaxation. The two novel loss functions truncated least square (TLS) and the Geman McClure (GM) are combined respectively. The outlier-mitigated planar-feature-based LiDAR localization is formulated with GNC and TLS or GM. More importantly, a triple-layer optimization method is proposed to solve the localization formulation. Besides the typical GNC relaxation, the control parameter is taken into consideration for tuning the outliers resistance degree. The outlier mitigated pose estimation and the weightings ranging from 0 to 1 for the exploited LiDAR measurements are finally produced. Extensive experiments of the proposed method is conducted on urban dataset. What's more, considering that TSL and GM provides distinct outlier mitigation patterns, the performances from them are investigated and compared.

## Problem Addressed

Safety-critical LiDAR localization requires fault detection and exclusion, but the conventional chi-square test is computationally intractable given the numerous LiDAR measurements and may mistakenly exclude inliers without reconsideration.

## Key Contributions

- Computationally tractable and flexible FDE via graduated non-convexity relaxation
- Outlier-mitigated planar-feature LiDAR localization formulated with GNC combined with truncated least squares and Geman-McClure losses
- Triple-layer optimization incorporating a control parameter to tune the degree of outlier resistance
- Extensive urban-dataset experiments comparing the distinct mitigation patterns of TLS and GM

## Conclusions

The proposed method produces outlier-mitigated pose estimates together with per-measurement weightings ranging from 0 to 1 for the exploited LiDAR measurements. Extensive experiments on urban datasets demonstrate the approach, and the distinct outlier-mitigation behaviors of the TLS and GM loss functions are investigated and compared.
