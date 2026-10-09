---
title: "TasFusion"
subtitle: "ROS1 Package for Multi-Sensor GNSS/IMU Fusion Navigation"
kind: "Code"
repo: "PolyU-TASLAB/TasFusion"
stars: 22
forks: 1
license: "GPL-3.0"
author: "ZHAO Jiaqi"
image: "images/opensource/TasFusion/demo.jpg"
summary: "A ROS1 package for Ceres-based GNSS/IMU sliding-window fusion, ready to run on the lab's GNSS-IMU-4G navigation module."
innovations:
  - "Sliding-window GNSS/IMU optimisation with IMU pre-integration and online bias estimation"
  - "Marginalisation, GNSS position and velocity constraints and built-in NLOS exclusion"
  - "Every function switchable from the launch file; NovAtel driver and NMEA parsers included"
impact:
  - "Validated on a dual-IMU + u-blox F9P + 4G module for outdoor robots"
  - "Hardware enquiries: hbwu@hkpolyu-wxresearch.cn"
links:
  - label: "Introduction video"
    url: "https://www.bilibili.com/video/BV1fiaqzNEEm"
figures:
  - image: "images/opensource/TasFusion/board.jpg"
    caption: "GNSS-IMU-4G navigation module"
  - image: "images/opensource/TasFusion/longdata.jpg"
    caption: "Long-distance test trajectory"
---
