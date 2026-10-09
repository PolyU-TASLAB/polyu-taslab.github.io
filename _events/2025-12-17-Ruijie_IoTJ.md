---
title: Our paper is accepted by IEEE Internet of Things Journal
subtitle: Example news
# author: xxx
image: images/news/ruijie_rttlio.png
tags: news
order: 
---

The paper "RTT-LIO: A Wi-Fi RTT-aided LiDAR-Inertial Odometry via Tightly-Coupled Factor Graph Optimization in Complex Scenes" has been accepted by the *IEEE Internet of Things Journal*. Congratulations to Ruijie and the co-authors!

- **Authors:** Ruijie Xu, Xikun Liu, Xin Wang, Weisong Wen and Yulong Huang

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/ruijie_rttlio.png" alt="System framework of RTT-LIO"></figure>
</div>
<p class="news-caption">System framework of RTT-LIO.</p>

### Abstract

The pursuit of reliable and high-precision indoor positioning has become increasingly critical with the widespread deployment of Unmanned Autonomous Systems (UAS) across smart cities. While Wi-Fi Round-Trip-Time (RTT) technology offers promising absolute positioning capabilities, it faces challenges from signal interference and processing delays. Similarly, LiDAR-inertial odometry (LIO) systems provide accurate relative positioning but suffer from cumulative drift over time. Existing methods have explored loosely coupled approaches, but they process sensor data separately and fail to fully exploit the complementary strengths of different sensors.

This research introduces a tightly-coupled RTT/LIO framework, with novel factor graph formulations that ensure consistency between RTT and LiDAR observations, alongside LiDAR-aided RTT outlier detection and exclusion. It also develops a new approach to estimate the positions of unknown access points (APs) using a prior trajectory and RTT observations. AP position estimation is based on kernel density estimation (KDE) and geometric diversity constraints (GDC), with the help of an adaptive RANSAC-based fault detection algorithm.

Compared with RTT-only implementations, state-of-the-art LIO systems and conventional loosely coupled approaches, the method reduced errors by 20–80% in extensive experiments. The [code and Wi-Fi RTT/LiDAR/IMU dataset](https://github.com/RuijieXu0408/RTT-LIO) and a [demo video](https://www.bilibili.com/video/BV1Y94MzYE7F) are publicly available.
