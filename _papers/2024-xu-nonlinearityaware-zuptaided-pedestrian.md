---
title: Nonlinearity-Aware ZUPT-Aided Pedestrian Inertial Navigation Based on Cubature Kalman Filter in Urban Canyons
authors:
- Ruijie Xu
- Shichao Chen
- Shiyu Bai
- Weisong Wen
publisher: IEEE Transactions on Instrumentation and Measurement
date: '2024-01-01'
doi: https://doi.org/g8t54n
image: images/papers/cards/2024-xu-nonlinearityaware-zuptaided-pedestrian.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Nonlinearity-Aware_ZUPT-Aided_Pedestrian_Inertial_Navigation_Based_on_Cubature_Kalman_Filter_in_Urban_Canyons.pdf
tags:
- Cubature Kalman filter
- CKF
- inertial sensor
- nonlinearity
- pedestrian navigation
- zero-velocity detection
repo: https://github.com/RuijieXu0408/PINSdatasets-based-on-Xsens-IMU.
citation_id: doi:10.1109/TIM.2024.3451578
---

## Abstract

Urban pedestrian navigation is a challenging issue as the most popular positioning source, global navigation satellite systems (GNSSs), is severely affected by signal reflections or blockages from high-rise buildings. Unlike the GNSS, the inertial measurement unit (IMU) is less sensitive to environmental conditions but is, unfortunately, subject to drift over time. Applying the motion constraints, such as the zero-velocity update (ZUPT), is a promising solution for mitigating the drift. However, existing zero-velocity (ZV) detections can cause false results in urban scenarios involving more complex pedestrian motions. Meanwhile, the IMU-based model’s nonlinearity further reduces the accuracy of the state estimation. This article proposes a nonlinearity-aware ZUPT-aided pedestrian inertial navigation in urban canyons to fill this gap. Our method begins with a gait interval (GI)-aided dual-threshold ZV detection scheme to prevent false or missed detections in complex pedestrian motions. A ZUPT-aided inertial navigation based on cubature Kalman filter (CKF) is formed to mitigate the impact of nonlinearity. Several datasets are collected to validate the effectiveness of the proposed method. The experimental results demonstrate that the proposed method can detect ZV more accurately and estimate pedestrian location more precisely with the CKF than extended Kalman filter (EKF) and unscented Kalman filter (UKF)-based methods. Meanwhile, the time consumption of the proposed method is essentially on par with the UKF-based method. It achieves a balance between computational efficiency and accuracy, which provides a low-drift self-contained real-time inertial navigation for pedestrians when external positioning data are unavailable. To benefit the research community, we open-source our dataset via GitHub: https://github.com/RuijieXu0408/PINSdatasets-based-on-Xsens-IMU.

## Problem Addressed

Pedestrian navigation in urban canyons cannot rely on GNSS due to signal blockage and reflections, while IMU-based navigation drifts over time. Existing zero-velocity detections produce false results under complex pedestrian motions, and the nonlinearity of the IMU model further degrades state estimation accuracy.

## Key Contributions

- Gait interval-aided dual-threshold zero-velocity detection combining acceleration variance and angular rate energy detectors
- Fitting of detected pedestrian intervals to remove erroneously detected outliers during walking
- ZUPT-aided pedestrian inertial navigation based on the cubature Kalman filter to mitigate nonlinear errors
- Open-source dataset released via GitHub

## Conclusions

The method detects zero-velocity intervals more accurately under complex motions, and the CKF-based update outperforms conventional Kalman-filter-based methods. It reduces RMSE by 67.95% and 95.42% compared with EKF and UKF respectively in the long-distance experiment, and by 49.03% and 69.04% in the 60 x 38 m loop closure experiment. The approach balances computational efficiency and accuracy, providing high-precision real-time pedestrian inertial navigation in GNSS-challenged environments.
