---
title: Our Paper Is Accepted by IEEE ICRA 2026
subtitle: Example news
# author: xxx
image: images/news/2026ICRA/system_framework.png
tags: news
order: 
---

Our paper "*Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit*" by Peiwen Yang, Weisong Wen, Runqiu Yang, Yuanyuan Zhang, Jiahao Hu, Yingming Chen, Naigui Xiao and Jiaqi Zhao has been accepted by the 2026 IEEE International Conference on Robotics &amp; Automation (ICRA 2026). Congratulations to Peiwen and the co-authors!

### Abstract

Model predictive control (MPC) faces significant limitations when applied to systems evolving on nonlinear manifolds, such as robotic attitude dynamics and constrained motion planning, where traditional Euclidean formulations struggle with singularities, over-parameterization and poor convergence. To overcome these challenges, this paper introduces FactorMPC, a factor-graph-based MPC toolkit that unifies system dynamics, constraints and objectives into a modular, user-friendly and efficient optimization structure. Our approach natively supports manifold-valued states with Gaussian uncertainties modeled in tangent spaces. By exploiting the sparsity and probabilistic structure of factor graphs, the toolkit achieves real-time performance even for high-dimensional systems with complex constraints. Velocity-extended on-manifold control barrier function (CBF)-based obstacle avoidance factors are designed for safety-critical applications. By bridging graphical models with safety-critical MPC, our work offers a scalable and geometrically consistent framework for integrated planning and control. Simulations and experimental results on a quadrotor demonstrate superior trajectory tracking and obstacle avoidance performance compared with baseline methods. To foster research reproducibility, we provide an open-source implementation offering plug-and-play factors. Code and supplementary materials are available at [https://github.com/RoboticsPolyu/FactorMPC](https://github.com/RoboticsPolyu/FactorMPC).

### System framework

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/2026ICRA/system_framework.png" alt="System framework of FactorMPC"></figure>
</div>
<p class="news-caption">System framework of FactorMPC.</p>
