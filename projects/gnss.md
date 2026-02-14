---
title: 3D LiDAR Aided GNSS Positioning
---

# 🛰️ 3D LiDAR Aided GNSS Positioning for Robotics Navigation

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
AI-driven GNSS positioning (<b class="blue">RTK, PPP, PPP-RTK</b>), 3D LiDAR aided NLOS/multipath mitigation, multi-sensor fusion for robust urban navigation. Our research develops advanced algorithms that integrate GNSS with 3D LiDAR and other sensors to achieve high-accuracy positioning in challenging urban environments where satellite signals are degraded by buildings and other obstacles.
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "gnss" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
