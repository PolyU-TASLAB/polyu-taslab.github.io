---
title: Our Autonomous Platforms
# subtitle: Knowledge Transfer to Unmanned Autonomous Systems
# author: Zhang Ziqi
image: images/project/Vehicle/ADV.png
tags: Autonomous-Driving
order: 
---
Demonstration of our Autonomous Driving Vehicles and their onboard sensor platforms.

## Introduction

An autonomous car, also known as a self-driving vehicle, is a sophisticated mode of transportation that can perceive its environment and navigate without human intervention. These vehicles employ a variety of advanced technologies to achieve safe and efficient driving, making them a significant innovation in modern transportation.

A critical aspect of autonomous vehicles is their ability to sense and localize themselves within their surroundings. This capability is essential for navigating complex environments, avoiding obstacles, and making real-time driving decisions. Accurate sensing and localization allow autonomous cars to interpret data from their surroundings and respond appropriately to dynamic conditions.

The autonomous driving vehicle operates under the comprehensive control of a CANBUS system. The host computer establishes a connection with the MCU, which is equipped with integrated ROS messaging capabilities. This integration allows the system to convert ROS messages into CAN signals, which are then transmitted to the MCU.

This architecture provides us with extensive access to the vehicle's functionalities. We can not only relay vital velocity information but also manage gear settings, including Drive (D), Park (P), Reverse (R), and Neutral (N). Additionally, the system enables control of various lighting functions, enhancing both safety and operational efficiency. Overall, this setup ensures seamless communication between components, facilitating precise control and monitoring of the vehicle’s performance.
## Sensor Platform

Currently, our lab has two autonomous vehicles deployed on the PolyU Main Campus and the PolyU-Wuxi Research Institute. Both vehicles are equipped with unique sensors, including LiDAR, cameras, and integrated GNSS/INS, for localization and navigation.

Here is the sensor suite:

| Sensor Type | Brand/Model | Parameters |
|-------------|-------------|------------|
| **LiDAR**   | Robosense RS-LiDAR-32 | 32 laser channels, 200m range, 360° horizontal FOV, 30° vertical FOV, 10Hz-20Hz scanning frequency |
| **Cameras** | HikRobot Event camera | 1280x720 resolution, 120dB dynamic range, 60fps frame rate, global shutter |
| **GNSS/INS**| CHCNav GNSS/INS | Dual-frequency GNSS receiver, integrated IMU, centimeter-level accuracy, real-time kinematic (RTK) support |


## ADV Demo Video 

### Testing
<div style="max-width: 850px; margin: 0 auto; border-radius: 15px; overflow: hidden;">
  <iframe width="850" height="480" src="https://www.youtube.com/embed/Q0nq1vHeinM" frameborder="0" allowfullscreen></iframe>
  <p style="text-align: center; margin-top: 10px;">ADV in PolyU Campus</p>
</div>

<div style="max-width: 850px; margin: 0 auto; border-radius: 15px; overflow: hidden;">
  <iframe width="850" height="480" src="https://youtu.be/xPd1KiWvAK8?si=o-ETk9Tx3xcYCiPe" frameborder="0" allowfullscreen></iframe>
  <p style="text-align: center; margin-top: 10px;">ADV in PolyU-Wuxi Research Institute</p>
</div>


<!-- <div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vehicle/EgoVehicle.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
  <p style="margin-top: 10px; text-align: center;">Autonomous Driving Simulation with Pedastrian Aviodance </p>
</div> -->
### Carla Simulation Video

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vehicle/Carla.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
  <p style="margin-top: 10px; text-align: center;">Carla Simulation</p>
</div>


### Researcher

[Dr. Weisong Wen](https://polyu-taslab.github.io/members/Wen_Weisong.html), [Mr. Zhang Ziqi](https://polyu-taslab.github.io/members/Zhang_Ziqi.html), [Mr. Huang Feng](https://polyu-taslab.github.io/members/Huang_Feng.html)
