---
title: UrbanNav:An Open-Sourced Multisensory Dataset for Benchmarking Positioning Algorithms Designed for Urban Areas
authors:
- Li-Ta Hsu
- Nobuaki Kubo
- Weisong Wen
- Wu Chen
- Zhizhao Liu
- Taro Suzuki
- Junichi Meguro
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2021-10-13'
doi: https://doi.org/g8t45f
image: images/papers/cards/2021-hsu-urbannavan-opensourced-multisensory.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/UrbanNav.pdf
tags:
- UrbanNav
- Dataset
citation_id: doi:10.33012/2021.17895
---

## Abstract

Urban canyon is typical in megacities like Hong Kong and Tokyo. Accurate positioning in urban canyons remains a challenging problem for the applications with navigation requirements, such as the navigation for pedestrian, autonomous driving vehicles and unmanned aerial vehicles. The GNSS positioning can be significantly degraded in urban canyons, due to the signal blockage by tall buildings. The visual positioning and LiDAR positioning can be considerably affected by numerous dynamic objects. To facilitate the research and development of robust, accurate and precise positioning using multiple sensors in urban canyons, we build a multi-sensoroy dataset collected in diverse challenging urban scenarios in Hong Kong and Tokyo, that provides full-suite sensor data, which includes GNSS, INS, LiDAR and cameras. We call this open-sourced dataset, UrbanNav. In 2019, we formed a joint working group under the joint efforts from International Association of Geodesy (IAG) and ION. This working group is currently under Sub-Commission 4.1: Emerging Positioning Technologies and GNSS Augmentations of IAG. After consolidating the suggestions and comments from intenational navigation researchers, the objectives of this work group are: 1. Open-sourcing positioning sensor data, including GNSS, INS, LiDAR and cameras collected in Asian urban canyons; 2. Raising the awareness of the urgent navigation requirement in highly-urbanized areas, especially in Asian-Pacific regions; 3. Providing an integrated online platform for data sharing to facilitate the development of navigation solutions of the research community; and 4. Benchmarking positioning algorithms based on the open-sourcing data. Currently, two pilot dataset can be downloaded by the link in the following. https://www.polyu-ipn-lab.com/download We also provide a GitHub page to answer possible issues that users may encounter. Meanwhile, we also provide example usage of the dataset for applications of LiDAR simultaneous localization and mapping (SLAM) and visual-inertial navigation system (VINS), etc. https://github.com/weisongwen/UrbanNavDataset In this conference paper, we will introduce the detail sensors setup, data format, the calibration of the intrinsic/extrinsic parameters, and the ground truth generation. We believe this opensource dataset can facilitate to identify the challenges of different sensors in urban canyons. Finally we will address the future maintenance directions of the UrbanNav dataset including the following: 1. Building a website to let the researchers upload their paper and result that evaluated based on the open-source data in terms of the proposed criteria. 2. Identifying the experts in the field to design the assessment criteria for different positioning algorithms. 3. Reporting the performance of the state-of-the-art positioning and integration algorithms in the urban canyons every 2 years.

## Problem Addressed

Accurate positioning in urban canyons remains difficult because tall buildings degrade GNSS signals and numerous dynamic objects affect visual and LiDAR positioning, while open multisensory datasets for such environments are scarce.

## Key Contributions

- UrbanNav, an open-sourced multisensory dataset collected in challenging urban scenarios in Hong Kong and Tokyo
- Full-suite sensor data including GNSS, INS, LiDAR, and cameras for benchmarking urban positioning
- Joint IAG and ION working group promoting open data sharing for Asian urban canyon navigation research
- Online data-sharing platform with example usage for LiDAR SLAM and GitHub-based user support

## Conclusions

Two pilot datasets are publicly released for download, accompanied by example usage for applications such as LiDAR simultaneous localization and mapping. The initiative aims to raise awareness of navigation needs in highly urbanized Asian-Pacific regions and to benchmark positioning algorithms on open data.
