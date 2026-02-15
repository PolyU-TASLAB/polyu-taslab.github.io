---
title: TasFusion
subtitle: ROS1 Package for Multi-Sensor GNSS/IMU Fusion Navigation
author: ZHAO Jiaqi
image: images/opensource/TasFusion/demo.gif
tags:
order:
---

A <b class="blue">ROS1 package</b> for Ceres-based <b class="blue">GNSS/IMU loosely coupled sliding-window optimization</b>, designed for robust multi-sensor navigation.

**[TasFusion](https://github.com/PolyU-TASLAB/TasFusion)** provides a complete multi-sensor navigation framework with the following features:

- **Ceres-based optimization** — Sliding-window GNSS/IMU loosely coupled fusion with IMU pre-integration and online bias estimation
- **Marginalization** — Preserves historical information for consistent state estimation
- **GPS constraints** — Supports both position and velocity constraints from GNSS
- **NLOS exclusion** — Built-in utilities to reject non-line-of-sight satellite signals
- **Flexible configuration** — All major functions can be enabled/disabled via launch file parameters
- **Supporting tools** — Includes GNSS message definitions, a NovAtel driver, and NMEA ROS parsing scripts

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

> **Reference Hardware Platform** ([Introduction Video](https://www.bilibili.com/video/BV1fiaqzNEEm)):
> TasFusion has been validated on a GNSS-IMU-4G integrated navigation module (dual-IMU + u-blox F9P-04B + 4G uplink), providing high-frequency measurements and reliable telemetry for outdoor deployments.
> For hardware inquiries, please contact **hbwu@hkpolyu-wxresearch.cn**.

**GitHub:** [https://github.com/PolyU-TASLAB/TasFusion](https://github.com/PolyU-TASLAB/TasFusion)
