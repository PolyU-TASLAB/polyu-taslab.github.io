---
title: Safety-certifiable Multi-Sensor Fusion
---

# 🔒 Safety-certifiable Multi-Sensor Fusion for Robotic Navigation in Urban Scenes

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
The <b class="blue">visual/LiDAR SLAM methods are challenged in complex urban scenarios</b>, especially when safety certification is required for autonomous systems. In this project, we aim to study the mechanism of the impacts caused by dynamic scenarios on visual/LiDAR SLAM methods, and develop <b class="blue">safety-certifiable navigation algorithms</b> that can quantify and guarantee the reliability of localization results. We try to answer the questions of how dynamic objects affect the state estimation of visual/LiDAR SLAM methods, how to improve robustness, and how to provide <b class="blue">safety-quantifiable localization</b> for robotics in complex urban environments.
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
Our research addresses several critical challenges:
<ul>
<li><b>Safety-certifiable AI for autonomous navigation</b> — quantifying the trustworthiness and integrity of localization</li>
<li><b>AI-enabled multi-sensor fusion</b> — tightly-coupled LiDAR/Camera/IMU/GNSS integration for robust positioning</li>
<li><b>Integrity monitoring</b> — real-time fault detection and protection level computation for safety-critical systems</li>
<li><b>Navigation-control joint optimization</b> — co-design of state estimation and vehicle control for improved reliability</li>
<li><b>Factor graph optimization</b> — flexible and robust estimation frameworks for multi-sensor integration</li>
</ul>
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "fusion" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
