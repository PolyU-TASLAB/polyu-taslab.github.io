---
title: 'Enhancing GNSS Positioning Accuracy for Road Monitoring Systems: A Factor Graph Optimization Approach Aided by Geospatial Information'
authors:
- Yihan Zhong
- Runzhi Hu
- Xiwei Bai
- Xingxing Li
- Li-Ta Hsu
- Weisong Wen
publisher: IEEE Transactions on Instrumentation and Measurement
date: '2024-01-01'
doi: https://doi.org/g8t65k
image: images/papers/cards/2024-zhong-enhancing-gnss-positioning-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Enhancing_GNSS_Positioning_Accuracy_for_Road_Monitoring_Systems_A_Factor_Graph_Optimization_Approach_Aided_by_Geospatial_Information.pdf
tags:
- Factor graph optimization
- FGO
- geospatial information
- global navigation satellite system
- GNSS
- map
- navigation
citation_id: 10.1109/TIM.2024.3369156
---

## Abstract

The global navigation satellite system (GNSS) is one of the most popular solutions to localize potential road cracks. Unfortunately, the accurate positioning of the GNSS in urban environments presents a significant challenge due to complex signal blockage and reflection phenomena. To tackle this, we propose a method that enhances GNSS positioning accuracy, particularly suited for the intricate layouts of urban canyons. Our approach integrates the prior map with lane line information into the factor graph optimization (FGO) algorithm, effectively mitigating the impacts of multipath effects and non-line-of-sight (NLOS). However, the poor accuracy of the initial guess from the GNSS positioning can easily lead to incorrect lane matching which is one of the main challenges of lane matching in highly urbanized areas. To fill this gap, this article proposes to use the switchable factor to model the potential incorrect lane matching by leveraging the redundancy of lane information across multiepochs. This article verified the effectiveness of this methodology using two datasets from the dense urban environment of Hong
Kong, collected using the low-cost automobile level receiver, and compared the results with conventional methods. Our findings affirm that integrating the FGO-based GNSS positioning system with map information significantly boosts positioning accuracy, demonstrating the robustness of our approach.

## Problem Addressed

Accurate GNSS positioning in urban environments is challenged by complex signal blockage and reflection, which limits applications such as localizing road cracks. Map-aided methods face a further problem: poor GNSS initial guesses easily lead to incorrect lane matching in highly urbanized areas.

## Key Contributions

- FGO-based GNSS positioning with a map-matching factor using manually marked lane information from Google Earth
- Multi-epoch lane matching model leveraging redundancy of lane information across epochs
- Switchable factor modeling potential incorrect lane matching to mitigate mis-lane-matching errors
- Validation on two dense-urban Hong Kong datasets with a low-cost automobile-level receiver

## Conclusions

The proposed FGO-Matching and FGO-Switch methods achieved superior positioning accuracy compared with conventional FGO on both challenging urban datasets, with computation time increasing by about 120% yet remaining acceptable for practical road-monitoring applications. FGO-Switch is less robust than FGO-Matching under bad initial guesses, since erroneous map matching propagates through the estimation. Future work includes more constellations and frequencies, carrier-phase measurements, IMU integration, and V2X data.
