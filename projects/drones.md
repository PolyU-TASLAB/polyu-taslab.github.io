---
title: Embodied Drones for City Maintenance
---

# 🚁 Embodied Drones for City Maintenance and Manipulation

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Maintaining urban infrastructure in dense city environments — particularly <b class="blue">external wall cleaning of high-rise buildings</b> and <b class="blue">structural inspection in urban canyons</b> — presents significant challenges that demand intelligent, physically interactive drone systems. This research develops <b class="blue">embodied drone platforms</b> that combine autonomous navigation in GPS-degraded urban canyons with contact-based manipulation capabilities for real-world city maintenance tasks.
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
Our approach addresses three fundamental challenges:
<ol>
<li><b>Autonomous Inspection in Urban Canyons</b> — Dense urban environments with tall buildings, narrow streets, and GPS-degraded conditions pose severe challenges for drone navigation. We develop AI-driven multi-sensor fusion algorithms (LiDAR/Camera/IMU/GNSS) and robust localization methods that enable drones to navigate safely and precisely in complex urban canyon environments. Our systems provide centimeter-level positioning for close-proximity inspection of building facades, bridges, and other urban structures.</li>
<li><b>External Wall Cleaning with Drones</b> — High-rise external wall cleaning is one of the most hazardous tasks in urban maintenance. We develop drone-based cleaning systems that integrate aerial manipulation with contact-aware flight control, enabling drones to approach building surfaces, maintain stable contact, and perform cleaning operations autonomously. Our force-controlled manipulation strategies ensure safe and effective cleaning while accommodating varying surface geometries, wind disturbances, and dynamic environmental conditions.</li>
<li><b>Software-Hardware Co-Design for Maintenance Drones</b> — We pursue an integrated approach to drone system design, jointly optimizing the AI software stack (perception, planning, contact control) with the hardware platform (airframe, cleaning/manipulation end-effectors, onboard compute) to achieve reliable embodied AI performance under the strict size, weight, and power (SWaP) constraints of aerial platforms.</li>
</ol>
</div>

<p align="center">
  <img width="700" src="{{ 'images/project/E2EDrone.png' | relative_url }}" alt="Embodied Drones">
</p>
<center><i>Embodied Drones for City Maintenance and Manipulation</i></center>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

## Demo Videos

<p align="center">
  <iframe src="//player.bilibili.com/player.html?bvid=BV1UsgDzeE5J&page=1&autoplay=0" width="560" height="315" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</p>
<center><i>Intelligent Cleaning UAV Demonstration — PolyU Wuxi Research Institute</i></center>

<p align="center">
  <iframe src="//player.bilibili.com/player.html?bvid=BV1fiaqzNEEm&page=1&autoplay=0" width="560" height="315" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</p>
<center><i>UAV System Demonstration — TAS Lab, PolyU</i></center>

{% include section.html %}

## Key Research Directions

<ul>
<li><b class="blue">Multi-sensor fusion for drone navigation in urban canyons</b> (GPS-degraded, NLOS-affected environments)</li>
<li><b class="blue">Close-proximity flight control</b> for building facade inspection and maintenance</li>
<li><b class="blue">Drone-based external wall cleaning</b> — contact-aware planning and force-controlled manipulation</li>
<li><b class="blue">UAV swarm coordination</b> for large-scale building inspection campaigns</li>
<li><b class="blue">3D reconstruction and defect detection</b> for structural health monitoring of urban infrastructure</li>
<li><b class="blue">Vision-language models</b> for intelligent mission planning and task understanding</li>
<li><b class="blue">Edge AI deployment</b> on resource-constrained drone platforms for real-time perception</li>
</ul>

{% include section.html %}

## Target Applications

<ul>
<li><b class="blue">External wall cleaning</b>: Autonomous drone-based cleaning of high-rise building facades, replacing dangerous manual rope-access work</li>
<li><b class="blue">Building facade inspection</b>: Crack detection, water leakage identification, and structural defect assessment in urban canyons</li>
<li><b class="blue">Bridge and infrastructure inspection</b>: Close-proximity structural health monitoring with aerial sensing and manipulation</li>
<li><b class="blue">Offshore wind turbine inspection</b>: Drone-based blade inspection and surface assessment in challenging marine environments</li>
</ul>

{% include section.html %}

## Recent News

<ul>
<li><b class="blue">June 2024</b>: Interview by RTHK on UAV-enabled window cleaning and aerial 3D printing</li>
<li><b class="blue">May 2024</b>: Interview by Hong Kong TVB and Ming Pao on UAV-enabled external wall cleaning technology</li>
<li><b class="blue">July 2024</b>: Interview by Toutiao (头条日报) on low-altitude economy applications</li>
</ul>

{% include section.html %}

## Press Coverage Photos

<table style="width:100%;border-collapse:collapse;border:none;margin:10px 0 20px;"><tr style="border:none;"><td style="width:33.3%;padding:6px;border:none;text-align:center;vertical-align:top;"><img src="{{ 'images/project/rthk.jpg' | relative_url }}" alt="RTHK Interview" style="width:100%;border-radius:8px;"><br>RTHK Interview</td><td style="width:33.3%;padding:6px;border:none;text-align:center;vertical-align:top;"><img src="{{ 'images/project/TVB.JPG' | relative_url }}" alt="TVB Coverage" style="width:100%;border-radius:8px;"><br>TVB Coverage</td><td style="width:33.3%;padding:6px;border:none;text-align:center;vertical-align:top;"><img src="{{ 'images/project/MINGBAO.JPG' | relative_url }}" alt="Ming Pao Coverage" style="width:100%;border-radius:8px;"><br>Ming Pao Coverage</td></tr></table>

{% include section.html %}

## Selected Publications (*: Corresponding author)

<style>
p[align="center"] { text-align: center !important; }
p[align="center"] img, p[align="center"] iframe { display: inline-block; max-width: 100%; }
center { text-align: center; font-size: 0.88em; color: #555; margin-top: 4px; }
.pub-list { list-style: none; padding-left: 0; }
.pub-item { margin: 10px 0; padding: 10px 14px; border-left: 3px solid var(--primary, #0795d9); background: #f9fbfd; font-size: 0.92em; line-height: 1.55; }
.pub-title { font-weight: 600; color: var(--primary, #0795d9); }
.pub-authors { font-size: 0.9em; color: #444; }
.pub-venue { font-size: 0.88em; color: #555; font-style: italic; }
.pub-meta { font-size: 0.85em; color: #888; }
</style>

<ul class="pub-list">

<li class="pub-item"><span class="pub-title">Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>., Yang, R., Zhang, Y., Hu, J., Chen, Y., Xiao, N., Zhao, J.</span><br><span class="pub-venue">IEEE International Conference on Robotics &amp; Automation (ICRA), 2026.</span></li>

<li class="pub-item"><span class="pub-title">Learning Safe, Optimal, Real-Time Flight Interaction with Deep Confidence-enhanced Reachability Guarantee.</span><br><span class="pub-authors">Zhang, Y., Wang, Y., Yan, P., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1, Citations: 2)</span></li>

<li class="pub-item"><span class="pub-title">Tightly Joined Positioning and Control Model for Unmanned Aerial Vehicles Based on Factor Graph Optimization.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>.*, Bai, S., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 2025.</span> <span class="pub-meta">(IF: 7.1, JCR Q1, Citations: 4)</span></li>

<li class="pub-item"><span class="pub-title">Online Dynamic Model Calibration for Reliable Control of Quadrotor Based on Factor Graph Optimization.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>.*, Bai, S., Hu, J.</span><br><span class="pub-venue">IEEE Transactions on Aerospace and Electronic Systems, 2025.</span> <span class="pub-meta">(IF: 5.7, JCR Q1, Citations: 2)</span></li>

<li class="pub-item"><span class="pub-title">RTT-LIO: A Wi-Fi RTT-aided LiDAR-Inertial Odometry via Tightly-Coupled Factor Graph Optimization in Complex Scenes.</span><br><span class="pub-authors">Xu, R., Liu, X., Wang, X., <strong>Wen, W</strong>., Huang, Y.</span><br><span class="pub-venue">IEEE Internet of Things Journal, 2025.</span> <span class="pub-meta">(IF: 8.9, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">Safe-Assured Learning-Based Deep SE(3) Motion Joint Planning and Control for UAV Interactions with Dynamic Environments.</span><br><span class="pub-authors">Zhang, Y., <strong>Wen, W</strong>., Yan, P.</span><br><span class="pub-venue">IEEE ITSC 2024.</span> <span class="pub-meta">(Citations: 4)</span></li>

<li class="pub-item"><span class="pub-title">SUG-UAV Multirotor Dataset with Multi-sensor Integration in Indoor and Urban Areas.</span><br><span class="pub-authors">Xiao, N., <strong>Wen, W</strong>.*, Hu, J., Yang, P., Zhao, J., Wu, C., Bai, S.</span><br><span class="pub-venue">IPIN 2024.</span> <span class="pub-meta">(Citations: 3)</span></li>

<li class="pub-item"><span class="pub-title">Tightly Joining Positioning and Control for Trustworthy Unmanned Aerial Vehicles Based on Factor Graph Optimization in Urban Transportation.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE ITSC 2023.</span> <span class="pub-meta">(Citations: 7)</span></li>

<li class="pub-item"><span class="pub-title">Tightly-Coupled Wi-Fi/LiDAR/Inertial Integration via Factor Graph Optimization for UAS.</span><br><span class="pub-authors">Xu, R., Liu, X., <strong>Wen, W</strong>.</span><br><span class="pub-venue">2025 IEEE/ION PLANS, 648-653.</span> <span class="pub-meta">(Citations: 1)</span></li>

</ul>

<p style="text-align:right;font-size:0.88em;margin-top:8px;"><a href="{{ 'research' | relative_url }}" style="color:var(--primary, #1a73e8);">→ Full publication list</a></p>

{% include section.html %}

## Acknowledgement and Collaborators

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
This research is supported by <b class="blue">The Hong Kong Polytechnic University</b>, the <b class="blue">Department of Science and Technology of Guangdong Province</b> (Drone System and Offshore Wind Turbines Inspection), <b class="blue">Esri China (HK) Limited</b> (Vision-Language-Action Models for Intelligent UAV Systems), and <b class="blue">Meituan</b> (Vision Aided GNSS-RTK Positioning for UAV System in Urban Canyons). We collaborate with leading research groups and industry partners in intelligent drone systems and urban maintenance solutions.
</div>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "drones" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
