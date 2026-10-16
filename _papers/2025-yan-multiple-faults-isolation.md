---
title: Multiple Faults Isolation for Multiconstellation GNSS Positioning Through Incremental Expansion of Consistent Measurements
authors:
- Penggao Yan
- Yingjie Hu
- Welson Wen
- Li-Ta Hsu
publisher: IEEE Sensors Journal
date: '2025-02-15'
doi: https://doi.org/hccr4g
citation_id: doi:10.1109/JSEN.2024.3524434
---

## Abstract

Fast and accurate fault detection and isolation (FDI) for multiple faults is crucial for satellite navigation systems. However, conventional deletion-based greedy search methods suffer from swamping effects, i.e., wrongly excluding healthy measurements, which leads to degradation in positioning performance after executing the isolation. This study proposes an incrementally expanding algorithm to isolate multiple faulty measurements in the multiconstellation global navigation satellite system (GNSS) positioning. The proposed algorithm is designed to find the most consistent set by incrementally expanding the minimum basic set with fault-free assumption. In each iteration, the no-fault hypothesis testing is conducted on the ordered studentized and jackknife residuals, enabling the correction of the fault-free assumption made in constructing the minimum basic set. The isolation performance and its impacts on positioning accuracy are evaluated in a worldwide simulation. The proposed method shows a 26% reduction in the swamping event rate and a 75% reduction in the mean postisolation positioning error, compared to the deletion-based greedy search method. Through Monte Carlo simulations, the stability of the proposed method regarding the number of faults and the fault magnitude is demonstrated. An application to the real-world dataset with artificially injected bias is also studied, showing a reduced postisolation positioning error.

## Problem Addressed

Deletion-based greedy search methods for multiple-fault detection and isolation in multiconstellation GNSS suffer from swamping effects, wrongly excluding healthy measurements and degrading positioning performance after isolation.

## Key Contributions

- Incrementally expanding algorithm isolating multiple faulty measurements in multiconstellation GNSS positioning
- Search for the most consistent measurement set by expanding a minimum basic set built under a fault-free assumption
- Per-iteration no-fault hypothesis testing on ordered studentized and jackknife residuals, correcting the initial fault-free assumption
- Worldwide simulation evaluation of isolation performance and its impact on positioning accuracy

## Conclusions

Compared with the deletion-based greedy search method, the proposed method reduces the swamping event rate by 26% and the mean post-isolation positioning error by 75% in worldwide simulations. Monte Carlo simulations demonstrate stability with respect to the number of faults and fault magnitude, and a real-world dataset with artificially injected bias confirms reduced post-isolation positioning error.
