---
title: GNSS NLOS Exclusion Based on Dynamic Object Detection Using LiDAR Point Cloud
authors:
- Weisong Weisong Wen
- Guohao Zhang
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Transportation Systems
date: '2021-02-01'
doi: https://doi.org/gprd59
image: images/papers/cards/2021-wen-gnss-nlos-exclusion.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/GNEB.pdf
tags:
- GPS
- GNSS
- NLOS
- LiDAR
- 3D point clouds
- object detection
- positioning
citation_id: doi:10.1109/TITS.2019.2961128
---

## Abstract

Absolute positioning is an essential factor for the arrival of autonomous driving. At present, GNSS is the indispensable source that can supply initial positioning in the commonly used high definition map-based LiDAR point cloud positioning solution for autonomous driving. However, the non-light-of-sight (NLOS) reception dominates GNSS positioning performance in super-urbanized areas. The recent proposed 3D map aided (3DMA) GNSS can mitigate the majority of the NLOS caused by buildings. However, the same phenomenon caused by moving objects in urban areas is currently not modeled in the 3D geographic information system (GIS). Therefore, we present a novel method to exclude the NLOS receptions caused by a double-decker bus, one of the symbolic tall moving objects in road transportations. To estimate the dimension and orientation of the double-decker buses relative to the GNSS receiver, LiDAR-based perception is utilized. By projecting the relative positions into GNSS Skyplot, the direct transmission path of satellite signals blocked by the moving objects can be identified and excluded from positioning. Finally, GNSS positioning is estimated by the weighted least square (WLS) method based on the remaining satellites after the NLOS exclusion. Both static and dynamic experiments are conducted in Hong Kong. The results show that the proposed NLOS exclusion using LiDAR-based perception can greatly improve the GNSS single point positioning (SPP) performance.

## Problem Addressed

NLOS reception dominates GNSS positioning performance in super-urbanized areas. While 3D mapping aided GNSS mitigates NLOS caused by buildings, NLOS caused by tall moving objects such as double-decker buses is not modeled in 3D geographic information systems.

## Key Contributions

- LiDAR-based perception estimates the dimension and orientation of double-decker buses relative to the GNSS receiver.
- Bus boundaries projected into the GNSS skyplot to identify satellite signals blocked by moving objects.
- NLOS exclusion criterion integrating elevation angle, SNR, and bus boundary.
- Weighted least-squares positioning using the surviving satellites after NLOS exclusion.

## Conclusions

Static and dynamic experiments in Hong Kong show that NLOS receptions caused by a double-decker bus can induce positioning errors up to 24 meters in the static case, and the proposed exclusion achieves an 8-meter improvement in the evaluated dynamic experiment. The method obtains the best performance among four conventional GNSS positioning methods.
