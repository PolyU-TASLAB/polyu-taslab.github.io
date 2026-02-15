---
title: 3D LiDAR Aided GNSS Positioning
---

# 🛰️ 3D LiDAR Aided GNSS Positioning for Robotics Navigation

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Positioning in urban environments is becoming essential due to the increasing demand for autonomous driving vehicles (ADV). The global navigation satellite system (GNSS) is currently one of the principal means of providing globally-referenced positioning for ADV localization. With the increased availability of multiple satellite constellations, GNSS can provide satisfactory performance in open-sky areas. However, the positioning accuracy is significantly degraded in highly-urbanized cities such as Hong Kong, due to signal reflection caused by static buildings and dynamic objects such as double-decker buses. If the direct line-of-sight (LOS) is blocked, and reflected signals from the same satellite are received, the notorious <b class="blue">non-line-of-sight (NLOS)</b> receptions occur. According to a recent review paper, NLOS is currently the major difficulty in the use of GNSS in intelligent transportation systems.
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Inspired by the strong perception capability of ADV using onboard sensors (such as 3D LiDAR), we continuously developed the <b class="blue">perception-aided NLOS mitigation methods</b> where the 3D LiDAR is employed to timely reconstruct the surrounding environments to identify the NLOS receptions. The idea was also reported in the industrial magazine in 2018. The work was further improved in 2020, where several drawbacks are relaxed and was awarded the <b class="blue">Best Presentation Award</b> in the session of Navigation in Urban Environments. Interestingly, this award is selected by the session chairs from <b class="blue">Waymo</b> and <b class="blue">Swift Navigation</b>. Meanwhile, the idea is transferred into industrial applications for high-accuracy offline mapping applications. Recently, we extended the LiDAR aided GNSS NLOS mitigation to the <b class="blue">GNSS Real-time Kinematic (RTK)</b>, leading to sub-meter level accuracy. Unfortunately, the fixed rate of the RTK is still not guaranteed as:
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
<ul>
<li>The existing method does not fully mitigate the NLOS with multiple reflections and multipath. It is still <b class="blue">an unknown question to model the multiple reflection and multipath</b>.</li>
<li>Poor satellite geometry due to the signal blockage and potential NLOS exclusion. It is still an unknown question to <b class="blue">effectively improve the geometry of the satellite constraints in dense urban canyons</b>.</li>
</ul>
</div>

<p align="center">
  <img width="600" src="{{ 'images/project/3DLA-GNSS.jpg' | relative_url }}" alt="3D LiDAR Aided GNSS Positioning">
</p>
<center><i>3D LiDAR Aided GNSS Positioning for Robotics Urban Navigation</i></center>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

## Recent News

<ul>
<li>May 2022, 1 paper accepted in <b class="blue">IEEE Transactions on Intelligent Transportation Systems</b>.
  <ul>
  <li><b class="blue">Wen, W</b>., and Hsu, L.T., 2022. 3D LiDAR Aided GNSS NLOS Mitigation in Urban Canyons. IEEE Transactions on Intelligent Transportation Systems.</li>
  </ul>
</li>
<li>23rd April 2022, our conference paper was accepted in <b class="blue">ION GNSS+ 2022</b>.
  <ul>
  <li>Liu, X., <b class="blue">Wen, W</b>*., and Hsu, L.T. 2022, September. 3D LiDAR Aided GNSS Real-time Kinematic Positioning via Coarse-to-fine Batch Optimization for High Accuracy Mapping in Dense Urban Canyons. In Proceedings of ION GNSS+ 2022.</li>
  </ul>
</li>
</ul>

{% include section.html %}

## Video Demonstration

<p align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/tvdkKQU9Lro" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>
<center><i>Demonstration: 3D LiDAR Aided NLOS Exclusion for GNSS Real-time Kinematic (RTK) Positioning in Urban Canyons</i></center>

<p align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/_Sh25vIe-xk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>
<center><i>Presentation in ION GNSS+ 2021: 3D LiDAR Aided NLOS Exclusion for GNSS RTK Positioning</i></center>

<p align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/YQPn3sHlcEg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>
<center><i>Demonstration: 3D LiDAR Aided NLOS Exclusion for GNSS Single Point Positioning</i></center>

<p align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/YZut8BTfYXU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>
<center><i>Presentation in ION GNSS+ 2020: 3D LiDAR Aided GNSS and Its Tightly Coupled Integration with INS</i></center>

<p align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/PJOSsWc8AhE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>
<center><i>Presentation in ION GNSS+ 2021: Continuous GNSS-RTK Aided by LiDAR/Inertial Odometry</i></center>

{% include section.html %}

## Related Papers (*: Corresponding author)

<style>
.pub-list { list-style: none; padding-left: 0; }
.pub-item { margin: 10px 0; padding: 10px 14px; border-left: 3px solid var(--primary, #0795d9); background: #f9fbfd; font-size: 0.92em; line-height: 1.55; }
.pub-title { font-weight: 600; color: var(--primary, #0795d9); }
.pub-authors { font-size: 0.9em; color: #444; }
.pub-venue { font-size: 0.88em; color: #555; font-style: italic; }
.pub-meta { font-size: 0.85em; color: #888; }
</style>

<h3>2025</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">3-D LiDAR-Aided GNSS NLOS Mitigation for Reliable GNSS-RTK Positioning in Urban Canyons.</span><br><span class="pub-authors">Liu, X., <strong>Wen, W</strong>.*, Huang, F., Gao, H., Wang, Y., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Instrumentation and Measurement, 74, 1-15, 2025.</span> <span class="pub-meta">(IF: 5.9, JCR Q1, Citations: 9)</span></li>

<li class="pub-item"><span class="pub-title">3D LiDAR Aided GNSS NLOS Correction by Direction-of-Arrival Estimation Using Doppler Measurements in Urban Canyons.</span><br><span class="pub-authors">Liu, X., <strong>Wen, W</strong>.*, Zhang, L., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">Fisheye Image/GNSS Based Multimodal Learning for GNSS NLOS/Multipath Correction: Enhancing Vehicle Positioning in Urban Canyons for Autonomous Driving.</span><br><span class="pub-authors">Hu, R., Liu, J., Zhong, Y., <strong>Wen, W</strong>., Xia, M., Huang, Y.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 2025.</span> <span class="pub-meta">(IF: 7.1, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">pyrtklib: An Open-source Package for Tightly Coupled Deep Learning and GNSS Integration for Positioning in Urban Canyons.</span><br><span class="pub-authors">Hu, R., Xu, P., Zhong, Y., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1, Citations: 7)</span></li>

<li class="pub-item"><span class="pub-title">Urban GNSS Positioning for Consumer Electronics: 3D Mapping and Advanced Signal Processing.</span><br><span class="pub-authors">Wang, J., Xia, M., Zhang, D., <strong>Wen, W</strong>., Chen, W., Shi, C.</span><br><span class="pub-venue">IEEE Transactions on Consumer Electronics, 2025.</span> <span class="pub-meta">(IF: 10.9, JCR Q1, Citations: 7)</span></li>
</ul>

<h3>2024</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">Integrity-Constrained Factor Graph Optimization for GNSS Positioning in Urban Canyons.</span><br><span class="pub-authors">Xia, X., <strong>Wen, W</strong>., Hsu, L.T.*</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 2024.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 5)</span></li>

<li class="pub-item"><span class="pub-title">Subspace-based Adaptive GMM Error Modeling for Fault-Aware Pseudorange-based Positioning in Urban Canyons.</span><br><span class="pub-authors">Yan, P., Xia, X., Brizzi, M., <strong>Wen, W</strong>., Hsu, L.T.*</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2024.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 4)</span></li>

<li class="pub-item"><span class="pub-title">Trajectory Smoothing Using GNSS/PDR Integration Via Factor Graph Optimization in Urban Canyons.</span><br><span class="pub-authors">Zhong, Y., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Internet of Things Journal, 2024.</span> <span class="pub-meta">(IF: 8.9, JCR Q1, Citations: 16)</span></li>

<li class="pub-item"><span class="pub-title">Enhancing GNSS Positioning Accuracy for Road Monitoring Systems: A Factor Graph Optimization Approach Aided by Geospatial Information.</span><br><span class="pub-authors">Zhong, Y., Hu, R., Bai, X., Li, X., Hsu, L.T., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Transactions on Instrumentation and Measurement, 73, 1-12, 2024.</span> <span class="pub-meta">(IF: 5.9, JCR Q1, Citations: 12)</span></li>
</ul>

<h3>2023</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">3D Vision Aided GNSS Real-time Kinematic Positioning for Autonomous Systems in Urban Canyons.</span><br><span class="pub-authors"><strong>Wen, W</strong>.*, Bai, X., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 2023.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 22)</span></li>

<li class="pub-item"><span class="pub-title">Hong Kong UrbanNav: An Open-Source Multisensory Dataset for Benchmarking Urban Navigation Algorithms.</span><br><span class="pub-authors">Hsu, L.T., Huang, F., Ng, H.F., Zhang, G., Zhong, Y., Bai, X., <strong>Wen, W</strong>.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 70(4), 2023.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 80)</span></li>

<li class="pub-item"><span class="pub-title">GLIO: Tightly-coupled GNSS/LiDAR/IMU Integration for Continuous and Drift-free State Estimation of Intelligent Vehicles in Urban Areas.</span><br><span class="pub-authors">Liu, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2023.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 52)</span></li>
</ul>

<h3>2021–2022</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">3D LiDAR Aided GNSS NLOS Mitigation in Urban Canyons.</span><br><span class="pub-authors"><strong>Wen, W</strong>., and Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2021.</span></li>

<li class="pub-item"><span class="pub-title">Time-correlated Window Carrier-phase Aided GNSS Positioning in Urban Canyons.</span><br><span class="pub-authors">Bai, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Aerospace and Electronic Systems, 2022.</span></li>

<li class="pub-item"><span class="pub-title">GNSS Outlier Mitigation via Graduated Non-convexity Factor Graph Optimization.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 71(1), 297-310, 2021.</span></li>

<li class="pub-item"><span class="pub-title">Factor Graph Optimization for GNSS/INS Integration: A Comparison with the Extended Kalman Filter.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Pfeifer, T., Bai, X., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 68(2), 315-331, 2021.</span></li>
</ul>

<h3>2018–2020</h3>

<ul class="pub-list">
<li class="pub-item"><span class="pub-title">Object-Detection-Aided GNSS and Its Integration With Lidar in Highly Urbanized Areas.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">IEEE Intelligent Transportation Systems Magazine, 12(3), 53-69, 2020.</span></li>

<li class="pub-item"><span class="pub-title">GNSS NLOS Exclusion Based on Dynamic Object Detection Using LiDAR Point Cloud.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2019.</span></li>

<li class="pub-item"><span class="pub-title">Correcting NLOS by 3D LiDAR and Building Height to Improve GNSS Single Point Positioning.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhang, G., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 66(4), 705-718, 2019.</span></li>

<li class="pub-item"><span class="pub-title">Tightly Coupled GNSS/INS Integration via Factor Graph and Aided by Fish-eye Camera.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Bai, X., Kan, Y.C., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 68(11), 10651-10662, 2019.</span></li>
</ul>

<p style="text-align:right;font-size:0.88em;margin-top:8px;"><a href="{{ 'research' | relative_url }}" style="color:var(--primary, #1a73e8);">→ Full publication list</a></p>

{% include section.html %}

## Press Coverage

<ul>
<li><b class="blue"><a href="https://insidegnss.com/perceived-environment-aided-gnss-single-point-positioning-an-example-using-lidar-scanner/">Inside GNSS</a></b> — Feature on perceived environment aided GNSS positioning</li>
<li><b class="blue">Innovation Award from TechConnect</b></li>
<li><b class="blue">Best Presentation Award in ION GNSS+ 2020</b> — Session on Navigation in Urban Environments</li>
</ul>

{% include section.html %}

## Acknowledgement and Collaborators

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
This research was funded by government and industry partners, including <b class="blue">Hong Kong Polytechnic University</b>, <b class="blue">Guangdong Basic and Applied Basic Research Foundation</b>, <b class="blue">Riemann Laboratory</b>, and <b class="blue">Huawei Technologies</b>.
</div>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "gnss" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
