---
title: GNSS Outliers Mitigation in Urban Areas Using Sparse Estimation Based on Factor Graph Optimization
authors:
- Xiwei Bai
- Weisong Wen
- Guohao Zhang
- Hoi-Fung Ng
- Li-Ta Hsu
publisher: 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC)
date: '2022-10-08'
doi: https://doi.org/g7kbfv
image: images/papers/cards/2022-bai-gnss-outliers-mitigation.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/GNSS_Outliers_Mitigation_in_Urban_Areas_Using_Sparse_Estimation_Based_on_Factor_Graph_Optimization.pdf
tags:
- Global navigation satellite system
- Urban areas
- Redundancy
- Receivers
- Position measurement
- Reflection
- Frequency estimation
citation_id: doi:10.1109/ITSC55140.2022.9921906
---

## Abstract

Global navigation satellite system (GNSS) plays a crucial role in providing the globally referenced positioning for self-driving systems. 
Unfortunately, the numerous multipath or non-line-of-sight (NLOS) receptions (known as outlier observations) caused by the signal reflections from buildings reduce the positioning accuracy of GNSS in dense urban environments. The recently investigated factor graphbased GNSS positioning formulation simultaneously considers the historical information, which significantly increases the measurement redundancy of state estimation. Taking this advantage, this paper proposes an outlier mitigation method where the bias involved in the outliers is estimated simultaneously with the position of the receiver. Specifically, the outliers are firstly detected using a pre-trained deep learning network. Secondly, an unknown variable associated with the bias is assigned to each identified outlier measurement. 
Then the position of the GNSS receiver, together with the bias of outlier measurements, is estimated simultaneously via the factor graph optimization (FGO) based on the pseudorange measurements and Doppler frequency shift. Finally, the effectiveness of the proposed method is validated using a dataset collected in the urban canyon by a low-cost automobilelevel GNSS receiver.

## Problem Addressed

Multipath and NLOS receptions caused by building reflections introduce outlier observations that severely reduce GNSS positioning accuracy in dense urban environments. Reliable positioning for self-driving systems requires these outliers to be detected and their effects mitigated.

## Key Contributions

- Pre-trained deep learning network to detect GNSS outlier measurements
- Unknown bias variable assigned to each identified outlier, estimated jointly with receiver position via factor graph optimization
- Sparse estimation over the factor-graph GNSS formulation integrating multi-epoch history to guarantee measurement redundancy
- Validation on urban-canyon data collected by a low-cost automobile-grade GNSS receiver

## Conclusions

Outlier measurements were identified by the deep learning network and their associated biases were estimated simultaneously with the receiver state using pseudorange and Doppler measurements. Preliminary results on data collected in urban Hong Kong showed that the impacts of GNSS outliers were mitigated for positioning. The achievable performance is limited by measurement redundancy, and future work includes adaptive covariance modeling for outlier measurements and evaluation on more urban data.
