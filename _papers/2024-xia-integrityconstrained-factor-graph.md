---
title: Integrity-Constrained Factor Graph Optimization for GNSS Positioning in Urban Canyons
authors:
- Xiao Xia
- Weisong Wen,
- Li-Ta Hsu
publisher: 'NAVIGATION: Journal of the Institute of Navigation'
date: '2024-01-01'
doi: https://doi.org/g8t575
image: images/papers/cards/2024-xia-integrityconstrained-factor-graph.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/navi.660.pdf
tags:
- factor graph optimization
- fault detection and exclusion
- GNSS positioning
- integrity-constrained positioning
- integrity monitoring
- switch variables
- urban canyons
citation_id: doi:10.33012/navi.660
---

## Abstract

Abstract Global navigation satellite system (GNSS) integrity monitoring (IM) has been introduced in aviation, but remains challenging for urban scenarios because of limited satellite visibility and strong multipath and non-line-of-sight effects. Consequently, factors such as limited measurement redundancy and inaccurate uncertainty modeling significantly compromise positioning and IM performance. To alleviate these issues, this paper proposes an integrity-constrained factor graph optimization model for GNSS positioning augmented by switch variables. In contrast to conventional IM methods, this method enhances redundancy through the factor graph structure. Instead of directly excluding measurements, the proposed method reweights the measurements by using switch variables to satisfy a chi-square test constraint within the optimization, ultimately yielding optimal positioning accuracy. Moreover, a proper protection level that conservatively bounds the positioning error can be derived by using the modified weighting matrix under a single-fault assumption. The effectiveness of the proposed method was verified based on data sets collected in open-sky and urban-canyon areas in Hong Kong.

## Problem Addressed

GNSS integrity monitoring, developed for aviation, performs poorly in urban canyons where limited satellite visibility and strong multipath and NLOS effects reduce measurement redundancy and make uncertainty modeling inaccurate. Directly excluding faulty measurements further degrades satellite geometry.

## Key Contributions

- Integrity-constrained factor graph optimization model for GNSS positioning augmented by switch variables
- Chi-square test constraint embedded in the optimization, enabling reweighting-based FDE without excluding satellites
- Protection level derivation using the modified weighting matrix under a single-fault assumption
- Validation on open-sky and urban-canyon datasets collected in Hong Kong

## Conclusions

The proposed RAIM framework for factor-graph-based GNSS positioning performs fault detection and exclusion by reweighting measurements through switch variables, avoiding satellite exclusion and preserving geometry. Evaluated on open-sky and urban datasets against snapshot residual-based RAIM, it executes reweighting-based FDE effectively and yields a conservative HPL that bounds positioning errors. Performance gains are constrained in harsher scenarios with poor satellite visibility and many faulty measurements, and depend on the tuning of switch prior factors.
