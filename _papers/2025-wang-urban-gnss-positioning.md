---
title: 'Urban GNSS Positioning for Consumer Electronics: 3D Mapping and Advanced Signal Processing'
authors:
- Jiale Wang
- Ming Xia
- Deyou Zhang
- Weisong Wen
- Wu Chen
- Chuang Shi
publisher: IEEE Transactions on Consumer Electronics
date: '2025-05-01'
doi: https://doi.org/g9hrnq
image: images/papers/cards/2025-wang-urban-gnss-positioning.jpg
citation_id: doi:10.1109/tce.2025.3552892
---

## Abstract

Smartphones, as ubiquitous consumer electronics de-vices, rely heavily on Global Navigation Satellite Systems (GNSS) for various applications, including navigation and location-based services. However, the small-sized and low-cost patch antennas used in smartphones are particularly susceptible to multipath effects and signal degradation, posing significant challenges for accurate positioning in urban environments. To address these issues, this study introduces a 3D-mapping-aided Precise Point Position-ing (3DMA PPP) algorithm. The algorithm incorporates 3D build-ing models to exclude non-line-of-sight (NLOS) satellites, while mitigating potential multipath effects and thermal noise on line-of-sight (LOS) satellites using Doppler smoothing filters and an optimized carrier-to-noise ratio (C/N0)-dependent stochastic model. Experiments conducted with Xiaomi Mi8 and Huawei Mate40 smartphones demonstrate that the proposed method achieves po-sitioning errors within 2 m, while improving the positioning accuracy of low-cost GNSS receivers to sub-meter levels. The results show a more than 50% improvement in positioning accuracy compared to conventional algorithms, significantly enhancing the utility of consumer-grade devices for urban navigation. This work highlights the potential for advanced GNSS techniques to em-power consumer electronics with precise and reliable positioning capabilities.

## Problem Addressed

The small, low-cost patch antennas in smartphones are highly susceptible to multipath effects and signal degradation, making accurate GNSS positioning in urban environments a persistent challenge for consumer electronics.

## Key Contributions

- Dual-frequency multi-GNSS PPP model tailored for low-cost smart devices with inconsistent dual-frequency measurements
- Two-step rapid NLOS satellite detection using sky masks generated from 3D building models
- Doppler smoothing filter accounting for ionospheric cumulative error to mitigate multipath and thermal noise
- Optimized C/N0-dependent stochastic model for reweighting LOS satellite measurements

## Conclusions

The Doppler smoothing filter mitigates more than 70% of thermal noise and multipath error, and correlation analysis shows smartphone GNSS measurement error correlates strongly only with C/N0. Overall positioning performance improves by more than 50% over the conventional PPP algorithm; errors of Xiaomi Mi8 and Huawei Mate40 smartphones drop from more than 5 m to 1-2 m, while low-cost u-blox ZED-F9P and Septentrio Mosaic-X5 receivers reach sub-meter accuracy.
