---
title: 'Fisheye Image/GNSS Based Multimodal Learning for GNSS NLOS/Multipath Correction: Enhancing Vehicle Positioning in Urban Canyons for Autonomous Driving'
authors:
- Runzhi Hu
- Jian Liu
- Yihan Zhong
- Weisong Wen
- Ming Xia
- Yulong Huang
publisher: IEEE Transactions on Vehicular Technology
date: '2026-06-01'
doi: https://doi.org/hccr38
image: images/papers/cards/2026-hu-fisheye-imagegnss-multimodal.jpg
citation_id: doi:10.1109/TVT.2025.3639402
---

## Abstract

The great development of smart urban transportation has led to the booming of the autonomous vehicle industry. Society places great expectations on autonomous driving to enhance safety and efficiency in transportation systems, particularly in challenging environments like urban canyons where precise positioning is crucial. Global Navigation Satellite System (GNSS) positioning modules are the crucial element of autonomous vehicles for absolute positioning. However, the GNSS pseudorange suffers significant biases and degradation due to the multipath and nonline-of-sight (NLOS) errors caused by tall buildings that widely exist in urban canyons. To improve GNSS positioning accuracy in harsh urban canyons, this paper introduces a deep multimodal learning-based approach to correct distorted pseudorange measurements. The vision features of the environment captured by the camera are integrated to form the multimodal network with GNSS measurements. Meanwhile, positional encoding (PE) is proposed to fuse the image features and the satellite position information in a higher-dimensional space. The biases are outputted by the network and are used for improved positioning. Compared to existing solutions, extensive test results show that the proposed method achieves improved positioning accuracy ranging from 12% to 20%. Moreover, the proposed method achieves epochwise pseudorange correction in just 0.5s on Jetson Orin Nano, meeting real-time requirements and demonstrating high practicality. This paper also opensources a dataset under varying time, satellite distributions, and lighting conditions with accurate NLOS labels. We release this dataset to the GNSS and deep learning communities, targeting its adoption as a standard benchmark for NLOS classification and pseudorange bias correction.

## Problem Addressed

GNSS pseudorange measurements in urban canyons suffer severe multipath and non-line-of-sight (NLOS) biases caused by tall buildings, degrading absolute positioning for autonomous vehicles. Simply excluding NLOS signals is counterproductive under limited satellite visibility, where the resulting poor geometry makes the position solution unreliable or even unsolvable.

## Key Contributions

- Deep multimodal network fusing fisheye camera vision features with GNSS measurements for pseudorange bias correction
- Positional encoding that fuses image features and satellite position information in a higher-dimensional space
- Epoch-wise pseudorange correction in 0.5 s on Jetson Orin Nano, meeting real-time requirements
- Open-source dataset spanning varied time, satellite distributions, and lighting conditions with accurate NLOS labels

## Conclusions

The multimodal method improved positioning accuracy by 12.2%, 19.1%, 20.1%, and 18.3% on the KLT1203, KLT2-209, KLT3-404, and KLT3-649 datasets respectively, outperforming conventional techniques. The network runs in real time on embedded hardware, demonstrating high practicality. The released dataset, covering diverse temporal, geometric, and illumination conditions, is intended as a benchmark for NLOS classification and pseudorange bias correction. Future work includes fusing LiDAR point clouds or HD-map models for low-illumination scenarios.
