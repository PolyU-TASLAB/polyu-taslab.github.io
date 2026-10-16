---
title: A novel GNSS based V2V cooperative localization to exclude multipath effect using consistency checks
authors:
- Guohao Zhang
- Weisong Wen
- Li-Ta Hsu
publisher: 2018 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2018-04-01'
doi: https://doi.org/g8tzc7
image: images/papers/cards/2018-zhang-novel-gnss-v2v.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/ANGV.pdf
tags:
- GNSS
- multipath
- NLOS
- V2V
- cooperative localization
- autonomous driving
- urban
- double difference
citation_id: doi:10.1109/PLANS.2018.8373540
---

## Abstract

Global Navigation Satellite System (GNSS) is essential for autonomous driving by providing absolute positioning solutions. However, the performance of GNSS measurement is significantly degraded in urban areas, due to the severe multipath and non-line-of-sight (NLOS) effects. To ensure the operation safety of autonomous driving applications, the GNSS localization performance is required to improve. In this study, a novel vehicle-to-vehicle (V2V) based cooperative localization algorithm with double-layers of consistency check (CC) is developed. GNSS pseudorange measurements of the ego-vehicle and surrounding vehicles conduct the first-layer of CC independently to exclude the multipath-biased measurement and obtaining their absolute positions. Then, the survived GNSS measurement and the absolute positions of each vehicles are shared in between, and further applied with double difference (DD) technique to obtain an accurate relative position between the surrounding vehicles. The second-layer CC is conducted during the GNSS DD-based relative positioning, to exclude the multipath and NLOS effects more comprehensively. Finally, the absolute and relative positions of surrounding vehicles are cooperated to optimize the final position of all participating vehicles. By the both simulation and real experimental results, the proposed algorithm is able to mitigate the multipath effect and significantly improve the accuracy of GNSS localization solutions to fulfill the safety requirements for autonomous driving.

## Problem Addressed

GNSS localization is significantly degraded in urban areas by severe multipath and NLOS effects, threatening the safety of autonomous driving. Single-receiver positioning alone cannot meet the required accuracy in such environments.

## Key Contributions

- Develops a vehicle-to-vehicle cooperative localization algorithm with double-layer consistency checks
- Applies a first-layer consistency check per vehicle to exclude multipath-biased pseudorange measurements
- Shares surviving measurements and applies double difference with a second-layer consistency check
- Optimizes final positions of all participating vehicles by cooperating absolute and relative positions

## Conclusions

Simulation and real experimental results show the double-layer consistency check effectively excludes multipath-affected measurements and the double difference technique eliminates systematic errors. The proposed algorithm significantly improves localization accuracy to within 10 meters even in dense urban environments. Future work will address partially shared measurements, multi-constellation receivers, and further accuracy improvements.
