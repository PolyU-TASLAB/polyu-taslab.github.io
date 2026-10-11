---
title: GLIO2 Paper Now Available on arXiv
subtitle: news
image: images/news/20261011_glio2_arxiv/video_poster.jpg
tags: news
order:
---

We are pleased to share that our new paper, "**GLIO2: A GPU-Parallelized Tightly-Coupled LiDAR–Inertial–GNSS System for Robust and Real-Time Global Localization and Mapping**", is now available on [arXiv](https://arxiv.org/abs/2610.12411).

The paper is authored by **Qi Zhang, Xikun Liu, Qijun Qin, Xiangru Wang, Junzhe Wang, Naigui Xiao, Jianhao Jiao and Weisong Wen**. The work was led by TASLAB MPhil student Qi Zhang.

<div class="news-photos" data-cols="1">
  <figure><a href="https://arxiv.org/abs/2610.12411"><img src="{{ site.baseurl }}/images/news/20261011_glio2_arxiv/video_poster.jpg" alt="GLIO2 paper now available on arXiv"></a></figure>
</div>
<p class="news-caption">Read GLIO2 on <a href="https://arxiv.org/abs/2610.12411">arXiv:2610.12411</a>.</p>

GLIO2 tightly couples scan-to-multiscan LiDAR constraints, IMU pre-integration and raw GNSS measurements in a unified sliding-window factor graph. Its GPU-parallel front end supports real-time operation on edge hardware, while an offline back end reuses the same factors to refine the complete trajectory.

### Why scan-to-multiscan?

Conventional scan-to-map systems align each LiDAR scan with a fixed map assembled from earlier scans. This creates an absolute LiDAR pose in the map frame, while GNSS supplies another absolute position in the Earth frame. If the map has accumulated error—or LiDAR registration becomes unreliable because of geometric degeneracy or moving traffic—the two absolute constraints can conflict.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20261011_glio2_arxiv/core_problem.png" alt="Comparison of conventional scan-to-map fusion and the GLIO2 scan-to-multiscan formulation"></figure>
</div>
<p class="news-caption">GLIO2 keeps LiDAR constraints relative and uses GNSS as the global absolute anchor.</p>

GLIO2 instead retains several movable keyframes and forms relative scan-to-multiscan constraints. Raw LiDAR correspondences, IMU pre-integration, and raw GNSS pseudorange and Doppler measurements are jointly optimized and repeatedly re-associated and relinearized. This allows a poor registration to be corrected as new information arrives rather than frozen into the trajectory.

The system was evaluated on the UrbanNav, MARS-LVIG and M3DGR public benchmarks, together with self-collected UAV and vehicle data. According to the paper, the complete pipeline runs at about **25 Hz** on an NVIDIA Jetson Orin NX. On a 5.66-km bridge route with severe LiDAR degeneracy, GLIO2 maintained 1.6-m horizontal accuracy while the evaluated competing baselines diverged.

### From benchmarks to real applications

The accompanying demonstrations also show GLIO2 operating as the localization source for an autonomous façade-cleaning UAV flying approximately 1–2.5 m from a glass curtain wall, and for a guide-dog robot completing a 210-m outdoor navigation route for a visually impaired user.

### Video explainer

<video
  controls
  muted
  playsinline
  preload="metadata"
  poster="{{ site.baseurl }}/images/news/20261011_glio2_arxiv/video_poster.jpg"
  style="display:block; width:100%; max-width:850px; margin:1em auto; border-radius:12px;">
  <source src="{{ site.baseurl }}/images/news/20261011_glio2_arxiv/glio2_explainer.mp4" type="video/mp4">
  Your browser does not support the video element.
</video>

The video explains the sensor-fusion problem, prior approaches, GLIO2's tightly coupled design, benchmark experiments and the two real-world deployments.

The source code and self-collected datasets are planned for release. Please visit the [arXiv page](https://arxiv.org/abs/2610.12411) for the paper and full experimental results.
