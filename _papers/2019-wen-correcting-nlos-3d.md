---
title: Correcting NLOS by 3D LiDAR and building height to improve GNSS single point positioning
authors:
- Weisong Wen
- Guohao Zhang
- Li‐Ta Hsu
publisher: Navigation
date: '2019-12-01'
doi: https://doi.org/g8tzc4
image: images/papers/cards/2019-wen-correcting-nlos-3d.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/CN3L.pdf
tags:
- NLOS
- GNSS
- 3D LiDAR
citation_id: doi:10.1002/navi.335
---

## Abstract

We present a novel method to detect the GNSS NLOS and correct the NLOS pseudorange measurements based on on‐board sensing. This paper demonstrates the use of LiDAR scanner and a list of building heights to describe the perceived environment. To estimate the geometry and pose of the top edges of buildings (TEBs) relative to the GNSS receiver, a surface segmentation method is employed to detect the TEBs of surrounding buildings using
3D LiDAR point clouds. The top edges of the building are extracted and extended using the building height list in Skyplot to identify the NLOS‐ affected ones. Innovatively, the NLOS delay in pseudorange is corrected based on the detected TEBs. Weighted least squares (WLS) is used to cooperate the corrected NLOS and other pseudorange measurements. Vehicle experiments are conducted in two different urban canyons to verify the effectiveness of the proposed method in improving GNSS single point positioning (SPP) accuracy.
1 |
INTRODUCTION
Positioning in urban environments is becoming essential due to the increasing need for autonomous vehicles. To achieve
L41 autonomous driving in all scenarios, centimeter‐level absolute positioning is required. The three‐dimensional (3D) Light Detection and Ranging (LiDAR) is widely used in autonomous driving vehicles.2,3 LiDAR, camera, and Inertial Navigation
Systems (INS) only provide relative positioning. Thus, these sensors are usually integrated with the Global
Navigation Satellite System (GNSS),4-7 as it is one of the indispensable sources that can provide absolute positioning. A GNSS/INS/LiDAR/high‐definition (HD) map integrated system can provide satisfactory localization service in sub‐urban8,9 areas. The suburban areas, in fact, can be regarded as GNSS‐friendly areas since the
GNSS receiver can receive sufficient direct signals transmitted from multi‐constellation GNSS.10 In urbanized cities, such as Tokyo, Hong Kong, and New York, the signals from satellites can be reflected, blocked, and diffracted by surrounding buildings before they are received by the receiver. If the direct light‐of‐sight (LOS) is blocked and reflected signals from the same satellite are received, the notorious non‐light‐

## Problem Addressed

GNSS single-point positioning in urbanized cities is severely degraded by NLOS receptions caused when buildings block and reflect satellite signals. Reliable absolute positioning is needed for autonomous driving, but NLOS effects dominate the error in urban canyons.

## Key Contributions

- Detects top edges of buildings (TEBs) from 3D LiDAR point clouds using a surface segmentation method
- Extends detected TEBs with a building height list in the skyplot to identify NLOS-affected satellites
- Corrects NLOS pseudorange delay based on the detected TEBs instead of excluding measurements
- Fuses corrected NLOS and healthy pseudoranges via weighted least squares for positioning

## Conclusions

Vehicle experiments in two different urban canyons show the proposed NLOS correction method obtains improved GNSS positioning accuracy compared with standalone weighted least squares. Correcting NLOS measurements is preferable to direct exclusion, and future work will integrate a sky-pointing camera with LiDAR for real-time sky view description.
