---
title: Real-time GNSS NLOS Detection and Correction Aided by Sky-Pointing Camera and 3D LiDAR
authors:
- Xiwei Bai
- Weisong Wen
- Guohao Zhang
- Li-Ta Hsu
publisher: ION Pacific PNT
date: '2019-05-01'
doi: https://doi.org/g8tzc5
image: images/papers/cards/2019-bai-realtime-gnss-nlos.jpg
buttons:
- type: manubot
  text: paper
  link: https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/publications/papers/Bai_Real-Time_Gnss_Nlos.pdf
tags:
- FGO
- 3D LiDAR
- NLOS
- RTK
- 3DMA GNSS
- Cameras
- Sensors
citation_id: doi:10.33012/2019.16845
---

## Abstract

Robust and globally referenced positioning is the basis of fully autonomous driving in diverse scenarios. Globally navigation satellite system (GNSS) is currently the main source providing globally referenced positioning. Satisfactory accuracy (5~10 meters) can be obtained in sparse areas. However, the GNSS positioning error can go up to even 100 meters in dense urban areas due to the multipath effects and none-line-of-sight (NLOS) reception caused by reflection and blockage from buildings. NLOS is currently the dominant component degrading the performance of GNSS positioning. Recently, the camera is employed to detect the NLOS satellites and then the NLOS are excluded from GNSS calculation. This exclusion can cause severe distortion of satellite distribution, due to the excessive NLOS receptions in deep urban canyon. This paper proposes to correct the NLOS receptions with the aid of 3D LiDAR ranging after detecting NLOS receptions using camera. The sky-pointing monocular camera is firstly employed to detect satellite visibility. Then, the NLOS delay is modeled using the satellite elevation angle, azimuth angle and distance from receiver to possible reflector which is ranged by 3D LiDAR. The pseudorange measurements are corrected using the estimated NLOS delay. Finally, the GNSS positioning is improved using corrected pseudorange measurements and healthy (visible) satellites. The proposed method is verified through real road tests in a deep urbanized canyon of Hong Kong. The result shows that the proposed method can effectively improve the GNSS positioning performance by decreasing the mean error from 22.01 to 14.96 meters.

## Problem Addressed

GNSS positioning error can reach 100 m in dense urban areas, where NLOS reception is the dominant error source. Excluding NLOS satellites after camera-based detection severely distorts the satellite distribution in deep urban canyons.

## Key Contributions

- Uses a sky-pointing monocular camera to detect satellite visibility from segmented sky view images
- Models NLOS delay from satellite elevation, azimuth, and LiDAR-ranged distance to possible reflectors
- Corrects pseudorange measurements using the estimated NLOS delay rather than excluding them
- Combines corrected and healthy pseudorange measurements for real-time GNSS positioning

## Conclusions

Real road tests in a deep urbanized canyon of Hong Kong show the method decreases the mean positioning error from 22.01 to 14.96 meters, while NLOS exclusion alone results in a larger error of 24.99 meters. NLOS correction thus radically alleviates NLOS effects without time-consuming ray-tracing. Future work will use a fish-eye camera with broader field of view and analyze the remaining multipath errors.
