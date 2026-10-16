---
title: "R\n                    <sup>2</sup>\n                    TT: High-Accuracy 3D Localization Using Ray-Tracing-Based Wi-Fi RTT Virtual Fingerprints for Challenging Scenarios"
authors:
- Xin Wang
- Xikun Liu
- Zhen Lyu
- Ruijie Xu
- Weisong Wen
publisher: IEEE Transactions on Mobile Computing
date: '2026-05-27'
doi: https://doi.org/hcb4mm
image: images/papers/cards/2026-wang-r-sup2sup-tt.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/R2TT_High-Accuracy_3D_Localization_Using_Ray-Tracing-Based_Wi-Fi_RTT_Virtual_Fingerprints_for_Challenging_Scenarios.pdf
tags:
- Indoor Localization
- Wi-Fi RTT
- Virtual Fingerprinting
- Ray Tracing
- Deep Learning
- 3D Localization
citation_id: doi:10.1109/TMC.2026.3697299
---

## Abstract

Wi-Fi fingerprinting based on signal strength adapts well to complex indoor signal distributions but is limited by low positioning accuracy and the high cost of fingerprint database construction. Wi-Fi round-trip time (RTT) positioning can achieve meter-level accuracy in open environments but suffers from significant signal reflection effects in complex indoor spaces. This paper proposes R2TT (Ray-Tracing RoundTrip Time), a high-precision 3D indoor positioning system that combines the advantages of fingerprint-based and ranging-based methods by leveraging virtual RTT ranging fingerprints. More importantly, virtual fingerprint generation eliminates the need for labor-intensive data collection, enabling efficient 3D fingerprint construction. The proposed method consists of two stages: (1) constructing a virtual RTT fingerprint database using low-cost light detection and ranging (LiDAR) and ray tracing techniques and (2) employing deep learning to capture signal reflection characteristics for robust and high-accuracy localization. Extensive evaluations demonstrate that in complex, reflective environments,
R2TT achieves a 3D positioning error of approximately 1.3 meters, improving 3D accuracy by over 65% compared to traditional least squares.

## Problem Addressed

Wi-Fi RSS fingerprinting adapts to complex indoor signal distributions but suffers from low positioning accuracy and costly fingerprint database construction, while Wi-Fi RTT ranging achieves meter-level accuracy only in open environments and degrades under signal reflection in complex indoor spaces.

## Key Contributions

- R2TT system combining fingerprint-based and ranging-based advantages through virtual RTT ranging fingerprints
- Low-cost virtual fingerprint generation using LiDAR-based reconstruction and ray tracing, eliminating manual data collection
- CNN-regression localization framework with sliding window mechanism capturing signal reflection characteristics
- First open-source RTT fingerprint dataset with raw observations, virtual fingerprints, and 3D environment data

## Conclusions

In complex, highly reflective environments, R2TT achieves a 3D positioning error of approximately 1.3 m, improving 3D accuracy by over 65% compared to traditional least squares. Reliability analysis shows the majority of reflective signals can be effectively simulated and integrated into the virtual fingerprints. Future work will enrich modeled signal paths, incorporate RSS and AOA features, and apply unsupervised domain adaptation to bridge the simulation-to-real gap.
