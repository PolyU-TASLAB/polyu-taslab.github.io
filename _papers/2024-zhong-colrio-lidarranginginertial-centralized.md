---
title: 'CoLRIO: LiDAR-Ranging-Inertial Centralized State Estimation for Robotic Swarms'
authors:
- Shipeng Zhong
- Hongbo Chen
- Yuhua Qi
- Dapeng Feng
- Zhiqiang Chen
- Jin Wu
- Weisong Wen
- Ming Liu
publisher: 2024 IEEE International Conference on Robotics and Automation (ICRA)
date: '2024-05-13'
doi: https://doi.org/hbfmst
image: images/papers/cards/2024-zhong-colrio-lidarranginginertial-centralized.jpg
citation_id: doi:10.1109/icra57147.2024.10611672
---

## Abstract

Collaborative state estimation using different heterogeneous sensors is a fundamental prerequisite for robotic swarms operating in GPS-denied environments, posing a significant research challenge. In this paper, we introduce a centralized system to facilitate collaborative LiDAR-ranging-inertial state estimation, enabling robotic swarms to operate without the need for anchor deployment. The system efficiently distributes computationally intensive tasks to a central server, thereby reducing the computational burden on individual robots for local odometry calculations. The server back-end establishes a global reference by leveraging shared data and refining joint pose graph optimization through place recognition, global optimization techniques, and removal of outlier data to ensure precise and robust collaborative state estimation. Extensive evaluations of our system, utilizing both publicly available datasets and our custom datasets, demonstrate significant enhancements in the accuracy of collaborative SLAM estimates. Moreover, our system exhibits remarkable proficiency in large-scale missions, seamlessly enabling ten robots to collaborate effectively in performing SLAM tasks. In order to contribute to the research community, we will make our code open-source and accessible at https://github.com/PengYu-team/Co-LRIO.

## Problem Addressed

Collaborative state estimation with heterogeneous sensors is a fundamental prerequisite for robotic swarms operating in GPS-denied environments, but it faces significant challenges in per-robot computational load and anchor-free co-localization.

## Key Contributions

- Tightly coupled LiDAR-inertial odometry built on fixed-lag smoothing and intensity-aided direct raw-point registration
- Centralized LiDAR-ranging-inertial state estimation enabling anchor-free co-localization for robotic swarms
- Server back-end combining place recognition, global pose graph optimization, and outlier removal
- Extensive evaluation on public and custom datasets demonstrating collaboration of up to ten robots; open-sourced

## Conclusions

CoLRIO enables multiple robots to collaboratively generate global SLAM estimates from concurrently collected data in real time. Extensive experiments demonstrate accurate and robust collaborative SLAM in large-scale missions, with up to 10 robots simultaneously contributing to the system.
