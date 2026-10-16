---
title: Roadside Infrastructure assisted LiDAR/Inertial-based Mapping for Intelligent Vehicles in Urban Areas
authors:
- Feng Huang
- Hang Chen
- Alpamys Urtay
- Dongzhe Su
- Weisong Wen
- Li-Ta Hsu
publisher: 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC)
date: '2023-09-24'
doi: https://doi.org/g8t658
image: images/papers/cards/2023-huang-roadside-infrastructure-assisted-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Roadside_Infrastructure_assisted_LiDAR_Inertial-based_Mapping_for_Intelligent_Vehicles_in_Urban_Areas.pdf
- type: website
  link: https://sites.google.com/view/v2x-cooperative-navigation
tags:
- Roadside Infrastructure
- LiDAR
- mapping
- localization
- V2X
- FGO
citation_id: 10.1109/ITSC57777.2023.10422552
---

## Abstract

Vehicle-infrastructure cooperation is an emerging technology towards fully autonomous driving. LiDAR/Inertial odometry (LIO) based on onboard sensors can provide precise state estimation and mapping locally but is subjected to drift accumulation over time. Limited by the level of intelligence from a single intelligent vehicle, the cellular vehicle-to-everything (CV2X) opened a new window for the realization of fully autonomous driving. How can the roadside intelligent infrastructure assist intelligent vehicles in mapping and localization? In this paper, we propose a roadside infrastructure (RSI) assisted LIO for reliable odometry and mapping, which benefits from the global constraint provided by RSIs. 
Specifically, RSI estimates the coarse vehicle state in the RSIbased LiDAR point cloud using a deep learning-based method. 
Based on the initial guess of the positioning state and the point cloud provided by the RSI, our system extracts a local LiDAR map that can refine registration with the RSI LiDAR point cloud. The accurately registered state then served as the global constraint in the graph-based optimization. To evaluate our approach, we collect the multi-view RSI and vehicle sensor data in the Hong Kong representative C-V2X testbed. Experimental results show that the absolute positioning accuracy of the proposed RSI-assisted LIO was significantly improved by 
84.3%. To benefit the research community, the data of this work is available on our project page3.

## Problem Addressed

Onboard LiDAR/inertial odometry drifts over time and single-vehicle sensing is limited in complex urban scenarios; how roadside intelligent infrastructure can assist vehicles in mapping and localization remains an open question.

## Key Contributions

- Roadside infrastructure (RSI) assisted LIO exploiting global constraints provided by RSIs
- Deep learning-based coarse vehicle state estimation in the RSI LiDAR point cloud
- Local map extraction and refined registration against the RSI point cloud used as a global constraint in graph optimization
- Multi-view RSI and vehicle sensor data collected in the Hong Kong C-V2X testbed and released publicly

## Conclusions

Experiments in the Hong Kong C-V2X testbed show the RSI-assisted LIO significantly improves absolute positioning accuracy by 84.3% and outperforms the state-of-the-art method. Future work includes evaluation in more urban scenarios, multi-RSI calibration, GNSS NLOS detection using the built maps, and GNSS integration when RSI is unavailable.
