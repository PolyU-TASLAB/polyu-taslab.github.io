---
title: Real-time Factor Graph Optimization Aided by Graduated Non-convexity Based Outlier Mitigation for Smartphone Decimeter Challenge
authors:
- Yihan Zhong
- Weisong Wen
- Hoi-Fung Ng
- Xiwei Bai
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2022-10-20'
doi: https://doi.org/g8t5r3
image: images/papers/cards/2022-zhong-realtime-factor-graph.jpg
buttons:
- type: manubot
  text: paper
  link: https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/publications/papers/xxx.pdf
tags: []
citation_id: doi:10.33012/2022.18382
---

## Abstract

Real-time reliable navigation in urban environments has received academic and commercial interest over recent years. Unfortunately, commercial sensors such as smartphones are implemented with low-cost antennas and chips for receiving satellite signals and suffered from severe signal degrading caused by the non-light-of-sight (NLOS) and multipath effect. Many conventional methods like extended Kalman filter (EKF) would always perform poorly in the urban environment. Factor graph optimization (FGO) has recently proved its reliable navigation performance in urban environments, utilizing the multi-epoch GNSS measurements to estimate the user position simultaneously. Furthermore, recent studies verified that outlier mitigation technologies using graduated non-convexity (GNC) could effectively improve GNSS positioning performance. However, those studies are mainly concerned with batch optimization which makes the computational load significant and leads to large time consumption, especially while the system integrates the GNC-based robust function in optimization for outlier mitigation. For smartphones application, this study proposed a real-time sliding window-based FGO with the implementation of GNC for outlier mitigation to guarantee reliability and low time consumption. This paper verifies the effectiveness of the contributions of this paper step by step using datasets in Shang Hai and Los Angeles. We also discussed the impact of the different sizes of sliding windows in terms of positioning error and time consumption.

## Problem Addressed

GNSS vehicular positioning is significantly degraded in urban canyons by outlier measurements such as multipath and NLOS receptions from building reflections. Existing local robust-estimation solutions can fall into local minima when downweighting such outliers.

## Key Contributions

- FGO-GNC formulation combining pseudorange/Doppler factor graph optimization with adaptive weighting estimation
- Non-convex Geman-McClure function with graduated non-convexity for global weight estimation via coarse-to-fine relaxation
- First GNC-aided FGO formulation globally estimating state and measurement weightings simultaneously
- Evaluation on Hong Kong urban-canyon datasets with automobile-level and smartphone-level receivers

## Conclusions

FGO-GNC improved GNSS positioning accuracy by mitigating outlier measurements without any additional sensors, verified on several urban-canyon datasets using both ITS-level and smartphone-level receivers. With the Huawei P40 Pro, the remaining error can still reach 13.6 m due to poor smartphone measurement quality. Future work includes applying FGO-GNC to carrier-phase RTK, multi-constellation and multi-frequency measurements, and fusing the vehicle dynamic model and phone IMU.
