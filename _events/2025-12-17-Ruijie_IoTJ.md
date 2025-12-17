---
title: Our paper is accepted by IEEE Internet of Things Journal
subtitle: Example news
# author: xxx
image: images/news/ruijie_rttlio.png
tags: news
order: 
---

It is great to share that our paper (“RTT-LIO: A Wi-Fi RTT-aided LiDAR-Inertial Odometry via Tightly-Coupled Factor Graph Optimization in Complex Scenes”, by Ruijie Xu, Xikun Liu, Xin Wang, Weisong Wen, and Yulong Huang) is accepted by the IEEE Internet of Things Journal. Congratulations to Ruijie and etc.!

## Abstract

The pursuit of reliable and high-precision indoor positioning has become increasingly critical with the widespread deployment of Unmanned Autonomous Systems (UAS) across smart cities. While Wi-Fi Round-Trip-Time (RTT) technology offers promising absolute positioning capabilities, it faces challenges from signal interference and processing delays. Similarly, LiDAR-inertial odometry (LIO) systems provide accurate relative positioning, but suffer from cumulative drift over time. Although existing methods have explored loosely coupled technologies, they process sensor data separately, failing to fully exploit the complementary strengths of different sensors. This research pioneered a tightly-coupled RTT/LIO framework, encompassing novel factor graph formulations that ensure consistency between RTT and LiDAR observations, alongside LiDAR-aided RTT outlier detection and exclusion. Furthermore, we developed an innovative approach to estimate the positions of unknown access points (AP) by using prior trajectory and RTT observations. AP position estimation is based on kernel density estimation (KDE) and geometric diversity constraints (GDC) with the help of an adaptive RANSAC-based fault detection algorithm. Compared to RTT-only implementations, state-of-the-art LIO systems, and conventional loosely coupled approaches, our method demonstrated error reductions of 20-80\% in extensive experiments. The [code, Wi-Fi RTT/LiDAR/IMU dataset](https://github.com/RuijieXu0408/RTT-LIO), and [demo video](https://www.bilibili.com/video/BV1Y94MzYE7F) of our proposed methodology has been made publicly available to display our research.


## System Framework

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/news/ruijie_rttlio.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>
