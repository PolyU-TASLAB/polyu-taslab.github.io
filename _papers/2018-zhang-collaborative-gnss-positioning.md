---
title: Collaborative GNSS Positioning with the Aids of 3D City Models
authors:
- Guohao Zhang
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2018-10-26'
doi: https://doi.org/g8tzc8
image: images/papers/cards/2018-zhang-collaborative-gnss-positioning.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/CGPA.pdf
tags:
- GNSS
- NLOS
- 3D Model
- 3DMA GNSS
- V2V
citation_id: doi:10.33012/2018.15830
---

## Abstract

GNSS collaborative positioning receives great attention because of the rapid development of vehicle-to-vehicle (V2V) communication. Its current bottleneck is in urban areas. During the calculation of double difference of GNSS measurements between two receivers to obtain their relative positions, the notorious multipath effects and NLOS reception in the pseudorange measurement cannot be eliminated. Even worse, these effects become more severe due to the multipath effects of two receivers are aggregated. Recently, the studies explored the use of 3D city models to aid GNSS positioning are increasing. It is widely believed the3D map aided (3DMA) GNSS is a solution to mitigate or even correct the multipath and NLOS effects. This paper therefore investigates the potential to aid GNSS collaborative positioning using 3D city models. The 3D models are used in two phases. The first phase is in single receiver level. The models is used to exclude NLOS measurements based on GNSS shadow matching (SDM) positioning result. The second phase is in multi-receiver level. The 3D building model is used together with broadcast ephemeris data to generate the predicted GNSS positioning error map. Based on the error map, each receiver will be labelled as, good, medium and bad, conditions. The receiver labelled as bad condition will be improved by the receiver labelled as good condition. Five low-cost GNSS receivers are used to conduct a static experiment. According to the result, the positioning accuracy of the receiver located at deep urban canyon will be improved from 26.6 to 17.9 meters, where its SDM result is 19.3 meters.

## Problem Addressed

GNSS collaborative positioning via vehicle-to-vehicle communication is bottlenecked in urban areas, where double-difference relative positioning aggregates the multipath and NLOS effects of both receivers. Existing methods cannot reliably remove these errors.

## Key Contributions

- Uses 3D city models with GNSS shadow matching to exclude NLOS measurements at the single-receiver level
- Generates a predicted GNSS positioning error map from 3D building models and broadcast ephemeris
- Labels receivers as good, medium, or bad condition and lets good receivers aid bad ones
- Applies double-layer consistency checks during double-difference relative positioning
- Validates the algorithm in a static experiment with five low-cost GNSS receivers

## Conclusions

The experiment shows the positioning accuracy of a receiver in a deep urban canyon improves from 26.6 to 17.9 meters, compared with 19.3 meters from shadow matching alone. The 3D map aided collaborative algorithm achieves more accurate positioning than the conventional least squares method. Future work will improve the predicted error map accuracy and investigate error distribution caused by DOP distortion.
