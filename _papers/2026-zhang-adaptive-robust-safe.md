---
title: Adaptive Robust Safe Policy Optimization with Distributional Risk Modeling for Uncertainty-aware Autonomous Navigation
authors:
- Yuanyuan Zhang
- Yingying Wang
- Weisong Wen
publisher: IEEE Transactions on Automation Science and Engineering
date: '2026-01-01'
doi: https://doi.org/hcncbg
citation_id: doi:10.1109/TASE.2026.3742790
---

## Abstract

Reinforcement learning (RL) has shown great potential in autonomous navigation by enabling agents to learn decision policies from direct environmental interaction. However, ensuring both safety and efficiency in dynamic and uncertain environments remains challenging because perception noise and environmental variability often undermine policy robustness and reliability. To address these issues, this paper proposes an adaptive robust safe policy optimization (ARSPO) framework, which integrates distributional risk modeling, robust transition augmentation, and adaptive safety regulation. Specifically, ARSPO incorporates a distributional value-cost critic to jointly estimate the return and cost distributions, capturing both performance and safety risks. A distortion-based robust value aggregation is introduced to enhance sensitivity to high-uncertainty regions. Meanwhile, a conditional Value-at-Risk (CVaR) based adaptive mechanism is developed to dynamically regulate the policy's risk preference, achieving a balance between exploratory optimism and safety assurance. Furthermore, a robust transition modeling mechanism is proposed to augment the training buffer with physically consistent perturbed state samples, enhancing generalization under stochastic dynamics. Extensive experiments in both simulated and real-world deployments demonstrate that ARSPO consistently outperforms state-of-the-art baselines in success rate, collision avoidance, and path efficiency.

## Problem Addressed

Reinforcement learning for autonomous navigation struggles to guarantee both safety and efficiency in dynamic, uncertain environments, because perception noise and environmental variability undermine policy robustness and reliability.

## Key Contributions

- ARSPO framework integrating distributional risk modeling, robust transition augmentation, and adaptive safety regulation
- Distributional value-cost critic jointly estimating return and cost distributions to capture performance and safety risks
- Distortion-based robust value aggregation enhancing sensitivity to high-uncertainty regions
- CVaR-based adaptive mechanism dynamically regulating policy risk preference between exploration and safety
- Robust transition modeling augmenting the training buffer with physically consistent perturbed state samples

## Conclusions

Extensive experiments in both simulated and real-world deployments show that ARSPO consistently outperforms state-of-the-art baselines in success rate, collision avoidance, and path efficiency. The framework improves robustness of navigation policies under stochastic dynamics and perception uncertainty.
