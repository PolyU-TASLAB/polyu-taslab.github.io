---
title: 'GNSS/LiDAR Integration Aided by Self-Adaptive Gaussian Mixture Models in Urban Scenarios: An Approach Robust to Non-Gaussian Noise'
authors:
- Weisong Wen
- Xiwei Bai
- Li-Ta Hsu
- Tim Pfeifer
publisher: 2020 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2020-04-01'
doi: https://doi.org/g8tzcw
image: images/papers/cards/2020-wen-gnsslidar-integration-aided.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/GLIA.pdf
tags:
- GNSS
- LiDAR
- Positioning
- Non-Gaussian noise
- Factor graph optimization
- Gaussian mixture models
- Urban canyon
citation_id: doi:10.1109/PLANS46316.2020.9110157
---

## Abstract

Accurate and globally referenced positioning is crucial to autonomous systems with navigation requirements, such as unmanned aerial vehicles (UAV) and autonomous driving vehicles (ADV). GNSS/LiDAR integration is a popular sensor pair that can provide outstanding positioning performance in open areas. However, the accuracy is significantly degraded in urban canyons, due to the excessive unmodeled non-Gaussian GNSS outliers caused by multipath effects and none-line-of-sight (NLOS) receptions. As a result, the violation of the Gaussian assumption can severely distort the sensor fusion process, such as the extended Kalman filter (EKF). To mitigate the effects of these non-Gaussian GNSS outliers, this paper proposes to leverage the Gaussian mixture model (GMM) to describe the potential noise of GNSS positioning and apply it to further sensor fusion. Instead of relying on excessive offline parameterization and tuning, the parameters of the GMM are estimated simultaneously based on the residuals of the GNSS measurements using an expectation-maximization (EM) algorithm. Then the state-of-the-art factor graph optimization (FGO) is applied to integrate the GNSS positioning and LiDAR odometry based on the estimated GMM. The experiment in a typical urban canyon is conducted to validate the performance of the proposed method. The result shows that the GMM can effectively mitigate the effects of GNSS outliers and improves positioning performance.

## Problem Addressed

GNSS/LiDAR integration degrades in urban canyons because excessive unmodeled non-Gaussian GNSS outliers from multipath and NLOS receptions violate the Gaussian noise assumption underlying fusion methods such as the extended Kalman filter.

## Key Contributions

- Gaussian mixture model (GMM) describes the potential non-Gaussian noise of GNSS positioning.
- GMM parameters estimated online from GNSS measurement residuals via expectation-maximization, without offline tuning.
- Factor graph optimization fuses GNSS positioning and LiDAR odometry under the estimated GMM.
- Validated with a real-world dataset recorded in Hong Kong urban canyons.

## Conclusions

The self-adaptive GMM effectively mitigates the effects of GNSS outliers and improves the positioning performance of GNSS/LiDAR integration in a typical urban canyon. The model can easily be adapted to other sensors such as vision or radar.
