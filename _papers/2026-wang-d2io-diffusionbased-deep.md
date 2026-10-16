---
title: 'D2IO: Diffusion-Based Deep Inertial Odometry for Pedestrian Indoor Localization'
authors:
- Yingying Wang
- Shaoting Qiu
- Yulong Huang
- Weisong Wen
publisher: IEEE Transactions on Industrial Informatics
date: '2026-05-28'
doi: https://doi.org/hcb4mp
image: images/papers/cards/2026-wang-d2io-diffusionbased-deep.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/D2IO_Diffusion-Based_Deep_Inertial_Odometry_for_Pedestrian_Indoor_Localization.pdf
tags:
- Diffusion model
- Inertial navigation
- Internet of Things
- Velocity estimation
citation_id: doi:10.1109/TII.2026.3693775
---

## Abstract

Indoor localization has been in demand for decades, but no standard solution exists like outdoor global positioning system (GPS). Different from radio frequency-based solutions that require dedicated infrastructure and are susceptible to environmental disturbances, inertial sensors are an ideal choice for indoor localization due to their robustness to environmental variations and low power consumption. Although deep learning has improved the accuracy of open-loop inertial odometry, cumulative errors still pose a significant challenge. In this article, we propose D2IO, an inertial odometry framework that integrates the diffusion model with a transformer architecture. Specifically, the inertial signals are
first transformed into a gravity-aligned coordinate frame, followed by the diffusion probabilistic model to augment both the input inertial sequence and output velocity sequence. An inverted transformer framework is then employed to extract spatial and temporal features from each segmented variable. We train the model on a public dataset and evaluate its performance using a 20-h self-collected dataset. The superior results on the challenging evaluation in terms of accuracy and efficiency demonstrate the effectiveness of the proposed D2IO.

## Problem Addressed

Inertial sensors are attractive for infrastructure-free indoor localization, and deep learning has improved open-loop inertial odometry accuracy, but cumulative errors still pose a significant challenge for pedestrian positioning.

## Key Contributions

- D2IO framework integrating a diffusion probabilistic model with a transformer architecture for inertial odometry
- Gravity-aligned coordinate transformation of inertial signals, with diffusion-based augmentation of input inertial and output velocity sequences
- Inverted transformer extracting spatial and temporal features from segmented variables, with MLP velocity distribution projection
- Loss function constraining both velocity sequence generation and distribution formulation

## Conclusions

Trained on a public dataset and evaluated on a 20-hour self-collected dataset, D2IO outperforms state-of-the-art learning-based methods and typical diffusion-based sequence generation approaches in both accuracy and efficiency. Extensive ablation experiments validate the effectiveness of the system design. Future work will incorporate non-intrusive modalities such as WiFi received signal strength to calibrate cumulative inertial errors.
