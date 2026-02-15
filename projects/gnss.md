---
title: 3D LiDAR Aided GNSS Positioning
---

# 🛰️ 3D LiDAR Aided GNSS Positioning for Robotics Navigation

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Positioning in urban environments is becoming essential due to the increasing demand for autonomous driving vehicles (ADV). The global navigation satellite system (GNSS) is currently one of the principal means of providing globally-referenced positioning for ADV localization. However, the positioning accuracy is significantly degraded in highly-urbanized cities due to signal reflection caused by static buildings and dynamic objects. If the direct line-of-sight (LOS) is blocked, and reflected signals from the same satellite are received, the notorious <b class="blue">non-line-of-sight (NLOS)</b> receptions occur.
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Inspired by the strong perception capability of ADV using onboard sensors (such as 3D LiDAR), we continuously develop <b class="blue">perception-aided NLOS mitigation methods</b> where 3D LiDAR is employed to timely reconstruct the surrounding environments to identify the NLOS receptions. We have extended the LiDAR aided GNSS NLOS mitigation to <b class="blue">GNSS Real-time Kinematic (RTK)</b>, leading to sub-meter level accuracy. Our research spans:
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
<ul>
<li><b>AI-driven GNSS positioning</b> — RTK, PPP, PPP-RTK with deep learning aided signal processing</li>
<li><b>3D LiDAR aided NLOS/multipath mitigation</b> — environment perception for signal quality assessment</li>
<li><b>Multi-sensor fusion</b> — GNSS/LiDAR/IMU tightly-coupled integration via factor graph optimization</li>
<li><b>High-accuracy mapping</b> — centimeter-level positioning in dense urban canyons</li>
</ul>
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "gnss" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
