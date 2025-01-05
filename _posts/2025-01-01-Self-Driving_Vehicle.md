---
title: Research and Test on Autonomous Driving Vehicle 
# subtitle: Knowledge Transfer to Unmanned Autonomous Systems
# author: Zhang Ziqi
image: images/projects/ADV.png
tags: Autonomous-Driving
order: 
---
<!-- ## Abstract

Precise localization is one of the indispensable components of a fully autonomous vehicle. Global Navigation Satellite System (GNSS) real-time kinematics (RTK) shows absolute positioning results at centimeter level in open sky areas. However, in urban canyon environments there are a large number of high-rise buildings and dynamic objects (moving vehicles, pedestrians) that block and reflect on the signal propagation, resulting in large GNSS measurement noise as well as suboptimal satellite geometry distributions, which further affects the positioning accuracy. In addition to GNSS, airborne sensors for positioning include Light Detection and Ranging (LiDAR) and Inertial Measurement Units (IMUs). However, the accuracy of LiDAR localization is also degraded due to the presence of a large number of dynamic objects. In addition, without a priori maps, LiDAR localization suffers from drift during long-term operation, even with the help of IMUs.

In this project, a LiDAR-assisted GNSS-RTK positioning method based on GNSS/IMU/LiDAR fusion is developed, which is capable of providing highly accurate positioning results in the urban canyons mentioned above. The developed system first performs 3D point cloud-assisted NLOS detection exclusion and LiDAR-assisted perihelion detection to eliminate the effects of outliers. Second, the system utilizes LiDAR landmark observations as “virtual satellites” to improve the geometric distribution of the original satellite observations. Finally, the original measurements from GNSS, LiDAR, and IMU are tightly integrated into a nonlinear optimization problem to obtain an accurate floating-point solution, and the LAMBDA method is further applied to solve the integer ambiguity to achieve high-precision positioning. The effectiveness of the proposed method in this project is fully verified in the evaluation results of the City Canyon of Hong Kong.



## Funding Body

Department of Science and Technology of Guangdong Province (GDSTC) 廣東省科學技術廳


## Researcher

[Dr. Weisong Wen](https://polyu-taslab.github.io/members/Wen_Weisong.html), Dr. Li-Ta Hsu, Dr. Jian Liu, [Feng Huang](https://polyu-taslab.github.io/members/Huang_Feng.html), [Xikun Liu](https://polyu-taslab.github.io/members/liu_xikun.html)， [Yihan Zhong](https://polyu-taslab.github.io/members/Zhong_Yihan.html)

## Status

Completed

## System Framework

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/GDSTC/pipeline.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Demonstration

### LiDAR-aided GNSS Fix 
<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/GDSTC/fix_gif.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

### NLOS detection 
<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/GDSTC/nlos_detection_gif.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

## Achievements

* Liu, X., Wen, W., & Hsu, L. T. (2023). GLIO: Tightly-coupled GNSS/LiDAR/IMU integration for continuous and drift-free state estimation of intelligent vehicles in urban areas. IEEE Transactions on Intelligent Vehicles.
* Huang, F., Wen, W., Zhang, J., Wang, C., & Hsu, L. T. (2023). Dynamic Object-aware LiDAR Odometry Aided by Joint Weightings Estimation in Urban Areas. IEEE Transactions on Intelligent Vehicles.
* Zhong, Y., Hu, R., Bai, X., Li, X., Hsu, L. T., & Wen, W. (2024). Enhancing GNSS Positioning Accuracy for Road Monitoring Systems: A Factor Graph Optimization Approach Aided by Geospatial Information. IEEE Transactions on Instrumentation and Measurement. -->
## Introduction
An autonomous car, also known as a self-driving vehicle, is a sophisticated mode of transportation that can perceive its environment and navigate without the need for human intervention. These vehicles employ a variety of advanced technologies to achieve safe and efficient driving, making them a significant innovation in modern transportation.

A critical aspect of autonomous vehicles is their ability to sense and localize themselves within their surroundings. This capability is essential for navigating complex environments, avoiding obstacles, and making real-time driving decisions. Accurate sensing and localization allow autonomous cars to interpret data from their surroundings and respond appropriately to dynamic conditions.

### ADV Test Video 
<div style="max-width: 850px; margin: 0 auto; border-radius: 15px; overflow: hidden;">
    <iframe src="https://www.youtube.com/embed/Q0nq1vHeinM?si=qCn-JtP2m65mRTAE" 
            style="width: 100%; height: auto; object-fit: cover; border-radius: 15px;" 
            frameborder="0" 
    </iframe>
</div>
