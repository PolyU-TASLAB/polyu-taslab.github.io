---
title: Online IMU-Odometer Calibration Using GNSS Measurements for Autonomous Ground Vehicle Localization
authors:
- Baoshan Song
- Xiao Xia
- Penggao Yan
- Yihan Zhong
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Transportation Systems
date: '2026-07-26'
doi: https://doi.org/hcb4mq
image: images/papers/cards/2026-song-online-imuodometer-calibration-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Online_IMU-Odometer_Calibration_Using_GNSS_Measurements_for_Autonomous_Ground_Vehicle_Localization.pdf
tags:
- GNSS
- sensor fusion
- extrinsic calibration
- factor graph optimization
- autonomous vehicles
citation_id: 10.1109/TITS.2026.3706684
---

## Abstract

Accurate calibration of intrinsic (odometer scaling factors) and extrinsic parameters (IMU–odometer translation and rotation) is essential for autonomous ground vehicle localization. Existing GNSS-aided approaches often rely on positioning results or raw measurements without ambiguity resolution, and their observability properties remain underexplored. This paper proposes a tightly coupled online calibration method that fuses IMU, odometer, and raw GNSS measurements (pseudo-range, carrier-phase, and Doppler) within an extendable factor graph optimization (FGO) framework, incorporating outlier mitigation and ambiguity resolution. Observability analysis reveals that two horizontal translation and three rotation parameters are observable under general motion, while vertical translation remains unobservable. Simulation and real-world experiments demonstrate superior calibration and localization performance over the state-of-the-art loosely coupled method. Specifically, the IMU-odometer positioning using our calibrated parameters achieves the absolute maximum error of 17.75 m while the one of LC method is 61.51 m, achieving up to 71.14% improvement. To foster further research, we also release the first open-source dataset that combines IMU, 2D odometer, and raw GNSS measurements from both rover and base stations.

## Problem Addressed

Accurate calibration of odometer scaling factors and IMU-odometer extrinsic parameters is essential for autonomous ground vehicle localization, yet existing GNSS-aided approaches rely on positioning results or raw measurements without ambiguity resolution, and their observability properties remain underexplored.

## Key Contributions

- Tightly coupled online calibration fusing IMU, odometer, and raw GNSS pseudorange, carrier-phase, and Doppler measurements in an extendable factor graph optimization framework.
- First method to jointly estimate navigation states and IMU-odometer parameters using raw GNSS with outlier mitigation and ambiguity resolution.
- Observability analysis showing two horizontal translation and three rotation parameters are observable under general motion, while vertical translation is unobservable.
- Released the first open-source dataset combining IMU, 2D odometer, and raw GNSS measurements from rover and base stations.

## Conclusions

Simulation and field experiments verify that the method significantly improves calibration accuracy and robustness over the state-of-the-art loosely coupled approach, reducing the absolute maximum positioning error from 61.51 m to 17.75 m, an improvement of up to 71.14%. Even in challenging environments where successful ambiguity resolution cannot be guaranteed, the tightly coupled framework with robust outlier rejection remains highly effective. The calibration problem is inherently non-convex and requires reliable initialization; convex relaxation or certifiable optimization techniques are left to future work.
