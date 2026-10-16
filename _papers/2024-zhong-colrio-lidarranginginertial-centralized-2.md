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
publisher: arXiv
date: '2024-01-01'
doi: https://doi.org/g8t65m
image: images/papers/cards/2024-zhong-colrio-lidarranginginertial-centralized-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2402.11790v2.pdf
tags:
- 3D LIDAR
- Muti-robot cooperative SLAM
- Performance evaluation
- Efficient mapping
citation_id: 10.48550/arXiv.2402.11790
---

## Abstract

Collaborative state estimation using different heterogeneous sensors is a fundamental prerequisite for robotic swarms operating in GPS-denied environments, posing a significant research challenge. In this paper, we introduce a central-ized system to facilitate collaborative LiDAR-ranging-inertial state estimation, enabling robotic swarms to operate without the need for anchor deployment. The system efficiently distributes computationally intensive tasks to a central server, thereby reducing the computational burden on individual robots for local odometry calculations. The server back-end establishes a global reference by leveraging shared data and refining joint pose graph optimization through place recognition, global optimization techniques, and removal of outlier data to ensure precise and robust collaborative state estimation. Extensive evaluations of our system, utilizing both publicly available datasets and our custom datasets, demonstrate significant enhancements in the accuracy of collaborative SLAM estimates. Moreover, our system exhibits remarkable proficiency in large-scale missions, seamlessly enabling ten robots to collaborate effectively in performing SLAM tasks. In order to contribute to the research community, we will make our code open-source and accessible at https://github.com/PengYu-team/Co-LRIO.

## Problem Addressed

Collaborative state estimation with heterogeneous sensors is a fundamental prerequisite for robotic swarms operating in GPS-denied environments, and achieving it without deploying anchors while keeping per-robot computation low is a significant research challenge.

## Key Contributions

- Tightly coupled LiDAR-inertial odometry with fixed-lag smoothing and intensity-aided direct raw-point registration
- Centralized LiDAR-ranging-inertial state estimation enabling anchor-free co-localization for robotic swarms
- Server back-end with place recognition, joint pose graph optimization, global optimization, and outlier removal
- Extensive evaluation of accuracy, communication, and scalability; open-source code and custom datasets

## Conclusions

Evaluations on public and custom datasets demonstrate significant improvements in the accuracy and robustness of collaborative SLAM estimates, with the system seamlessly supporting ten robots collaborating in real time on large-scale missions. Future work aims to scale to potentially hundreds of agents via simulation and distributed or decentralized structures, and to enhance resilience to significant outlier distance and loop measurements using robust incremental optimization.
