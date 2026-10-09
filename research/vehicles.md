---
title: "End-to-End Autonomous Vehicles"
layout: "research-topic"
banner: true
eyebrow: "Research direction"
topic: "vehicles"
subtitle: "Safety-certifiable end-to-end driving for urban logistics"
intro: |
  Autonomous vehicles can transform logistics and urban mobility, but driving safely on Hong Kong's dense,
  GNSS-degraded streets is still a grand challenge. We develop **end-to-end learning** for driving together with
  **safety certification**, and take both from campus tests to real logistics fleets.

  Our platforms combine GNSS-RTK, LiDAR, cameras and IMU with **V2X communication** and roadside sensing, and are
  validated with partners such as SF Express and Rino.ai in campus delivery, last-mile transport and connected-vehicle
  trials.
figure:
  image: "images/project/E2ELV.jpg"
  caption: "End-to-end and safety-certifiable autonomous vehicles for logistics"
focus:
  - "End-to-end driving"
  - "Integrity monitoring"
  - "V2X & roadside sensing"
  - "HD mapping"
  - "Logistics vehicles"
pillars:
  - title: "End-to-end autonomous driving"
    text: "Networks that learn to drive from raw LiDAR, camera, IMU and GNSS data, unifying perception, prediction, planning and control in one differentiable framework."
  - title: "Safety certification and integrity monitoring"
    text: "Integrity monitoring quantifies in real time how far the navigation solution can be trusted, so the vehicle can detect unsafe states and trigger fail-safe manoeuvres."
  - title: "Real-world deployment for logistics"
    text: "Full-stack vehicle platforms for campus patrol, autonomous delivery and connected fleets, with robust localisation in urban canyons."
approach_figure:
  image: "images/project/AGV_demo.jpg"
  caption: "Autonomous vehicle platform for campus logistics and urban navigation"
videos:
  - bilibili: "BV1ktZcYdEWD"
    title: "Autonomous driving test, TAS Lab, PolyU"
  - youtube: "Q0nq1vHeinM"
    title: "Autonomous driving demonstration on the PolyU campus"
  - youtube: "90fOkCs_ID4"
    title: "Localisation and control"
  - youtube: "FQ5aHB4o3jg"
    title: "Perception and control"
---

{% include section.html %}

## Field Demonstrations

<div class="rt-media rt-media-single">
  <figure>
    <a href="{{ 'images/project/demo_20220923.jpg' | relative_url }}" target="_blank" rel="noopener"><img src="{{ 'images/project/demo_20220923.jpg' | relative_url }}" alt="Campus security patrol demonstration with an unmanned ground vehicle" loading="lazy"></a>
    <figcaption>Campus security patrol with an unmanned ground vehicle, demonstrated to the PolyU Campus Facilities and Sustainability Office and Health and Safety Office (Sept 2022)</figcaption>
  </figure>
</div>

{% include section.html %}

## Collaborators

<p class="rt-section-lead">We work with industry partners including Huawei, Meituan, Tencent and iDriverplus, the
<a href="https://msc.berkeley.edu/">Mechanical Systems Control Lab</a> at UC Berkeley and
<a href="https://www.tu-chemnitz.de/">Chemnitz University of Technology</a> in Germany.</p>

{% include section.html %}

## Selected Publications

<ul class="pub-list">

<li class="pub-item"><span class="pub-title">Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>., Yang, R., Zhang, Y., Hu, J., Chen, Y., Xiao, N., Zhao, J.</span><br><span class="pub-venue">IEEE International Conference on Robotics &amp; Automation (ICRA), 2026.</span></li>

<li class="pub-item"><span class="pub-title">EIRM-RL: Epistemic Integrity Risk Monitoring Inspired Safe Reinforcement Learning for Trustworthy Autonomous Navigation.</span><br><span class="pub-authors">Zhang, Y., Wang, Y., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Internet of Things Journal, 13(2), 3500-3512, 2025.</span> <span class="pub-meta">(IF: 8.9, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">Learning Safe, Optimal, Real-Time Flight Interaction with Deep Confidence-enhanced Reachability Guarantee.</span><br><span class="pub-authors">Zhang, Y., Wang, Y., Yan, P., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">Safety-quantifiable Line Feature-based Monocular Visual Localization with 3D Prior Map.</span><br><span class="pub-authors">Zheng, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1, Citations: 3)</span></li>

<li class="pub-item"><span class="pub-title">Continuous Error Map Aided Adaptive Multi-Sensor Integration for Connected Autonomous Vehicles in Urban Scenarios.</span><br><span class="pub-authors">Huang, F., <strong>Wen, W</strong>.*, Zhang, G., Su, D., Huang, Y.</span><br><span class="pub-venue">IEEE Transactions on Instrumentation and Measurement, 2025.</span> <span class="pub-meta">(IF: 5.9, JCR Q1, Citations: 4)</span></li>

<li class="pub-item"><span class="pub-title">Fault Detection Algorithm for Gaussian Mixture Noises: An Application in Lidar/IMU Integrated Localization Systems.</span><br><span class="pub-authors">Yan, P., Li, Z., Huang, F., <strong>Wen, W</strong>., Hsu, L.T.</span><br><span class="pub-venue">NAVIGATION: Journal of the Institute of Navigation, 72(1), 2025.</span> <span class="pub-meta">(IF: 3.1, JCR Q1, Citations: 6)</span></li>

<li class="pub-item"><span class="pub-title">Safety-Quantifiable Planar-Feature-based LiDAR Localization with a Prior Map for Intelligent Vehicles in Urban Scenarios.</span><br><span class="pub-authors">Zhang, J., Liu, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2024.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 2)</span></li>

<li class="pub-item"><span class="pub-title">A Novel Consistent-Robust SINS/GNSS/NHC Integrated Navigation Method for Autonomous Vehicles Under Intermittent GNSS Outage.</span><br><span class="pub-authors">Du, S., Huang, Y.*, <strong>Wen, W</strong>., Zhang, Y.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2024.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 13)</span></li>

<li class="pub-item"><span class="pub-title">Tightly-coupled Visual/Inertial/Map Integration with Observability Analysis for Reliable Localization of Intelligent Vehicles.</span><br><span class="pub-authors">Zheng, X., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2024.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 3)</span></li>

<li class="pub-item"><span class="pub-title">Integration of Vehicle Dynamic Model and System Identification Model for Extending the Navigation Service Under Sensor Failures.</span><br><span class="pub-authors">Yan, P., <strong>Wen, W</strong>.*, Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2023.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 11)</span></li>

<li class="pub-item"><span class="pub-title">Dynamic Object-Aware LiDAR Odometry Aided by Joint Weightings Estimation in Urban Areas.</span><br><span class="pub-authors">Huang, F., <strong>Wen, W</strong>., Zhang, J.*, Wang, C., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2023.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 9)</span></li>

<li class="pub-item"><span class="pub-title">ECMD: An Event-Centric Multisensory Driving Dataset for SLAM.</span><br><span class="pub-authors">Chen, P., Guan, W., Huang, F., Zhong, Y., <strong>Wen, W</strong>., Hsu, L.T., Lu, P.*</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2023.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 31)</span></li>

<li class="pub-item"><span class="pub-title">An Improved Inertial Preintegration Model in Factor Graph Optimization for High Accuracy Positioning of Intelligent Vehicles.</span><br><span class="pub-authors">Zhang, L., <strong>Wen, W</strong>.*, Zhang, T., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Vehicles, 2023.</span> <span class="pub-meta">(IF: 14.3, JCR Q1, Citations: 16)</span></li>

<li class="pub-item"><span class="pub-title">UrbanLoco: A Full Sensor Suite Dataset for Mapping and Localization in Urban Scenes.</span><br><span class="pub-authors"><strong>Wen, W</strong>., Zhou, Y., Zhang, G., Fahandezh-Saadi, S., Bai, X., Zhan, W., Tomizuka, M., Hsu, L.T.</span><br><span class="pub-venue">IEEE ICRA 2020, 2310-2316.</span> <span class="pub-meta">(Citations: 184)</span></li>

<li class="pub-item"><span class="pub-title">UrbanNav: An Open-sourced Multisensory Dataset for Benchmarking Positioning Algorithms Designed for Urban Areas.</span><br><span class="pub-authors">Hsu, L.T., Kubo, N., <strong>Wen, W</strong>., Chen, W., Liu, Z., Suzuki, T., Meguro, J.</span><br><span class="pub-venue">ION GNSS+ 2021.</span> <span class="pub-meta">(Citations: 149)</span></li>

</ul>

<p class="pub-more"><a href="{{ 'publications' | relative_url }}">Full publication list →</a></p>
