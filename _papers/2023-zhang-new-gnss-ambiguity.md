---
title: A New GNSS Ambiguity Resolution Method Through Mixed Integer Programming
authors:
- Hongmin Zhang
- Weisong Wen
- Li-Ta Hsu
publisher: ION GNSS+, The International Technical Meeting of the Satellite Division of The Institute of Navigation
date: '2023-10-05'
doi: https://doi.org/hcc4r3
citation_id: doi:10.33012/2023.19317
---

## Abstract

Fixing ambiguity to a correct integer value is an essential part of high-accuracy positioning using the global navigation satellite system (GNSS) real-time kinematic (RTK). A lot of research has been done on this problem in the past decades. The least-squares ambiguity decorrelation adjustment (LAMBDA) is widely applied for estimating integer ambiguity. In general, the float ambiguity variables are resolved based on the least square estimation using the double-differenced code and carrier measurements. Then the integer ambiguity is resolved by the LAMBDA method which exploits the information content of the full ambiguity variance-covariance matrix, with statistical decorrelation as the objective in constructing the ambiguity transformation. One of the well-recognized challenges of the LAMBDA method is its reliance on the covariance matrix associated with float ambiguity. Moreover, the correlation between the float parameters and the integer ambiguities is not fully explored in the two-step optimization. Instead of resolving the integer ambiguity in a two-step-based manner, can we directly resolve the float state (position of the user) and integer ambiguities simultaneously in a tighter manner? To answer this question, this paper exploits to use of the mixed-integer program (MIP) to solve the GNSS-RTK positioning problem. In particular, the classical branch and bound algorithm of MIP is applied in this research. This algorithm uses a divide-and-conquer strategy to partition the solution space into subproblems and then optimizes individually over each subproblem, in order to find the best solution globally. At each subproblem in the branch and bound algorithm, the position parameter and integer ambiguity are estimated simultaneously to minimize the objective function. In this paper, epoch-by-epoch positioning experiment shows that the positioning performance can be improved a lot based on an MIP method when compared with the conventional method. Moreover, integer ambiguity can be obtained for all epochs. For some epochs, when LAMBDA cannot fix ambiguity successfully, the MIP method can get a reasonable integer value for ambiguity to improve the position accuracy. Compared with the conventional method, the newly proposed algorithm doesn't directly rely heavily on the quality of float ambiguity estimation and the associated covariance which is indispensable for conventional LAMBDA algorithms. We can get integer ambiguity directly along with ambiguity-fixed position results in one step via the MIP method.

## Problem Addressed

The widely used LAMBDA method for GNSS RTK integer ambiguity resolution relies on the float ambiguity covariance matrix and does not fully exploit the correlation between float parameters and integer ambiguities in its two-step optimization.

## Key Contributions

- Mixed-integer programming formulation resolving the float state (user position) and integer ambiguities simultaneously
- Classical branch-and-bound algorithm partitioning the solution space into subproblems optimized individually for a global optimum
- Joint estimation of position and integer ambiguity at each subproblem to minimize the objective function

## Conclusions

Epoch-by-epoch positioning experiments show that the MIP-based method considerably improves positioning performance compared with the conventional two-step LAMBDA approach, demonstrating the benefit of solving position and integer ambiguities jointly in a tighter formulation.
