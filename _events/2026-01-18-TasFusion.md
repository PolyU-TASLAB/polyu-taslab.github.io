---
title: PolyU TAS LAB Releases TasFusion: A GNSS/IMU Sliding-Window Optimization Framework
subtitle: news
image: images/opensource/TasFusion/demo.gif
tags: news
---

## PolyU TAS LAB Releases TasFusion: A GNSS/IMU Sliding-Window Optimization Framework

The PolyU Trustworthy AI and Autonomous Systems Laboratory (TAS LAB) has officially released TasFusion, an open-source ROS1 framework for multi-sensor navigation and state estimation.

TasFusion provides a Ceres-based GNSS/IMU loosely coupled sliding-window optimization framework, designed for research and experimental validation in outdoor navigation scenarios. The system supports IMU pre-integration, online bias estimation, marginalization to preserve historical information, and GNSS position and velocity constraints. All major functions are configurable through ROS launch parameters, enabling flexible deployment and ablation studies.

The framework is accompanied by a complete toolchain, including GNSS message definitions, NLOS exclusion utilities, NovAtel receiver drivers, and NMEA parsing scripts. TasFusion has been validated on a GNSS-IMU-4G integrated navigation module (dual-IMU, u-blox F9P-04B, and 4G link), demonstrating reliable performance with high-frequency measurements and stable telemetry in real-world environments.

TasFusion was developed in the context of the AAE4203 course at The Hong Kong Polytechnic University and is further supported by the Research Center for Autonomous System in Smart Transportation, PolyU-Wuxi Technology and Innovation Research Institute, reflecting close integration between education, research, and applied engineering.

The project is now publicly available on GitHub and is intended to support research in navigation, sensor fusion, autonomous systems, and intelligent transportation applications.

🔗 GitHub Repository:
https://github.com/PolyU-TASLAB/TasFusion


<table align="center" width="100%">
  <tr>
    <td align="center" width="33%">
      <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/opensource/TasFusion/board.png" style="width:100%; max-width:380px;"/>
    </td>
    <td align="center" width="33%">
      <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/opensource/TasFusion/demo.gif" style="width:100%; max-width:380px;"/>
    </td>
    <td align="center" width="33%">
      <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/opensource/TasFusion/longdata.png" style="width:100%; max-width:380px;"/>
    </td>
  </tr>
</table>

> Reference Hardware Platform ([Introduction Video](https://www.bilibili.com/video/BV1fiaqzNEEm)):
>
> TasFusion has been validated on GNSS-IMU-4G integrated navigation module (dual-IMU + u-blox F9P-04B + 4G uplink), providing high-frequency measurements and reliable telemetry for outdoor deployments.
>
> For inquiries regarding this hardware platform, please contact **hbwu@hkpolyu-wxresearch.cn**.





