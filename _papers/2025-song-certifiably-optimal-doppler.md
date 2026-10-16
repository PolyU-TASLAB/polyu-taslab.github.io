---
title: Certifiably Optimal Doppler Positioning using Opportunistic LEO Satellites
authors:
- Baoshan Song
- Weisong Wen
- Qi Zhang
- Bing Xu
- Li-Ta Hsu
publisher: arXiv
date: '2025-09-21'
doi: https://arxiv.org/abs/2509.17198
image: images/papers/cards/2025-song-certifiably-optimal-doppler.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2509.17198v1.pdf
tags:
- LEO satellite
- Doppler positioning
- signal of opportunity
- convex optimization
- semidefinite programming
citation_id: arXiv:2509.17198
---

## Abstract

To provide backup and augmentation to global navigation satellite system (GNSS), Doppler shift from Low Earth Orbit (LEO) satellites can be employed as signals of opportunity (SOP) for position, navigation and timing (PNT). Since the Doppler positioning problem is non-convex, local searching methods may produce two types of estimates: a global optimum without notice or a local optimum given an inexact initial estimate. As exact initialization is unavailable in some unknown environments, a guaranteed global optimization method in no need of initialization becomes necessary. To achieve this goal, we propose a certifiably optimal LEO Doppler positioning method by utilizing convex optimization. In this paper, the certifiable positioning method is implemented through a graduated weight approximation (GWA) algorithm and semidefinite programming (SDP) relaxation. To guarantee the optimality, we derive the necessary conditions for optimality in ideal noiseless cases and sufficient noise bounds conditions in noisy cases. Simulation and real tests are conducted to evaluate the effectiveness and robustness of the proposed method. Specially, the real test using Iridium-NEXT satellites shows that the proposed method estimates an certifiably optimal solution with an 3D positioning error of 140 m without initial estimates while Gauss-Newton and Dog-Leg are trapped in local optima when the initial point is equal or larger than 1000 km away from the ground truth. Moreover, the certifiable estimation can also be used as initialization in local searching methods to lower down the 3D positioning error to 130 m.

## Problem Addressed

LEO Doppler positioning is non-convex, so local search methods either find a global optimum without notice or converge to a local optimum given an inexact initial estimate, while exact initialization is unavailable in unknown environments.

## Key Contributions

- Certifiably optimal LEO Doppler positioning method based on convex optimization requiring no initialization
- Implementation through a graduated weight approximation algorithm and semidefinite programming relaxation
- Derivation of necessary optimality conditions in noiseless cases and sufficient noise-bound conditions in noisy cases
- Evaluation in simulation and real tests with Iridium-NEXT satellites; code and data open-sourced

## Conclusions

Simulation and real tests using Iridium-NEXT satellites show that the proposed method estimates a certifiably optimal solution. The convex relaxation approach guarantees global optimality without precise initialization, addressing the key risk of local optimization in LEO Doppler positioning.
