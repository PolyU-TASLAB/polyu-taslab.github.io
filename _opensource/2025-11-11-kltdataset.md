---
title: KLT Dataset
subtitle: Urban GNSS Dataset with LOS/NLOS Labels
author: Runzhi Hu
image: images/opensource/kltdataset/NLOS_crop.gif
tags:
order:
---

An open <b class="blue">urban GNSS dataset</b> with <b class="blue">LOS/NLOS satellite labels</b> for benchmarking GNSS positioning in challenging environments.

**[KLT Dataset](https://github.com/ebhrz/KLTDataset)** is a light urban scenario dataset collected for GNSS research, providing labeled satellite signal conditions to support studies in multipath mitigation, NLOS detection, and robust positioning.

**Dataset Contents:**
- **GNSS raw measurements** — Collected using a u-blox F9P receiver with pseudorange and carrier phase observations
- **Ground truth** — High-precision reference trajectories from a SPAN-CPT system
- **LOS/NLOS labels** — Per-satellite labels for GPS and BeiDou constellations
- **Additional sensors** — IMU, LiDAR, and camera recordings included in the ROS bag file
- **Quick-start scripts** — Configuration files and start scripts provided for immediate use

<p align="center">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vision_aided_GNSS_RTK/NLOS.gif" alt="KLT Dataset — NLOS Visualization" style="width:100%; max-width:750px; border-radius:8px;">
</p>

**GitHub:** [https://github.com/ebhrz/KLTDataset](https://github.com/ebhrz/KLTDataset)
