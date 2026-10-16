---
title: New Integrated Navigation Scheme for the Level 4 Autonomous Vehicles in Dense Urban Areas
authors:
- Li-Ta Hsu
- Weisong Wen
publisher: 2020 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2020-04-01'
doi: https://doi.org/gpsz9f
image: images/papers/cards/2020-hsu-new-integrated-navigation.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/NINS.pdf
tags:
- Autonomous Driving Vehicle
- Positioning
- Perception
- GNSS
- LiDAR
- Camera
- PASIN
- Urban canyon
citation_id: doi:10.1109/PLANS46316.2020.9109962
---

## Abstract

Accurate and globally referenced positioning is fatal to the safety-critical autonomous driving vehicles (ADV). 
Multi-sensor integration is becoming ubiquitous for ADV to guarantee the robustness and accuracy of the navigation system. 
Unfortunately, the existing sensor integration systems are still heavily challenged in urban canyons, such as Tokyo and Hong 
Kong. The main reason behind the performance degradation is due to the varying environmental conditions, such as tall buildings and surrounded dynamic objects. GNSS receiver is an indispensable sensor for ADV, which relies heavily on the environmental conditions. The performance of GNSS can be significantly affected by signal reflections and blockages from buildings or dynamic objects. With the enhanced capability of perception, fully or partially sensing the environment real-time becomes possible using onboard sensors, such as camera or 
LiDAR. Inspired by the fascinating progress in perception, this paper proposes a new integrated navigation scheme, the perception aided sensor integrated navigation (PASIN). Instead of directly integrating the sensor measurements from diverse sensors, the PASIN leverages the onboard and real-time perception to assist the single measurement, such as GNSS positioning, before it is integrated with other sensors including inertial navigation systems (INS). This paper reviews several 
PASIN, especially on the GNSS positioning. As an example, 
GNSS is aided by the perception of a camera or LiDAR sensors, are conducted in dense urban canyons to validate this novel sensor integration scheme. The proposed PASINS can also be extended to LiDAR- or visual- centered navigation system in the future.

## Problem Addressed

Existing multi-sensor integration systems for Level 4 autonomous vehicles remain heavily challenged in dense urban canyons, where tall buildings and surrounding dynamic objects make GNSS performance strongly dependent on environmental conditions.

## Key Contributions

- Perception aided sensor integrated navigation (PASIN) scheme using real-time onboard perception to assist individual measurements before fusion.
- GNSS NLOS exclusion for dynamic objects aided by camera or LiDAR object detection.
- NLOS correction aided by LiDAR perception and building heights, plus NLOS remodeling during sensor integration.
- Demonstrations of GNSS aided by camera or LiDAR perception conducted in dense urban canyons.

## Conclusions

Leveraging real-time perception to validate and calibrate single-sensor measurements before integration improves GNSS positioning in dense urban canyons, as shown by the presented applications. The scheme can be extended to LiDAR- or visual-centered navigation systems in the future.
