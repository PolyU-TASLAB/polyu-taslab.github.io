---
title: 'Watch Your Position: Neural Inertial Localization With a Single Wrist-Worn Device'
authors:
- Shiyu Bai
- Yizhi Lyu
- Zhen Lyu
- Ruijie Xu
- Xin Wang
- Weisong Wen
publisher: IEEE Transactions on Mobile Computing
date: '2026-01-08'
doi: https://doi.org/hcb4mg
image: images/papers/cards/2026-bai-watch-your-position.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Watch_Your_Position_Neural_Inertial_Localization_With_a_Single_Wrist-Worn_Device.pdf
tags:
- Smartwatch
- inertial odometry
- indoor localization
- deep learning,
- IMU
citation_id: doi:10.1109/TMC.2026.3672619
---

## Abstract

Wearable devices, such as smartwatches, have been widely used by the public for health monitoring, exercise tracking, and message alerts. Regarding localization applications, although smartwatches have been explored by many researchers, current solutions typically require combining data from multiple sensors or multiple mobile devices for reliable position estimation, which is inconvenient for practical usage. In this paper, we propose a novel indoor localization method that relies solely on an inertial measurement unit (IMU) of a smartwatch. First, we design a smartwatchbased neural inertial odometry (WNIO) that adapts to multiple motion patterns and achieves low-drift dead reckoning. Second, we detect interactions between the arm and the environment, such as opening a door, to formulate absolute position measurements that help constrain error drift. A multi-hypothesis Kalman filter (MHKF) is employed to ensure reliable matching and localization.
We conducted real-world experiments to validate the effectiveness of the proposed method. The results demonstrate that our method achieves reliable dead reckoning across various motion patterns, including walking and running at different speeds. Furthermore, the method effectively mitigates error drift without relying on any external signals.

## Problem Addressed

Smartwatch-based indoor localization typically requires combining data from multiple sensors or mobile devices for reliable position estimation, which is inconvenient for practical everyday use.

## Key Contributions

- First neural inertial localization method relying solely on smartwatch IMU data without external devices or signals
- Wearable neural inertial odometry (WNIO) adapting to varying arm-swing motions with adaptive error-state Kalman filter attitude refinement
- Human-environment interaction detection (e.g., door opening) exploited as absolute position constraints
- Multi-hypothesis Kalman filter resolving ambiguous activity associations for reliable matching

## Conclusions

Real-world experiments demonstrate reliable dead reckoning across motion patterns including walking and running at different speeds, with error drift effectively mitigated without any external signals. The physics-guided attitude pre-alignment improves generalization across motion patterns, and the multi-hypothesis Kalman filter achieves better position matching than traditional activity-sequence-based methods. Future work will integrate NFC and BLE proximity information for additional absolute position corrections.
