---
title: Tightly Joined Positioning and Control Model for Unmanned Aerial Vehicles Based on Factor Graph Optimization
authors:
- Peiwen Yang
- Weisong Wen
- Shiyu Bai
- Li-Ta Hsu
publisher: arXiv
date: '2024-01-01'
doi: https://doi.org/g8xpq9
image: images/papers/cards/2024-yang-tightly-joined-positioning.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2404.14724v2.pdf
tags:
- Positioning;
- Model predictive contro
- Dynamic mode
- Factor graph optimization
citation_id: 10.48550/arXiv.2404.14724
---

## Abstract

The existing motion control pipeline, where the positioning and control are decoupled, struggles to adapt to epistemic and aleatoric uncertainty and nonlinear dynamics. As a result, the motion control reliability of the unmanned aerial vehicle (UAV) is significantly challenged in complex dynamic areas. For example, the ubiquitous global navigation satellite system (GNSS) positioning can be degraded by the signal reflections from surrounding high-rising buildings in complex urban areas, leading to significantly increased positioning uncertainty. Given that positioning and control are highly correlated, this research proposes a tightly joining positioning and control model (JPCM) based on factor graph optimization (FGO). Specifically, the sensor measurements are formulated as the factors in the probabilistic factor graph. In addition, the model predictive control (MPC) is also formulated as the additional factor in the probabilistic factor graph. The factor graph contributed by both the positioning-related factors and the MPC-based factors deeply exploits the complementariness of positioning and control. Finally, we validate the effectiveness and resilience of the proposed method using simulations and real-world experiments that show significantly improved trajectory following performance. To benefit the research community, we open-source our code and make it available at https://github.com/RoboticsPolyu/IPN_MPC.

## Problem Addressed

Conventional UAV motion control pipelines decouple positioning and control, so they struggle with epistemic and aleatoric uncertainty and nonlinear dynamics, for example when GNSS positioning is degraded by reflections from high-rise buildings in urban areas.

## Key Contributions

- Formulates positioning and control as a unified factor graph optimization problem
- Encodes sensor measurements as positioning factors and model predictive control as control factors
- Solves the joined factor graph with GTSAM to yield state and control input together
- Adds aerodynamic drag modeling (JPCM-drag) and validates in quadrotor simulation and real experiments
- Open-sources the code for the research community

## Conclusions

Simulations under disturbances such as abrupt movements and aerodynamic drag show the proposed method converges with smaller errors than conventional MPC. Lemniscate trajectory tracking experiments with a quadrotor demonstrate real-time and robust tracking performance. Future work includes safety-quantifiable monitoring, integrating more sensors, and testing in urbanized areas.
