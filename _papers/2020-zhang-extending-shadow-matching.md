---
title: Extending Shadow Matching to Tightly-Coupled GNSS/INS Integration System
authors:
- Guohao Zhang
- Weisong Wen
- Bing Xu
- Li-Ta Hsu
publisher: IEEE Transactions on Vehicular Technology
date: '2020-05-01'
doi: https://doi.org/ggq4dk
image: images/papers/cards/2020-zhang-extending-shadow-matching.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/ESMT.pdf
tags:
- Global navigation satellite system
- Position measurement
- Satellites
- Buildings
- Three-dimensional displays
- Estimation
- Noise measurement
- GNSS
- sensor integration
- localization
- 3D building model
citation_id: doi:10.1109/TVT.2020.2981093
---

## Abstract

Performing precise positioning is still challenging for autonomous driving. Global navigation satellite system (GNSS) performance can be significantly degraded due to the non-lineof-sight (NLOS) reception. Recently, the studies of 3D building model aided (3DMA) GNSS positioning show promising positioning improvements in urban canyons. In this study, the benefits of
3DMA GNSS are further extended to the GNSS/inertial navigation system (INS) integration system. Based on the shadow matching solution and scoring information of candidate positions, two methods are proposed to better classify the line-of-sight (LOS) and NLOS satellite measurements. Aided by the satellite visibility information, the NLOS-induced pseudorange measurement error can be mitigated before fusing GNSS with the INS in the looselycoupled or tightly-coupled integration system. Both the proposed satellitevisibilityestimationmethodsachieveover80%LOS/NLOS classification accuracy for most of the scenarios in the urban area, which are at least 10% improvement over the carrier-to-noise ratio (C/N0)-based method. By further extending the satellite visibility estimation to exclude NLOS measurements and adjust the measurement noise covariance, the proposed 3DMA GNSS/INS tightly-coupled integrated positioning achieves nearly a factor of 3 improvements comparing to the conventional GNSS/INS integration method during the vehicular experiment in the urban canyon.

## Problem Addressed

GNSS performance is significantly degraded by NLOS reception in urban canyons, and the benefits of 3D building model aided GNSS have not been fully extended to GNSS/INS integrated positioning systems.

## Key Contributions

- Two satellite visibility estimation methods based on the shadow matching solution and candidate-position scoring information.
- Visibility information mitigates NLOS-induced pseudorange errors before loosely or tightly coupled GNSS/INS fusion.
- Over 80% LOS/NLOS classification accuracy in most urban scenarios, at least 10% above the C/N0-based method.
- NLOS exclusion combined with measurement noise covariance adjustment in the integration.

## Conclusions

The shadow matching aided GNSS/INS tightly coupled system achieves an RMSE of 6.5 meters in a dense-urban vehicular test, nearly three times more accurate than the conventional tightly coupled integration approach. In harsh environments with limited sky view, NLOS exclusion may leave too few measurements for robust estimation, so NLOS correction is identified as future work.
