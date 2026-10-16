---
title: Combining Deep Gaussian Process and Rule-Based Method for Decision-Making in Self-Driving Simulation with Small Data
authors:
- Wenqi Fang
- Huiyun Li
- Shaobo Dang
- Hui Huang
- Lei Peng
- Li-Ta Hsu
- Weisong Wen
publisher: 2019 15th International Conference on Computational Intelligence and Security (CIS)
date: '2019-12-01'
doi: https://doi.org/g8tzc3
image: images/papers/cards/2019-fang-combining-deep-gaussian.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/CDGP.pdf
tags:
- gaussian process
- kernel function
- rule-based
- decision-making
citation_id: doi:10.1109/CIS.2019.00063
---

## Abstract

Self-driving vehicle is a popular and promising
field in artificial intelligence. Conventional architecture consists of multiple sensors, which work collaboratively to sense the units on road to yield a precise and safe driving strategy.
Besides the precision and safety, the quickness of decision is also a major concern. In order to react quickly, the vehicle need to predict its next possible action, such as acceleration, brake and steering angle, according to its latest few actions and status. In this paper, we treat this decision-making problem as a regression problem and use deep gaussian process to predict its next action. The regression model is trained using simulation data sets and accurately captures the most significant features. Combined with rule-based method, it can be used in Torcs simulation engine to realize successful loop trip on virtual roads. The proposed method outperforms the existing reinforcement learning methods on the performance indicators of time consumption and the size of data volume. It may be useful for real road tests in the future.

## Problem Addressed

Self-driving vehicles must decide their next action (acceleration, brake, steering) quickly from recent actions and states, but reinforcement learning approaches require large amounts of training data and time. Data-efficient decision-making in simulation remains a challenge.

## Key Contributions

- Formulates self-driving decision-making as a regression problem predicting the next vehicle action
- Applies a deep Gaussian process trained on small simulation datasets to capture significant features
- Combines the regression model with a rule-based method in the TORCS simulation engine
- Compares against reinforcement learning (DDPG) on time consumption and data volume

## Conclusions

The combined deep Gaussian process and rule-based method realizes a successful loop trip on virtual roads in simulation. It costs much less time and needs much less data than a well-trained DDPG network, and the authors believe it can be extended to more complex road tests.
