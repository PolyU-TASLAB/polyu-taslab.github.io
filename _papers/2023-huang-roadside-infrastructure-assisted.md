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
image: images/papers/cards/2023-huang-roadside-infrastructure-assisted.jpg
citation_id: doi:10.1109/itsc57777.2023.10422552
---

## Abstract

Vehicle-infrastructure cooperation is an emerging technology towards fully autonomous driving. LiDAR/Inertial odometry (LIO) based on onboard sensors can provide precise state estimation and mapping locally but is subjected to drift accumulation over time. Limited by the level of intelligence from a single intelligent vehicle, the cellular vehicle-to-everything (CV2X) opened a new window for the realization of fully autonomous driving. How can the roadside intelligent infrastructure assist intelligent vehicles in mapping and localization? In this paper, we propose a roadside infrastructure (RSI) assisted LIO for reliable odometry and mapping, which benefits from the global constraint provided by RSIs. 
Specifically, RSI estimates the coarse vehicle state in the RSIbased LiDAR point cloud using a deep learning-based method. 
Based on the initial guess of the positioning state and the point cloud provided by the RSI, our system extracts a local LiDAR map that can refine registration with the RSI LiDAR point cloud. The accurately registered state then served as the global constraint in the graph-based optimization. To evaluate our approach, we collect the multi-view RSI and vehicle sensor data in the Hong Kong representative C-V2X testbed. Experimental results show that the absolute positioning accuracy of the proposed RSI-assisted LIO was significantly improved by 
84.3%. To benefit the research community, the data of this work is available on our project page3.

## Problem Addressed

LiDAR/inertial odometry provides precise local state estimation and mapping but is subject to drift accumulation over time, and a single intelligent vehicle has limited perception intelligence in complex urban scenarios.

## Key Contributions

- Roadside infrastructure-assisted LiDAR/inertial odometry framework providing global constraints for mapping
- Deep learning-based coarse vehicle state estimation within the infrastructure LiDAR point cloud
- Local LiDAR map extraction and refined registration against the roadside point cloud
- Graph-based optimization using the accurately registered state as a global constraint

## Conclusions

Evaluated on multi-view roadside and vehicle sensor data collected in the Hong Kong C-V2X testbed, the proposed RSI-assisted LIO improves absolute positioning accuracy by 84.3% over the state-of-the-art method. Future work includes evaluation in more challenging urban scenarios, calibration of multiple roadside infrastructures, and GNSS NLOS detection using the resulting point cloud maps.
