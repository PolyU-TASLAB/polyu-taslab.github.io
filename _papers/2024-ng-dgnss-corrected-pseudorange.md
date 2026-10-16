---
title: DGNSS Corrected Pseudorange and Time-Differenced Carrier Phase (TDCP) Measurements using Differentiable Factor Graph Optimization (DFGO)
authors:
- Hoi-Fung Ng
- Penghui Xu
- Yihan Zhong
- Guohao Zhang
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2024-10-09'
doi: https://doi.org/g8t5zd
image: images/papers/cards/2024-ng-dgnss-corrected-pseudorange.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/Ivan2024GNSS24-0239.pdf
tags:
- Time-Differenced Carrier Phase
- Differentiable Factor Graph Optimization
citation_id: doi:10.33012/2024.19908
---

## Abstract

Google Smartphone Decimeter Challenge (SDC) provides a dataset for the communities to verify their leading-edge algorithm for precise smartphone GNSS positioning under the same baseline. This year's dataset provides more variety on the vendors of smartphones' GNSS chips, where the new data from affordable smartphones is believed to be noisier, increasing the position uncertainty.
This study integrates the pseudorange, time-differenced carrier phase (TDCP) measurements, and estimated velocity using factor graph optimization (FGO) to provide an optimal and robust position estimation. In the optimization process, properly excluding and weighting the measurement is the key for only using healthy measurements for state estimation.
This study also uses the differentiable FGO (DFGO) to determine the covariance for the GNSS positioning adaptively. The positioning results show that the network can provide a more robust and reliable performance than the traditional model-based approach.

## Problem Addressed

Precise smartphone GNSS positioning is challenged by the noisier GNSS chips of affordable smartphones included in the Google Smartphone Decimeter Challenge, which increase position uncertainty. Robust estimation requires properly excluding and weighting unhealthy measurements.

## Key Contributions

- Factor graph optimization integrating DGNSS-corrected pseudorange, time-differenced carrier phase, and estimated velocity
- Differentiable factor graph optimization adaptively learning measurement weighting for GNSS positioning
- Outlier detection and exclusion schemes using CORS-based observation-space representation corrections
- Least-squares initialization with consistency checks for position, velocity, clock offset, and clock drift

## Conclusions

Evaluation on the challenge training data shows the FGO framework provides better positioning performance than the traditional model-based approach, with outlier exclusion and Sigma-epsilon weighting giving the best results. Selecting and weighting healthy measurements is shown to be critical for reliable FGO-based GNSS positioning.
