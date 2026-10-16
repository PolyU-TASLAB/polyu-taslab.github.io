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
image: images/papers/cards/2023-huang-adaptive-multisensor-integrated.jpg
citation_id: doi:10.1109/itsc57777.2023.10422216
---

## Abstract

There has been a widespread study on multi-sensor integration to achieve precise and robust odometry for autonomous vehicles (AVs) in urban areas. LiDAR odometry and visual odometry can be affected by structureless scenarios and numerous dynamic objects. GNSS positioning can be degenerated due to the multipath and non-line-of-sight signals by buildings. Therefore, selecting appropriate weighing for heterogeneous sensors is a challenge for multi-sensor fusion. 
With the advancements in cellular vehicle-to-everything (C-V2X) and intelligent roadside units (RSUs), vehicles and the RSUs can collaborate to deliver reliable service. Inspired by this, this paper investigates continuous error maps for available sensors under different time conditions (noon, sunset, and night) to improve the positioning performance of surrounding AVs in complex urban environments. In particular, this paper presents an error-mapaided multi-sensor integrated system, which benefits from the error information collected by a sensor-rich AV. Then the error information is uploaded to the RSUs which is then distributed to the AVs. A smaller weight is assigned if a larger error is queried from the error map. To validate our approach, experiments were performed using the realistic CARLA simulator and our selfdeveloped GNSS RUMS simulator. To benefit the research community, we open-sourced the implementation on our project page3.

## Problem Addressed

Multi-sensor fusion for autonomous vehicles in urban areas is challenged by degraded LiDAR and visual odometry in structureless or dynamic scenes and by GNSS degradation from multipath and NLOS signals. Selecting appropriate weights for heterogeneous sensors is therefore difficult.

## Key Contributions

- Continuous error map estimation for vehicle-infrastructure cooperation under different time conditions
- Error-map-aided adaptive multi-sensor integrated system that downweights sensors with larger queried errors
- Error information collected by a sensor-rich vehicle, uploaded to roadside units, and distributed to surrounding vehicles
- Open-sourced implementation evaluated with CARLA and a self-developed GNSS RUMS simulator

## Conclusions

Sensor error maps can be deployed as an additional layer on top of the high-definition map for V2X applications in urban areas. Realistic simulation demonstrates that the multi-sensor integrated system benefits from prior error information obtained through error map estimation. Future work includes sensor sharing among multiple vehicles and roadside units and evaluation in the Hong Kong C-V2X testbed.
