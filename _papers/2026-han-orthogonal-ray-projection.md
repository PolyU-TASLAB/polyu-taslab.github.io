---
title: 'Orthogonal Ray Projection: A Tangent-Space Visual Measurement Model for Robust Visual-Inertial Odometry'
authors:
- Bing Han
- Tuan Li
- Yuezu Lv
- Weisong Wen
- Zhipeng Wang
- Chuang Shi
publisher: IEEE Robotics and Automation Letters
date: '2026-03-13'
doi: https://doi.org/hcb4mh
image: images/papers/cards/2026-han-orthogonal-ray-projection.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Orthogonal_Ray_Projection_A_Tangent-Space_Visual_Measurement_Model_for_Robust_Visual-Inertial_Odometry.pdf
tags:
- Visual-inertial odometry
- orthogonal ray
- projection
- tangent space parameterization
- estimator consistency
- geometry linearity.
citation_id: doi:10.1109/LRA.2026.3673929
---

## Abstract

The reprojection error in Visual-Inertial Odometry (VIO) suffers from high nonlinearity due to perspective division, which degrades estimator consistency and robustness, particularly under large depth uncertainty. To address this, we propose a novel visual measurement model, the Orthogonal Ray Projection
Error (ORPE), which is formulated in the tangent space of the observation ray. By minimizing the orthogonal distance between the estimated landmark and the measurement ray, ORPE decouples the measurement error from the scalar depth, rendering the residual function linear with respect to the feature position. We derive the exact analytical Jacobians and an uncertainty propagation model, integrating ORPE into both the MSCKF-based
OpenVINS and the optimization-based ORB-SLAM3 frameworks.
Simulations confirm that ORPE achieves geometric linearity for features, while significantly reducing the system nonlinearity with respect to camera pose. Extensive real-world experiments demonstrate that the proposed method significantly improves trajectory accuracy and estimator consistency in challenging weak-parallax scenarios, while maintaining computational efficiency comparable to standard approaches.
Received 23 December 2025; accepted 4 March 2026. Date of publication
13 March 2026; date of current version 20 March 2026. This article was recommended for publication by Associate Editor C. Chen and Editor A.
Kim upon evaluation of the reviewers' comments. This work was supported in part by Beijing Natural Science Foundation under Grant 4254104, in part by the National Key Research and Development Program of China under
Grant 2022YFB3904604, and in part by the Beijing Institute of Technology
Research Fund Program for Young Scholars under Grant XSQD-202222003.
(Corresponding author: Tuan Li.)
Bing Han and Tuan Li are with the School of Interdisciplinary Science,
Beijing Institute of Technology, Beijing 100081, China, and also with the State
Key Laboratory of CNS/ATM, Beijing Institute of Technology, Beijing 100081,
China (e-mail: 3220232614@bit.edu.cn; tuanli@buaa.edu.cn).
Yuezu Lv is with the School of Artificial Intelligence, Beijing Institute of
Technology, Beijing 100181, China

## Problem Addressed

The reprojection error in visual-inertial odometry suffers from high nonlinearity due to perspective division, which degrades estimator consistency and robustness, particularly under large depth uncertainty.

## Key Contributions

- Orthogonal Ray Projection Error (ORPE) model formulated in the tangent space of the observation ray, eliminating perspective division
- Residual linear in feature position, decoupling measurement error from scalar depth and naturally handling infinite depth
- Exact analytical Jacobians and uncertainty propagation from pixel noise to tangent space covariance
- Integration into MSCKF-based OpenVINS and optimization-based ORB-SLAM3 with open-source release

## Conclusions

Simulations confirm ORPE achieves geometric linearity for features while significantly reducing system nonlinearity with respect to camera pose. Extensive real-world experiments show significantly improved trajectory accuracy and estimator consistency in challenging weak-parallax scenarios, with computational efficiency comparable to standard approaches. As a geometric model, its robustness remains constrained by feature tracking quality in dynamic or low-texture scenes.
