---
title: TasFusion
subtitle: 
author: ZHAO Jiaqi
image: images/opensource/TasFusion/demo.gif
tags: 
order:
---
<!-- Add breif description here.  -->

ROS1 package designed for Ceres-based GNSS/IMU loosely coupled sliding-window optimization

<!-- Add Main body here -->

[TasFusion](https://github.com/PolyU-TASLAB/TasFusion.git) is a ROS1 package designed for multi-sensor navigation. Its core functionality provides a Ceres-based GNSS/IMU loosely coupled sliding-window optimization framework, along with supporting tools including GNSS message definitions, NLOS exclusion utilities, a NovAtel driver, and NMEA ROS parsing scripts.

The central sensor-fusion node supports IMU pre-integration, online bias estimation, marginalization to preserve historical information, and GPS position/velocity constraints. All major functions can be flexibly enabled or disabled through parameters configured in launch files.

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

Github Repository: https://github.com/PolyU-TASLAB/TasFusion.git

> Reference Hardware Platform ([Introduction Video](https://www.bilibili.com/video/BV1fiaqzNEEm)):
>
> TasFusion has been validated on GNSS-IMU-4G integrated navigation module (dual-IMU + u-blox F9P-04B + 4G uplink), providing high-frequency measurements and reliable telemetry for outdoor deployments.
>
> For inquiries regarding this hardware platform, please contact **hbwu@hkpolyu-wxresearch.cn**.

<!-- Add picture. -->

<!-- <div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/huawei_mapping.gif" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div> -->

<!-- Add video. -->

<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/m2Lm8RY2uYI?si=3g26doqQz-9AnBOi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->
