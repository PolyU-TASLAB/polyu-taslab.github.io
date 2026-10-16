---
title: Roadside GNSS Aided Multi-Sensor Integrated System for Vehicle Positioning in Urban Areas
authors:
- Feng Huang
- Yihan Zhong
- Hang Chen
- Dongzhe Su
- Jin Wu
- Weisong Wen
- Li-Ta Hsu
publisher: 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
date: '2025-10-19'
doi: https://doi.org/hccr4m
image: images/papers/cards/2025-huang-roadside-gnss-aided.jpg
citation_id: doi:10.1109/IROS60139.2025.11246475
---

## Abstract

Global navigation satellite system (GNSS) positioning can be significantly degraded due to multipath and non-line-of-sight (NLOS) signals in urban areas. Cellular vehicle-to-everything (C-V2X) technology provides new opportunities to enhance GNSS performance from a single intelligent vehicle by leveraging roadside GNSS (RSG) and C-V2X. Inspired by this, we propose an RSG-aided GNSS/LiDAR/IMU (RSG-GLIO) method to achieve reliable odometry and mapping, which leverages the high-quality double-differenced (DD) measurements provided by nearby RSG, effectively mitigating shared random errors such as multipath and NLOS. Our RSG-GLIO first estimates the absolute state of the vehicle using onboard sensors. Utilizing this initial positioning estimate, the proposed method introduces a coarse-to-fine selection scheme to identify consistent DD observations from available RSG measurements. Finally, the consistent roadside DD constraints are jointly optimized into factor graph optimization (FGO). Static and dynamic data are extensively evaluated using multiple RSG receivers deployed in the Hong Kong C-V2X testbed to evaluate the effectiveness of roadside-aided positioning. The results demonstrate a significant 36.6% improvement in terms of absolute positioning accuracy compared to the state-of-the-art GLIO method. Furthermore, we showcase the potential for employing RSG as low-cost base stations in dense urban areas. The data of our work is publicly accessible at https://github.com/DarrenWong/RSG-GLIO.

## Problem Addressed

GNSS positioning in urban areas is significantly degraded by multipath and non-line-of-sight signals, which a single intelligent vehicle's onboard sensors cannot fully overcome.

## Key Contributions

- RSG-GLIO method aiding GNSS/LiDAR/IMU odometry and mapping with roadside GNSS double-differenced measurements
- Coarse-to-fine selection scheme identifying consistent double-differenced observations from roadside measurements
- Joint factor graph optimization of consistent roadside double-differenced constraints
- Static and dynamic evaluation with multiple roadside receivers in the Hong Kong C-V2X testbed, with public data

## Conclusions

The RSG-GLIO method achieves a 36.6% improvement in absolute positioning accuracy compared to the state-of-the-art GLIO method, and demonstrates the potential of roadside GNSS receivers as low-cost base stations in dense urban areas. A known limitation is the reliance on the availability of urban roadside infrastructure and C-V2X coverage.
