---
title: An Enhanced-Adaptive MEMS-Based SINS/OD Integrated Navigation Method Assisted by Prior Feature Domains Association
authors:
- Siyuan Du
- Lina Gao
- Yulong Huang
- Weisong Wen
- Yonggang Zhang
publisher: IEEE Transactions on Instrumentation and Measurement
date: '2026-01-01'
doi: https://doi.org/hcmzqf
image: images/papers/cards/2026-du-enhancedadaptive-memsbased-sinsod.jpg
citation_id: doi:10.1109/TIM.2026.3738173
---

## Abstract

In the field of autonomous vehicles, the microelectromechanical system (MEMS)-based strap-down inertial navigation system/odometer (SINS/OD) integrated navigation is frequently used in environments where global navigation satellite systems (GNSSs) are unavailable. The state-space model (SSM) of existing SINS/OD integrated navigation methods is affected by inaccurate navigation states, limiting estimation performance. Meanwhile, the uncertainties in MEMS-inertial measurement units and OD measurements significantly constrain the performance of long-endurance positioning. To improve estimation accuracy and practical robustness, an enhanced-adaptive method based on the transformation-fusion mechanism (TFM) is proposed, which adaptively selects either left-invariant or right-invariant premeasurement updates based on the average normalized residual squared sum (NRSS) within a sliding window. The prior feature domains (PFDs)-based association method is proposed to further improve the long-endurance navigation accuracy, where the PFD includes the direct-strike-line (DSL) and direct-strike-angle (DSA), defined by fixed speed bump locations. Speed bumps are identified based on the proposed sliding window-based multidimensional feature detection method, and their positions are retrieved by associating the calculated navigation feature domain (NFD) with the PFDs, which will be used as an additional pseudo-measurement to assist long-endurance navigation. Simulation and vehicle experiments demonstrate that, compared with existing state-of-the-art methods, the proposed method achieves superior long-term positioning accuracy using only a low-cost SINS/OD configuration and leveraging existing road infrastructure.

## Problem Addressed

MEMS-based SINS/odometer integrated navigation, commonly used where GNSS is unavailable, is limited by inaccurate state-space models and by measurement uncertainties in low-cost MEMS-IMU and odometer sensors, constraining long-endurance positioning performance.

## Key Contributions

- Transformation-fusion mechanism adaptively selecting left- or right-invariant premeasurement updates via average normalized residual squared sum in a sliding window
- Prior feature domains (direct-strike-line and direct-strike-angle) association using fixed speed bump locations as pseudo-measurements
- Sliding-window multidimensional speed bump detection combining time-domain peak-peak and frequency-domain energy proportion analysis

## Conclusions

Simulation and vehicle experiments demonstrate that the proposed method achieves higher long-endurance positioning accuracy than existing state-of-the-art methods, using only a low-cost SINS/OD configuration and leveraging existing road infrastructure. The two complementary strategies—state-space model refinement and speed-bump pseudo-measurement association—jointly constrain navigation error growth. Future work may adopt unsupervised adaptive thresholding or lightweight machine learning classifiers for speed bump identification.
