---
title: Integrity-Monitored Deep Reinforcement Learning for Safe and Robust Autonomous Navigation
authors:
- Yuanyuan Zhang
- Yingying Wang
- Baoshan Song
- Weisong Wen
publisher: 2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC)
date: '2025-11-18'
doi: https://doi.org/hccr4k
image: images/papers/cards/2025-zhang-integritymonitored-deep-reinforcement.jpg
citation_id: doi:10.1109/ITSC60802.2025.11423028
---

## Abstract

Ensuring safe and robust autonomous navigation under uncertainty remains a fundamental challenge for deploying deep reinforcement learning (DRL) in real-world applications. This paper presents an integrity monitoring deep reinforcement learning (IM-DRL) framework that incorporates integrity monitoring (IM) principles inspired by global navigation satellite systems (GNSS). A novel integrity cost model (ICM) is introduced to quantify observation trustworthiness through probabilistic metrics, enabling adaptive safety constraints under sensor degradation and transient faults. IM-DRL combines these integrity metrics with model-based uncertainty estimation, allowing the agent to dynamically adjust safety thresholds in response to varying observation quality. To further enhance robustness, the framework injects systematically biased
Gaussian noise into observations, simulating realistic sensor degradation and generating risk-critical scenarios without adversarial training. The resulting policy optimization remains computationally efficient while ensuring verifiable safety. Experimental results show that IM-DRL reduces the collision rate by up to 60.6% compared to baseline methods, and exhibits strong generalization and adaptability in environments with severe observation disturbances, demonstrating its promise for safe and robust autonomous navigation.

## Problem Addressed

Deploying deep reinforcement learning for real-world autonomous navigation remains fundamentally challenging because safety and robustness must be ensured under sensor degradation, transient faults, and observation uncertainty.

## Key Contributions

- IM-DRL framework incorporating GNSS-inspired integrity monitoring principles into deep reinforcement learning
- Integrity cost model quantifying observation trustworthiness through protection level and alert limit metrics
- Adaptive safety thresholds combining integrity metrics with model-based uncertainty estimation
- Systematically biased Gaussian noise injection to simulate sensor degradation without adversarial training cost

## Conclusions

IM-DRL reduces the collision rate by up to 60.6% compared to baseline methods and outperforms state-of-the-art baselines in success rate and safety, even under severe sensor noise. The framework generalizes well in environments with strong observation disturbances while remaining computationally efficient.
