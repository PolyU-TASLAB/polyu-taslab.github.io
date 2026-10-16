---
title: 3D Mapping Database Aided GNSS Based Collaborative Positioning Using Factor Graph Optimization
authors:
- Guohao Zhang
- Hoi-Fung Ng
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Transportation Systems
date: '2021-10-01'
doi: https://doi.org/ggt6br
image: images/papers/cards/2021-zhang-3d-mapping-database.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/3MDA.pdf
tags:
- Global navigation satellite system
- Collaboration
- Roads
- Ray tracing
- Three-dimensional displays
- Optimization
- Satellites
citation_id: doi:10.1109/TITS.2020.2988531
---

## Abstract

The recent development in vehicle-to-everything (V2X) communication opens a new opportunity to improve the positioning performance of the road users. We explore the benefit of connecting the raw data of the global navigation satellite system (GNSS) from the agents. In urban areas, GNSS positioning is highly degraded due to signal blockage and reflection.
3D building model can play a major role in mitigating the GNSS multipath and non-line-of-sight (NLOS) effects. To combine the benefits of 3D models and V2X, we propose a novel 3D mapping aided (3DMA) GNSS-based collaborative positioning method that makes use of the available surrounding GNSS receivers' measurements. By complementarily integrating the ray-tracing based 3DMA GNSS and the double difference technique, the random errors (such as multipath and NLOS) are mitigated while eliminating the systematic errors (such as atmospheric delay and satellite clock/orbit biases) between road user. To improve the accuracy and robustness of the collaborative algorithm, factor graph optimization (FGO) is employed to optimize the positioning solutions among agents. Multiple low-cost GNSS receivers are used to collect both static and dynamic data in Hong Kong and to evaluate the proposed algorithm by post-processing. We reduce the GNSS positioning error from over 30 meters to less than
10 meters for road users in a deep urban canyon.

## Problem Addressed

GNSS positioning in dense urban areas is severely degraded by signal blockage and reflection, causing multipath and NLOS errors for road users. Although V2X communication allows sharing raw GNSS measurements between agents, combining them effectively requires mitigating random errors while eliminating systematic errors such as atmospheric delay and satellite clock/orbit biases.

## Key Contributions

- Complementary integration of ray-tracing 3DMA GNSS with double-difference collaborative positioning without additional sensors
- Double-difference technique eliminates systematic errors between road users while ray tracing mitigates multipath and NLOS
- Factor graph optimization over multi-agent measurements for robust positioning amid frequent outliers
- Static and dynamic evaluation with multiple low-cost GNSS receivers in Hong Kong

## Conclusions

Using a receiver in a GNSS-friendly area as anchor, the proposed method reduced the degraded receiver's RMSE from 30.9 m (conventional least squares) to 7.8 m. With factor graph optimization applied across all measurements, most participating agents achieved RMSE below 10 m in dense urban areas. Remaining challenges include the high computational cost of ray tracing, quadratically growing pairwise evaluation, and the stability of uncertainty estimated from positioning error maps; intelligently selecting collaborating agents is identified as promising future work.
