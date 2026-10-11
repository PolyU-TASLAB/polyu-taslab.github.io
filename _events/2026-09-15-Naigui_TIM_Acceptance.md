---
title: Paper on Outlier-Aware LiDAR/IMU/UWB Integration Accepted by IEEE Transactions on Instrumentation and Measurement
subtitle: news
image: images/news/20260915_liuo_tim/cover.jpg
tags: news
order:
---

We are pleased to share that the paper "**Outlier-Aware LiDAR/IMU/UWB Integration with NLOS Mitigation and Anchor Self-Calibration in Complex Scenarios**" has been accepted for publication in the [IEEE Transactions on Instrumentation and Measurement (TIM)](https://ieee-ims.org/publication/ieee-tim) on 15 September 2026.

The paper is authored by **Naigui Xiao, Weisong Wen, Lu Bai, Xiangru Wang, Jiahao Hu, Qi Zhang, Jianhao Jiao, Zhen Lyu and Feng Huang**. The work was led by PhD student Naigui Xiao at TASLAB, The Hong Kong Polytechnic University, in collaboration with Dr. Lu Bai at Chalmers University of Technology.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20260915_liuo_tim/cover.jpg" alt="LIUO paper accepted by IEEE Transactions on Instrumentation and Measurement"></figure>
</div>
<p class="news-caption">LIUO integrates LiDAR, IMU and UWB for drift-bounded localization in GNSS-challenged environments.</p>

The proposed **LiDAR–inertial–UWB odometry (LIUO)** framework addresses two practical obstacles to deploying UWB-aided localization: labor-intensive anchor calibration and degraded ranging measurements under non-line-of-sight (NLOS) propagation.

Its main technical contributions are:

- a continuous-time factor graph based on non-uniform B-splines that associates asynchronous LiDAR, IMU and UWB measurements with the trajectory at their original timestamps;
- online self-calibration of 3D UWB anchor positions, jointly optimized with the vehicle trajectory and IMU biases; and
- map-aware NLOS mitigation based on geometric penetration depth (GPD), which uses the LiDAR map to estimate signal-path obstruction and adapt the uncertainty of each UWB measurement.

The system was evaluated on the public UrbanV2X benchmark and self-collected urban and indoor datasets. On UrbanV2X, the full self-calibrating LIUO configuration reduced APE RMSE from **12.374 m for FAST-LIO2 to 4.878 m**, while reducing the fitted long-distance drift rate from **6.18 to 3.16 mm/m**. The GPD-based NLOS detector achieved **92.39% precision**, with an average processing time of approximately **0.31 ms per UWB measurement**.

### Open-source code and datasets

The implementation and datasets are now available in the [PolyU-TASLAB/LIUO GitHub repository](https://github.com/PolyU-TASLAB/LIUO).

### Video demonstration

<div style="position:relative; width:100%; max-width:850px; margin:1em auto; padding-top:56.25%; overflow:hidden; border-radius:12px;">
  <iframe
    src="https://www.youtube.com/embed/pGqk48h-OBc"
    title="LIUO video demonstration"
    style="position:absolute; inset:0; width:100%; height:100%; border:0;"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

The video is also available directly on [YouTube](https://www.youtube.com/watch?v=pGqk48h-OBc). Congratulations to Naigui and all co-authors!
