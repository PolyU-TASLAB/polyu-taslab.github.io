---
title: 'POPL-SLAM: A Pose-Only Representation-Based Visual-Inertial SLAM With Point and Structural Line Features'
authors:
- Tuan Li
- Bing Han
- Dayu Yan
- Weisong Wen
- Zhipeng Wang
- Chuang Shi
publisher: IEEE Transactions on Aerospace and Electronic Systems
date: '2026-01-01'
doi: https://doi.org/hccr4d
image: images/papers/cards/2026-li-poplslam-poseonly-representationbased.jpg
citation_id: doi:10.1109/TAES.2025.3630568
---

## Abstract

The geometric regularity of man-made structures imposes distinct constraints on visual-inertial simultaneous localization and mapping (VI-SLAM) systems. To effectively leverage this geometric information, we integrate distance and angular data from linear structural features to enforce additional constraints on point-based VI-SLAM. To mitigate the computational overhead of high-level features, we propose pose-only-based point and line (POPL)-SLAM, which adopts a pose-only (PO) approach to implicitly model points and structural lines. First, we develop a progressive vanishing point (VP) estimation technique leveraging inertial measurement unit (IMU) preintegration priors. By formulating a nonorthogonal constraint optimization, this technique efficiently estimates VPs without per-frame recalculations. Second, we introduce a PO framework for a point-line SLAM system, implicitly modeling points and lines to formulate constraints. This approach eliminates linearization errors during optimization and markedly improves computational efficiency. For structural line features, we concurrently incorporate Euclidean and angular distance errors to comprehensively capture positional and orientational information. Extensive experiments on public real-world datasets demonstrate that POPL-SLAM outperforms state-of-the-art point-line VI-SLAM systems in accuracy, efficiency, and robustness.

## Problem Addressed

Point-based visual-inertial SLAM underexploits the geometric regularity of man-made structures, while incorporating high-level structural line features typically adds heavy computational overhead and linearization errors.

## Key Contributions

- POPL-SLAM, a VI-SLAM system using pose-only implicit representation of both point and structural line features
- Progressive vanishing point estimation leveraging IMU preintegration priors via nonorthogonal constraint optimization, without per-frame recalculation
- Pose-only point-line formulation that eliminates linearization errors and improves computational efficiency
- Joint Euclidean and angular distance errors for structural lines capturing positional and orientational constraints

## Conclusions

On the EuRoC, TUM-VI, and UMA-VI datasets, POPL-SLAM outperforms state-of-the-art point-line VI-SLAM systems in accuracy, efficiency, and robustness, achieving the highest localization accuracy with an average ATE of 0.028 m. The progressive vanishing point detection significantly reduces computational time, and ablation studies confirm the contribution of the pose-only representation and structural lines.
