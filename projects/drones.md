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
<li><b>External Wall Cleaning with Drones</b> — High-rise external wall cleaning is one of the most hazardous tasks in urban maintenance. We develop drone-based cleaning systems that integrate aerial manipulation with contact-aware flight control, enabling drones to approach building surfaces, maintain stable contact, and perform cleaning operations autonomously.</li>
<li><b>Software-Hardware Co-Design for Maintenance Drones</b> — We pursue an integrated approach to drone system design, jointly optimizing the AI software stack (perception, planning, contact control) with the hardware platform (airframe, cleaning/manipulation end-effectors, onboard compute) to achieve reliable embodied AI performance under the strict size, weight, and power (SWaP) constraints of aerial platforms.</li>
</ol>
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
<b>Key Research Directions:</b>
<ul>
<li><b>Multi-sensor fusion</b> for drone navigation in urban canyons (GPS-degraded, NLOS-affected environments)</li>
<li><b>Close-proximity flight control</b> for building facade inspection and maintenance</li>
<li><b class="blue">Drone-based external wall cleaning</b> — contact-aware planning and force-controlled manipulation</li>
<li><b>UAV swarm coordination</b> for large-scale building inspection campaigns</li>
<li><b>3D reconstruction and defect detection</b> for structural health monitoring of urban infrastructure</li>
<li><b>Edge AI deployment</b> on resource-constrained drone platforms for real-time perception</li>
</ul>
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "drones" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
