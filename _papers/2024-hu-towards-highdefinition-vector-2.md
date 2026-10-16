---
title: 'Towards high-definition vector map construction based on multi-sensor integration for intelligent vehicles: Systems and error quantification'
authors:
- Runzhi Hu
- Shiyu Bai
- Weisong Wen
- Xin Xia
- Li-Ta Hsu
publisher: IET Intelligent Transport Systems
date: '2024-06-22'
doi: https://doi.org/g8t65p
image: images/papers/cards/2024-hu-towards-highdefinition-vector-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/IET_Intelligent_Trans_Sys_2024.pdf
tags:
- HDVM
- Vector Map
- LiDAR
- GNSS
- INS
- intelligent vehicles
repo: https://github.com/ebhrz/HDMap
citation_id: 10.1049/itr2.12524
---

## Abstract

A lightweight, high-definition vector map (HDVM) enables fully autonomous vehicles. However, the generation of HDVM remains a challenging problem, especially in complex urban scenarios. Moreover, numerous factors in the urban environment can degrade the accuracy of HDVM, necessitating a reliable error quantification. To address these chal-lenges, this paper presents an open-source and generic HDVM generation pipeline that integrates the global navigation satellite system (GNSS), inertial navigation system (INS), light detection and ranging (LiDAR), and camera. The pipeline begins by extracting semantic information from raw images using the Swin Transformer. The absolute 3D information of semantic objects is then retrieved using depth from the 3D LiDAR, and pose estimation from GNSS/INS integrated navigation system. Vector information (VI), such as lane lines, is extracted from the semantic information to construct the HDVM. To assess the potential error of the HDVM, this paper systematically quantifies the impacts of two key error sources, segmentation and LiDAR-camera extrinsic parameter error. An error propagation scheme is first formed to illustrate how these errors fundamentally influence the accuracy of the HDVM. The effectiveness of the proposed pipeline is demonstrated through our code available at https://github.com/ebhrz/HDMap. The performance is verified using typical datasets, including indoor garages and complex urban scenarios.

## Problem Addressed

Generating lightweight high-definition vector maps for fully autonomous vehicles remains challenging in complex urban scenarios, and numerous environmental and sensor factors degrade map accuracy without reliable error quantification.

## Key Contributions

- Open-source generic HDVM generation pipeline integrating GNSS, INS, LiDAR, and camera
- Swin Transformer semantic extraction with LiDAR depth and GNSS/INS pose to vectorize both horizontal and vertical map elements
- Error propagation scheme systematically quantifying segmentation and LiDAR-camera extrinsic parameter errors
- Verification on indoor garage and challenging outdoor urban-canyon datasets

## Conclusions

The pipeline achieves sub-meter accuracy in both indoor and outdoor experiments and enables reliable, incremental HDVM generation, with code released to the community. The error quantification model theoretically and experimentally links segmentation and extrinsic calibration errors to final map error. Future work includes vectorizing more elements, improving segmentation and extrinsic calibration, and exploiting crowdsourced data for HD map updates.
