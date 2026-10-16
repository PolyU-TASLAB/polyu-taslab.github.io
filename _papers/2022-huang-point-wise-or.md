---
title: Point Wise or Feature Wise? A Benchmark Comparison of Publicly Available Lidar Odometry Algorithms in Urban Canyons
authors:
- Feng Huang
- Weisong Wen
- Jiachen Zhang
- Li-Ta Hsu
publisher: IEEE Intelligent Transportation Systems Magazine
date: '2022-11-01'
doi: https://doi.org/g8t5r4
image: images/papers/cards/2022-huang-point-wise-or.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Point_Wise_or_Feature_Wise.pdf
tags:
- Feature extraction
- Point cloud compression
- Real-time systems
- Laser radar
- Three-dimensional displays
- Heuristic algorithms
- Global navigation satellite system
- Autonomous systems
citation_id: doi:10.1109/MITS.2021.3092731
---

## Abstract

Robust and precise localization is essential for an autonomous system with navigation requirements. Lidar odometry (LO) has been extensively studied in the past decades to realize this goal. 
Satisfactory accuracy can be achieved in scenarios with abundant environmental features using existing LO algorithms. Unfortunately, the performance of the LO is significantly degraded in urban canyons with numerous dynamic objects and complex environmental structures. Meanwhile, it is still not clear from the existing literature which LO algorithms perform well in such challenging environments. To fill this gap, this article evaluates an array of popular and extensively studied LO pipelines using the data sets collected in urban canyons of Hong Kong. 
We present the results in terms of their positioning accuracy and computational efficiency. The three major factors dominating the performance of LO in urban canyons are concluded, including the egovehicle dynamic, moving objects, and the degree of urbanization. According to our experiment results, point wise accomplishes better accuracy in urban canyons while feature-wise achieves cost-efficiency and satisfactory positioning accuracy.
Authorized licensed use limited to: Hong Kong Polytechnic University. Downloaded on December 09,2024 at 10:46:50 UTC from IEEE Xplore. Restrictions apply. 

IEEE INTELLIGENT TRANSPORTATION SYSTEMS MAGAZINE • 157 • NOVEMBER/DECEMBER 2022 measurements occurring from moving objects can even introduce additional nonconvexity. Many variants of ICP have been proposed to improve its efficiency and accuracy, such as trimmed [26] and normal 
ICP [27]. Among these ICP variants, generalized-ICP (G-ICP) [16] is the most popular variant, with distinct accuracy. Instead of formulating the cost function directly by finding point-wise correspondence, the G-ICP, which benefits from standard ICP and the point-to-plane method introduced by Chen and Medioni [28], optimizes the transformation via a distribution-to-distribution fashion. Compared with conventional ICP, G-ICP explores the geometry correlation with points via distribution modeling. As a result, G-ICP is less sensitive to the initial guess compared with

## Problem Addressed

LiDAR odometry performance degrades significantly in urban canyons due to numerous dynamic objects and complex environmental structures, yet existing literature does not make clear which publicly available LO algorithms perform well in such challenging environments.

## Key Contributions

- Comprehensive benchmark of publicly available LiDAR odometry pipelines on urban-canyon datasets from Hong Kong
- Comparison in terms of positioning accuracy and computational efficiency
- Identification of three dominant degradation factors: ego-vehicle dynamics, moving objects, and degree of urbanization

## Conclusions

The benchmark concludes that point-wise methods achieve better accuracy in urban canyons, while feature-wise methods offer computational efficiency with satisfactory positioning accuracy. The performance of LO in urban canyons is dominated by the ego-vehicle dynamics, moving objects, and the degree of urbanization.
