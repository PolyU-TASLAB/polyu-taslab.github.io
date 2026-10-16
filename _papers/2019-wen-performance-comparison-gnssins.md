---
title: Performance Comparison of GNSS/INS Integrations Based on EKF and Factor Graph Optimization
authors:
- Weisong Wen
- Yin Chiu Kan
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2019-10-11'
doi: https://doi.org/ggtk8c
image: images/papers/cards/2019-wen-performance-comparison-gnssins.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/PCGI.pdf
tags:
- GNSS
- INS
- Integration
- Extended Kalman filter
- Factor graph optimization
- Window size
- Urban canyons
- Positioning Navigation
citation_id: doi:10.33012/2019.17129
---

## Abstract

The recently proposed factor graph optimization (FGO) is adopted to integrate GNSS/INS attracted lots of attention and improved the performance over the existing EKF-based 
GNSS/INS integrations. However, a comprehensive comparison of those two GNSS/INS integration schemes in the urban canyon is not available. Moreover, the performance of the FGO-based 
GNSS/INS integration rely heavily on the size of the window of optimization. Effectively tuning the window size is still an open question. To fill this gap, this paper evaluates both loosely and tightly-coupled integrations using both EKF and FGO via the challenging dataset collected in the urban canyon. The detailed analysis of the results for the advantages of the FGO is also given in this paper by degenerating the FGO-based estimator to an 
“EKF like estimator”. More importantly, we analyze the effects of window size against the performance of FGO, by considering both the GNSS pseudorange error distribution and environmental conditions.

## Problem Addressed

Factor graph optimization (FGO) for GNSS/INS integration has attracted attention, but a comprehensive comparison with EKF-based integration in urban canyons is missing. Moreover, FGO performance relies heavily on the optimization window size, whose tuning remains an open question.

## Key Contributions

- Compares four GNSS/INS integration schemes (loosely/tightly coupled with EKF and FGO) on urban canyon data
- Analyzes the sources of FGO's advantage by degenerating the FGO estimator into an EKF-like estimator
- Analyzes window size effects against GNSS pseudorange error distributions and environmental conditions
- Validates all schemes on a challenging real dataset collected in the urban canyons of Hong Kong

## Conclusions

Tightly coupled GNSS/INS integration outperforms the loosely coupled one, and tightly coupled integration using FGO achieves the best performance in the comparison. FGO's advantage over EKF comes from multiple iterations, the larger amount of data used in optimization, and re-linearization across all states. The proper window size is highly correlated with environmental conditions, suggesting environmental context-awareness as a promising way to adaptively tune the window size.
