---
title: SMARTPHONE LEVEL INDOOR/OUTDOOR UBIQUITOUS PEDESTRIAN POSITIONING 3DMA GNSS/VINS INTEGRATION USING FGO
authors:
- H.-Y. Ho
- H.-F. Ng
- Y.-T. Leung
- W. Wen
- L.-T. Hsu
- Y. Luo
publisher: The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences
date: '2023-05-25'
doi: https://doi.org/g8t572
image: images/papers/cards/2023-ho-smartphone-level-indooroutdoor.jpg
citation_id: doi:10.5194/isprs-archives-xlviii-1-w1-2023-175-2023
---

## Abstract

This paper discusses ubiquitous smartphone pedestrian positioning challenges in urban canyons and GNSS-denied areas such as indoor spaces. Existing sensor-based techniques, including GNSS, INS, and VIO, have limitations that affect positioning accuracy and reliability. A machine learning-based approach is suggested to employ Support Vector Machine (SVM) to classify indoor/outdoor (IO) detection using GNSS measurement data. The proposed system integrates local estimates on VIO and 3D mapping aided (3DMA) 
GNSS measurements using Factor Graph Optimization (FGO) with an IO detection switch to estimate precise pose and eliminate global drift. The effectiveness of the system is evaluated through real-world experiments that produce notable outcomes.

## Problem Addressed

Ubiquitous smartphone pedestrian positioning is challenged in urban canyons and GNSS-denied indoor spaces, where GNSS, INS, and VIO each have limitations that affect positioning accuracy and reliability.

## Key Contributions

- Support Vector Machine classification for indoor/outdoor detection using GNSS measurement data
- Integration of VIO local estimates and 3DMA GNSS measurements via factor graph optimization
- Indoor/outdoor detection switch enabling precise local pose estimation and global drift elimination

## Conclusions

The FGO-based framework integrating VIO and 3DMA GNSS measurements with an indoor/outdoor detection switch enables precise local pose estimation and eliminates global drift. Real-world experiments produced notable outcomes demonstrating the system's effectiveness. Limitations include a training model tied to a single smartphone device and a campus-only dataset, leaving generalization to other environments for future work.
