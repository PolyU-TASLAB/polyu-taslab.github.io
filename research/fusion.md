---
title: "Safety-certifiable Multi-Sensor Fusion"
layout: "research-topic"
banner: true
eyebrow: "Research direction"
topic: "fusion"
subtitle: "Robot navigation that knows when it can be trusted"
intro: |
  Visual and LiDAR SLAM are challenged in complex urban scenes: moving vehicles, repetitive structures and degraded GNSS
  make errors appear silently. For autonomous systems that must be certified, an accurate answer is not enough — the
  system also has to bound its own error.

  We study how dynamic scenes affect visual, LiDAR and inertial state estimation, make the fusion robust to them, and
  bring aviation-style **integrity monitoring** — fault detection, exclusion and protection levels — to robots, cars,
  aircraft and wearables.
figure:
  image: "images/project/multi-sensor.jpg"
  caption: "GNSS/LiDAR/visual/inertial integration for robot navigation"
focus:
  - "GNSS/LiDAR/camera/IMU fusion"
  - "Integrity monitoring"
  - "Protection levels"
  - "Prior-map localisation"
  - "Inertial deep learning"
  - "Factor graph optimisation"
pillars:
  - title: "Robust fusion in dynamic scenes"
    text: "Detect and remove moving objects and outliers so that LiDAR, visual and inertial odometry stay consistent in crowded streets."
  - title: "Safety-quantifiable localisation"
    text: "Line- and plane-feature localisation against 3D prior maps, with a quantified error bound for every pose."
  - title: "Integrity monitoring for multi-sensor systems"
    text: "Fault modes, alert limits and protection levels adapted from aviation ARAIM to urban vehicles, aircraft and wearables."
approach_figure:
  image: "images/project/visualSafety.png"
  caption: "Safety-certifiable visual localisation with a 3D prior map"
videos:
  - youtube: "W_i-LOaLP4o"
    title: "Safety-quantifiable line-feature monocular visual localisation with a 3D prior map"
  - youtube: "vrxQQMUQdD4"
    title: "Multi-sensor integrated navigation system for autonomous driving"
  - youtube: "iOp-QNSww40"
    title: "Low-cost solid-state LiDAR/inertial localisation with a prior map"
  - youtube: "X_t4EDOdKMY"
    title: "ION GNSS+ 2021 talk: coarse-to-fine LiDAR SLAM with dynamic object removal"
---

{% include section.html %}

## Selected Publications

<h3 class="pub-year">2025</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">POPL-SLAM: A Pose-Only Representation-Based Visual-Inertial SLAM With Point and Structural Line Features.</span><br><span class="pub-authors">Li, T., Han, B., Yan, D., <strong>Wen, W</strong>., Wang, Z., Shi, C.</span><br><span class="pub-venue">IEEE Transactions on Aerospace and Electronic Systems, 62, 1509-1525, 2025.</span> <span class="pub-meta">(IF: 5.7, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">Safety-quantifiable Line Feature-based Monocular Visual Localization with 3D Prior Map.</span><br><span class="pub-authors">Zheng, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1, Citations: 3)</span></li>

<li class="pub-item"><span class="pub-title">Fault Detection Algorithm for Gaussian Mixture Noises: An Application in Lidar/IMU Integrated Localization Systems.</span><br><span class="pub-authors">Yan, P., Li, Z., Huang, F., <strong>Wen, W</strong>., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 72(1), 2025.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 6)</span></li>

<li class="pub-item"><span class="pub-title">Multi-Sensor Plug-and-Play Navigation Based on Resilient Information Filter.</span><br><span class="pub-authors">Meng, Q., Su, C., Jiang, Y., <strong>Wen, W</strong>., Meng, X.</span><br><span class="pub-venue">IEEE Sensors Journal, 2025.</span> <span class="pub-meta">(IF: 4.5, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">A Novel Lie Group-based Reliable IMM Estimation Method for SINS/GNSS/OD/NHC Integrated Navigation in Complex Environments.</span><br><span class="pub-authors">Du, S., Huang, Y., <strong>Wen, W</strong>., Zhang, Y.</span><br><span class="pub-venue">IEEE Internet of Things Journal, 2025.</span> <span class="pub-meta">(IF: 8.9, JCR Q1, Citations: 5)</span></li>

<li class="pub-item"><span class="pub-title">Graph-Based Indoor 3D Pedestrian Location Tracking With Inertial-Only Perception.</span><br><span class="pub-authors">Bai, S., <strong>Wen, W</strong>.*, Su, D., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Mobile Computing, 2025.</span> <span class="pub-meta">(IF: 9.2, JCR Q1, Citations: 5)</span></li>
</ul>

<h3 class="pub-year">2024</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">Safety-Quantifiable Planar-Feature-based LiDAR Localization with a Prior Map for Intelligent Vehicles in Urban Scenarios.</span><br><span class="pub-authors">Zhang, J., Liu, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2024.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 2)</span></li>

<li class="pub-item"><span class="pub-title">Factor Graph Optimization-Based Smartphone IMU-Only Indoor SLAM With Multi-Hypothesis Turning Behavior Loop Closures.</span><br><span class="pub-authors">Bai, S., <strong>Wen, W</strong>.*, Hsu, L.T., Yang, P.</span><br><span class="pub-venue">IEEE Transactions on Aerospace and Electronic Systems, 2024.</span> <span class="pub-meta">(IF: 5.7, JCR Q1, Citations: 9)</span></li>

<li class="pub-item"><span class="pub-title">Tightly-coupled Visual/Inertial/Map Integration with Observability Analysis for Reliable Localization of Intelligent Vehicles.</span><br><span class="pub-authors">Zheng, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2024.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 3)</span></li>

<li class="pub-item"><span class="pub-title">Integrity-Constrained Factor Graph Optimization for GNSS Positioning in Urban Canyons.</span><br><span class="pub-authors">Xia, X., <strong>Wen, W</strong>., Hsu, L.T.*</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 2024.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 5)</span></li>

<li class="pub-item"><span class="pub-title">FGO-MFI: Factor Graph Optimization-based Multi-sensor Fusion and Integration for Reliable Localization.</span><br><span class="pub-authors">Zhu, J., Zhuo, G., Xia, X.*, <strong>Wen, W</strong>., Xiong, L., Leng, B., Liu, W.</span><br><span class="pub-venue">Measurement Science and Technology, 35(8), 086303, 2024.</span> <span class="pub-meta">(IF: 3.4, JCR Q1, Citations: 7)</span></li>
</ul>

<h3 class="pub-year">2023</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">GLIO: Tightly-coupled GNSS/LiDAR/IMU Integration for Continuous and Drift-free State Estimation of Intelligent Vehicles in Urban Areas.</span><br><span class="pub-authors">Liu, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2023.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 52)</span></li>

<li class="pub-item"><span class="pub-title">Low-cost Solid-state LiDAR/Inertial Based Localization with Prior Map for Autonomous Systems in Urban Scenarios.</span><br><span class="pub-authors">Zhong, Y., Huang, F., Zhang, J., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IET Intelligent Transport Systems, 17(3), 474-486, 2023.</span> <span class="pub-meta">(IF: 2.3, JCR Q2, Citations: 9)</span></li>
</ul>

<h3 class="pub-year">2018–2022</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">AGPC-SLAM: Absolute Ground Plane Constrained 3D Lidar SLAM.</span><br><span class="pub-authors"><strong>Wen, W</strong>., &amp; Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 69(3), 2022.</span></li>

<li class="pub-item"><span class="pub-title">Coarse-to-Fine Loosely-Coupled LiDAR-Inertial Odometry for Urban Positioning and Mapping.</span><br><span class="pub-authors">Zhang, J., <strong>Wen, W</strong>.*, Huang, F., Chen, X., Hsu, L.T.</span><br><span class="pub-venue">Remote Sensing, 13, 2371, 2021.</span></li>

<li class="pub-item"><span class="pub-title">Point Wise or Feature Wise? A Benchmark Comparison of Publicly Available Lidar Odometry Algorithms in Urban Canyons.</span><br><span class="pub-authors">Huang, F., <strong>Wen, W</strong>., Zhang, J., Hsu, L.T.*</span><br><span class="pub-venue">IEEE Intelligent Transportation Systems Magazine, 2021.</span></li>

<li class="pub-item"><span class="pub-title">Robust Visual-Inertial Integrated Navigation System Aided by Online Sensor Model Adaption for Autonomous Ground Vehicles in Urban Areas.</span><br><span class="pub-authors">Bai, X., <strong>Wen, W</strong>., Hsu, L.T.</span><br><span class="pub-venue">Remote Sensing, 12(10), 1686, 2020.</span></li>

<li class="pub-item"><span class="pub-title">Performance Analysis of NDT-based Graph SLAM for Autonomous Vehicle in Diverse Typical Driving Scenarios of Hong Kong.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Hsu, L.T., Zhang, G.</span><br><span class="pub-venue">Sensors, 18, 3928, 2018.</span></li>
</ul>

<p class="pub-more"><a href="{{ 'publications' | relative_url }}">Full publication list →</a></p>
