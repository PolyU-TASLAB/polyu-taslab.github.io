---
title: 'Enhancing LEO-GNSS Positioning in Urban Canyons: A Factor Graph Optimization Approach with StarLink Simulations'
authors:
- Yixin Gao
- Weisong Wen
- Xikun Liu
- Feng Huang
- Jiahao Hu
- Dongzhe Su
publisher: 2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC)
date: '2025-11-18'
doi: https://doi.org/hccr4j
image: images/papers/cards/2025-gao-enhancing-leognss-positioning.jpg
citation_id: doi:10.1109/ITSC60802.2025.11423756
---

## Abstract

Extensive research has explored augmenting GNSS positioning with LEO satellites to enhance urban accuracy and reliability. However, effectively integrating LEO and GNSS constellations remains an open challenge. To address this, this paper proposes a scalable, open-source
Factor
Graph
Optimization (FGO) framework for LEO-GNSS positioning, designed to seamlessly integrate additional sensors. By jointly optimizing pseudorange and Doppler shift measurements from both constellations, the framework aims to improve positioning accuracy and stability. Validation using complex urban canyon datasets from Hong Kong and simulated Starlink signals demonstrates notable accuracy improvements over GNSS-only systems. Furthermore, this study releases the first open-source
FGO-based
LEO-GNSS fusion positioning algorithm, providing a foundational platform for autonomous systems research.

## Problem Addressed

Augmenting GNSS with LEO satellites promises better urban positioning accuracy and reliability, but effectively integrating LEO and GNSS constellations remains an open challenge.

## Key Contributions

- Scalable, extensible factor graph optimization framework for LEO-GNSS positioning, integrable with IMU and LiDAR
- Joint optimization of pseudorange and Doppler shift measurements from both LEO and GNSS constellations
- Validation on Hong Kong urban canyon datasets with simulated Starlink signals
- First open-source FGO-based LEO-GNSS fusion positioning algorithm

## Conclusions

Simulations in Hong Kong's high-density urban canyons show the FGO framework with simulated LEO signals achieves a 47.32% reduction in 2D positioning mean error compared to standalone GNSS. Acknowledged limitations include the omission of multipath effects in the LEO signal simulation, Starlink not being designed for dedicated PNT services, and a 15-degree elevation mask reflecting open-sky rather than severe urban blockage.
