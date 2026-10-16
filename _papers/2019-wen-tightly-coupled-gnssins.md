---
title: Tightly Coupled GNSS/INS Integration via Factor Graph and Aided by Fish-Eye Camera
authors:
- Weisong Wen
- Xiwei Bai
- Yin Chiu Kan
- Li-Ta Hsu
publisher: IEEE Transactions on Vehicular Technology
date: '2019-11-01'
doi: https://doi.org/ggtk79
image: images/papers/cards/2019-wen-tightly-coupled-gnssins.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/TCGI.pdf
tags:
- GNSS
- INS
- camera
- integration
- factor graph
- positioning
- autonomous driving
citation_id: doi:10.1109/TVT.2019.2944680
---

## Abstract

GNSS/INS integrated solution has been extensively studied over the past decades. However, its performance relies heavily on environmental conditions and sensor costs. The GNSS positioning can obtain satisfactory performance in the open area. Unfortunately, its accuracy can be severely degraded in a highly urbanized area, due to the notorious multipath effects and none-line-of-sight (NLOS) receptions. As a result, excessive GNSS out-liers occur, which causes a huge error in GNSS/INS integration. This paper proposes to apply a fish-eye camera to capture the sky view image to further classify the NLOS and line-of-sight (LOS) measurements. In addition, the raw INS and GNSS measurements are tightly integrated using a state-of-the-art probabilistic factor graph model. Instead of excluding the NLOS receptions, this paper makes use of both the NLOS and LOS measurements by treating them with different weightings. Experiments conducted in typical urban canyons of Hong Kong showed that the proposed method could effectively mitigate the effects of GNSS outliers, and an improved accuracy of GNSS/INS integration was obtained, when compared with the conventional GNSS/INS integration.

## Problem Addressed

GNSS/INS integration accuracy is severely degraded in highly urbanized areas because multipath effects and NLOS receptions produce excessive GNSS outliers. Conventional tightly coupled integration cannot handle these outliers effectively.

## Key Contributions

- Employs a fish-eye camera to capture sky view images and classify LOS and NLOS measurements
- Tightly integrates raw INS and GNSS measurements using a probabilistic factor graph model
- Re-weights LOS and NLOS measurements differently instead of excluding NLOS receptions
- Evaluates multiple GNSS standalone and tightly coupled integrations in Hong Kong urban canyons

## Conclusions

Experiments in typical Hong Kong urban canyons show the method effectively mitigates GNSS outliers compared with conventional EKF-based tightly coupled integration. The mean positioning error is reduced from 8.31 to 3.21 meters in urban canyon 1 and from 7.28 to 4.73 meters in urban canyon 2. Future work includes integrating LiDAR-based positioning and deep learning based image segmentation.
