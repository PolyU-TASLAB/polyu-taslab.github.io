---
title: An Efficient Detector for Faulty GNSS Measurements Detection With Non-Gaussian Noises
authors:
- Penggao Yan
- Baoshan Song
- Xiao Xia
- Weisong Wen
- Li-Ta Hsu
publisher: arXiv
date: '2025-07-05'
doi: https://arxiv.org/abs/2507.03987
image: images/papers/cards/2025-yan-efficient-detector-faulty.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2507.03987v1.pdf
tags:
- Faulty GNSS Measurements
- Non-Gaussian Noise
citation_id: arXiv:2507.03987
---

## Abstract

Fault detection is crucial to ensure the reliability of navigation systems. However, mainstream fault detection methods are developed based on Gaussian assumptions on nominal errors, while current attempts at non-Gaussian fault detection are either heuristic or lack rigorous statistical properties. The performance and reliability of these methods are challenged in real-world applications. This paper proposes the jackknife detector, a fault detection method tailored for linearized pseudorange-based positioning systems under non-Gaussian nominal errors. Specifically, by leveraging the jackknife technique, a test statistic is derived as a linear combination of measurement errors, eliminating the need for restrictive distributional assumptions while maintaining computational efficiency. A hypothesis test with the Bonferroni correction is then constructed to detect potential faults in measurements. Theoretical analysis proves the equivalence between the jackknife detector and the solution separation (SS) detector, while revealing the former’s superior computational efficiency. Through a worldwide simulation and a real-world satellite clock anomaly detection experiment——both involving non-Gaussian nominal errors——the proposed jackknife detector demonstrates equivalent detection performance to the SS detector but achieves a fourfold improvement in computational efficiency. These results highlight the jackknife detector’s substantial potential for real-time applications requiring robust and efficient fault detection in non-Gaussian noise environments.

## Problem Addressed

Mainstream GNSS fault detection methods assume Gaussian nominal errors, while existing non-Gaussian approaches are heuristic or lack rigorous statistical properties, challenging their performance and reliability in real-world applications.

## Key Contributions

- Jackknife detector for linearized pseudorange-based positioning systems under non-Gaussian nominal errors
- Test statistic derived as a linear combination of measurement errors, eliminating restrictive distributional assumptions
- Hypothesis test with Bonferroni correction; theoretical proof of equivalence with the solution separation detector
- Validated through worldwide simulation and real-world satellite clock anomaly detection

## Conclusions

The jackknife detector demonstrates equivalent detection performance to the solution separation detector while achieving a fourfold improvement in computational efficiency. Both the worldwide simulation and the real-world satellite clock anomaly experiment, involving non-Gaussian nominal errors, highlight its potential for real-time robust fault detection.
