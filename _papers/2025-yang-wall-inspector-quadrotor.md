---
title: 'Wall Inspector: Quadrotor Control in Wall-proximity Through Model Compensation'
authors:
- Peiwen Yang
- Weisong Wen
- Runqiu Yang
- Yingming Chen
- Cheuk Chi Tsang
publisher: arXiv
date: '2025-09-25'
doi: https://arxiv.org/abs/2509.21496
image: images/papers/cards/2025-yang-wall-inspector-quadrotor.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2509.21496v1.pdf
tags: []
citation_id: arxiv:2509.21496
---

## Abstract

The safe operation of quadrotors in near-wall urban or indoor environments (e.g., inspection and search-and-rescue missions) is challenged by unmodeled aerodynamic effects arising from wall-proximity. It generates complex vortices that induce destabilizing suction forces, potentially leading to hazardous vibrations or collisions. This paper presents a comprehensive solution featuring (1) a physics-based suction force model that explicitly characterizes the dependency on both rotor speed and wall distance, and (2) a suction-compensated model predictive control (SC-MPC) framework designed to ensure accurate and stable trajectory tracking during wallproximity operations. The proposed SC-MPC framework incorporates an enhanced dynamics model that accounts for suction force effects, formulated as a factor graph optimization problem integrating system dynamics constraints, trajectory tracking objectives, control input smoothness requirements, and actuator physical limitations. 
The suction force model parameters are systematically identified through extensive experimental measurements across varying operational conditions. Experimental validation demonstrates SC-MPC's superior performance, achieving 2.1 cm root mean squared error (RMSE) in X-axis and 2.0 cm RMSE in Y-axis position control - representing 74% and 79% improvements over cascaded proportional-integralderivative (PID) control, and 60% and 53% improvements over standard MPC respectively. The corresponding mean absolute error (MAE) metrics (1.2 cm X-axis, 1.4 cm Y-axis) similarly outperform both baselines. The evaluation platform employs a ducted quadrotor design that provides collision protection while maintaining aerodynamic efficiency. To facilitate reproducibility and community adoption, we have open-sourced our complete implementation, including control system codebase, experimental datasets, and demonstration videos, available at https://anonymous.4open.science/r/SC-MPC-6A61. 
 
 
 

 
2 
 
NOMENCLATURE 
 kP k -th plane frame 
 
 w world frame 
 
 b body frame 
 p position rotation m 
R rotation matrix 
 v velocity m/s b
ω angular velocity rad/s sF suction force in the world frame 
N sk 
Suction fo

## Problem Addressed

Safe quadrotor operation near walls in urban or indoor environments is challenged by unmodeled aerodynamic wall-proximity effects that generate complex vortices and destabilizing suction forces, risking vibrations or collisions.

## Key Contributions

- Physics-based suction force model explicitly characterizing dependency on rotor speed and wall distance
- Suction-compensated model predictive control (SC-MPC) framework formulated as factor graph optimization
- Integrates system dynamics constraints, trajectory tracking objectives, control smoothness, and actuator limitations
- Model parameters identified through extensive experiments; control code, datasets, and videos open-sourced

## Conclusions

SC-MPC achieves 2.1 cm RMSE in X-axis and 2.0 cm RMSE in Y-axis position control, representing 74% and 79% improvements over cascaded PID control and 60% and 53% improvements over standard MPC. Simulation and trajectory tracking experiments on a ducted quadrotor demonstrate accurate and safe flights in wall proximity.
