---
title: End-to-End Autonomous Vehicles
---

# 🚗 End-to-End and Safety-Certifiable Autonomous Vehicles for Logistics Applications

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Autonomous vehicles hold transformative potential for logistics and urban mobility, yet deploying them safely in real-world environments remains a grand challenge. This research focuses on developing <b class="blue">end-to-end learning frameworks</b> and <b class="blue">safety-certifiable navigation systems</b> for autonomous vehicles in logistics applications — from campus delivery and last-mile transportation to urban freight operations.
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
Our approach integrates three core elements:
<ol>
<li><b>End-to-End Autonomous Driving</b> — We develop neural network architectures that learn to drive directly from raw sensor inputs (LiDAR, camera, IMU, GNSS) to control outputs, enabling autonomous vehicles to handle complex urban scenarios including dense traffic, dynamic obstacles, and GPS-degraded environments. Our end-to-end pipelines unify perception, prediction, planning, and control into a single differentiable framework.</li>
<li><b>Safety Certification and Integrity Monitoring</b> — Unlike conventional black-box approaches, our systems incorporate rigorous safety certification mechanisms. We design integrity monitoring algorithms that quantify the trustworthiness of navigation solutions in real time, enabling the vehicle to detect unsafe states and trigger fail-safe maneuvers. This is critical for logistics applications where reliability and regulatory compliance are paramount.</li>
<li><b>Real-World Deployment for Logistics</b> — We bridge the gap between research and application by developing full-stack autonomous vehicle platforms for logistics use cases, including campus patrol, autonomous delivery, and connected fleet management. Our platforms feature multi-sensor fusion (GNSS-RTK/LiDAR/Camera/IMU), <b class="blue">V2X communication</b>, and robust localization in challenging urban canyon environments.</li>
</ol>
</div>

<p align="center">
  <img width="700" src="{{ 'images/project/E2ELV.png' | relative_url }}" alt="End-to-End Autonomous Vehicles">
</p>
<center><i>End-to-End and Safety-Certifiable Autonomous Vehicles for Logistics Applications</i></center>

<p align="center">
  <img width="600" src="{{ 'images/project/AGV_demo.png' | relative_url }}" alt="Autonomous Vehicle Platform">
</p>
<center><i>Autonomous Vehicle Platform for Campus Logistics and Urban Navigation</i></center>

<p align="center">
  <img width="700" src="{{ 'images/project/demo_20220923.jpg' | relative_url }}" alt="Campus UGV patrol demonstration">
</p>
<center><i>Campus Security Patrol Demonstration with UGV — PolyU AAE/CFSO, Sept 2022</i></center>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

## Demo Videos

<div style="text-align:center;margin:20px 0;">
<iframe src="//player.bilibili.com/player.html?bvid=BV1ktZcYdEWD&page=1&autoplay=0" width="100%" height="400" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:700px;border-radius:8px;"></iframe>
<p style="font-size:0.85em;color:#555;margin-top:6px;">Autonomous Driving Test — TAS Lab, PolyU</p>
</div>

<table style="width:100%;border-collapse:collapse;border:none;margin:10px 0 20px;"><tr style="border:none;"><td style="width:33.3%;padding:6px;border:none;text-align:center;vertical-align:top;"><iframe width="100%" height="180" src="https://www.youtube.com/embed/Q0nq1vHeinM" title="Autonomous driving PolyU campus demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:8px;"></iframe><p style="font-size:0.82em;color:#555;margin-top:4px;">Autonomous driving PolyU campus demo</p></td><td style="width:33.3%;padding:6px;border:none;text-align:center;vertical-align:top;"><iframe width="100%" height="180" src="https://www.youtube.com/embed/90fOkCs_ID4" title="Localization and Control" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:8px;"></iframe><p style="font-size:0.82em;color:#555;margin-top:4px;">Localization and Control</p></td><td style="width:33.3%;padding:6px;border:none;text-align:center;vertical-align:top;"><iframe width="100%" height="180" src="https://www.youtube.com/embed/FQ5aHB4o3jg" title="Perception and control" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="border-radius:8px;"></iframe><p style="font-size:0.82em;color:#555;margin-top:4px;">Perception and Control</p></td></tr></table>

{% include section.html %}

## News

<ul>
<li>Sept 2022, we welcome the <b class="blue">PolyU Campus Facilities and Sustainability Office (CFSO)</b> and <b class="blue">Health and Safety Office (HSO)</b> to attend the demonstration of AAE/CFSO Campus Security Patrol with Unmanned Ground Vehicle (UGV)</li>
</ul>

{% include section.html %}

## Selected Publications (*: Corresponding author)

<style>
.pub-list { list-style: none; padding-left: 0; }
.pub-item { margin: 10px 0; padding: 10px 14px; border-left: 3px solid var(--primary, #0795d9); background: #f9fbfd; font-size: 0.92em; line-height: 1.55; }
.pub-title { font-weight: 600; color: var(--primary, #0795d9); }
.pub-authors { font-size: 0.9em; color: #444; }
.pub-venue { font-size: 0.88em; color: #555; font-style: italic; }
.pub-meta { font-size: 0.85em; color: #888; }
</style>

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

<p style="text-align:right;font-size:0.88em;margin-top:8px;"><a href="{{ 'research' | relative_url }}" style="color:var(--primary, #1a73e8);">→ Full publication list</a></p>

{% include section.html %}

## Acknowledgement and Collaborators

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
This research is supported by government and industry partners, including the <b class="blue">Hong Kong Polytechnic University</b>, <b class="blue">Guangdong Basic and Applied Basic Research Foundation</b>, <b class="blue">Hong Kong Smart Traffic Fund</b>, <b class="blue">Innovation and Technology Fund</b>, <b class="blue"><a href="https://www.huawei.com/">Huawei Technologies</a></b>, <b class="blue"><a href="https://www.meituan.com/">Meituan</a></b>, <b class="blue"><a href="https://www.tencent.com/">Tencent</a></b>, and <b class="blue"><a href="https://www.idriverplus.com/cn/index.html">iDriverplus</a></b>. We also collaborate closely with the <b class="blue"><a href="https://msc.berkeley.edu/">Mechanical Systems Control Lab</a></b> at the University of California, Berkeley, and the <b class="blue"><a href="https://www.tu-chemnitz.de/">Chemnitz University of Technology</a></b> in Germany.
</div>

<p align="center">
  <img width="700" src="{{ 'images/project/funding.jpg' | relative_url }}" alt="Funding and Collaborators">
</p>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "vehicles" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
