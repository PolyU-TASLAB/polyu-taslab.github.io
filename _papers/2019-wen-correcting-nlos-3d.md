---
title: Correcting NLOS by 3D LiDAR and building height to improve GNSS single point positioning
authors:
- Weisong Wen
- Guohao Zhang
- Li-Ta Hsu
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

We present a novel method to detect the GNSS NLOS and correct the NLOS pseudorange measurements based on on - board sensing. This paper demonstrates the use of LiDAR scanner and a list of building heights to describe the perceived environment. To estimate the geometry and pose of the top edges of buildings (TEBs) relative to the GNSS receiver, a surface segmentation method is employed to detect the TEBs of surrounding buildings using 3D LiDAR point clouds. The top edges of the building are extracted and extended using the building height list in Skyplot to identify the NLOS - affected ones. Innovatively, the NLOS delay in pseudorange is corrected based on the detected TEBs. Weighted least squares (WLS) is used to cooperate the corrected NLOS and other pseudorange measurements. Vehicle experiments are conducted in two different urban canyons to verify the effectiveness of the proposed method in improving GNSS single point positioning (SPP) accuracy.

## Problem Addressed

GNSS single-point positioning in urbanized cities is severely degraded by NLOS receptions caused when buildings block and reflect satellite signals. Reliable absolute positioning is needed for autonomous driving, but NLOS effects dominate the error in urban canyons.

## Key Contributions

- Detects top edges of buildings (TEBs) from 3D LiDAR point clouds using a surface segmentation method
- Extends detected TEBs with a building height list in the skyplot to identify NLOS-affected satellites
- Corrects NLOS pseudorange delay based on the detected TEBs instead of excluding measurements
- Fuses corrected NLOS and healthy pseudoranges via weighted least squares for positioning

## Conclusions

Vehicle experiments in two different urban canyons show the proposed NLOS correction method obtains improved GNSS positioning accuracy compared with standalone weighted least squares. Correcting NLOS measurements is preferable to direct exclusion, and future work will integrate a sky-pointing camera with LiDAR for real-time sky view description.
