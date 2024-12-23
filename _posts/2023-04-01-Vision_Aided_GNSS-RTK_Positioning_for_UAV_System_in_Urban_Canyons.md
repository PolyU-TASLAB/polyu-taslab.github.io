---
title: Vision Aided GNSS-RTK Positioning for UAV System in Urban Canyons
subtitle: Fisheye Camera Aided GNSS NLOS Detection and Learning-based Pseudorange Bias Correction for Intelligent Vehicles in Urban Canyons
# author: XNG
image: images/project/Vision_aided_GNSS_RTK/framework.png
tags: Artificial intelligence, Deep learning, GNSS
order: 
---
## Abstract

The global navigation satellite system (GNSS) is low-cost and is highly expected by intelligent vehicles, which can provide reliable absolute positioning service in open areas. Unfortunately, the performance of the GNSS positioning is significantly degraded in urban canyons, due to the notorious non-line-of-sight (NLOS) receptions and multipath interference caused by signal reflections. To fill this gap, this paper proposed a fisheye camera-based GNSS NLOS detection method, where the state-of-the-art Swin Transformer model is employed to segment the sky and non-sky view areas within the image. Instead of directly excluding the detected GNSS NLOS receptions that would significantly degrade the geometry of satellite distribution, this paper proposed to directly estimate the bias of the NLOS receptions and multipath by a tightly-coupled integration model of GNSS least square and the deep neural network (DNN). The effectiveness of the proposed method was validated on multiple datasets from urban canyons in Hong Kong. In particular, a GNSS NLOS detection accuracy of more than 99.0% is achieved in the evaluated dataset. By correcting the bias involved from the GNSS NLOS and multipath, improved positioning accuracy about 5% is obtained using the proposed method.


## Funding Body

Meituan (Collaborative)/深圳市美團機器人研究院

## Researcher

[Dr. Weisong Wen](https://polyu-taslab.github.io/members/Wen_Weisong.html), [Runzhi Hu](https://polyu-taslab.github.io/members/runzhi_hu.html), Penghui Xu, [Yihan Zhong](https://polyu-taslab.github.io/members/yihan_zhong.html)

## Status

Undergoing

## System Framework

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vision_aided_GNSS_RTK/framework.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## NLOS Detection Results

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vision_aided_GNSS_RTK/NLOS.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Position Result

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vision_aided_GNSS_RTK/position.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>


## Achievements

* Hu, Runzhi, Weisong Wen, and Li–Ta Hsu. "Fisheye Camera Aided GNSS NLOS Detection and Learning-Based Pseudorange Bias Correction for Intelligent Vehicles in Urban Canyons." 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC). IEEE, 2023.

