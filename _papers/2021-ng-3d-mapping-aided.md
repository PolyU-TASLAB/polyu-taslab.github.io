---
title: '3D Mapping Aided GNSS Using Gauss-Newton Algorithm: An Example on GNSS Shadow Matching'
authors:
- Hoi-Fung Ng
- Guohao Zhang
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2021-10-13'
doi: https://doi.org/g8t45d
image: images/papers/cards/2021-ng-3d-mapping-aided.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Ng_3D_Mapping_Aided.pdf
tags:
- GNSS
- Mapping
- NLOS
- Gauss-Newton
- 3DMA
citation_id: doi:10.33012/2021.17994
---

## Abstract

Global navigation satellite system (GNSS) provides an all-time positioning service that covers the entire world. Technology development impacts our daily life, positioning becomes essential. At meanwhile, urbanization induced the side-effect to position, especially for GNSS. High rise buildings and obstacles can block and reflect the GNSS signals. Using a 3D building model is a new era to aid urban positioning, namely 3D mapping aided (3DMA) GNSS. Conventional 3DMA GNSS uses position hypothesis candidates to estimate the receiver location. Throughout simulation at each distributed candidate, the one with the highest similarity to measurements tends to be the receiver location. Two obvious shortcomings of positioning hypothesis candidate are: first, candidate distribution must cover the truth location to provide satisfactory performance. Second, the computation load is proportional to the number of distributed candidates, and unwanted computation load may be caused during the estimation process. This study tries to overcome these limitations by replacing the positioning hypothesis candidates with nonlinear least squares to estimate the receiver location. Contributions of this study will be reducing the computation load requirement while maintaining the identical positioning performance. We selected shadow matching as the showcase to demonstrate the impacts of our proposed method on the 3DMA GNSS with actual GNSS data from a low-cost receiver.

## Problem Addressed

Conventional 3DMA GNSS distributes position hypothesis candidates, which must cover the true receiver location and whose computation load grows proportionally with the number of candidates, making estimation inefficient.

## Key Contributions

- Express 3DMA GNSS mathematically as an objective function instead of a candidate-scoring problem.
- Optimize the objective as a nonlinear least-squares problem using the Gauss-Newton algorithm.
- Demonstrate the approach on GNSS shadow matching with real data from a low-cost receiver.

## Conclusions

The snapshot-based nonlinear least-squares approach achieves similar positioning accuracy to the candidate-based approach while requiring far fewer sampling positions during estimation. The method is sensitive to large initial location errors and location-dependent variables in the prediction function, and may fail to converge when too few features are available.
