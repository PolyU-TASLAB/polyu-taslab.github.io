---
title: LiDAR Aided Cycle Slip Detection for GNSS Real-Time Kinematic Positioning in Urban Environments
authors:
- Feng Huang
- Weisong Wen
- Hoi-Fung Ng
- Li-Ta Hsu
publisher: 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC)
date: '2022-10-08'
doi: https://doi.org/g8t5rx
image: images/papers/cards/2022-huang-lidar-aided-cycle.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Lidar_aided_cycle.pdf
tags:
- Navigation
- GNSS-RTK
- LiDAR
- Cycle Slip
- Urban Canyons
citation_id: doi:10.1109/ITSC55140.2022.9921814
---

## Abstract

Cycle slip of carrier-phase measurements is a common error source in global navigation satellite systems (GNSS) real-time kinematic (RTK) positioning. It limits the performance of the GNSS-RTK in urban canyons due to the excessive signal reflections from buildings. To fill this gap, this paper proposes a LiDAR-aided cycle slip detection method for 
GNSS-RTK, which benefits from the consecutive relative pose estimated by LiDAR odometry. Specifically, the difference between the triple-differenced carrier-phase measurements and that of prediction based on the LiDAR odometry is used to detect the potential cycle slips. The associated integer ambiguity is reestimated if the cycle slip is observed to obtain an improved 
GNSS-RTK positioning. Experiments were conducted in a typical urban scenario of Hong Kong to verify the performance and effectiveness of the proposed method. The results demonstrated that the performance of the cycle slip can be effectively improved using the proposed method compared to the conventional loss of lock indicator (LLI) based method. Both the 
GNSS-RTK fixing rate and positioning accuracy can be improved by 17.33% and 13.86%, respectively with the help of the proposed LiDAR-aided method.

## Problem Addressed

Cycle slips in carrier-phase measurements are a common error source in GNSS real-time kinematic positioning, and excessive signal reflections in urban canyons make them frequent, limiting RTK fixing rate and accuracy. Conventional loss-of-lock-indicator-based detection is insufficient in such environments.

## Key Contributions

- LiDAR-aided cycle slip detection exploiting consecutive relative pose from LiDAR odometry
- Detection based on the difference between triple-differenced carrier-phase measurements and LiDAR-odometry predictions
- Integer ambiguity re-estimation after detected slips to improve GNSS-RTK positioning
- Step-by-step experimental comparison against conventional methods on Hong Kong urban-canyon data

## Conclusions

Experiments in a typical Hong Kong urban scenario show the LiDAR-aided method detects cycle slips more effectively than the conventional LLI-based method. The GNSS-RTK fixing rate and positioning accuracy were improved by 17.33% and 13.86%, respectively. Future work includes GNSS-LiDAR-inertial multi-sensor fusion to reduce the global drift of LiDAR for long-term autonomous driving.
