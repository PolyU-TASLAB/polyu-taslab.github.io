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
image: images/papers/cards/2024-xia-indoor-altitude-estimation.jpg
citation_id: doi:10.1088/1361-6501/ad7487
---

## Abstract

Indoor pedestrian altitude information plays a key role in such applications as emergency relief and military reconnaissance. However, height errors of inertial positioning grow without boundary because of the altitude channel divergence of the Strap-down Inertial Navigation
System. This article proposes a new vertical location method based on the foot-mounted Inertial
Measurement Unit and online floor modeling. First, the number of stairs at each step is calculated after the height of each step is corrected by the error compensation model. Second, the prior height is estimated by utilizing the number of stairs and the stair height. Then, the key point library related to the floor is built online. Finally, the error correction of the vertical displacement is carried out by matching the prior height with the key point library. The gait classification shows that the accuracy based on the error compensation model can reach up to
99%. Moreover, the maximum altitude error is less than 1 m and the accumulated vertical positioning errors are eliminated completely when a pedestrian walks up and down inside a multi-story building, and all these have verified accuracy and robustness of vertical indoor positioning.

## Problem Addressed

Height errors of inertial indoor positioning grow without bound because of the altitude channel divergence of the strapdown inertial navigation system, limiting applications such as emergency relief and military reconnaissance.

## Key Contributions

- Vertical localization method combining a foot-mounted IMU with online floor modeling
- Error compensation model correcting per-step height before counting stairs at each step
- Prior height estimation from stair counts and stair height
- Online floor key point library matched against prior height to correct vertical displacement

## Conclusions

Gait classification based on the error compensation model reaches up to 99% accuracy. The maximum altitude error is less than 1 m and accumulated vertical positioning errors are completely eliminated when a pedestrian walks up and down inside a multi-story building, verifying the accuracy and robustness of the method.
