---
title: 'Wall Inspector: Quadrotor control in wall-proximity through model compensation'
authors:
- Peiwen Yang
- Weisong Wen
- Runqiu Yang
- Yingming Chen
- Cheuk Chi Tsang
publisher: Aerospace Science and Technology
date: '2026-05-27'
doi: https://doi.org/hcb4mn
image: images/papers/cards/2026-yang-wall-inspector-quadrotor.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/1-s2.0-S1270963826010850-main.pdf
tags:
- Ducted rotor
- Model predictive control (MPC)
- Quadrotor
- Wall-proximity effect
- Trajectory tracking
citation_id: doi:10.1016/j.ast.2026.112706
---

## Abstract

The safe operation of quadrotors in near-wall urban or indoor environments (e.g., inspection and search-and-rescue missions) is challenged by unmodeled aerodynamic effects arising from wall-proximity. It generates complex vortices that induce destabilizing suction forces, potentially leading to hazardous vibrations or colli­ sions. This paper presents a comprehensive solution featuring (1) a physics-based suction force model that explicitly characterizes the dependency on both rotor speed and wall distance, and (2) a suction-compensated model predictive control (SC-MPC) framework designed to ensure accurate and stable trajectory tracking dur­ ing wall-proximity operations. The proposed SC-MPC framework incorporates an enhanced dynamics model that accounts for suction force effects, formulated as a factor graph optimization problem integrating system dy­ namics constraints, trajectory tracking objectives, control input smoothness requirements, and actuator physical limitations. The suction force model parameters are systematically identified through extensive experimental measurements across varying operational conditions. Experimental validation demonstrates SC-MPC’s superior performance, achieving 2.1 cm root mean squared error (RMSE) in X-axis and 2.0 cm RMSE in Y-axis position control - representing 74% and 79% improvements over cascaded proportional-integral-derivative (PID) control, and 60% and 53% improvements over standard MPC respectively. The corresponding mean absolute error (MAE) metrics (1.2 cm X-axis, 1.4 cm Y-axis) similarly outperform both baselines. The evaluation platform employs a ducted quadrotor design that provides collision protection while maintaining aerodynamic efficiency. To facil­ itate reproducibility and community adoption, we have open-sourced our complete implementation, including control system codebase, experimental datasets, and demonstration videos, available at https://github.com/R oboticsPolyu/SC-MPC.

## Problem Addressed

Quadrotors flying near walls in urban or indoor missions experience unmodeled aerodynamic effects: wall-proximity vortices induce destabilizing suction forces that can cause hazardous vibrations or collisions.

## Key Contributions

- Physics-based suction force model explicitly characterizing dependence on both rotor speed and wall distance, validated by smog flow visualization and force measurements
- Suction-compensated model predictive control framework formulated as factor graph optimization over dynamics, tracking, smoothness, and actuator constraints
- Systematic model parameter identification through extensive experiments across varying operational conditions
- Open-sourced implementation on a ducted quadrotor platform providing collision protection with aerodynamic efficiency

## Conclusions

SC-MPC achieves 2.1 cm RMSE in X-axis and 2.0 cm RMSE in Y-axis position control during wall-proximity flight, representing 74% and 79% improvements over cascaded PID control and 60% and 53% improvements over standard MPC. The corresponding MAE metrics of 1.2 cm (X) and 1.4 cm (Y) likewise outperform both baselines.
