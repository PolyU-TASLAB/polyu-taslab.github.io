---
title: Safe-Assured Learning-Based Deep SE(3) Motion Joint Planning and Control for UAV Interactions with Dynamic Environments
authors:
- Yuanyuan Zhang
- Weisong Wen
- Penggao Yan
publisher: 2024 IEEE 27th International Conference on Intelligent Transportation Systems (ITSC)
date: '2024-09-24'
doi: https://doi.org/hcc4rz
image: images/papers/cards/2024-zhang-safeassured-learningbased-deep.jpg
citation_id: doi:10.1109/itsc58415.2024.10919536
---

## Abstract

In the era of low-altitude economy, ensuring a safe and agile flight of Unmanned aerial vehicles (UAVs) through the obstacle environment is significant to expanding their interactive applications. Deep reinforcement learning (DRL) based methods have demonstrated promising performance in achieving reliable navigation and precise task execution for UAVs. However, due to its trial-and-error search characteristic, DRL fails to balance safety robustness while pursuing agile performance, especially during training. Moreover, this problem is exacerbated due to the existence of uncertain observation noise in dynamic environments. To address this issue, this paper proposes a safe-assured learning-based deep SE(3) joint planning and control framework. This framework firstly achieves high-level safety decision-making, online complex motion planning, and control for UAVs by seamlessly integrating DRL with nonlinear model predictive control (NMPC). Secondly, this paper constructs a safe stochastic reachability certificate to calculate the stochastic forward reachable set of planned trajectories under uncertain conditions to perform specific safe collision probability checks. This safety foresight mechanism adaptively selects belief space actions from planned actions to interact with the environment, further improving safety while reducing training time. In the simulation of the agile traversal of a fast-moving gate by UAV, we demonstrate that the proposed method can effectively reduce total collision incidents and training time, thereby enhancing training safety and efficiency to a large extent.

## Problem Addressed

Deep reinforcement learning for UAV navigation fails to balance safety robustness with agile performance, especially during trial-and-error training, and the problem is exacerbated by uncertain observation noise in dynamic environments.

## Key Contributions

- Deep SE(3) joint planning and control framework combining DRL policy search with model-based NMPC online constrained optimization
- Safe stochastic reachability certificate computing stochastic forward reachable sets for collision probability checks
- Safety foresight mechanism adaptively selecting belief-space actions, improving safety while reducing training time
- Validated on agile traversal of a fast-moving gate, reducing collisions and training time versus RIL

## Conclusions

In moving-gate traversal simulations, the proposed method reduces total collision incidents and training time compared with RIL, balancing agile performance and safety. The approach addresses the conservatism and potential danger caused by approximation errors and observation noise in optimization and policy execution.
