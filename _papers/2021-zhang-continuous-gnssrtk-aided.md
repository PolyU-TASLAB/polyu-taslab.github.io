---
title: Continuous GNSS-RTK Aided by LiDAR/Inertial Odometry with Intelligent GNSS Selection in Urban Canyons
authors:
- Jiachen Zhang
- Weisong Wen
- Feng Huang
- Xiaodong Chen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2021-10-13'
doi: https://doi.org/g8t45c
image: images/papers/cards/2021-zhang-continuous-gnssrtk-aided.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Zhang_Continuous_Gnss-Rtk_Aided.pdf
tags:
- GNSS-RTK
- GNSS
- NLOS
- urban canyons
- LIO
citation_id: doi:10.33012/2021.18089
---

## Abstract

Accurate and globally referenced positioning is the key prerequisite for fully successful autonomous systems. Global Navigation Satellite System (GNSS) could provide global positioning service in open areas. Unfortunately, under denes urban areas, in which it is typical for autonomous systems to operate, the performance of GNSS suffers from non-line-of-sight (NLOS) receptions and multipath effects caused by GNSS signal reflection and blockage from surrounding buildings. Thus, it will lead to position measurements with terribly large errors and GNSS outage. To facilitate long-term stable and accurate navigation, this paper proposes a method of continuous GNSS Real-time Kinematic (RTK) positioning aided by he 3D light detection and ranging (LiDAR) /inertial odometry (LIO) with intelligent GNSS selection in urban canyons. The coarse-to-fine LIO keeps on generating a 34th International Technical Meeting of the Satellite Division of the Institute of Navigation (ION GNSS+ 2021), September 20-24, 2021 4198 https://doi.org/10.33012/2021.18089 locally accurate motion estimation and a registered point cloud map. Inspired by the outstanding capability of the environmental description of 3D LiDAR, available GNSS-RTK under light urban environment is detected as the degree of urbanization is evaluated via the sky-mask elevation angle calculation, which will be further integrated with the relative motion estimation from LIO based on factor graph optimization. Therefore, the continuous and accurate positioning is guaranteed by the local estimation from low-drift LIO in highly urbanized areas and global correction once the “Available GNSS-RTK” is obtained. The experimental results in a typical urban canyon in Hong Kong shows that the performance of the proposed integration pipeline is significantly improved in comparison with that without GNSS-RTK selection. 1.

## Problem Addressed

In dense urban areas GNSS suffers from NLOS receptions and multipath effects caused by signal reflection and blockage, leading to large positioning errors and outages. Long-term autonomous navigation requires continuous, globally referenced positioning despite these degradations.

## Key Contributions

- Intelligent available GNSS-RTK selection exploiting the registered 3D point cloud map from LiDAR/inertial odometry.
- Degree of urbanization evaluated via sky-mask elevation angle calculation to detect trustworthy GNSS-RTK.
- Loosely coupled available-GNSS-RTK/LiDAR/inertial integration pipeline based on factor graph optimization.
- Verification on data collected in typical urban areas of Hong Kong.

## Conclusions

The absolute trajectory error of the proposed pipeline is significantly improved compared with loosely coupling all received GNSS-RTK measurements. Continuous and accurate positioning is maintained by low-drift LiDAR/inertial odometry locally and by global correction whenever an available GNSS-RTK is detected.
