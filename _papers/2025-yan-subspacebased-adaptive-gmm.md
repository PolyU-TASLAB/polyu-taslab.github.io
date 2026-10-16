---
title: Subspace-Based Adaptive GMM Error Modeling for Fault-Aware Pseudorange-Based Positioning in Urban Canyons
authors:
- Penggao Yan
- Xiao Xia
- Michele Brizzi
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Vehicles
date: '2025-05-01'
doi: https://doi.org/g8t54p
image: images/papers/cards/2025-yan-subspacebased-adaptive-gmm.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/YangPenggao2024Subspace-based_Adaptive_GMM_Error_Modeling_for_Fault-Aware_Pseudorange-based_Positioning_in_Urban_Canyons.pdf
tags:
- Cubature Kalman filter
- Inertial sensor
- Nonlinearity
- Pedestrian navigation
- Zero-velocity (ZV) detection
citation_id: doi:10.1109/TIV.2024.3450198
---

## Abstract

Global navigation satellite system (GNSS) positioning is essential for achieving absolute vehicular positioning in urban scenarios; however, it suffers from limited measurement redundancy and substantial faults caused by complex urban environments. In this work, we propose the subspace-based adaptive error modeling and fault detection and exclusion (FDE) method for pseudorange-based GNSS positioning in urban canyons, which integrates the adaptive error modeling into the FDE process and the positioning-solving process. Notably, we divide the pseudorange measurement space into subspaces regarding elevation angle and carrier-to-noise ratio (C/N0), each of which maintains a Gaussian mixture model (GMM) to adaptively characterize measurement error profiles. Results show that the proposed method has the ability to detect environmental changes.
In addition, the proposed method outperforms the conventional
FDE method with Gaussian assumptions, reducing the mean positioning error by 16 % and 9 % in slightly and medium urbanized datasets, respectively. The impacts of step size (elevation angle and C/N0) and time window of the proposed method are discussed through controlled experiments.

## Problem Addressed

GNSS positioning in urban canyons suffers from limited measurement redundancy and substantial faults caused by complex environments, and conventional fault detection and exclusion with Gaussian assumptions cannot adapt to changing measurement error profiles.

## Key Contributions

- Subspace-based adaptive GMM error modeling, partitioning measurements by elevation angle and carrier-to-noise ratio
- Adaptive incremental pseudorange error modeling (AIPEM) algorithm for real-time error distribution tracking
- AdaptiveFDE algorithm integrating error models into fault detection, exclusion, and the WLS positioning solution
- Experimental validation on two urban datasets with controlled analysis of step size and time window parameters

## Conclusions

The evolution of the adaptive error models correlates strongly with the surroundings, indicating an ability to sense environmental changes. Compared with the conventional FDE method under Gaussian assumptions, mean positioning error is reduced by 16% on the slightly urbanized KLT dataset and by 9% on the medium urbanized TST dataset. Controlled experiments provide practical guidelines for step size and time window selection.
