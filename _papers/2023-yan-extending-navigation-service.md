---
title: 'Extending Navigation Service under Sensor Failures: An Approach by Integrating System Identification and Vehicle Dynamic Model'
authors:
- Penggao Yan
- Li-Ta Hsu
- Weisong Wen
publisher: 2023 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2023-04-24'
doi: https://doi.org/g8t576
image: images/papers/cards/2023-yan-extending-navigation-service.jpg
citation_id: doi:10.1109/plans53410.2023.10140089
---

## Abstract

Localization plays a vital role in various autonomous systems, providing essential information for perception and planning tasks. 
However, mainstream localization methods are based on the sensors approach, which is vulnerable in some extreme conditions where sensors probably fail in a short period, such as the camera-based visual positioning. This study proposes a sensor-free localization method by integrating vehicle dynamic models and an online system identification module. First, a system identification process is conducted online to identify the system dynamics of the powertrain system and the steering system of the autonomous vehicle. Then, the identified system responses are taken as the control input of the vehicle dynamic model to produce the positioning results. The simulated experiments show that the proposed method achieves better positioning performance than the conventional vehicle dynamic models. In addition, the extendibility of the proposed method is explored by fusing it with extra sensors based on the extended Kalman filter (EKF). Furthermore, the navigation ability of the proposed method without sensors is also examined along a trajectory of 
140 meters. The proposed method successfully accomplishes the navigation task without any collisions, demonstrating the effectiveness in enhancing the security of autonomous systems with navigation needs when sensors fail in extreme conditions.

## Problem Addressed

Mainstream localization methods depend on sensors that are vulnerable to short-term failures under extreme conditions, leaving autonomous systems without positioning exactly when it is most needed.

## Key Contributions

- Sensor-free localization method integrating vehicle dynamic models with online system identification
- Online identification of powertrain and steering system dynamics using ARX models updated by RLS
- Identified system responses used as control inputs of the vehicle dynamic model to produce positioning
- Extended Kalman filter fusion with extra sensors demonstrating extendibility

## Conclusions

The proposed VDM-OnSI method reduces absolute trajectory error by more than 77% compared with the conventional vehicle dynamic model in Gazebo simulation. Fusion with extra sensors via EKF further boosts positioning performance, and VDM-OnSI is the only tested method that completes the 140-meter navigation path without collisions when sensors fail. It can serve as a safety countermeasure keeping autonomous vehicles operating during short sensor outages.
