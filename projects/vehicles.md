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
<li><b>Safety Certification and Integrity Monitoring</b> — Unlike conventional black-box approaches, our systems incorporate rigorous safety certification mechanisms. We design integrity monitoring algorithms that quantify the trustworthiness of navigation solutions in real time, enabling the vehicle to detect unsafe states and trigger fail-safe maneuvers.</li>
<li><b>Real-World Deployment for Logistics</b> — We bridge the gap between research and application by developing full-stack autonomous vehicle platforms for logistics use cases, including campus patrol, autonomous delivery, and connected fleet management. Our platforms feature multi-sensor fusion (GNSS-RTK/LiDAR/Camera/IMU), <b class="blue">V2X communication</b>, and robust localization in challenging urban canyon environments.</li>
</ol>
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "vehicles" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
