---
title: Safety-quantifiable Line Feature-based Monocular Visual Localization with 3D Prior Map
authors:
- Xi Zheng
- Weisong Wen
- Li-Ta Hsu
publisher: arXiv
date: '2022-01-01'
doi: https://doi.org/g8t6kp
image: images/papers/cards/2022-zheng-safetyquantifiable-line-featurebased.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2211.15127v1.pdf
tags:
- Global navigation satellite system (GNSS)
- LiDAR
- sensor fusion
- non-line-of-sight (NLOS)
- LiDAR inertial odometry
- urban areas
citation_id: doi:10.48550/arXiv.2211.15127
---

## Abstract

Accurate and safety-quantifiable localization is of great significance for safety-critical autonomous systems, such as unmanned ground vehicles (UGV) and unmanned aerial vehicles (UAV). The visual odometry-based method can provide accurate positioning in a short period but is subjected to drift over time. 
Moreover, the quantification of the safety of the localization solution (the error is bounded by a certain value) is still a challenge. 
To fill the gaps, this paper proposes a safety-quantifiable line feature-based visual localization method with a prior map. The visual-inertial odometry provides a high-frequency local pose estimation which serves as the initial guess for the visual localization. By obtaining a visual line feature pair association, a foot point-based constraint is proposed to construct the cost function between the 2D lines extracted from the real-time image and the 3D lines extracted from the high-precision prior 3D point cloud map. Moreover, a global navigation satellite systems (GNSS) receiver autonomous integrity monitoring (RAIM) inspired method is employed to quantify the safety of the derived localization solution. Among that, an outlier rejection (also wellknown as fault detection and exclusion) strategy is employed via the weighted sum of squares residual with a Chi-squared probability distribution. A protection level (PL) scheme considering multiple outliers is derived and utilized to quantify the potential error bound of the localization solution in both position and rotation domains. The effectiveness of the proposed safetyquantifiable localization system is verified using the datasets collected in the UAV indoor and UGV outdoor environments.

## Problem Addressed

Visual odometry provides accurate short-term positioning but drifts over time, and quantifying the safety of a visual localization solution, i.e., bounding its error, remains an open challenge for safety-critical UGV and UAV systems.

## Key Contributions

- Line-feature-based monocular visual localization against a prior 3D point cloud map, with VIO providing the initial guess
- Foot-point-based pixel-level point-to-point constraint transforming 2D-3D line association into a reprojection model
- RAIM-inspired safety quantification with chi-square outlier rejection and protection levels considering multiple outliers in position and rotation domains
- Validation on UAV indoor and UGV outdoor datasets

## Conclusions

Experiments on UAV and UGV platforms show the proposed method outperforms comparison algorithms in accuracy and robustness, and the protection-level error quantification is efficient under the multiple-outlier assumption for both translational and rotational motions. Future work includes embedding the line-feature factor into VINS for a tightly coupled scheme and improving safety quantification by modeling lighting changes, motion blur, and feature degeneracy.
