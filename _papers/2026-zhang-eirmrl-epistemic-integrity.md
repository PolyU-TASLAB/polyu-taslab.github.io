---
title: 'EIRM-RL: Epistemic Integrity Risk Monitoring Inspired Safe Reinforcement Learning for Trustworthy Autonomous Navigation'
authors:
- Yuanyuan Zhang
- Yingying Wang
- Weisong Wen
publisher: IEEE Internet of Things Journal
date: '2026-01-15'
doi: https://doi.org/hccr39
image: images/papers/cards/2026-zhang-eirmrl-epistemic-integrity.jpg
citation_id: doi:10.1109/JIOT.2025.3633765
---

## Abstract

Reinforcement learning (RL) has shown great potential for autonomous navigation in Internet of Things (IoT) environments, where various and changing uncertainties pose significant challenges for safe, real-world deployment. Existing safe RL methods typically employ heuristic constraints while neglecting the combined impact of multiple uncertainty sources, reducing robustness and interpretability. Drawing on concepts from global navigation satellite system (GNSS) integrity monitoring, this article proposes an epistemic integrity risk monitoring reinforcement learning (EIRM-RL) framework to enable trustworthy autonomous navigation under uncertainty.
EIRM-RL extends the GNSS protection level concept to RL by utilizing an assembled world model that quantifies and incorporates sensor noise, systematic bias, and epistemic uncertainty.
Furthermore, the framework continuously monitors a dynamic epistemic risk probability, which is incorporated into policy optimization as an adaptive safety constraint via Lagrangian duality.
This method enables the agent to proactively avoid hazards and effectively balance safety and performance, even in highly uncertain environments. Extensive experiments demonstrate that
EIRM-RL achieves superior success rates, collision avoidance, and robustness compared to state-of-the-art safe RL methods, while maintaining high efficiency.

## Problem Addressed

Reinforcement learning for autonomous navigation in IoT environments faces diverse and changing uncertainties that hinder safe real-world deployment. Existing safe RL methods rely on heuristic constraints and neglect the combined impact of multiple uncertainty sources, reducing robustness and interpretability.

## Key Contributions

- EIRM-RL framework inspired by GNSS integrity monitoring for trustworthy navigation under uncertainty
- Assembled world model quantifying sensor noise, systematic bias, and epistemic uncertainty, extending the GNSS protection level concept to RL
- Dynamic epistemic risk probability incorporated into policy optimization as an adaptive safety constraint via Lagrangian duality

## Conclusions

Extensive simulations in static and dynamic environments show EIRM-RL consistently outperforms state-of-the-art baselines in mission success rate, collision rate, and cumulative reward, especially under sensor noise and fault conditions. Ablation studies highlight the critical role of risk monitoring and comprehensive uncertainty modeling. Real-world experiments confirm a UGV reliably reaches its target and avoids obstacles under dynamic hazards and sensor perturbations. Remaining limitations include the Gaussian noise assumption and the need for validation in crowded multiagent environments.
