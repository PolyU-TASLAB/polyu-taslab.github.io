---
title: Huawei-PolyU High-accuracy Localization Project (second phase)
subtitle: Knowledge Transfer to Unmanned Autonomous Systems
# author: XNG
image: images/project/huawei_mapping.gif
tags: Localization, mapping, sensor fusion, RTK, GNSS, LiDAR, IMU, Virtual satellites, Cycle slip detection
order: 
---
## Abstract

Accurate positioning is one of the indispensable components for the fully autonomous driving vehicle. Global Navigation Satellite System (GNSS) Real-time Kinematic (RTK) has shown centimeter-level absolute positioning results in open-sky areas. However, it is also known suffering from polluted GNSS measurements and poor satellites' geometry due to signal blockage and reflection in urban canyons, like Hong Kong and Tokyo, where are filled with tall buildings and excessive dynamic objects (moving vehicles, pedestrians). Apart from GNSS, the onboard sensors for positioning also include light detection and ranging (LiDAR) and the inertial measurement unit (IMU). However, the accuracy of LiDAR positioning is also deteriorated due to the unexpected dynamic objects. Moreover, without a prior map, it will also suffer from drift during long-term operation even with the help of IMU. 

In this project, the LiDAR aided GNSS-RTK method based on the GNSS/IMU/LiDAR is developed to provide highly accurate positioning results in the urban canyons mentioned above. The developed system firstly takes the advantage of raw measurements from GNSS, LiDAR and IMU by tightly integrating them into a nonlinear optimization problem to obtain accurate float solution. Particularly, NLOS exclusion and cycle slip detection are performed to eliminate the impact of the outliers. Secondly, the system utilizes the LiDAR landmarks as "virtual satellites" to improve the distribution geometry of the received satellites to achieve a higher possibility on fix resolution. The evaluation results in urban canyons of Hong Kong show the effectiveness of the developed method.


## Funding Body

Huawei Technologies Co.Ltd. (HK$2,150,000, Aug 2021 - Aug 2022)

## Researcher

Dr. Weisong Wen, Dr. Li-Ta Hsu, Dr. Jiachen Zhang, Dr. Xiwei Bai, HUANG Feng, Xikun Liu

## Status

Completed

## System Framework

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/huawei_mapping_framework.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Mapping Results

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/huawei_mapping.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>
