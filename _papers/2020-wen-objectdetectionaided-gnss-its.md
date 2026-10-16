---
title: Object-Detection-Aided GNSS and Its Integration With Lidar in Highly Urbanized Areas
authors:
- Weisong Wen
- Guohao Zhang
- Li-Ta Hsu
publisher: IEEE Intelligent Transportation Systems Magazine
date: '2020-01-01'
doi: https://doi.org/gqqbhp
image: images/papers/cards/2020-wen-objectdetectionaided-gnss-its.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/ODAG.pdf
tags:
- Global navigation satellite system
- Three-dimensional displays
- Laser radar
- Simultaneous localization and mapping
- Uncertainty
- Urban areas
citation_id: doi:10.1109/MITS.2020.2994131
---

## Abstract

Positioning is a key function for autonomous vehicles that requires globally referenced localization information. Lidarbased mapping, which refers to simultaneous localization and mapping (SLAM), provides continuous positioning in diverse scenarios. 
However, SLAM error can accumulate through time. Besides, only relative positioning is provided by SLAM. The Global Navigation 
Satellite System (GNSS) receiver is one of the significant sensors for providing globally referenced localization, and it is usually integrated with lidar in autonomous driving. However, the performance of the GNSS is severely challenged due to the reflection and blockage caused by buildings in superurbanized cities, including Hong Kong, China; Tokyo; and New York, resulting in the notorious non-line-of-sight (NLOS) receptions. Moreover, the uncertainty of the GNSS positioning is ambiguous, leading to the incorrect tuning of its weight during GNSS-lidar integration. This article innovatively employs lidar to identify the NLOS measurement of the GNSS receiver using point-cloud-based object detection. Measurements from satellites suffering from NLOS reception will be excluded based on the proposed fault detection and exclusion (FDE) algorithm. Then, GNSS-weight least-square positioning is conducted based on the surviving measurements from FDE. The noise covariance of the GNSS positioning is calculated by considering the potential location errors caused by the NLOS and the remaining LOS measurements. The improved GNSS result and its corresponding noise covariance are integrated with lidar through a graph-based SLAM-integration framework. Experimental results indicate that the proposed GNSS-lidar integration can obtain improved positioning accuracy in a highly urbanized area in Hong Kong.
MAP: ©ISTOCKPHOTO/MADMAXER. CAR: ©ISTOCKPHOTO/JOHAVEL
GNSS-BASED 
GNSS-BASED 
GNSS-BASED 
POSITIONING
POSITIONING
POSITIONING
Authorized licensed use limited to: Hong Kong Polytechnic University. Downloaded on December 09,2024 at 06:30:23 UTC from IEEE Xplore. Restrictions apply. 

IEEE INTELLIGENT TRANSPORTATION SYSTEMS MAGAZINE • 54 • FALL 2020 utonomous vehicles [1], [2] receive increasing attention due to

## Problem Addressed

GNSS positioning is severely challenged by NLOS receptions in super-urbanized cities, and the ambiguous uncertainty of GNSS positioning leads to incorrect weighting during GNSS-lidar integration.

## Key Contributions

- Lidar point-cloud-based object detection identifies NLOS measurements of the GNSS receiver.
- Fault detection and exclusion algorithm removes measurements from satellites suffering NLOS reception.
- GNSS noise covariance computed considering potential location errors from NLOS and remaining LOS measurements.
- Graph-based SLAM framework integrates the improved GNSS result and its covariance with lidar.

## Conclusions

Experimental results in a highly urbanized area of Hong Kong indicate that the proposed object-detection-aided GNSS and its integration with lidar obtain improved positioning accuracy.
