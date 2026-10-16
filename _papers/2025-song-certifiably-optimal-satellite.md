---
title: Certifiably Optimal Satellite Orbit Determination Based on Doppler Measurements for Low-Earth-Orbit Satellites
authors:
- Baoshan Song
- Weisong Wen
- Li-Ta Hsu
publisher: 2025 IEEE/ION Position, Location and Navigation Symposium (PLANS)
date: '2025-04-28'
doi: https://doi.org/hcc4rv
image: images/papers/cards/2025-song-certifiably-optimal-satellite.jpg
citation_id: doi:10.1109/plans61210.2025.11028259
---

## Abstract

Low-Earth Orbit (LEO) satellite is promising to provide intelligent services in the future. To fulfill the need, orbit determination (OD) is vital for accurate satellite positions.
Doppler-based OD has been widely studied for its low-cost and convenience. Mainstream Doppler-based OD methods rely on local estimation, which require accurate initialization and may converge to suboptimal solution. We address this problem by utilizing convex optimization theory. First, we model Doppler-based
OD with quadratic constrained quadratic program (QCQP) and semi-definite program (SDP) for a convex expression. Then, we derive the necessary conditions for solving the globally optimal solution of this OD problem in both noiseless and noise cases.
In noise case, parameter noises including Doppler measurement and satellite velocity noise are considered. Specially, we derive an explicit parameter noise bound to guarantee the optimality.
Results of simulation show that local optimization based OD converges to local optima when initial point is 1500 km away from the ground truth. In comparison, our proposed method does not require initialization and provides certifiably optimal OD solutions, even under mild noises. Furthermore, a demonstration of explicit noise bound shows 6 m/s for satellite velocity noise and 8 m/s for Doppler measurement noise. Within this predicted noise range, the estimate proves to be optimal.

## Problem Addressed

Mainstream Doppler-based orbit determination for LEO satellites relies on local estimation, which requires accurate initialization and may converge to suboptimal solutions.

## Key Contributions

- Formulation of Doppler-based orbit determination as QCQP and SDP for a convex problem expression
- Derivation of necessary conditions for the globally optimal solution in noiseless and noisy cases
- Explicit parameter noise bound guaranteeing optimality under Doppler and satellite velocity noise
- To the authors' knowledge, the first certifiably optimal Doppler-based orbit determination method

## Conclusions

Simulations show local optimization converges to local optima when the initial point is 1500 km from ground truth, whereas the proposed method requires no initialization and yields certifiably optimal solutions even under mild noise. The demonstrated explicit noise bounds are 6 m/s for satellite velocity noise and 8 m/s for Doppler measurement noise, within which the estimate is proven optimal.
