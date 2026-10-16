---
title: Tightly Joining Positioning and Control for Trustworthy Unmanned Aerial Vehicles Based on Factor Graph Optimization in Urban Transportation
authors:
- Peiwen Yang
- Weisong Wen
publisher: 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)
date: '2023-09-24'
doi: https://doi.org/g8t66c
image: images/papers/cards/2023-yang-tightly-joining-positioning-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Tightly_Joining_Positioning_and_Control_for_Trustworthy_Unmanned_Aerial_Vehicles_Based_on_Factor_Graph_Optimization_in_Urban_Transportation.pdf
tags:
- FGO
- UAV
- MPC
- GNSS
repo: https://github.com/RoboticsPolyu/IPN_MPC
citation_id: 10.1109/ITSC57777.2023.10422537
---

## Abstract

Unmanned aerial vehicles (UAV) showed great potential in improving the efficiency of parcel delivery applications in the coming smart cities era. Unfortunately, the trustworthy positioning and control algorithms of the UAV are significantly challenged in complex urban areas. For example, the ubiquitous global navigation satellite system (GNSS) positioning can be degraded by the signal reflections from surrounding highrising buildings, leading to significantly increased positioning uncertainty. An additional challenge is introduced to the control algorithm due to the complex wind disturbances in urban canyons. Given the fact that the system positioning and control are highly correlated with each other, for example, the system dynamics of the control can largely help with the positioning, this paper proposed a joint positioning and control method (JPCM) based on factor graph optimization (FGO), which combines sensors' measurements and control intention. In particular, the positioning measurements are formulated as the factors in the factor graph model, such as the positioning from the GNSS. The model predictive control (MPC) is also formulated as the additional factors in the factor graph model.
By solving the factor graph contributed by both the positioning factor and the MPC-based factors, the complementariness of positioning and control can be fully explored. To guarantee reliable system dynamic parameters, we validate the effectiveness of the proposed method using a simulated quadrotor system which showed significantly improved trajectory following performance. To benefit the research community, we open-source our code and make it available at https://github.com/
RoboticsPolyu/IPN_MPC.

## Problem Addressed

UAV positioning and control are significantly challenged in complex urban areas by GNSS degradation from signal reflections and complex wind disturbances, although positioning and control are highly correlated and usually treated separately.

## Key Contributions

- Joint positioning and control method (JPCM) unifying sensor measurements and control intention in one factor graph
- Positioning measurements such as GNSS formulated as factors alongside model predictive control factors
- Design framework for the unified factor graph including dynamic control and trajectory tracking factors
- Open-sourced code validated on a simulated quadrotor system

## Conclusions

Simulation results with a quadrotor system show the proposed method converges with smaller errors than nominal MPC and yields significantly improved trajectory-following performance. Future research will introduce IMU simulation into the system.
