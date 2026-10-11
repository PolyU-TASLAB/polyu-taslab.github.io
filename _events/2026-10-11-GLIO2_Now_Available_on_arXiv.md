---
title: GLIO2 Paper Now Available on arXiv
subtitle: news
image: images/news/20261011_glio2_arxiv/cover.jpg
tags: news
order:
---

We are pleased to share that our new paper, "**GLIO2: A GPU-Parallelized Tightly-Coupled LiDAR–Inertial–GNSS System for Robust and Real-Time Global Localization and Mapping**", is now available on [arXiv](https://arxiv.org/abs/2610.12411).

The paper is authored by **Qi Zhang, Xikun Liu, Qijun Qin, Xiangru Wang, Junzhe Wang, Naigui Xiao, Jianhao Jiao and Weisong Wen**.

<div class="news-photos" data-cols="1">
  <figure><a href="https://arxiv.org/abs/2610.12411"><img src="{{ site.baseurl }}/images/news/20261011_glio2_arxiv/cover.jpg" alt="GLIO2 paper now available on arXiv"></a></figure>
</div>
<p class="news-caption">Read GLIO2 on <a href="https://arxiv.org/abs/2610.12411">arXiv:2610.12411</a>.</p>

GLIO2 tightly couples scan-to-multiscan LiDAR constraints, IMU pre-integration and raw GNSS measurements in a unified sliding-window factor graph. Its GPU-parallel front end supports real-time operation on edge hardware, while an offline back end reuses the same factors to refine the complete trajectory.

The system was evaluated on the UrbanNav, MARS-LVIG and M3DGR public benchmarks, together with self-collected UAV and vehicle data. According to the paper, the complete pipeline runs at about **25 Hz** on an NVIDIA Jetson Orin NX. On a 5.66-km bridge route with severe LiDAR degeneracy, GLIO2 maintained 1.6-m horizontal accuracy while the evaluated competing baselines diverged.

The source code and self-collected datasets are planned for release. Please visit the [arXiv page](https://arxiv.org/abs/2610.12411) for the paper and full experimental results.
