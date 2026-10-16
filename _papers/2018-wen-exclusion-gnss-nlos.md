---
title: 'Exclusion of GNSS NLOS receptions caused by dynamic objects in heavy traffic urban scenarios using real-time 3D point cloud: An approach without 3D maps'
authors:
- Weisong Wen
- Guohao Zhang
- Li-Ta Hsu
publisher: 2018 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2018-04-01'
doi: https://doi.org/g8tzc9
image: images/papers/cards/2018-wen-exclusion-gnss-nlos.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/EGNR.pdf
tags:
- GPS
- GNSS
- LiDAR
- 3D point clouds
- Object detection
- NLOS exclusion
- Urban canyon
citation_id: doi:10.1109/PLANS.2018.8373377
---

## Abstract

Absolute positioning is an essential factor for the arrival of autonomous driving. Global Navigation Satellites System (GNSS) receiver provides absolute localization for it. GNSS solution can provide satisfactory positioning in open or sub-urban areas, however, its performance suffered in super-urbanized area due to the phenomenon which are well-known as multipath effects and NLOS receptions. The effects dominate GNSS positioning performance in the area. The recent proposed 3D map aided (3DMA) GNSS can mitigate most of the multipath effects and NLOS receptions caused by buildings based on 3D city models. However, the same phenomenon caused by moving objects in urban area is currently not modelled in the 3D geographic information system (GIS). Moving objects with tall height, such as the double-decker bus, can also cause NLOS receptions because of the blockage of GNSS signals by surface of objects. Therefore, we present a novel method to exclude the NLOS receptions caused by double-decker bus in highly urbanized area, Hong Kong. To estimate the geometry dimension and orientation relative to GPS receiver, a Euclidean cluster algorithm and a classification method are used to detect the double-decker buses and calculate their relative locations. To increase the accuracy and reliability of the proposed NLOS exclusion method, an NLOS exclusion criterion is proposed to exclude the blocked satellites considering the elevation, signal noise ratio (SNR) and horizontal dilution of precision (HDOP). Finally, GNSS positioning is estimated by weighted least square (WLS) method using the remaining satellites after the NLOS exclusion. A static experiment was performed near a double-decker bus stop in Hong Kong, which verified the effectiveness of the proposed method.

## Problem Addressed

3D map aided GNSS can mitigate multipath and NLOS caused by static buildings, but NLOS receptions caused by dynamic tall objects such as double-decker buses are not modeled in 3D GIS data. These dynamic blockages degrade GNSS positioning in heavy-traffic urban scenarios.

## Key Contributions

- Detects double-decker buses from real-time 3D point clouds using Euclidean clustering and classification
- Estimates bus geometry and orientation relative to the GNSS receiver and projects boundaries into the skyplot
- Proposes an NLOS exclusion criterion considering elevation angle, SNR, and HDOP
- Estimates GNSS positioning via weighted least squares using the remaining satellites after exclusion

## Conclusions

A static experiment near a double-decker bus stop in Hong Kong shows the method achieves the best performance among four conventional methods and effectively excludes NLOS measurements. Positioning errors caused by double-decker bus NLOS receptions can reach 24 meters overall, confirming that exclusion of such NLOS receptions is necessary. Elevation and SNR filters clearly improve performance, and dynamic experiments are planned for future work.
