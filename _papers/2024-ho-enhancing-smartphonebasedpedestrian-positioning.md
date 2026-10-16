---
title: 'Enhancing Smartphone-based Pedestrian Positioning: Using Factor Graph Optimization with Indoor/Outdoor Detection for 3DMA GNSS/Visual-Inertial State Estimation'
authors:
- Hiu-Yi Ho
- Hoi-Fung Ng
- Weisong Wen
- Yanlei Gu
- Li-Ta Hsu
publisher: Journal of Data Science and Intelligent Systems
date: '2024-10-31'
doi: https://doi.org/g8t4vb
image: images/papers/cards/2024-ho-enhancing-smartphonebasedpedestrian-positioning.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Enhancing_Smartphone_based.pdf
tags:
- FGO
- pedestrian positioning
- smartphone
- sensor integration
- IO
- VINS
- 3DMA GNSS
citation_id: doi:10.47852/bonviewJDSIS42022961
---

## Abstract

This paper explores the pervasive challenges of pedestrian positioning using smartphones in densely populated urban environments where global navigation satellite system (GNSS) signals are inaccessible, for example, in indoor areas. Existing sensor-based positioning methods, such as inertial navigation systems, GNSS, and visual-inertial odometry (VIO), suffer from inherent restrictions that compromise the accuracy and reliability of the positioning performance. An approach based on machine learning is proposed to address these limitations, employing the support vector machine (SVM) algorithm to accurately distinguish indoor/outdoor (IO) based on the measurement of GNSS. The proposed approach in this study seamlessly incorporates 3D mapping aided (3DMA) GNSS measurements and localized estimations derived by VIO via factor graph optimization (FGO), complemented by an IO detection switch, to achieve accurate pose estimation and effectively eliminate global drift. The system’s effectiveness and robustness are rigorously assessed through comprehensive extensive real-life experiments, with an average reduction of 4 meters, leading to noteworthy and statistically significant findings.

## Problem Addressed

Smartphone-based pedestrian positioning in densely populated urban environments is unreliable where GNSS signals are inaccessible, such as indoor areas. Existing sensor-based methods including inertial navigation, GNSS, and visual-inertial odometry suffer inherent restrictions that compromise positioning accuracy and reliability.

## Key Contributions

- SVM-based machine learning approach distinguishing indoor/outdoor environments from GNSS measurements
- Factor graph optimization framework fusing 3DMA GNSS measurements with visual-inertial odometry local estimations
- Indoor/outdoor detection switch enabling accurate pose estimation and global drift elimination
- Extensive real-life experiments demonstrating an average 4-meter positioning error reduction

## Conclusions

Comprehensive real-life experiments demonstrate that fusing 3DMA GNSS and VIO via factor graph optimization with indoor/outdoor detection achieves accurate pose estimation and effectively eliminates global drift. The system achieves an average positioning error reduction of 4 meters, with statistically significant findings.
