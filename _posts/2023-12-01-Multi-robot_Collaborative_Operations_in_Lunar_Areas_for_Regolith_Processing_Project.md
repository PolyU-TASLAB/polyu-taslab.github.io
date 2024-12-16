---
title: Multi-robot Collaborative Operations in Lunar Areas for Regolith Processing (first phase)
subtitle: High Accuracy Positioning with Multi-sensory Integration for Robotics in Complex Scenarios
# author: CYM
image: images/project/robotic_arms.gif
tags: Multi-robot collaboration, MPC, mapping, Leader-Follower Formation Algorithm, sensor-fusion, Visual odometry, LiDAR, IMU
order: 
---
## Abstract

Researches on lunar surface requires heavy participation of Unmanned Autonomous Systems(UASs), such as autonomous vehicle with robotic arms to collect soil samples from the rugged surface.

Accurate positioning is one of the indispensable components for the fully autonomous driving vehicle. Global Navigation Satellite System (GNSS) Real-time Kinematic (RTK) has shown centimeter-level absolute positioning results in open-sky areas. However, it is also known suffering from polluted GNSS measurements and poor satellites' geometry due to signal blockage and reflection in urban canyons, like Hong Kong and Tokyo, where are filled with tall buildings and excessive dynamic objects (moving vehicles, pedestrians). Apart from GNSS, the onboard sensors for positioning also include light detection and ranging (LiDAR) and the inertial measurement unit (IMU). However, the accuracy of LiDAR positioning is also deteriorated due to the unexpected dynamic objects. Moreover, without a prior map, it will also suffer from drift during long-term operation even with the help of IMU. 

In this project, the LiDAR aided GNSS-RTK method based on the GNSS/IMU/LiDAR is developed to provide highly accurate positioning results in the urban canyons mentioned above. The developed system firstly takes the advantage of raw measurements from GNSS, LiDAR and IMU by tightly integrating them into a nonlinear optimization problem to obtain accurate float solution. Particularly, NLOS exclusion and cycle slip detection are performed to eliminate the impact of the outliers. Secondly, the system utilizes the LiDAR landmarks as "virtual satellites" to improve the distribution geometry of the received satellites to achieve a higher possibility on fix resolution. The evaluation results in urban canyons of Hong Kong show the effectiveness of the developed method.


## Funding Body

Research Centre for Deep Space Explorations(RCDSE) (Dec 2023 - Dec 2025)

## Researcher

[Dr. Weisong Wen](https://polyu-taslab.github.io/members/Wen_Weisong.html), Dr. Li-Ta Hsu, Dr. Jiachen Zhang, Dr. Xiwei Bai, [HUANG Feng](https://polyu-taslab.github.io/members/Huang_Feng.html), [Xikun Liu](https://polyu-taslab.github.io/members/liu_xikun.html)

## Status

Ongoing

## System Framework

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/huawei_mapping_framework.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Demonstration

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/speedy_clipped_ms_AO.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Achievements

* 3DLA GNSS-RTK received award at TechConnect 2021 due to impactful research and innovation.  
* Wen, W. W., & Hsu, L. T. (2022). 3D LiDAR aided GNSS NLOS mitigation in urban canyons. IEEE Transactions on Intelligent Transportation Systems, 23(10), 18224-18236. 
* Liu, X., Wen, W., Huang, F., Gao, H., Wang, Y., & Hsu, L. T. (2024). 3D LiDAR aided GNSS NLOS mitigation for reliable GNSS-RTK positioning in urban canyons. Journal of Geodesy (Major revision).
* Zhong, Y., Huang, F., Zhang, J., Wen, W., & Hsu, L. T. (2023). Low‐cost solid‐state LiDAR/inertial‐based localization with prior map for autonomous systems in urban scenarios. IET Intelligent Transport Systems, 17(3), 474-486. 
* Zhang, J., Wen, W., Huang, F., Wang, Y., Chen, X., & Hsu, L. T. (2022). GNSS-RTK Adaptively Integrated with LiDAR/IMU Odometry for Continuously Global Positioning in Urban Canyons. Applied Sciences, 12(10), 5193.
* Huang, F., Wen, W., Ng, H. F., & Hsu, L. T. (2022, October). Lidar aided cycle slip detection for gnss real-time kinematic positioning in urban environments. In 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC) (pp. 1572-1578). IEEE. 
* Wen, W., & Hsu, L. T. (2021, September). 3D LiDAR aided GNSS real-time kinematic positioning. In Proceedings of the 34th International Technical Meeting of the Satellite Division of The Institute of Navigation (ION GNSS+ 2021) (pp. 2212-2220).
