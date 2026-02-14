---
title: Embodied Drones for City Maintenance
---

# 🚁 Embodied Drones for City Maintenance and Manipulation

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Intelligent drones and <b class="blue">UAV swarm systems</b>, aerial manipulation for urban infrastructure, software-hardware co-design for efficient embodied AI drone systems. Our research develops autonomous drone platforms capable of performing complex manipulation and inspection tasks in urban environments, from window cleaning to infrastructure monitoring.
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "drones" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
