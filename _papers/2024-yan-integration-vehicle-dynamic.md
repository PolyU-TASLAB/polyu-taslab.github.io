---
title: Integration of Vehicle Dynamic Model and System Identification Model for Extending the Navigation Service Under Sensor Failures
authors:
- Penggao Yan
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Intelligent Vehicles
date: '2024-01-01'
doi: https://doi.org/g8t573
image: images/papers/cards/2024-yan-integration-vehicle-dynamic.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/IVDMS.pdf
tags:
- Autonomous  vehicles
- localization
- sensor  failure
- system identification
- vehicle dynamic models
citation_id: doi:10.1109/TIV.2023.3273185
---

## Abstract

Accurate and reliable localization is of great importance for autonomous vehicles (AV). 
Mainstream localization approaches in autonomous vehicles (AV) are limited by the reliability of onboard sensors, which could be vulnerable to sensor failure, such as signal outages of the camera and signal spoofing of the global navigation satellite systems (GNSS). 
Different from these active or passive sensors, the vehicle dynamic model (VDM), which is the application of physical laws to a vehicle in motion, is environmentally independent and is capable of providing vehicle motion estimation continuously. 
However, the performance of the VDM-based motion estimation is dominated by the accuracy of the system dynamics model. To tackle this issue, this study proposes a sensor-free localization method VDM-SI by integrating system identification into the design of vehicle dynamic models (VDM). A system identification process based on low-order process models is proposed to identify the system dynamics of the AV, where the identified system responses are taken as the control input of VDM to estimate the vehicular positioning. The localization experiments in two scenarios show that the mean absolute translation error of 
VDM-SI can be reduced by 70% compared to conventional VDM methods. In addition, VDM-SI is experimentally proven to improve the localization performance of sensor fusion-based localization systems with high noise levels. Furthermore, in the application of re-localization after sensors fail and recover, 
VDM-SI shows strength in enhancing the security of AVs in extreme conditions.

## Problem Addressed

Autonomous vehicle localization relies on onboard sensors vulnerable to failures such as camera signal outages and GNSS spoofing, while the environment-independent vehicle dynamic model is limited by the accuracy of system dynamics modeling.

## Key Contributions

- VDM-SI sensor-free localization method integrating system identification into vehicle dynamic model design
- Low-order process-model system identification capturing powertrain and steering dynamics as VDM control inputs
- Reduces mean absolute translation error by 70% compared with conventional VDM methods
- Improves fusion-based localization under high sensor noise and re-localization after sensor failure recovery

## Conclusions

Localization experiments in two scenarios show that the mean absolute translation error of VDM-SI is reduced by 70% compared to conventional VDM methods. VDM-SI also improves fusion-based localization under high noise levels and provides more accurate initial guesses for re-localization after sensors recover, enhancing the security of AVs in extreme conditions.
