---
title: Safety-certifiable Multi-Sensor Fusion
---

# 🔒 Safety-certifiable Multi-Sensor Fusion for Robotic Navigation in Urban Scenes

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Safety-certifiable AI for autonomous navigation, AI-enabled multi-sensor fusion (<b class="blue">LiDAR/Camera/IMU/GNSS</b>), integrity monitoring and navigation-control joint optimization. Our research focuses on developing fusion algorithms that not only achieve high accuracy but also provide safety guarantees and integrity monitoring for safety-critical autonomous systems.
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "fusion" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
