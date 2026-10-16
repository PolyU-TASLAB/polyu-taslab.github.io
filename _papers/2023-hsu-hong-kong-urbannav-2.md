---
title: 'Hong Kong UrbanNav: An Open-Source Multisensory Dataset for Benchmarking Urban Navigation Algorithms'
authors:
- Li-Ta Hsu
- Feng Huang
- Hoi-Fung Ng
- Guohao Zhang
- Yihan Zhong
- Xiwei Bai,
- Weisong Wen
publisher: 'NAVIGATION: Journal of the Institute of Navigation'
date: '2023-01-01'
doi: https://doi.org/gsk3ck
image: images/papers/cards/2023-hsu-hong-kong-urbannav-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/navi.602.full.pdf
tags:
- dynamic objects
- gnss raw data
- gnss/ins/lidar/camera
- ground truth
- localization
- positioning
- urban canyons
repo: https://github.com/IPNL-POLYU/UrbanNavDataset
citation_id: 10.33012/navi.602
---

## Abstract

Accurate positioning in urban canyons remains a challenging problem. To facilitate the research and development of reliable and precise positioning methods using multiple sensors in urban canyons, we built a multisensory dataset, 
UrbanNav, collected in diverse, challenging urban scenarios in Hong Kong. 
The dataset provides multi-sensor data, including data from multi-frequency global navigation satellite system (GNSS) receivers, an inertial measurement unit (IMU), multiple light detection and ranging (lidar) units, and cameras. 
Meanwhile, the ground truth of the positioning (with centimeter-level accuracy) is postprocessed by commercial software from NovAtel using an integrated 
GNSS real-time kinematic and fiber optics gyroscope inertial system. In this paper, the sensor systems, spatial and temporal calibration, data formats, and scenario descriptions are presented in detail. Meanwhile, the benchmark performance of several existing positioning methods is provided as a baseline. Based on the evaluations, we conclude that GNSS can provide satisfactory results in a middle-class urban canyon if an appropriate receiver and algorithms are applied. Both visual and lidar odometry are satisfactory in deep urban canyons, whereas tunnels are still a major challenge. Multisensory integration with the aid of an IMU is a promising solution for achieving seamless positioning in cities. The dataset in its entirety can be found on GitHub at https://github.com/
IPNL-POLYU/UrbanNavDataset.
Keywords dynamic objects, gnss raw data, gnss/ins/lidar/camera, ground truth, localization, positioning, urban canyons

HSU et al.
     or open areas (Levinson et al., 2011) with good sky visibility for GNSS positioning and abundant environment features for lidar units and cameras. Unfortunately, the performance of existing positioning technologies is significantly degraded in the urban scenarios of megacities, such as Hong Kong, Tokyo, and New York City, due to complex building structures, unstable illumination conditions, and excessive expected dynamic objects.
Poor GNSS positioning in urban canyons: GNSS positioning is significantly degraded in urban canyons because of signal reflection

## Problem Addressed

Accurate positioning in urban canyons remains challenging due to complex building structures, and existing multisensory datasets do not satisfy the requirements for benchmarking urban navigation algorithms in such scenarios.

## Key Contributions

- Open-source multisensory dataset collected in diverse, challenging urban scenarios in Hong Kong
- Multi-frequency GNSS receivers, IMU, multiple lidars, and cameras with detailed spatial and temporal calibration
- Centimeter-level ground truth post-processed from GNSS RTK and fiber-optic gyroscope inertial system
- Baseline benchmark performance of several existing positioning methods

## Conclusions

Benchmarks show GNSS can provide satisfactory results in a middle-class urban canyon when appropriate receivers and algorithms are applied. Visual and lidar odometry are satisfactory in deep urban canyons, whereas tunnels remain a major challenge. Multisensory integration aided by an IMU is a promising solution for seamless positioning in cities.
