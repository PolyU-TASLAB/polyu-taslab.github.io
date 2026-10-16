---
title: Indoor altitude estimation assisted by inertial compensation and online floor modeling
authors:
- Ming Xia
- Jiale Wang
- Chuang Shi
- Weisong Wen
publisher: Measurement Science and Technology
date: '2024-09-05'
doi: https://doi.org/g8t54m
image: images/papers/cards/2024-xia-indoor-altitude-estimation-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Xia_2024_Meas._Sci._Technol._35_126302.pdf
tags:
- altitude estimation
- inertial compensation
- floor modeling
- gait classification
- indoor positioning
citation_id: 10.1088/1361-6501/ad7487
---

## Abstract

Indoor pedestrian altitude information plays a key role in such applications as emergency relief and military reconnaissance. However, height errors of inertial positioning grow without boundary because of the altitude channel divergence of the Strap-down Inertial Navigation
System. This article proposes a new vertical location method based on the foot-mounted Inertial
Measurement Unit and online floor modeling. First, the number of stairs at each step is calculated after the height of each step is corrected by the error compensation model. Second, the prior height is estimated by utilizing the number of stairs and the stair height. Then, the key point library related to the floor is built online. Finally, the error correction of the vertical displacement is carried out by matching the prior height with the key point library. The gait classification shows that the accuracy based on the error compensation model can reach up to
99%. Moreover, the maximum altitude error is less than 1 m and the accumulated vertical positioning errors are eliminated completely when a pedestrian walks up and down inside a multi-story building, and all these have verified accuracy and robustness of vertical indoor positioning.

## Problem Addressed

Indoor pedestrian height errors from inertial positioning grow without bound because of altitude channel divergence of the strapdown inertial navigation system.

## Key Contributions

- Vertical positioning method based on foot-mounted IMU and online floor modeling
- Error compensation model correcting the height of each step and counting stairs per step
- Prior height estimated from stair count and stair height, with a floor key-point library built online
- Vertical displacement corrected by matching prior height against the key-point library

## Conclusions

Gait classification based on the error compensation model reaches up to 99% accuracy. The maximum altitude error is less than 1 m, and accumulated vertical positioning errors are eliminated completely when a pedestrian walks up and down inside a multi-story building, verifying the accuracy and robustness of vertical indoor positioning.
