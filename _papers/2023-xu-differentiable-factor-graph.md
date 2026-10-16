---
title: Differentiable Factor Graph Optimization with Intelligent Covariance Adaptation for Accurate Smartphone Positioning
authors:
- Penghui Xu
- Hoi-Fung Ng
- Yihan Zhong
- Guohao Zhang
- Weisong Wen
- Bo Yang
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2023-10-05'
doi: https://doi.org/hcc4r4
citation_id: doi:10.33012/2023.19297
---

## Abstract

Factor graph optimization (FGO) has recently become a popular approach for Global Navigation Satellite System (GNSS) positioning. Weighting being used in the FGO is crucial to the performance. Great efforts have been spent in deciding the weighting with various approaches, including uncertainties estimated from devices, statistical modeling, empirical model, etc. In this paper, we proposed a differentiable FGO (DFGO) for intelligent covariance adaptation to determine the weighting for state estimation. Adaptive weightings are obtained via the neural network, which is trained with ground truth location via backpropagation. The end-to-end training for the DFGO can make use of the information from the data while maintaining the benefits of the estimation framework. The weighting from the DFGO is demonstrated to perform better in positioning than the weighting calculated from the measurement uncertainties, which shows the feasibility of the DFGO approach.

## Problem Addressed

Factor graph optimization for GNSS positioning depends critically on measurement weighting, which is difficult to determine accurately using device-reported uncertainties, statistical modeling, or empirical models.

## Key Contributions

- Differentiable factor graph optimization framework enabling intelligent covariance adaptation for GNSS positioning
- Neural network producing adaptive measurement weightings for state estimation
- End-to-end training with ground truth locations via backpropagation through the estimation framework

## Conclusions

The weightings learned by the differentiable FGO yield better positioning accuracy than weightings derived from measurement uncertainties, demonstrating the feasibility of end-to-end trained covariance adaptation that exploits data information while retaining the benefits of the estimation framework.
