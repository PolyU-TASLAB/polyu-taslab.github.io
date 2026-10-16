---
title: 'UrbanLoco: A Full Sensor Suite Dataset for Mapping and Localization in Urban Scenes'
authors:
- Weisong Wen
- Yiyang Zhou
- Guohao Zhang
- Saman Fahandezh-Saadi
- Xiwei Bai
- Wei Zhan
- Masayoshi Tomizuka
- Li-Ta Hsu
publisher: 2020 IEEE International Conference on Robotics and Automation (ICRA)
date: '2020-05-01'
doi: https://doi.org/g8tzcz
image: images/papers/cards/2020-wen-urbanloco-full-sensor.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/UrbanLoco.pdf
tags:
- Global navigation satellite system
- Cameras
- Laser radar
- Urban areas
- Robot sensing systems
- Trajectory
- Satellites
citation_id: doi:10.1109/ICRA40945.2020.9196526
---

## Abstract

Mapping and localization is a critical module of autonomous driving, and significant achievements have been reached in this field. Beyond Global Navigation Satellite System (GNSS), research in point cloud registration, visual feature matching, and inertia navigation has greatly en-hanced the accuracy and robustness of mapping and localization in different scenarios. However, highly urbanized scenes are still challenging: LIDAR- and camera-based methods perform poorly with numerous dynamic objects; the GNSS-based solutions experience signal loss and multipath problems; the inertia measurement units (IMU) suffer from drifting. Unfortunately, current public datasets either do not adequately address this urban challenge or do not provide enough sensor information related to map-ping and localization. Here we present UrbanLoco: a map-∗Both authors contributed equally to this work. †lt.hsu@polyu.edu.hk ping/localization dataset collected in highly-urbanized en-vironments with a full sensor-suite. The dataset includes 13 trajectories collected in San Francisco and Hong Kong, covering a total length of over 40 kilometers. Our dataset includes a wide variety of urban terrains: urban canyons, bridges, tunnels, sharp turns, etc. More importantly, our dataset includes information from LIDAR, cameras, IMU, and GNSS receivers. Now the dataset is publicly available through the link in the footnote 1.

## Problem Addressed

Mapping and localization in highly urbanized scenes remain challenging: LiDAR- and camera-based methods struggle with numerous dynamic objects, GNSS suffers signal loss and multipath, and IMUs drift. Existing public datasets inadequately address these urban challenges or lack sufficient sensor information.

## Key Contributions

- First large-scale full-sensor-suite dataset focused on urban mapping and localization challenges.
- 13 trajectories from San Francisco and Hong Kong totaling over 40 kilometers, covering urban canyons, bridges, tunnels, and sharp turns.
- Full sensor suite: one LiDAR, six 360-degree cameras (one in Hong Kong), one IMU, and one GNSS receiver, with calibration logs.
- Urbanization measure for localization defined and evaluated across existing mapping and localization datasets.
- Public release through a dataset website with related APIs for users.

## Conclusions

UrbanLoco provides a publicly available full-sensor-suite dataset collected in highly urbanized environments, including over 40 kilometers of trajectories across San Francisco and Hong Kong. It fills the gap of existing datasets for benchmarking mapping and localization in challenging urban scenes.
