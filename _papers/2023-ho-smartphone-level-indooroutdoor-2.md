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
image: images/papers/cards/2023-ho-smartphone-level-indooroutdoor-2.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/isprs-archives-XLVIII-1-W1-2023-175-2023.pdf
citation_id: doi:10.5194/isprs-archives-XLVIII-1-W1-2023-175-2023
---

## Abstract

This paper discusses ubiquitous smartphone pedestrian positioning challenges in urban canyons and GNSS-denied areas such as indoor spaces. Existing sensor-based techniques, including GNSS, INS, and VIO, have limitations that affect positioning accuracy and reliability. A machine learning-based approach is suggested to employ Support Vector Machine (SVM) to classify indoor/outdoor (IO) detection using GNSS measurement data. The proposed system integrates local estimates on VIO and 3D mapping aided (3DMA) 
GNSS measurements using Factor Graph Optimization (FGO) with an IO detection switch to estimate precise pose and eliminate global drift. The effectiveness of the system is evaluated through real-world experiments that produce notable outcomes.

## Problem Addressed

Ubiquitous smartphone pedestrian positioning across urban canyons and GNSS-denied indoor spaces remains challenging, because GNSS, INS, and VIO each have limitations that degrade positioning accuracy and reliability in one or both regimes.

## Key Contributions

- Support Vector Machine classification of indoor/outdoor status using GNSS measurement data
- Factor graph optimization integrating VIO local estimates with 3DMA GNSS measurements
- Indoor/outdoor detection switch enabling precise local pose estimation while eliminating global drift
- Real-world experimental evaluation of the smartphone-based system

## Conclusions

The proposed FGO-based framework integrating VIO and 3DMA GNSS with an indoor/outdoor detection switch achieved precise local pose estimation and eliminated global drift, demonstrated through real-world experiments. Limitations remain: the trained SVM model is based on a single smartphone and may not generalize to other devices, and the dataset covers only a campus environment, leaving more dynamic and complex urban canyons unexplored.
