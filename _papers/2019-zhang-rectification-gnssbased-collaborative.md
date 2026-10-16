---
title: Rectification of GNSS-based collaborative positioning using 3D building models in urban areas
authors:
- Guohao Zhang
- Weisong Wen
- Li-Ta Hsu
publisher: GPS Solutions
date: '2019-06-06'
doi: https://doi.org/g8tzc6
image: images/papers/cards/2019-zhang-rectification-gnssbased-collaborative.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/RGCP.pdf
tags:
- GNSS
- 3D model
- urban canyon
citation_id: doi:10.1007/s10291-019-0872-9
---

## Abstract

7 
GNSS collaborative positioning receives great attention because of the rapid development of 
8 vehicle-to-vehicle (V2V) communication. Its current bottleneck is in urban areas. During the 
9 relative positioning using GNSS double difference pseudorange measurements, the multipath 
10 effects and non-line-of-sight (NLOS) reception cannot be eliminated, or even worse, both might 
11 be aggregated. It has been widely demonstrated that 3D map aided (3DMA) GNSS can mitigate 
12 or even correct the multipath and NLOS effects. We, therefore, investigate the potential of aiding 
13 
GNSS collaborative positioning using 3D city models. These models are used in two phases. First, 
14 the building models are used to exclude NLOS measurements at a single receiver using GNSS 
15 shadow matching (SDM) positioning. Second, the models are used together with broadcast 
16 ephemeris data to generate a predicted GNSS positioning error map. Based on this error map, each 
17 receiver will be identified as experiencing healthy or degraded conditions. The receiver 
18 experiencing degraded condition will be improved by the receiver experiencing the healthy 
19 condition, hence the aspect of collaborative positioning. Five low-cost GNSS receivers are used to 
20 conduct experiments. According to the result, the positioning accuracy of the receiver in a deep 
21 urban area improves from 46.2 to 14.4 meters. 
22 
 
23 
Introduction 
24 
One of the bottlenecks of intelligent transportation system (ITS) is the positioning accuracy of 
25 vehicles. To improve the accuracy of positioning, an inertial navigation system (INS) is always 
26 integrated with GNSS (Groves 2013). Due to progress in computing capability, LiDAR is 
27 employed for simultaneous localization and mapping (SLAM) (Levinson et al. 2007). Unlike other 
28 
This is a post-peer-review, pre-copyedit version of an article published in GPS Solutions. The final authenticated version is available online at: http://dx.doi.org/10.1007/s10291-019-0872-9
This is the Pre-Published Version.

2 
 sensors measuring the relative position, the GNSS also provides absolute positions without 
29 accumulated error. Therefore, the GNSS soluti

## Problem Addressed

GNSS collaborative positioning enabled by vehicle-to-vehicle communication is bottlenecked in urban areas, where multipath and NLOS effects are not eliminated, or are even aggregated, in double-difference relative positioning. A way to rectify degraded receivers is needed.

## Key Contributions

- Uses 3D building models with GNSS shadow matching to exclude NLOS measurements at each single receiver
- Generates a predicted GNSS positioning error map from 3D models and broadcast ephemeris data
- Classifies receivers as healthy or degraded based on the predicted error map
- Improves degraded receivers collaboratively using measurements from healthy receivers

## Conclusions

Experiments with five low-cost GNSS receivers show that the positioning accuracy of a receiver in a deep urban area improves from 46.2 to 14.4 meters with the proposed 3D city model aided collaborative positioning. The results demonstrate the potential of 3D map aiding for collaborative GNSS positioning in urban areas.
