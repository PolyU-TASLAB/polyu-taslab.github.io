---
title: Adaptive Multi-Sensor Integrated Navigation System Aided by Continuous Error Map from RSU for Autonomous Vehicles in Urban Areas
authors:
- Feng Huang
- Weisong Wen
- Guohao Zhang
- Dongzhe Su
- Li-Ta Hsu
publisher: 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)
date: '2023-09-24'
doi: https://doi.org/g8t659
image: images/papers/cards/2023-huang-adaptive-multisensor-integrated-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Adaptive_Multi-Sensor_Integrated_Navigation_System_Aided_by_Continuous_Error_Map_from_RSU_for_Autonomous_Vehicles_in_Urban_Areas.pdf
- type: website
  link: https://sites.google.com/view/v2x-cooperative-navigation
tags:
- C-V2X
- GNSS
- roadside units
- Continuous Error Map
citation_id: 10.1109/ITSC57777.2023.10422216
---

## Abstract

There has been a widespread study on multi-sensor integration to achieve precise and robust odometry for autonomous vehicles (AVs) in urban areas. LiDAR odometry and visual odometry can be affected by structureless scenarios and numerous dynamic objects. GNSS positioning can be degenerated due to the multipath and non-line-of-sight signals by buildings. Therefore, selecting appropriate weighing for heterogeneous sensors is a challenge for multi-sensor fusion. With the advancements in cellular vehicle-to-everything (C-V2X) and intelligent roadside units (RSUs), vehicles and the RSUs can collaborate to deliver reliable service. Inspired by this, this paper investigates continuous error maps for available sensors under different time conditions (noon, sunset, and night) to improve the positioning performance of surrounding AVs in complex urban environments. In particular, this paper presents an error-map-aided multi-sensor integrated system, which benefits from the error information collected by a sensor-rich AV. Then the error information is uploaded to the RSUs which is then distributed to the AVs. A smaller weight is assigned if a larger error is queried from the error map. To validate our approach, experiments were performed using the realistic CARLA simulator and our self-developed GNSS RUMS simulator. To benefit the research community, we open-sourced the implementation on our project page33https://sites.google.com!view/v2x-cooperative-navigation..

## Problem Addressed

LiDAR and visual odometry degrade in structureless or dynamic scenes and GNSS suffers multipath and NLOS in urban areas, making appropriate weighting of heterogeneous sensors a key challenge for multi-sensor fusion.

## Key Contributions

- Continuous error map estimation for vehicle-infrastructure cooperation under different time conditions (noon, sunset, night)
- Error-map-aided adaptive multi-sensor integrated system exploiting prior error information shared via RSUs
- Adaptive weighting assigning smaller weights where larger errors are queried from the error map
- Validation with the CARLA simulator and a self-developed GNSS RUMS simulator; implementation open-sourced

## Conclusions

Sensor error maps can be deployed as an additional layer on top of high-definition maps for V2X applications. Realistic simulations demonstrate that the multi-sensor integrated system benefits from prior error information obtained from error map estimation. Future work includes sensor sharing among multiple vehicles and RSUs and evaluation in the Hong Kong C-V2X testbed with industrial partner ASTRI.
