---
title: Integration of Vehicle Dynamic Model and System Identified Model for Navigation in Autonomous Mobile Robots
authors:
- Penggao Yan
- Li-Ta Hsu
- Weisong Wen
publisher: The International Technical Meeting of the The Institute of Navigation
date: '2023-02-13'
doi: https://doi.org/g8t6km
image: images/papers/cards/2023-yan-integration-vehicle-dynamic.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/ITM_fullpaper-submit_v3_1.pdf
tags:
- Autonomous Mobile Robots
- vehicle dynamic models
citation_id: doi:10.33012/2023.18637
---

## Abstract

Vehicle dynamic models are the basis of various navigation algorithms in autonomous mobile robots (AMRs), describing the vehicle motion purely by physical law. However, its simplifications on the system complexity and assumptions on the environments prevent it from providing accurate positioning results. Instead of introducing sensors to correct its pose estimation error, this study aims to utilize the endogenous information of AMRs to improve positioning performance. A system identification process is conducted to identify the system dynamics of the plants in AMRs, where the identified system dynamics is integrated into the development of vehicle dynamic models. Experiments on two scenarios show that the proposed method achieves better positioning results and navigation performance than conventional vehicle dynamic models, demonstrating the potential of endogenous information in AMRs to enhance their ability on navigation tasks. In addition, this study contributes to the literature that builds the bridge between system identification and navigation in AMRs.

## Problem Addressed

Vehicle dynamic models simplify system complexity and rely on environmental assumptions, preventing accurate positioning, while typical error corrections depend on introducing additional sensors.

## Key Contributions

- System identification of autonomous mobile robot plant dynamics integrated into vehicle dynamic model development
- Use of endogenous information, namely control commands and measured responses, to compensate pose estimation
- Loosely coupled integration applicable to different vehicle dynamic models, verified on two datasets

## Conclusions

Experiments in two scenarios show that the proposed VDM-SI method significantly outperforms conventional vehicle dynamic models in positioning and navigation performance. Thanks to its loosely coupled property, the method can be applied to different VDMs and integrated into mainstream sensor-fusion navigation architectures. The offline identification cannot capture time-varying system dynamics, motivating future online system identification and fusion with LiDAR or camera sensors.
