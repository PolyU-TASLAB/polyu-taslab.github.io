---
title: Multi-robot Collaborative Operations in Lunar Areas for Regolith Processing (first phase)
subtitle: High Accuracy Positioning with Multi-sensory Integration for Robotics in Complex Scenarios
# author: CYM
image: 
tags: Multi-robot collaboration, MPC, Leader-Follower Formation Algorithm, sensor-fusion, LiDAR, IMU
order: 
---
## Abstract
Research on the lunar surface necessitates significant involvement of Unmanned Autonomous Systems (UASs), including autonomous vehicles equipped with robotic arms for the collection of soil samples from the challenging terrain. Two primary challenges must be overcome in executing such tasks: firstly, ensuring precise control accuracy on the rugged surface, and secondly, addressing the safety concerns associated with the operation of space robotics.

In order to address the challenges encountered during the scientific research task, a multi-robot collaboration system has been proposed. The system leverages multi-robot positioning techniques to ensure precise and accurate positioning. By incorporating Factor Graph Optimization (FGO) in conjunction with multi-sensor aided GNSS positioning, the system aims to enhance the overall positioning accuracy. Our FGO-based RTK/INS/Odometer (RIO) integration successfully mitigates outliers, achieving a Root Mean Square Error (RMSE) of 0.30 meters. This represents a significant improvement of 79.2% and 93.6% compared to RTKLIB-RTK and F9P-RTK, respectively. Within our multi-robot framework, FGO-based RIO-OM plays a crucial role in optimizing the collective state of the entire team. By integrating individual robot position estimates, relative position data, and sensor information into a comprehensive global optimization problem, the system ensures efficient and effective collaboration among the robots. In completing prototype of current phase of this project,Leader-Follower Formation Algorithm is also applied. The algorithm is a low-cost & common strategy for multi-robot formation. In this approach, one robot is designated as the leader, and the other robots, referred to as followers, adjust their positions and movements based on the leader's state (position and velocity). Each robot controls its own movement to follow the leader and maintain its relative position and distance. Each robot detects obstacles in its surroundings using sensors (e.g., LiDAR, ultrasonic sensors, etc.) and adjusts its trajectory to avoid collisions while maintaining the formation.

In the upcoming stages of this project, our focus will be on enhancing the prototype, with a particular emphasis on improving multi-robot collaboration. Through the implementation of Positioning and Leader-Follower algorithms, the robots will be able to autonomously navigate to the designated soil container locations by utilizing both global and local path planning strategies. The Leader robot will take charge of guiding the Follower robots, thereby ensuring synchronized task execution and accurate navigation towards the target. To conclude, the multi-robot system designed for simulating the lunar soil sampling process incorporates automated navigation, soil identification, and collection functionalities. Utilizing onboard cameras, the robots capture real-time images and leverage OpenCV image processing algorithms for identifying soil containers embedded with QR codes. Upon successful QR code recognition, the robot promptly computes the precise position and orientation of the soil container to facilitate accurate targeting. The extracted QR code data is then utilized for precise localization and task assignment.



## Funding Body

Research Centre for Deep Space Explorations(RCDSE) (Dec 2023 - Dec 2025)

## Researcher

[Dr. Weisong Wen](https://polyu-taslab.github.io/members/Wen_Weisong.html) , Qian Liang 

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

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/speed_4_combined_arms.gif" alt="Team Banner" 
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

