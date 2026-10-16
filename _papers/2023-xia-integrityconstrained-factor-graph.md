---
title: Integrity-constrained Factor Graph Optimization for GNSS Positioning
authors:
- Xiao Xia
- Li-Ta Hsu
- Weisong Wen
publisher: 2023 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2023-04-24'
doi: https://doi.org/hcc4r6
image: images/papers/cards/2023-xia-integrityconstrained-factor-graph.jpg
citation_id: doi:10.1109/plans53410.2023.10140009
---

## Abstract

The concept of global navigation satellite system (GNSS) integrity refers to the measure of trust of the GNSS positioning solution, which is vital for safety-critical applications such as aviation and autonomous driving. While integrity monitoring was firstly introduced and widely applied in the GNSS aviation field, it is not suitable for GNSS positioning in urban scenarios due to unique circumstances such as limited satellite visibility, strong multipath and nonline-of-sight (NLOS) effects. For example, the direct exclusion of the GNSS multipath and NLOS would significantly degrade the geometry constraints, thus leading to highly conservative integrity monitoring (IM). As a result, the limited GNSS measurement redundancy and the inaccurate measurement uncertainty modeling in urban canyons will severely degrade the performance of both the GNSS positioning and integrity monitoring. To alleviate these issues, this paper proposed an integrity-constrained factor graph optimization (FGO) for 
GNSS positioning with the help of switchable constraints. 
Compared to the conventional GNSS IM methods which consider measurements in single epoch or two successive epochs, the proposed method improves the measurement redundancy by the factor graph structure. Meanwhile, the switch variable, which is introduced by switchable constraints and connected with each pseudorange measurement, can not only estimate the measurement uncertainties, but also satisfying the Chi-square testing of the conventional fault detection and exclusion (FDE) while maintaining satellite geometry. In particular, the calculated protection levels consider the effect of switch variables, hence bound the position error more accurately. The performance of this proposed method is evaluated on open-sky dataset with manually injected biases with gaussian random noise.

## Problem Addressed

GNSS integrity monitoring, vital for safety-critical applications, is unsuitable for urban scenarios where limited satellite visibility and strong multipath and NLOS effects reduce measurement redundancy and distort uncertainty modeling. Directly excluding faulty measurements significantly degrades satellite geometry, leading to overly conservative integrity monitoring.

## Key Contributions

- Integrity-constrained factor graph optimization for GNSS positioning using switchable constraints
- Switch variables connected to each pseudorange measurement to estimate uncertainties and satisfy chi-square FDE testing
- Reweighting-based FDE that maintains satellite geometry while improving measurement redundancy
- Protection level calculation accounting for the reweighting effect of switch variables

## Conclusions

Evaluated on an open-sky dataset with manually injected biases, the method effectively performs fault detection and exclusion by reweighting measurements while maintaining satellite geometry. The calculated horizontal protection level bounds the position error well, though it remains conservative under the single-fault assumption. Future work includes incorporating HPL calculation into the factor graph and validating with differential GNSS and more challenging urban data.
