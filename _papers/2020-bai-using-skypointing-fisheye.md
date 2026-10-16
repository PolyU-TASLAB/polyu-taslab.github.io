---
title: Using Sky-pointing fish-eye camera and LiDAR to aid GNSS single-point positioning in urban canyons
authors:
- Xiwei Bai
- Weisong Wen
- Li-Ta Hsu
publisher: IET Intelligent Transport Systems
date: '2020-05-29'
doi: https://doi.org/g8tzc2
image: images/papers/cards/2020-bai-using-skypointing-fisheye.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/USFC.pdf
tags: []
citation_id: doi:10.1049/iet-its.2019.0587
---

## Abstract

Robust and globally-referenced positioning is indispensable for autonomous driving vehicles. Global navigation satellite system (GNSS) is still an irreplaceable sensor. Satisfactory accuracy (about 1 m) can be obtained in sparse areas.
However, the GNSS positioning error can be up to 100 m in dense urban areas due to the multipath effects and non-line-of-sight (NLOS) receptions caused by reflection and blockage from buildings. NLOS is currently the dominant factor degrading the performance of GNSS positioning. Recently, the camera has been employed to detect the NLOS and then to exclude the NLOS measurements from GNSS calculation. The exclusion of NLOS measurements can cause severe distortion of satellite distribution, due to the excessive NLOS receptions in deep urban canyons. Correcting the NLOS receptions with the aid of 3D light detection and ranging after detection of NLOS receptions using a fish-eye camera was proposed in this study. Finally, the
GNSS positioning was improved by using the healthy and corrected NLOS pseudo-range measurements. The proposed method is evaluated through real road tests in typical highly urbanised canyons of Hong Kong. The evaluation results show that the proposed method can effectively improve the positioning performance.

## Problem Addressed

GNSS positioning in dense urban areas can degrade to errors of up to 100 m due to multipath effects and NLOS receptions caused by building reflection and blockage. Simply excluding detected NLOS measurements severely distorts the satellite distribution in deep urban canyons.

## Key Contributions

- Uses a sky-pointing fish-eye camera to detect NLOS satellite receptions from the segmented sky view
- Corrects NLOS pseudorange measurements with 3D LiDAR ranging instead of excluding them
- Performs GNSS single-point positioning with both healthy and corrected NLOS pseudorange measurements
- Evaluates the method in real road tests in highly urbanized canyons of Hong Kong

## Conclusions

Real road tests in typical highly urbanized canyons of Hong Kong show that correcting rather than excluding NLOS receptions effectively improves GNSS positioning performance. The approach avoids the satellite geometry distortion caused by excessive NLOS exclusion in deep urban canyons.
