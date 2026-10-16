---
title: Learning-Based Wifi-IMU Fusion for Unconstrained Pedestrian Indoor Localization
authors:
- Yingying Wang
- Yulong Huang
- Ming Xia
- Weisong Wen
publisher: 2025 44th Chinese Control Conference (CCC)
date: '2025-07-28'
doi: https://doi.org/hcc4rt
image: images/papers/cards/2025-wang-learningbased-wifiimu-fusion.jpg
citation_id: doi:10.23919/ccc64809.2025.11179451
---

## Abstract

Indoor activities constitute a majority of a person's daily life, making location awareness essential for modern intelligent services. Widely adopted indoor localization must be seamlessly integrated into daily life. Inertial measurement unit (IMU) and WiFi received signal strength indicator (RSSI) are two ubiquitous non-intrusive sensing modalities. However, IMUs suffer from substantial cumulative errors, while RSSI measurements are inherently unstable. This paper proposes fusing IMU with
RSSI. A 100Hz velocity sequence is generated from the measured 6D inertial data, serving as the input for the propagation stage in an Extended Kalman Filter (EKF) framework. The update stage occurs only when RSSI is sampled, where the observed planar position and the corresponding uncertainty are derived from transformed RSSI values from hundreds of selected and sorted access points (APs). The filtered position not only corrects the position fingerprints obtained from RSSI samples but also refines the densely sampled inertial positions. Data collected on the CUHK campus validate the effectiveness of our fusion system.

## Problem Addressed

IMU-based pedestrian indoor localization suffers substantial cumulative errors, while WiFi RSSI measurements are inherently unstable, so neither ubiquitous non-intrusive modality alone provides reliable positioning.

## Key Contributions

- Readily implementable system for collecting WiFi RSSI, IMU signals, and ground-truth positions as a WiFi-IMU fusion benchmark
- End-to-end derivation of planar position estimates and uncertainties from hundreds of selected and sorted access point RSSI features
- EKF fusion framework propagating 100 Hz inertial velocity and updating only when RSSI is sampled
- Self-collected dataset with nearly 6 hours of test data on the CUHK campus

## Conclusions

Data collected on the CUHK campus validate the effectiveness of the proposed fusion system. The filtered position both corrects RSSI fingerprint positions and refines the densely sampled inertial positions, yielding a mutually beneficial integration of the two modalities.
