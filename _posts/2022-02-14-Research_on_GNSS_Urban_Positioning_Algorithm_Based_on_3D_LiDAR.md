---
title: Research on GNSS Urban Positioning Algorithm Based on 3D LiDAR
subtitle: Knowledge Transfer to Unmanned Autonomous Systems
# author: XNG
image: images/project/GDSTC/fgo.png
tags: Localization, mapping, sensor-fusion, RTK, GNSS, LiDAR, IMU
order: 
---
## Abstract

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
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/GDSTC/fgo.png" alt="Team Banner" 
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
* Zhong, Y., Hu, R., Bai, X., Li, X., Hsu, L. T., & Wen, W. (2024). Enhancing GNSS Positioning Accuracy for Road Monitoring Systems: A Factor Graph Optimization Approach Aided by Geospatial Information. IEEE Transactions on Instrumentation and Measurement.

