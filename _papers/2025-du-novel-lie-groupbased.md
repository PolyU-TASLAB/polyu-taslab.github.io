---
title: A Novel Lie Group-Based Reliable IMM Estimation Method for SINS/GNSS/OD/NHC Integrated Navigation in Complex Environments
authors:
- Siyuan Du
- Yulong Huang
- Weisong Wen
- Yonggang Zhang
publisher: IEEE Internet of Things Journal
date: '2025-01-09'
doi: https://doi.org/g9hrnn
image: images/papers/cards/2025-du-novel-lie-groupbased.jpg
buttons:
- type: manubot
  text: paper
  link: https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/publications/papers/A_Novel_Lie_Group-based_Reliable_IMM_Estimation_Method_for_SINS_GNSS_OD_NHC_Integrated_Navigation_in_Complex_Environments.pdf
tags:
- Autonomous vehicle
- integrated navigation
- Lie group
- interactive multiple model
- mounting error angle
- variational Bayesian
citation_id: doi:10.1109/JIOT.2025.3527555
---

## Abstract

In the field of autonomous driving, the micro-electromechanical systems (MEMS)-based vehicle navigation usually adopts multi-sensor integrated navigation to achieve high-precision positioning. However, due to the complex environments, the accuracy and reliability of navigation sensors may be significantly reduced. To address these challenges, the interacting multiple model (IMM)-based strapdown inertial navigation system/global navigation satellite system/odometer/non-holonomic constrain (SINS/GNSS/OD/NHC) integrated navigation is adopted. Unfortunately, due to the use of traditional state-space model (SSM), the existing IMM estimation methods often suffer from poor estimation consistency, and the mounting error angle will also make OD/NHC subfilter models affect estimation consistency during the interaction process. Moreover, complex environments lead to frequent model switching, and relying on inaccurate model probabilities may cause significant fluctuations in the subfilter outputs, thereby reducing estimation accuracy. In contrast, the proposed IMM estimation method constructs Lie group-based subfilter SSM, which improves estimation consistency. Additionally, the velocity-bias-based mounting error angle estimation method is proposed by using variational Bayesian (VB) techniques, which further refines the OD/NHC models in IMM. On the other hand, a dynamic likelihood adaptive mechanism (DLAM) is introduced to improve reliability and mitigate the negative effects of frequent switching. Simulation and field test results demonstrate that the proposed velocity-bias-based mounting error angle estimation method has fast convergence speed and high convergence accuracy. Additionally, the proposed Lie group-based reliable IMM estimation method has better accuracy and robustness in complex environments as compared to the existing IMM estimation methods.

## Problem Addressed

MEMS-based multisensor integrated navigation for autonomous driving loses accuracy and reliability in complex environments. Existing IMM estimation methods built on traditional state-space models suffer poor estimation consistency, mounting error angles corrupt the OD/NHC subfilter models, and frequent model switching causes large fluctuations in subfilter outputs.

## Key Contributions

- Lie group-based subfilter state-space model that improves estimation consistency within the IMM
- Velocity-bias-based mounting error angle estimation using variational Bayesian techniques to refine OD/NHC models
- Dynamic likelihood adaptive mechanism to improve reliability and mitigate effects of frequent model switching
- Validation through simulation and field tests in complex navigation environments

## Conclusions

The proposed velocity-bias-based MEA estimation method demonstrates fast convergence speed and high convergence accuracy. Simulation and field test results show that the Lie group-based reliable IMM estimation method achieves higher accuracy and robustness in complex environments than existing IMM estimation methods.
