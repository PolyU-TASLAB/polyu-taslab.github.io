---
title: Trajectory Smoothing Using GNSS/PDR Integration via Factor Graph Optimization in Urban Canyons
authors:
- Yihan Zhong
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Internet of Things Journal
date: '2024-07-15'
doi: https://doi.org/g8t54w
image: images/papers/cards/2024-zhong-trajectory-smoothing-using.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/YihanZhong2024Trajectory_Smoothing_Using_GNSS_PDR_Integration_via_Factor_Graph_Optimization_in_Urban_Canyons.pdf
tags:
- Factor graph optimization
- Global navigation satellite system
- Pedestrian dead reckoning
citation_id: doi:10.1109/JIOT.2024.3396360
---

## Abstract

Smooth and accurate global navigation satellite system (GNSS) positioning for pedestrians in urban canyons is still a challenge due to the multipath effects and the nonlineof-sight (NLOS) receptions caused by the reflections from surrounding buildings. Factor graph optimization (FGO) attracts more and more attention in GNSS society for improving urban
GNSS positioning by effectively exploiting the measurement redundancy from historical information to resist the outlier measurements. Unfortunately, the FGO-based GNSS standalone positioning is still challenged in highly urbanized areas. As an extension of the previous FGO-based GNSS positioning method, the potential of the pedestrian dead reckoning (PDR) model in
FGO to improve the GNSS standalone positioning performance in urban canyons is exploited in this article. Specifically, the relative motion of the pedestrian is estimated based on the raw acceleration measurements from the onboard smartphone inertial measurement unit (IMU) via the PDR algorithm. Then, the raw
GNSS pseudorange, Doppler measurements, and relative motion from PDR are integrated using the FGO. Given the context of pedestrian navigation with a small acceleration most of the time, a novel soft motion model is proposed to smooth the states involved in the factor graph model. This article verified the effectiveness of employing the PDR model in FGO step-by-step through two data sets collected in dense urban canyons of Hong Kong using smartphone-level GNSS receivers. The comparison between the conventional extended Kalman filter, several existing methods, and FGO-based integration is presented. The proposed method shows better results than the conventional FGO method in all test data sets, with at least a 22% decrease in the mean value of the positioning error. The proposed method reduces the average localization error from 31.64 m to 18.51 m in a deep urban area.

## Problem Addressed

GNSS positioning for pedestrians in urban canyons suffers from multipath and NLOS receptions caused by reflections from surrounding buildings, and FGO-based GNSS standalone positioning remains challenged in highly urbanized areas.

## Key Contributions

- Tightly coupled FGO-based GNSS/PDR integration connecting consecutive epochs with pseudorange and Doppler measurements
- PDR-derived relative motion from smartphone IMU providing additional relative constraints between consecutive states
- Soft motion model exploiting low pedestrian acceleration for trajectory smoothing and GNSS outlier resistance
- Progressive validation of PDR and soft-motion factors on two Hong Kong urban canyon datasets

## Conclusions

The proposed method outperforms conventional FGO on all test datasets with at least a 22% decrease in mean positioning error, reducing the average localization error from 31.64 m to 18.51 m in a deep urban area. Applying the soft motion model factor further helps resist potential GNSS outliers.
