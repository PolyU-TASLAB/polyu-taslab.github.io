---
title: Integrity Monitoring for GNSS Positioning Via Factor Graph Optimization in Urban Canyons
authors:
- Weisong Wen
- Qian Meng
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2021-10-13'
doi: https://doi.org/g8t45g
image: images/papers/cards/2021-wen-integrity-monitoring-gnss.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Wen_Integrity_Monitoring_Gnss.pdf
tags:
- GNSS
- FGO
- Failure detection and exclusion
- urban canyon
citation_id: doi:10.33012/2021.18157
---

## Abstract

Fault detection and exclusion (FDE) is significant for integrity monitoring of GNSS positioning for autonomous systems with navigation requirements. Moreover, the urban canyon scenario introduces additional challenges to the existing FDE for integrity monitoring, causing missed or false alarms, due to the significantly increased percentage of fault measurements. This paper proposed a sliding window aided FDE for GNSS positioning based on factor graph optimization (FGO) to alleviate these key issues. Different from the existing snapshot-based and the sequential-based (e.g. Extended Kalman filter) integrity monitoring methods where only the current or two consecutive epochs of measurements are considered in the FDE process, the proposed method in this paper improves the measurement redundancy with the help of the sliding window structure. Meanwhile, the GNSS measurements inside the sliding window are considered multiple times which enables the reconsideration of fault measurements. 
Moreover, the FGO employs multiple iterations and re-linearizations which improves the initial guess of the state estimation for 
FDE. The effectiveness of the proposed method is verified through a challenging dataset collected in urban canyons of Hong 
Kong using automobile-level low-cost GNSS receivers.

## Problem Addressed

Urban canyons sharply increase the percentage of faulty GNSS measurements, causing missed or false alarms in existing fault detection and exclusion (FDE) methods for integrity monitoring. Snapshot and sequential EKF-based methods consider only the current or two consecutive epochs.

## Key Contributions

- Sliding-window aided FDE based on factor graph optimization increases measurement redundancy.
- Measurements inside the window are used multiple times, enabling reconsideration of faulty measurements.
- Multiple iterations and re-linearizations in FGO improve the initial state guess for FDE.
- Evaluated on a challenging Hong Kong urban canyon dataset with low-cost automobile-level receivers.

## Conclusions

The sliding-window FDE improves GNSS positioning accuracy on the evaluated urban canyon dataset, and the improvement grows with increased window size. Future work includes reusing prior outlier measurements across windows, computing integrity protection levels, and employing additional sensors to detect GNSS outliers.
