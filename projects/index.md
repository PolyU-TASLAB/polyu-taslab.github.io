---
title: Research
nav:
  order: 3
  tooltip: Research projects and directions
---

# {% include icon.html icon="fa-solid fa-flask" %}Research

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Our research aims to build algorithm foundations for <b class="blue">embodied AI</b> that enable trustworthy perception, navigation, and control of autonomous systems. We develop practical embodied AI-driven autonomous systems — including <b class="blue">drones</b>, <b class="blue">intelligent vehicles</b>, and <b class="blue">legged/humanoid robots</b> — with end-to-end learning and safety certification capabilities. Our work spans five core research directions as below.
</div>

{% include section.html %}

<style>
.rd-section-title {
  display: flex;
  align-items: center;
  gap: 0.5em;
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--primary, #0795d9);
  margin: 1.5em 0 0.3em 0;
  padding-bottom: 0.3em;
  border-bottom: 2px solid var(--primary, #0795d9);
}
.rd-section-title .rd-icon {
  font-size: 1.1em;
}
.rd-desc {
  font-size: 0.93em;
  color: #555;
  margin: 0.2em 0 0.8em 0;
  line-height: 1.55;
  text-align: justify;
}
.rd-count {
  font-size: 0.85em;
  font-weight: 400;
  color: #888;
}
</style>

{% assign gnss_posts = site.posts | where: "research_direction", "gnss" | sort: "date" | reverse %}
{% assign fusion_posts = site.posts | where: "research_direction", "fusion" | sort: "date" | reverse %}
{% assign vehicles_posts = site.posts | where: "research_direction", "vehicles" | sort: "date" | reverse %}
{% assign humanoid_posts = site.posts | where: "research_direction", "humanoid" | sort: "date" | reverse %}
{% assign drones_posts = site.posts | where: "research_direction", "drones" | sort: "date" | reverse %}

<div class="rd-section-title">
  <span class="rd-icon">🛰️</span>
  3D LiDAR Aided GNSS Positioning for Robotics Navigation
  <span class="rd-count">({{ gnss_posts.size }})</span>
</div>
<div class="rd-desc">
AI-driven GNSS positioning (RTK, PPP, PPP-RTK), 3D LiDAR aided NLOS/multipath mitigation, multi-sensor fusion for robust urban navigation.
</div>

{% for post in gnss_posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}

{% include section.html %}

<div class="rd-section-title">
  <span class="rd-icon">🔒</span>
  Safety-certifiable Multi-Sensor Fusion for Robotic Navigation in Urban Scenes
  <span class="rd-count">({{ fusion_posts.size }})</span>
</div>
<div class="rd-desc">
Safety-certifiable AI for autonomous navigation, AI-enabled multi-sensor fusion (LiDAR/Camera/IMU/GNSS), integrity monitoring and navigation-control joint optimization.
</div>

{% for post in fusion_posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}

{% include section.html %}

<div class="rd-section-title">
  <span class="rd-icon">🚗</span>
  End-to-End and Safety-Certifiable Autonomous Vehicles for Logistics Applications
  <span class="rd-count">({{ vehicles_posts.size }})</span>
</div>
<div class="rd-desc">
End-to-end learning for self-driving, safety certification for logistics applications, V2X-assisted connected autonomous driving.
</div>

{% for post in vehicles_posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}

{% include section.html %}

<div class="rd-section-title">
  <span class="rd-icon">🤖</span>
  Embodied AI for Humanoid/Legged Robotics
  <span class="rd-count">({{ humanoid_posts.size }})</span>
</div>
<div class="rd-desc">
Large AI models and vision-language-action models for robotic perception and control, bio-inspired embodied intelligence, multimodal learning for humanoid/legged robots.
</div>

{% for post in humanoid_posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}

{% include section.html %}

<div class="rd-section-title">
  <span class="rd-icon">🚁</span>
  Embodied Drones for City Maintenance and Manipulation
  <span class="rd-count">({{ drones_posts.size }})</span>
</div>
<div class="rd-desc">
Intelligent drones and UAV swarm systems, aerial manipulation for urban infrastructure, software-hardware co-design for efficient embodied AI drone systems.
</div>

{% for post in drones_posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
