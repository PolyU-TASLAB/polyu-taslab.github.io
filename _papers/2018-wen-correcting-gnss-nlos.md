---
title: Correcting GNSS NLOS by 3D LiDAR and Building Height
authors:
- Weisong Wen
- Guohao Zhang
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2018-10-26'
doi: https://doi.org/g54dhj
image: images/papers/cards/2018-wen-correcting-gnss-nlos.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/CGN3.pdf
tags:
- GNSS
- NLOS
- 3D LiDAR
- 3DMA GNSS
citation_id: doi:10.33012/2018.15984
---

## Abstract

Occurrence of autonomous driving introduces high requirement in GNSS positioning performance. GNSS is currently the only source providing absolute positioning information. It is indispensable for initial position estimation for the high definition map-based localization solution in autonomous driving. Satisfactory positioning accuracy can be obtained in open space or sub-urban areas. However, its performance is heavily challenged in super-urbanized scenarios with the positioning error going up to even 100 meters, due to the well-known NLOS receptions which dominates the GNSS positioning errors. The recent state-of-art range-based 3D map aided GNSS (3DMA GNSS) can mitigate most of the NLOS receptions. However, ray-tracing simulation is time-consuming. Therefore, we present a novel method to detect the NLOS caused by surrounding buildings and correct the pseudorange measurements using 3D point clouds and building height without ray-tracing simulation. To estimate the geometry and pose of the building relative to GNSS receiver, a surface segmentation method is employed to detect the surrounding building walls. NLOS errors are estimated by integrating the geometry, pose relative to the GNSS receiver and satellites information. Finally, position estimation of GNSS receiver is implemented by weighted least square (WLS) based on the corrected and healthy pseudorange measurements. Dynamic experiment is conducted to evaluate the errors caused by the NLOS receptions and to verify the effectiveness of the proposed method in a deep urbanized area, Hong Kong.

## Problem Addressed

GNSS positioning error in super-urbanized scenarios can reach 100 m, dominated by NLOS receptions from buildings. Range-based 3D map aided GNSS can mitigate NLOS but requires time-consuming ray-tracing simulation.

## Key Contributions

- Detects surrounding building walls from 3D LiDAR point clouds using a surface segmentation method
- Integrates building height information to extend detected buildings to their actual height
- Estimates NLOS errors from building geometry, pose relative to the receiver, and satellite information
- Corrects pseudoranges without ray-tracing and positions via weighted least squares

## Conclusions

The dynamic experiment in a deep urbanized area of Hong Kong verifies that the method corrects NLOS receptions and improves GNSS positioning. NLOS exclusion is shown to be harmful in super-urbanized areas, producing dramatically larger errors of 394.05 meters with 241.01 meters standard deviation, so correction is needed instead. Most NLOS errors are caused by satellites at low elevation angles of 18 to 36 degrees.
