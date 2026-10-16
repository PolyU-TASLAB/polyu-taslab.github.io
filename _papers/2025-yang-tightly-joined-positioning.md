---
title: Tightly Joined Positioning and Control Model for Unmanned Aerial Vehicles Based on Factor Graph Optimization
authors:
- Peiwen Yang
- Weisong Wen
- Shiyu Bai
- Li-Ta Hsu
publisher: IEEE Transactions on Vehicular Technology
date: '2025-12-01'
doi: https://doi.org/hccr4f
image: images/papers/cards/2025-yang-tightly-joined-positioning.jpg
citation_id: doi:10.1109/TVT.2025.3589556
---

## Abstract

The existing motion control pipeline, where the positioning and control are decoupled, struggles to adapt to epistemic and aleatoric uncertainty and nonlinear dynamics. As a result, the motion control reliability of the unmanned aerial vehicle (UAV) is significantly challenged in complex dynamic areas. For example, the ubiquitous global navigation satellite system (GNSS) positioning can be degraded by the signal reflections from surrounding high-rising buildings in complex urban areas, leading to significantly increased positioning uncertainty. Given that positioning and control are highly correlated, this research proposes a tightly joining positioning and control model (JPCM) based on factor graph optimization (FGO). Specifically, the sensor measurements are formulated as the factors in the probabilistic factor graph. In addition, the model predictive control (MPC) is also formulated as the additional factor in the probabilistic factor graph. The factor graph contributed by both the positioning-related factors and the 
MPC-based factors deeply exploits the complementariness of positioning and control. Finally, we validate the effectiveness and resilience of the proposed method using simulations and realworld experiments that show significantly improved trajectory following performance. To benefit the research community, we open-source our code and make it available at https://github.com/RoboticsPolyu/IPN_MPC.

## Problem Addressed

The conventional motion control pipeline, where positioning and control are decoupled, struggles to adapt to epistemic and aleatoric uncertainty and nonlinear dynamics, challenging UAV control reliability in complex areas such as urban canyons where GNSS is degraded by signal reflections.

## Key Contributions

- Tightly joined positioning and control model (JPCM) unifying both problems in a single factor graph solved via GTSAM
- Sensor measurements formulated as absolute and relative factors; MPC dynamics, trajectory following, and input constraints as control-based factors
- JPCM-drag variant incorporating aerodynamic drag into the dynamics model to eliminate path following offset
- Open-source code release with quadrotor simulation and lemniscate trajectory tracking validation

## Conclusions

Simulations under disturbances such as abrupt movements and aerodynamic drag show the method converges with smaller errors and better resilience than conventional MPC. Trajectory tracking experiments with a quadrotor demonstrate real-time, robust tracking performance. Future work will develop safety-quantifiable monitoring, integrate more sensors, and test in urbanized areas.
