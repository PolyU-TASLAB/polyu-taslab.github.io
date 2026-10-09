---
title: PolyU TASLAB Releases TasFusion - A GNSS/IMU Sliding-Window Optimization Framework
subtitle: news
image: images/opensource/TasFusion/longdata.png
tags: news
---

The Trustworthy AI and Autonomous Systems Laboratory (TASLAB) at The Hong Kong Polytechnic University (PolyU) has released TasFusion, an open-source ROS1 framework for multi-sensor navigation and state estimation. The project is publicly available on GitHub: [https://github.com/PolyU-TASLAB/TasFusion](https://github.com/PolyU-TASLAB/TasFusion).

<div class="news-photos" data-cols="2" data-fit="contain" data-ratio="wide">
  <figure><img src="{{ site.baseurl }}/images/opensource/TasFusion/board.png" alt="GNSS-IMU-4G integrated navigation module"></figure>
  <figure><img src="{{ site.baseurl }}/images/opensource/TasFusion/longdata.png" alt="TasFusion results on a long dataset"></figure>
</div>
<p class="news-caption">The GNSS-IMU-4G reference hardware platform and TasFusion results.</p>

### Features

TasFusion provides a Ceres-based GNSS/IMU loosely coupled sliding-window optimization framework, designed for research and experimental validation in outdoor navigation scenarios. The system supports IMU pre-integration, online bias estimation, marginalization to preserve historical information, and GNSS position and velocity constraints. All major functions are configurable through ROS launch parameters, enabling flexible deployment and ablation studies.

The framework comes with a complete toolchain, including GNSS message definitions, NLOS exclusion utilities, NovAtel receiver drivers and NMEA parsing scripts.

<div class="news-video">
  <video src="{{ site.baseurl }}/images/opensource/TasFusion/demo.mp4" poster="{{ site.baseurl }}/images/opensource/TasFusion/demo.jpg" autoplay loop muted playsinline preload="metadata" style="width:100%; height:100%;"></video>
</div>

### Reference hardware platform

TasFusion has been validated on a GNSS-IMU-4G integrated navigation module (dual-IMU, u-blox F9P-04B and 4G uplink), which provides high-frequency measurements and reliable telemetry for outdoor deployments ([introduction video](https://www.bilibili.com/video/BV1fiaqzNEEm)). For inquiries about this hardware platform, please contact **hbwu@hkpolyu-wxresearch.cn**.

### Background

TasFusion was developed in the context of the AAE4203 course at PolyU and is further supported by the Research Center for Autonomous System in Smart Transportation, PolyU-Wuxi Technology and Innovation Research Institute, reflecting close integration between education, research and applied engineering. It is intended to support research in navigation, sensor fusion, autonomous systems and intelligent transportation applications.
