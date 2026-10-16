---
title: Safety-Quantifiable Line Feature-Based Monocular Visual Localization With 3D Prior Map
authors:
- Xi Zheng
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Transportation Systems
date: '2025-06-02'
doi: https://doi.org/g9qf62
image: images/papers/cards/2025-zheng-safetyquantifiable-line-featurebased.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Safety-Quantifiable_Line_Feature-Based_Monocular_Visual_Localization_With_3D_Prior_Map.pdf
- type: source
  text: code
  link: https://github.com/ZHENGXi-git/SafetyQuantifiable-PLVINS
tags:
- Safety quantification
- state estimation
- visual localization
- prior map
- outlier rejection
- protection level
repo: https://github.com/ZHENGXi-git/SafetyQuantifiable-PLVINS
citation_id: doi:10.1109/TITS.2025.3572620
---

## Abstract

Accurate and safety-quantifiable localization is of great significance for safety-critical autonomous systems, such as Autonomous ground vehicles (AGVs) and autonomous aerial vehicles (AAVs). The visual odometry-based method can provide accurate positioning in a short period but is subject to drift over time. Moreover, the quantification of the safety of the localization solution (the error is bounded by a certain value) is still a challenge. To fill the gaps, this paper proposes a safety-quantifiable line feature-based visual localization method with a prior map. The visual-inertial odometry provides a high-frequency local pose estimation, which serves as the initial guess for the visual localization. By obtaining a visual line feature pair association, a foot point-based constraint is proposed to construct the cost function between the 2D lines extracted from the real-time image and the 3D lines extracted from the high-precision prior 3D point cloud map. Moreover, a global navigation satellite system (GNSS) receiver autonomous integrity monitoring (RAIM) inspired method is employed to quantify the safety of the derived localization solution. Among that, an outlier rejection (also well-known as fault detection and exclusion) strategy is employed via the weighted sum of squares residual with a Chi-squared probability distribution. A protection level (PL) scheme considering multiple outliers is derived and utilized to quantify the potential error bound of the localization solution in both position and rotation domains. The effectiveness of the proposed safety-quantifiable localization system is verified using the datasets collected by AAV and AGV in indoor and outdoor environments, respectively. The open-source code is available at https://github.com/ZHENGXi-git/SafetyQuantifiable-PLVINS

## Problem Addressed

Visual odometry provides accurate short-term positioning but drifts over time, and quantifying the safety of the localization solution—bounding its error with a certain value—remains an open challenge for safety-critical autonomous ground and aerial vehicles.

## Key Contributions

- Safety-quantifiable line feature-based monocular visual localization with a high-precision 3D prior point cloud map
- Pixel-level point-to-point line constraint model reformulating 2D-3D line association as a reprojection optimization
- GNSS RAIM-inspired safety quantification with chi-squared weighted-residual outlier rejection
- Protection level scheme accounting for multiple outliers in both position and rotation domains, with open-source code

## Conclusions

Experiments on datasets collected by autonomous aerial and ground vehicles in indoor and outdoor environments show the method outperforms comparison algorithms in accuracy and robustness. The protection level effectively quantifies state estimation error bounds under multiple-outlier assumptions in both translational and rotational domains. Future work includes tightly coupled integration with VINS, efficient prior-map storage for large coverage areas, and broader use of protection levels for real-time safety assessment in robotic deployments.
