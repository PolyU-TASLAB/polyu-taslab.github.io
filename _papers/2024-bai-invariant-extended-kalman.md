---
title: Invariant Extended Kalman Filtering for Pedestrian Deep-Inertial Odometry
authors:
- Shiyu Bai
- Weisong Wen
- Yue Yu
- Li-Ta Hsu
publisher: The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences
date: '2024-10-21'
doi: https://doi.org/g8t5nb
image: images/papers/cards/2024-bai-invariant-extended-kalman.jpg
citation_id: doi:10.5194/isprs-archives-xlviii-4-2024-607-2024
---

## Abstract

Indoor localization for pedestrians, which relies solely on inertial odometry, has been a topic of great interest. Its significance lies in its ability to provide positioning solutions independently, without the need for external data. Although traditional strap-down inertial navigation shows rapid drift, the introduction of pedestrian dead reckoning (PDR), and artificial intelligence (AI) has enhanced the applicability of inertial odometry for indoor localization. However, inertial odometry continues to be affected by drift, inherent to the nature of dead reckoning. This implies that even a slight error at a given moment can lead to a significant decrease in accuracy after continuous integration operations. In this paper, we propose a novel approach aimed at enhancing the positioning accuracy of inertial odometry. Firstly, we derive a learning-based forward speed using inertial measurements from a smartphone. Unlike mainstream methods where the learned speed is directly used to determine the position, we use the forward speed combined with non-holonomic constraint (NHC) as a measurement to update the state predicted within a strap-down inertial navigation framework. 
Secondly, we employ an invariant extended Kalman filter (IEKF)-based state estimation to facilitate fusion to cope with the nonlinearity arising from the system and measurement model. Experimental tests are carried out in different scenarios using an iPhone 
12, and traditional methods, including PDR, robust neural inertial navigation (RONIN), and the EKF-based method, are compared. 
The results suggest that the method we propose surpasses these traditional methods in performance.

## Problem Addressed

Pedestrian indoor localization relying solely on inertial odometry suffers from drift inherent to dead reckoning, where even small errors accumulate through continuous integration and significantly degrade positioning accuracy.

## Key Contributions

- Deep-inertial odometry based on velocity updates, with a neural network regressing forward speed from IMU data
- Learned forward speed combined with non-holonomic constraint as measurement updates within a strapdown inertial navigation framework
- Avoids the influence of heading uncertainty that affects mainstream direct-position learning methods
- Invariant extended Kalman filter integration model coping with system and measurement nonlinearity, outperforming EKF-based fusion

## Conclusions

Experiments conducted in different scenarios using an iPhone 12 show that the proposed IEKF-based deep-inertial odometry outperforms traditional methods, including PDR, RONIN, and the EKF-based method.
