---
title: 'Factor Graph Optimization for Tightly-Coupled GNSS Pseudorange/Doppler/Carrier Phase/INS Integration: Performance in Urban Canyons of Hong Kong'
authors:
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2022-10-20'
doi: https://doi.org/g8t5r2
buttons:
- type: manubot
  text: paper
  link: https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/publications/papers/xxx.pdf
tags: []
citation_id: doi:10.33012/2022.18337
---

## Abstract

The combination of the global navigation satellite system (GNSS) and the inertial navigation system (INS) is extensively studied due to their complementariness. The recently investigated factor graph optimization (FGO)-based GNSS/INS integration positioning showed significantly improved performance in urban canyons, due to the global optimization property and the increased measurement redundancy of FGO, compared with the extended Kalman filtering (EKF) based method. However, only the GNSS pseudorange measurement was utilized in the existing FGObased GNSS/INS integration, and the potential of the Doppler frequency and carrier-phase measurements is still to be explored. To fill this gap, this paper proposed a tightly-coupled GNSS/INS integration via FGO by exploiting the potential of diverse raw GNSS measurements. Specifically, the GNSS pseudorange, Doppler frequency, and time-differenced carrier-phase (TDCP) measurements are integrated with the INS via factor graph optimization. The effectiveness of the proposed method is verified step-by-step using the challenging datasets collected using both automobile-level GNSS receivers in urban canyons of Hong Kong.

## Problem Addressed

Existing FGO-based GNSS/INS integration uses only pseudorange measurements, leaving the potential of Doppler frequency and carrier-phase measurements unexplored for positioning in urban canyons.

## Key Contributions

- Tightly-coupled GNSS/INS integration via factor graph optimization exploiting diverse raw GNSS measurements
- Joint fusion of GNSS pseudorange, Doppler frequency, and time-differenced carrier-phase measurements with INS
- Step-by-step verification using challenging urban canyon datasets from automobile-level GNSS receivers in Hong Kong

## Conclusions

Evaluation on challenging datasets collected with automobile-level GNSS receivers in the urban canyons of Hong Kong verifies the effectiveness of the tightly-coupled integration, confirming that exploiting Doppler and time-differenced carrier-phase measurements alongside pseudorange improves FGO-based GNSS/INS positioning performance.
