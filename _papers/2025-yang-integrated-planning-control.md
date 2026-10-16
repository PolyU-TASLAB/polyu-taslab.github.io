---
title: 'Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit'
authors:
- Peiwen Yang
- Weisong Wen
- Runqiu Yang
- Yuanyuan Zhang
- Jiahao Hu
- Yingming Chen
- Naigui Xiao
- Jiaqi Zhao
publisher: arXiv
date: '2025-10-05'
doi: https://arxiv.org/abs/2510.04278
image: images/papers/cards/2025-yang-integrated-planning-control.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2510.04278v1.pdf
tags: []
citation_id: arxiv:2510.04278
---

## Abstract

Model predictive control (MPC) faces significant limitations when applied to systems evolving on nonlinear mani-folds, such as robotic attitude dynamics and constrained motion planning, where traditional Euclidean formulations struggle with singularities, over-parameterization, and poor convergence. To overcome these challenges, this paper introduces FactorMPC, a factor-graph based MPC toolkit that unifies system dynamics, constraints, and objectives into a modular, user-friendly, and efficient optimization structure. Our approach natively supports manifold-valued states with Gaussian uncertainties modeled in tangent spaces. By exploiting the sparsity and probabilistic structure of factor graphs, the toolkit achieves real-time performance even for high-dimensional systems with complex constraints. The velocity-extended on-manifold control barrier function (CBF)-based obstacle avoidance factors are designed for safety-critical applications. By bridging graphical models with safety-critical MPC, our work offers a scalable and geometrically consistent framework for integrated planning and control. The simulations and experimental results on the quadrotor demonstrate superior trajectory tracking and obstacle avoidance performance compared to baseline methods. To foster research reproducibility, we have provided open-source implementation offering plug-and-play factors. Code and supplementary materials available at: https://anonymous. 4open.science/r/FactorMPC-EBF0.

## Problem Addressed

Model predictive control applied to systems evolving on nonlinear manifolds, such as robotic attitude dynamics and constrained motion planning, suffers from singularities, over-parameterization, and poor convergence under traditional Euclidean formulations.

## Key Contributions

- Unified factor graph representation for integrated planning and control incorporating dynamics, state constraints, and safety barriers.
- Explicitly derived on-manifold residuals and Jacobians ensuring numerical stability for systems on nonlinear manifolds.
- Novel velocity-extended on-manifold control barrier function framework for safety in dynamic environments.
- Open-source FactorMPC toolkit with modular, plug-and-play factors natively supporting manifold-valued states with tangent-space Gaussian uncertainties.

## Conclusions

Simulations and physical quadrotor experiments demonstrate superior or competitive trajectory tracking and obstacle avoidance compared with state-of-the-art baseline methods. The toolkit achieves real-time control rates comparable to custom solutions while retaining a flexible, modular optimization structure. Future work will embed learned dynamics models and neural policies directly as factors within the optimization graph.
