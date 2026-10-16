---
title: Time-Correlated Window-Carrier-Phase-Aided GNSS Positioning Using Factor Graph Optimization for Urban Positioning
authors:
- Xiwei Bai
- Weisong Wen
- Li-Ta Hsu
publisher: IEEE Transactions on Aerospace and Electronic Systems
date: '2022-08-01'
doi: https://doi.org/gpsz9z
image: images/papers/cards/2022-bai-timecorrelated-windowcarrierphaseaided-gnss.jpg
citation_id: doi:10.1109/TAES.2022.3149730
---

## Abstract

This paper proposes an improved global navigation satellite system (GNSS) positioning method that explores the time correlation between consecutive epochs of the code and carrier phase measurements which significantly increases the robustness against outlier measurements. Instead of relying on the time difference carrier phase (TDCP) which only considers two neighboring epochs using an extended Kalman filter (EKF) estimator, this paper proposed to employ the carrier-phase measurements inside a window, the so-called window carrier-phase (WCP), to constrain the states inside a factor graph. 
A left null space matrix is employed to eliminate the shared unknown ambiguity variables and therefore, correlated the associated states inside the WCP. Then the pseudorange, Doppler, and the constructed WCP measurements are integrated simultaneously using factor graph optimization (FGO) to estimate the state of the GNSS receiver. We evaluated the performance of the proposed method in two typical urban canyons in Hong Kong, achieving the mean positioning error of 1.76 meters and 2.96 meters, respectively, using the automobile-level GNSS receiver. 
Meanwhile, the effectiveness of the proposed method is further evaluated using a low-cost smartphone level GNSS receiver and similar improvement is also obtained, compared with several existing GNSS positioning methods.

## Problem Addressed

GNSS positioning in urban canyons suffers from excessive outlier measurements caused by surrounding high-rise buildings. EKF-based time-difference carrier phase methods exploit only two neighboring epochs and cannot fully use the time correlation of carrier-phase measurements.

## Key Contributions

- Window carrier-phase (WCP) constraint exploiting time correlation of code and carrier-phase measurements across multiple epochs.
- Left null space matrix eliminates shared unknown ambiguity variables, correlating states inside the WCP.
- Simultaneous fusion of pseudorange, Doppler, and WCP measurements via factor graph optimization.
- Validation with automobile-level and smartphone-level GNSS receivers in Hong Kong urban canyons.

## Conclusions

The method achieved mean positioning errors of 1.76 meters and 2.96 meters in two typical Hong Kong urban canyons using an automobile-level GNSS receiver, outperforming several existing GNSS positioning methods. Similar improvement was obtained with a low-cost smartphone-level receiver. A remaining limitation is the assumption of constant integer ambiguity, motivating future cycle-slip detection within the factor graph.
