---
title: Towards Accurate Vehicle-to-Pedestrian Relative Positioning Aided by Inter-Frame and Inter-Agent GNSS Measurement Collaboration Using Factor Graph Optimization for Smart Summon
authors:
- Yihan Zhong
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2023-10-05'
doi: https://doi.org/hcc4r5
citation_id: doi:10.33012/2023.19471
---

## Abstract

Accurate relative positioning is of great importance for the smart summon (SS) application launched by Tesla autonomous driving vehicles (ADV), where the ADV could approach the user with a smartphone automatically. In particular, meters level relative positioning accuracy is expected by the SS application. The existing ultra-wideband (UWB) or the dedicated short-range communication (DSRC) are popular but are limited by the external infrastructure. The global navigation satellite system (GNSS) Real-Time Kinematic (RTK) can provide centimeter-level positioning accuracy, but it relies on the presence of reference stations. The GNSS double-difference (DD) based relative positioning is a promising replacement that can provide sub-meter level relative positioning accuracy in open areas. This is mainly due to systematic error elimination by using the DD operation. However, the DD operation is mainly done within the two users in the same time epoch (epoch-to-epoch based) to update the state using the filtering, such as the extended Kalman filter. In fact, the neighboring users share similar atmosphere errors within a short period. Inspired by this, this paper proposes to encode the raw GNSS pseudorange measurements into a factor graph model and perform the “dense” double difference operation to the raw measurements within a short period. As a result, the strong time correlation involved in the raw GNSS measurements can be effectively explored. In particular, a dense factor graph model can be constructed based on the factors derived from the GNSS Doppler, pseudorange measurements, and the relative constraints derived from the “dense” double-difference measurements. The effectiveness of the proposed “dense” double-difference model is validated using the dataset collected in sub-urban scenarios by comparing it with the conventional epoch-to-epoch-based method.

## Problem Addressed

Smart summon applications need meter-level vehicle-to-pedestrian relative positioning, but UWB and DSRC require external infrastructure, GNSS RTK depends on reference stations, and epoch-to-epoch double-difference filtering ignores the time correlation shared by neighboring receivers.

## Key Contributions

- Factor graph model encoding raw GNSS pseudorange measurements for vehicle-to-pedestrian relative positioning
- Dense double-difference operation applied to raw measurements over a short period to exploit strong time correlation
- Dense factor graph combining GNSS Doppler factors, pseudorange factors, and dense double-difference relative constraints

## Conclusions

Evaluated on datasets collected in sub-urban scenarios, the proposed dense double-difference factor graph model improves relative positioning compared with the conventional epoch-to-epoch-based method, confirming that exploiting inter-epoch measurement correlation benefits vehicle-to-pedestrian relative positioning.
