---
title: A Novel Consistent-Robust SINS/GNSS/NHC Integrated Navigation Method for Autonomous Vehicles Under Intermittent GNSS Outage
authors:
- Siyuan Du
- Yulong Huang
- Weisong Wen
- Yonggang Zhang
publisher: IEEE Transactions on Intelligent Vehicles
date: '2024-12-01'
doi: https://doi.org/g8t54s
image: images/papers/cards/2024-du-novel-consistent-robust-sinsgnssnhc.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/WenyuYang2024LiDAR_Stereo_Visual_Inertial_Pose_Estimation_Based_on_Feedforward_and_Feedbacks.pdf
tags:
- LiDAR Stereo Visual Inertial odometry
- Feedforward-feedback LiDAR Visual Inertial System
citation_id: doi:10.1109/TIV.2024.3406756
---

## Abstract

Autonomous vehicles are widely used in logistics, public transportation, and specialized industries, its high-precision navigation and positioning is predominantly supported through strapdown inertial navigation system/global navigation satellite system (SINS/GNSS) integrated navigation, thus ensuring safe and efficient operations. In practice, GNSS is prone to intermittent outage due to environment interference, while Non-Holonomic
Constraint (NHC) can significantly improve navigation accuracy.
Unfortunately, the mounting error angle and lever arm lead to
NHC mismatch, and the performance of existing NHC method is also affected by the state-space model inconsistency and nonstationarity outlier noises. To solve the problems, a consistent-robust SINS/GNSS/NHC integrated navigation method is proposed, which includes two stages: off-line calibration and online navigation. In off-line calibration stage, a two-step-based estimation method is proposed to determine the mounting error angle and lever arm. The more consistent state-space model is deduced to estimate mounting error angle using the virtual dead-reckoning constructed from the posteriori straight-driving data, based on which the lever arm can be accurately estimated using posterior turn-driving data. In online navigation stage, the Lie group-based
NHC model is established, and the non-stationary outlier noise is modeled as Gaussian-Student's t mixture distribution. Meanwhile, the strong tracking method is introduced to fine-calibrate the accuracy of initial parameter. Finally, the variational Bayesian is used to jointly estimate the navigation state and parameters. The simulation and car-mounted field test results illustrate that the proposed method has better estimation accuracy than existing state-of-theart methods, enhancing the navigation and positioning capabilities of autonomous vehicles during intermittent GNSS outage.

## Problem Addressed

SINS/GNSS integrated navigation for autonomous vehicles degrades during intermittent GNSS outages caused by environmental interference. Although non-holonomic constraints (NHC) improve accuracy, mounting error angles and the lever arm cause NHC mismatch, while state-space model inconsistency and non-stationary outlier noise further degrade performance.

## Key Contributions

- Two-step offline calibration estimating NHC mounting error angle and lever arm using virtual dead-reckoning and posterior driving data
- Lie group-based consistent NHC model improving state-space model consistency for online navigation
- Gaussian-Student's t mixture-based variational Bayesian robust filtering handling non-stationary outlier noise
- Strong tracking method fine-calibrating the initial nominal measurement covariance
- Validated by simulations and car-mounted field tests under intermittent GNSS outage

## Conclusions

The two-stage method estimates the NHC mounting error angle and lever arm offline, then applies a consistent Lie group NHC model with GSTM-based variational Bayesian robust filtering online. Simulation and car-mounted field test results show higher convergence and estimation accuracy than existing state-of-the-art methods during intermittent GNSS outages.
