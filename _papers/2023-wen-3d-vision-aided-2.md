---
title: 3D Vision Aided GNSS Real-Time Kinematic Positioning for Autonomous Systems in Urban Canyons
authors:
- Weisong Wen
- Xiwei Bai,
- Li-Ta Hsu
publisher: 'NAVIGATION: Journal of the Institute of Navigation'
date: '2023-01-01'
doi: https://doi.org/gsbsnc
image: images/papers/cards/2023-wen-3d-vision-aided-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/3DVAGRTK.pdf
tags:
- 3D vision
- autonomous system
- GNSS-RTK
- urban canyons
- NLOS
citation_id: 10.33012/navi.590
---

## Abstract

In this paper, a three-dimensional vision-aided method is proposed to improve global navigation satellite system (GNSS) real-time kinematic (RTK) position­ ing. To mitigate the impact of reflected non-line-of-sight (NLOS) reception, a sky-pointing camera with a deep neural network was employed to exclude these measurements. However, NLOS exclusion results in distorted satellite geometry. To fill this gap, complementarity between the low-lying visual landmarks and the healthy but high-elevation satellite measurements was explored to improve the geometric constraints. Specifically, inertial measurement units, visual landmarks captured by a forward-looking camera, and healthy GNSS measurements were tightly integrated via sliding window optimization to estimate the GNSS-RTK float solution. The integer ambiguities and the fixed GNSS-RTK solution were then resolved. The effectiveness of the proposed method was verified using several challenging data sets collected in urban canyons in Hong Kong.

## Problem Addressed

GNSS real-time kinematic positioning in urban canyons suffers from reflected NLOS reception, and camera-based NLOS exclusion distorts satellite geometry, degrading the positioning solution.

## Key Contributions

- Sky-pointing camera with deep neural network to exclude NLOS measurements
- Exploits complementarity between low-lying visual landmarks and healthy high-elevation satellites to improve geometric constraints
- Tightly integrates IMU, forward-looking visual landmarks, and healthy GNSS measurements via sliding-window optimization for the RTK float solution
- Integer ambiguity resolution to obtain the fixed GNSS-RTK solution

## Conclusions

The proposed 3D vision-aided method was verified on several challenging datasets collected in urban canyons in Hong Kong. By combining visual landmarks with healthy GNSS measurements, it mitigates the impact of NLOS reception while compensating for the degraded satellite geometry caused by NLOS exclusion.
