---
title: Embodied AI for Humanoid/Legged Robotics
---

# 🤖 Embodied AI for Humanoid/Legged Robotics

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Large AI models and <b class="blue">vision-language-action models</b> for robotic perception and control, bio-inspired embodied intelligence, multimodal learning for humanoid/legged robots. Our research explores how foundation models and multimodal learning can enable robots to perceive, reason, and interact with the physical world in a human-like manner.
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "humanoid" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
