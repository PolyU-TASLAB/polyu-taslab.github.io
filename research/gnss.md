---
title: "3D LiDAR Aided GNSS Positioning"
layout: "research-topic"
banner: true
eyebrow: "Research direction"
topic: "gnss"
subtitle: "AI-driven satellite positioning that stays accurate in dense urban canyons"
intro: |
  Satellite positioning works well in open sky but breaks down in cities such as Hong Kong, where tall buildings and
  double-decker buses block and reflect the signals. These **non-line-of-sight (NLOS)** receptions and multipath are the
  main difficulty in using GNSS for intelligent vehicles, drones and robots.

  We let the robot's own perception — 3D LiDAR, cameras and learned models — reveal which satellites are blocked or
  reflected, and then correct or exclude them inside robust factor-graph estimators. The work began with LiDAR-aided NLOS
  exclusion, which won a **Best Presentation Award at ION GNSS+ 2020** (selected by session chairs from Waymo and Swift
  Navigation), and now extends to GNSS-RTK, PPP-RTK, 5G and LEO satellites.
figure:
  image: "images/project/3DLA-GNSS.jpg"
  caption: "3D LiDAR aided GNSS positioning for urban robot navigation"
focus:
  - "NLOS & multipath modelling"
  - "3D LiDAR aided GNSS"
  - "GNSS-RTK & PPP-RTK"
  - "Factor graph optimisation"
  - "Deep learning for GNSS"
  - "Open datasets & code"
pillars:
  - title: "Perceive the signal environment"
    text: "Real-time 3D LiDAR and camera perception identifies the buildings and vehicles that block or reflect each satellite signal."
  - title: "Model and correct NLOS and multipath"
    text: "Physical and learned models correct biased pseudoranges or exclude them, from single-point positioning to RTK."
  - title: "Improve satellite geometry"
    text: "LiDAR landmarks act as 'virtual satellites', and 5G and LEO signals add constraints where blocked satellites leave poor geometry."
  - title: "Robust estimation with factor graphs"
    text: "Robust losses, multi-epoch ambiguity resolution and integrity constraints keep the solution reliable in deep canyons."
videos:
  - youtube: "tvdkKQU9Lro"
    title: "3D LiDAR aided NLOS exclusion for GNSS-RTK positioning in urban canyons"
  - youtube: "YQPn3sHlcEg"
    title: "3D LiDAR aided NLOS exclusion for GNSS single-point positioning"
  - youtube: "_Sh25vIe-xk"
    title: "ION GNSS+ 2021 talk: 3D LiDAR aided NLOS exclusion for GNSS-RTK"
  - youtube: "YZut8BTfYXU"
    title: "ION GNSS+ 2020 talk: 3D LiDAR aided GNSS and its tight integration with INS"
  - youtube: "PJOSsWc8AhE"
    title: "ION GNSS+ 2021 talk: continuous GNSS-RTK aided by LiDAR/inertial odometry"
---

{% include section.html %}

## Recognition & Media

<ul class="rt-list">
  <li><b>Best Presentation Award</b>, ION GNSS+ 2020, session on Navigation in Urban Environments</li>
  <li><b>Innovation Award</b>, TechConnect</li>
  <li>Featured by <a href="https://insidegnss.com/perceived-environment-aided-gnss-single-point-positioning-an-example-using-lidar-scanner/">Inside GNSS</a> on perceived-environment-aided GNSS positioning</li>
</ul>

{% include section.html %}

## Selected Publications

<h3 class="pub-year">2025</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">3-D LiDAR-Aided GNSS NLOS Mitigation for Reliable GNSS-RTK Positioning in Urban Canyons.</span><br><span class="pub-authors">Liu, X., <strong>Wen, W</strong>.*, Huang, F., Gao, H., Wang, Y., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Instrumentation and Measurement, 74, 1-15, 2025.</span> <span class="pub-meta">(IF: 5.9, JCR Q1, Citations: 9)</span></li>

<li class="pub-item"><span class="pub-title">3D LiDAR Aided GNSS NLOS Correction by Direction-of-Arrival Estimation Using Doppler Measurements in Urban Canyons.</span><br><span class="pub-authors">Liu, X., <strong>Wen, W</strong>.*, Zhang, L., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">Fisheye Image/GNSS Based Multimodal Learning for GNSS NLOS/Multipath Correction: Enhancing Vehicle Positioning in Urban Canyons for Autonomous Driving.</span><br><span class="pub-authors">Hu, R., Liu, J., Zhong, Y., <strong>Wen, W</strong>., Xia, M., Huang, Y.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 2025.</span> <span class="pub-meta">(IF: 7.1, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">pyrtklib: An Open-source Package for Tightly Coupled Deep Learning and GNSS Integration for Positioning in Urban Canyons.</span><br><span class="pub-authors">Hu, R., Xu, P., Zhong, Y., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1, Citations: 7)</span></li>

<li class="pub-item"><span class="pub-title">Urban GNSS Positioning for Consumer Electronics: 3D Mapping and Advanced Signal Processing.</span><br><span class="pub-authors">Wang, J., Xia, M., Zhang, D., <strong>Wen, W</strong>., Chen, W., Shi, C.</span><br><span class="pub-venue">IEEE Transactions on Consumer Electronics, 2025.</span> <span class="pub-meta">(IF: 10.9, JCR Q1, Citations: 7)</span></li>
</ul>

<h3 class="pub-year">2024</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">Integrity-Constrained Factor Graph Optimization for GNSS Positioning in Urban Canyons.</span><br><span class="pub-authors">Xia, X., <strong>Wen, W</strong>., Hsu, L.T.*</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 2024.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 5)</span></li>

<li class="pub-item"><span class="pub-title">Subspace-based Adaptive GMM Error Modeling for Fault-Aware Pseudorange-based Positioning in Urban Canyons.</span><br><span class="pub-authors">Yan, P., Xia, X., Brizzi, M., <strong>Wen, W</strong>., Hsu, L.T.*</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2024.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 4)</span></li>

<li class="pub-item"><span class="pub-title">Trajectory Smoothing Using GNSS/PDR Integration Via Factor Graph Optimization in Urban Canyons.</span><br><span class="pub-authors">Zhong, Y., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Internet of Things Journal, 2024.</span> <span class="pub-meta">(IF: 8.9, JCR Q1, Citations: 16)</span></li>

<li class="pub-item"><span class="pub-title">Enhancing GNSS Positioning Accuracy for Road Monitoring Systems: A Factor Graph Optimization Approach Aided by Geospatial Information.</span><br><span class="pub-authors">Zhong, Y., Hu, R., Bai, X., Li, X., Hsu, L.T., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Transactions on Instrumentation and Measurement, 73, 1-12, 2024.</span> <span class="pub-meta">(IF: 5.9, JCR Q1, Citations: 12)</span></li>
</ul>

<h3 class="pub-year">2023</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">3D Vision Aided GNSS Real-time Kinematic Positioning for Autonomous Systems in Urban Canyons.</span><br><span class="pub-authors"><strong>Wen, W</strong>.*, Bai, X., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 2023.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 22)</span></li>

<li class="pub-item"><span class="pub-title">Hong Kong UrbanNav: An Open-Source Multisensory Dataset for Benchmarking Urban Navigation Algorithms.</span><br><span class="pub-authors">Hsu, L.T., Huang, F., Ng, H.F., Zhang, G., Zhong, Y., Bai, X., <strong>Wen, W</strong>.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 70(4), 2023.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 80)</span></li>

<li class="pub-item"><span class="pub-title">GLIO: Tightly-coupled GNSS/LiDAR/IMU Integration for Continuous and Drift-free State Estimation of Intelligent Vehicles in Urban Areas.</span><br><span class="pub-authors">Liu, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2023.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 52)</span></li>
</ul>

<h3 class="pub-year">2021–2022</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">3D LiDAR Aided GNSS NLOS Mitigation in Urban Canyons.</span><br><span class="pub-authors"><strong>Wen, W</strong>., and Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2021.</span></li>

<li class="pub-item"><span class="pub-title">Time-correlated Window Carrier-phase Aided GNSS Positioning in Urban Canyons.</span><br><span class="pub-authors">Bai, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Aerospace and Electronic Systems, 2022.</span></li>

<li class="pub-item"><span class="pub-title">GNSS Outlier Mitigation via Graduated Non-convexity Factor Graph Optimization.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 71(1), 297-310, 2021.</span></li>

<li class="pub-item"><span class="pub-title">Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Pfeifer, T., Bai, X., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 68(2), 315-331, 2021.</span></li>
</ul>

<h3 class="pub-year">2018–2020</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">Object-Detection-Aided GNSS and Its Integration With Lidar in Highly Urbanized Areas.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">IEEE Intelligent Transportation Systems Magazine, 12(3), 53-69, 2020.</span></li>

<li class="pub-item"><span class="pub-title">GNSS NLOS Exclusion Based on Dynamic Object Detection Using LiDAR Point Cloud.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2019.</span></li>

<li class="pub-item"><span class="pub-title">Correcting NLOS by 3D LiDAR and Building Height to Improve GNSS Single Point Positioning.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 66(4), 705-718, 2019.</span></li>

<li class="pub-item"><span class="pub-title">Tightly Coupled GNSS/INS Integration via Factor Graph and Aided by Fish-eye Camera.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Bai, X., Kan, Y.C., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 68(11), 10651-10662, 2019.</span></li>
</ul>

<p class="pub-more"><a href="{{ 'publications' | relative_url }}">Full publication list →</a></p>
