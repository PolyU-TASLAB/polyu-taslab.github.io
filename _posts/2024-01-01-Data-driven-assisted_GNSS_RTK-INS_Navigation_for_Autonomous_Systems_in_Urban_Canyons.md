---
title: Data-driven-assisted GNSS RTK/INS Navigation for Autonomous Systems in Urban Canyons 
subtitle: AI-aided Navigation
# author: XNG
image: images/project/Data_driven_structure.png
tags: GNSS Positioning, NLOS/Multipath Correction, Autonomous Driving, Positional Encoding, Multimodal Network, Vision Feature
order: 
---
## Abstract

The great development of smart urban transportation has led to the booming of the autonomous vehicle industry. Society places great expectations on autonomous driving to enhance safety and efficiency in transportation systems, particularly in challenging environments like urban canyons where precise positioning is crucial. Global Navigation Satellite System (GNSS) positioning modules are the crucial element of autonomous vehicles for absolute positioning. However, the GNSS pseudorange suffers significant biases and degradation due to the multipath and non-line-of-sight (NLOS) errors caused by tall buildings that widely exist in urban canyons. To improve GNSS positioning accuracy in harsh urban canyons, this paper introduces a deep multimodal learning-based approach to correct distorted pseudorange measurements. The vision features of the environment captured by the camera are integrated to form the multimodal network with GNSS measurements. Meanwhile, positional encoding (PE) is proposed to fuse the image features and the satellite position information in higher-dimensional space. The biases are outputted by the network and are used for improved positioning. Compared to existing solutions, extensive test results show that the proposed method achieves improved positioning accuracy ranging from 12\% to 20\%. Additionally, the method proposed in this paper takes only 0.5 seconds to perform epoch-by-epoch pseudorange correction on Jetson Orin Nano, which meets the real-time requirements and shows extremely high practical value. This paper also opensources a dataset under varying time, satellite distributions, and lighting conditions with accurate NLOS labels. We aim to contribute this dataset to the GNSS and deep learning communities, aspiring to establish it as the benchmark for NLOS classification and pseudorange bias correction. The datasets can be accessed at [github](https://github.com/ebhrz/KLTDataset).


## Funding Body

PolyU (UGC)

## Researcher

[Dr. Weisong Wen](https://polyu-taslab.github.io/members/Wen_Weisong.html), [Runzhi Hu](https://polyu-taslab.github.io/members/runzhi_hu.html), Dr. Jian Liu, [Yihan Zhong](https://polyu-taslab.github.io/members/yihan_zhong.html), Dr. Ming Xia

## Status

Undergoing

## System Framework

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Data_driven_structure.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Positioning Results

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Data_driven_boxplot.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Achievements

* Dataset Link: [https://github.com/ebhrz/KLTDataset](https://github.com/ebhrz/KLTDataset)

