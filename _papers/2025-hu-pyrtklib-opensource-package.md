---
title: 'pyrtklib: An Open-Source Package for Tightly Coupled Deep Learning and GNSS Integration for Positioning in Urban Canyons'
authors:
- Runzhi Hu
- Penghui Xu
- Yihan Zhong
- Weisong Wen
publisher: IEEE Transactions on Intelligent Transportation Systems
date: '2025-04-11'
doi: https://doi.org/g9hrns
image: images/papers/cards/2025-hu-pyrtklib-opensource-package.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/pyrtklib_An_Open-Source_Package_for_Tightly_Coupled_Deep_Learning_and_GNSS_Integration_for_Positioning_in_Urban_Canyons.pdf
- type: source
  text: code
  link: https://github.com/IPNL-POLYU/pyrtklib
tags:
- Artificial intelligence
- deep learning
- GNSS
- RTKLIB
repo: https://github.com/IPNL-POLYU/pyrtklib
citation_id: doi:10.1109/TITS.2025.3552691
---

## Abstract

Global Navigation Satellite Systems (GNSS) are crucial for intelligent transportation systems (ITS), providing essential positioning capabilities globally. However, in urban canyons, the GNSS performance could significantly degraded due to the blockage of direct GNSS signals. The pseudorange measurements are largely affected and the conventional model of weighting observations is not suitable in urban canyons. This paper addresses these challenges by integrating
Artificial Intelligence (AI), specifically deep learning, into GNSS positioning process to enhance positioning accuracy. Traditional methods have primarily focused on pseudorange correction due to the absence of ground truth for weight estimation. In response, we propose an innovative indirect training approach using deep learning to optimize both pseudorange bias and weight estimation, aiming to minimize the positioning errors. To support this integration, we developed pyrtklib, a Python binding for the open-source RTKLIB tool, bridging the gap between traditional GNSS algorithms, typically developed in Fortran or C, and modern Python-based AI frameworks. Comparative analyses demonstrate that our method surpasses established tools like goGPS and RTKLIB in positioning accuracy, marking a significant advancement in the field. The source code of tightly coupled deep learning and GNSS integration, along with pyrtklib, is available on GitHub at https://github.com/ebhrz/TDL-GNSS and https://github.com/IPNL-POLYU/pyrtklib.

## Problem Addressed

GNSS positioning in urban canyons is severely degraded by signal blockage, which corrupts pseudorange measurements and invalidates conventional observation weighting models. Integrating deep learning with GNSS is further hindered by the absence of ground truth for weight estimation and by the gap between C/Fortran GNSS tools and Python-based AI frameworks.

## Key Contributions

- Network that predicts pseudorange biases, tightly coupled into least-squares correction of GNSS measurements
- Network that predicts a weight for each measurement, applied within the weighted least squares process
- Network that jointly predicts weights and biases per measurement to improve positioning accuracy
- Indirect training scheme that optimizes bias and weight estimation without ground-truth labels
- Open-sourced pyrtklib, a Python binding for RTKLIB auto-generated via metaprogramming with pycparser and pybind11

## Conclusions

The tightly coupled deep learning aided GNSS SPP method outperformed RTKLIB and goGPS, with TDL-BW (simultaneously predicting weights and biases) performing best by effectively distinguishing LOS from NLOS satellites. Both pyrtklib and the deep learning subsystem are open source, and pyrtklib was downloaded approximately 20,000 times over six months. The framework is designed to accommodate more advanced architectures such as CNNs, RNNs, and transformers.
