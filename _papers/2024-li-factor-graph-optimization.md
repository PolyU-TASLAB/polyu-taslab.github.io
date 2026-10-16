---
title: Factor Graph Optimization Based Multi Epoch Ambiguity Resolution for GNSS RTK and its Evaluation in Hong Kong Urban Canyons
authors:
- Yuan Li
- Xikun Liu
- Weisong Wen
- Li-Ta Hsu
- Yilong Yuan
- Guangyu Bian
- Qiaoyun Chen
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2024-10-09'
doi: https://doi.org/g8t5zf
image: images/papers/cards/2024-li-factor-graph-optimization.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/2024/runzhihu2024pyrtklib2409.12996v1.pdf
tags:
- Artificial intelligence
- Deep learning
- GNSS
- RTKLIB
citation_id: doi:10.33012/2024.19805
---

## Abstract

Artificial intelligence (AI) is revolutionizing numerous fields, with increasing applications in Global Navigation
Satellite Systems (GNSS) positioning algorithms in intelligent transportation systems (ITS) via deep learning. However, a significant technological disparity exists as traditional GNSS algorithms are often developed in Fortran or C, contrasting with the
Python-based implementation prevalent in deep learning tools. To address this discrepancy, this paper introduces pyrtklib, a Python binding for the widely utilized open-source GNSS tool, RTKLIB.
This binding makes all RTKLIB functionalities accessible in
Python, facilitating seamless integration. Moreover, we present a deep learning subsystem under pyrtklib, which is a novel deep learning framework that leverages pyrtklib to accurately predict weights and biases within the GNSS positioning process. The use of pyrtklib enables developers to easily and quickly prototype and implement deep learning-aided GNSS algorithms, showcasing its potential to enhance positioning accuracy significantly.

## Problem Addressed

Traditional GNSS positioning algorithms are implemented in Fortran or C, whereas deep learning tools are predominantly Python-based, creating a technological gap that hinders the development and prototyping of deep learning-aided GNSS algorithms.

## Key Contributions

- pyrtklib, an open-source Python binding for RTKLIB auto-generated via pycparser and pybind11 metaprogramming
- Network predicting pseudorange biases tightly coupled into least-squares correction of GNSS measurements
- Network predicting per-measurement weights applied in the weighted least-squares process
- TDL-BW network jointly predicting weights and biases, distinguishing LOS and NLOS satellites
- Open-source deep learning subsystem for training and predicting weights and biases in GNSS positioning

## Conclusions

TDL-BW, which simultaneously predicts weights and biases, outperforms RTKLIB and goGPS, effectively differentiating LOS and NLOS satellites with appropriate weights and biases. Both pyrtklib and the deep learning subsystem are open-sourced, with pyrtklib downloaded approximately 20,000 times over six months.
