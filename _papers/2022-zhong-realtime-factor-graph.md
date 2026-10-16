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

Accurate and globally referenced global navigation satellite system (GNSS)based vehicular positioning can be achieved in outlier-free open areas. However, the performance of GNSS can be significantly degraded by outlier measurements, such as multipath effects and non-line-of-sight (NLOS) receptions arising from signal reflections of buildings. Inspired by the advantage of batch historical data in resisting outlier measurements, in this paper, we propose a graduated non-convexity factor graph optimization (FGO-GNC) to improve the GNSS positioning performance, where the impact of GNSS outliers is mitigated by estimating the optimal weightings of GNSS measurements. Different from the existing local solutions, the proposed FGO-GNC employs the non-convex
Geman McClure (GM) function to globally estimate the weightings of GNSS measurements via a coarse-to-fine relaxation. The effectiveness of the proposed method is verified through several challengingdatasetscollectedinurbancanyonsofHongKongusing automobile level and low-cost smartphone level GNSS receivers.

## Problem Addressed

GNSS vehicular positioning is significantly degraded in urban canyons by outlier measurements such as multipath and NLOS receptions from building reflections. Existing local robust-estimation solutions can fall into local minima when downweighting such outliers.

## Key Contributions

- FGO-GNC formulation combining pseudorange/Doppler factor graph optimization with adaptive weighting estimation
- Non-convex Geman-McClure function with graduated non-convexity for global weight estimation via coarse-to-fine relaxation
- First GNC-aided FGO formulation globally estimating state and measurement weightings simultaneously
- Evaluation on Hong Kong urban-canyon datasets with automobile-level and smartphone-level receivers

## Conclusions

FGO-GNC improved GNSS positioning accuracy by mitigating outlier measurements without any additional sensors, verified on several urban-canyon datasets using both ITS-level and smartphone-level receivers. With the Huawei P40 Pro, the remaining error can still reach 13.6 m due to poor smartphone measurement quality. Future work includes applying FGO-GNC to carrier-phase RTK, multi-constellation and multi-frequency measurements, and fusing the vehicle dynamic model and phone IMU.
