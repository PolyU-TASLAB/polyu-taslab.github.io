---
title: 'Factor graph optimization for GNSS/INS integration: A comparison with the extended Kalman filter'
authors:
- Weisong Wen
- Tim Pfeifer
- Xiwei Bai
- Li‐Ta Hsu
publisher: NAVIGATION
date: '2021-05-22'
doi: https://doi.org/gj5n6w
image: images/papers/cards/2021-wen-factor-graph-optimization.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Wen_Factor_graph_for_GNSS.pdf
tags:
- GNSS
- extended Kalman filter
- Failure detection and exclusion
- urban canyon
- FGO
- INS
- integration
- navigation
- positioning
- window size
citation_id: doi:10.1002/navi.421
---

## Abstract

Factor graph optimization (FGO) recently has attracted attention as an alternative to the extended Kalman filter (EKF) for GNSS-INS integration. This study evaluates both loosely and tightly coupled integrations of GNSS code pseudorange and INS measurements for real-time positioning, using both conventional EKF and FGO with a dataset collected in an urban canyon in Hong Kong. The FGO strength is analyzed by degenerating the FGO-based estimator into an “EKF-like estimator.” In addition, the effects of window size on FGO performance are evaluated by considering both the GNSS pseudorange error models and environmental conditions. We conclude that the conventional FGO outper-forms the EKF because of the following two factors: (1) FGO uses multiple iterations during the estimation to achieve a robust estimation; and (2) FGO better explores the time correlation between the measurements and states, based on a batch of historical data, when the measurements do not follow the Gaussian noise assumption.

## Problem Addressed

Factor graph optimization has emerged as an alternative to the extended Kalman filter for GNSS/INS integration, but the sources of its performance advantage and the role of design choices such as window size were not well understood.

## Key Contributions

- Systematic comparison of EKF and FGO for loosely and tightly coupled GNSS pseudorange/INS integration
- Analysis of FGO strength by degenerating the FGO estimator into an EKF-like estimator
- Evaluation of window-size effects on FGO considering GNSS pseudorange error models and environmental conditions
- Real-time positioning assessment on an urban canyon dataset collected in Hong Kong

## Conclusions

The conventional FGO outperforms the EKF for two reasons: it applies multiple iterations during estimation to achieve robust estimates, and it better exploits time correlation between measurements and states from a batch of historical data when measurements do not follow Gaussian noise assumptions.
