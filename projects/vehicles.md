---
title: End-to-End Autonomous Vehicles
---

# 🚗 End-to-End and Safety-Certifiable Autonomous Vehicles for Logistics Applications

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
<b class="blue">End-to-end learning</b> for self-driving, safety certification for logistics applications, <b class="blue">V2X-assisted</b> connected autonomous driving. Our research develops neural network architectures that learn the entire driving pipeline from sensor inputs to vehicle control, with a focus on safety certification and real-world deployment for logistics and urban transportation.
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "vehicles" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
