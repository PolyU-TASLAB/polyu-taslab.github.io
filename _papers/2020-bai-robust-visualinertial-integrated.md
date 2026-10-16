---
title: Robust Visual-Inertial Integrated Navigation System Aided by Online Sensor Model Adaption for Autonomous Ground Vehicles in Urban Areas
authors:
- Xiwei Bai
- Weisong Wen
- Li-Ta Hsu
publisher: Remote Sensing
date: '2020-05-25'
doi: https://doi.org/ghrstp
image: images/papers/cards/2020-bai-robust-visualinertial-integrated.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/RVIN.pdf
tags:
- visual-inertial integrated navigation system (VINS)
- VINS
- dynamic objects
- adaptive tuning
- positioning
- autonomous systems
- urban canyons
citation_id: doi:10.3390/rs12101686
---

## Abstract

The visual-inertial integrated navigation system (VINS) has been extensively studied over the past decades to provide accurate and low-cost positioning solutions for autonomous systems.
Satisfactory performance can be obtained in an ideal scenario with sufficient and static environment features. However, there are usually numerous dynamic objects in deep urban areas, and these moving objects can severely distort the feature-tracking process which is critical to the feature-based
VINS. One well-known method that mitigates the effects of dynamic objects is to detect vehicles using deep neural networks and remove the features belonging to surrounding vehicles. However, excessive feature exclusion can severely distort the geometry of feature distribution, leading to limited visual measurements. Instead of directly eliminating the features from dynamic objects, this study proposes to adopt the visual measurement model based on the quality of feature tracking to improve the performance of the VINS. First, a self-tuning covariance estimation approach is proposed to model the uncertainty of each feature measurement by integrating two parts: (1) the geometry of feature distribution (GFD); (2) the quality of feature tracking. Second, an adaptive M-estimator is proposed to correct the measurement residual model to further mitigate the effects of outlier measurements, like the dynamic features. Different from the conventional M-estimator, the proposed method effectively alleviates the reliance on the excessive parameterization of the M-estimator. Experiments were conducted in typical urban areas of Hong Kong with numerous dynamic objects. The results show that the proposed method could effectively mitigate the effects of dynamic objects and improved accuracy of the VINS is obtained when compared with the conventional VINS method.

## Problem Addressed

Dynamic objects in deep urban areas severely distort the feature-tracking process critical to feature-based visual-inertial navigation systems. Removing the features of surrounding vehicles can in turn distort the geometry of the feature distribution and limit visual measurements.

## Key Contributions

- Adapt the visual measurement model online based on feature tracking quality rather than eliminating features.
- Self-tuning covariance estimation combining geometry of feature distribution and quality of feature tracking.
- Adaptive M-estimator corrects the measurement residual model, alleviating reliance on excessive parameterization.
- Experiments conducted in typical urban areas of Hong Kong with numerous dynamic objects.

## Conclusions

The online sensor model adaption effectively mitigates the effects of dynamic objects, and improved VINS accuracy is obtained compared with the conventional VINS method.
