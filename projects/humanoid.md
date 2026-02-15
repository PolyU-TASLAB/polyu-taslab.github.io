---
title: Embodied AI for Humanoid/Legged Robotics
---

# 🤖 Embodied AI for Humanoid/Legged Robotics

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Humanoid and legged robots represent the next frontier of embodied AI — machines that can perceive, reason, and physically interact with the world in a human-like manner. This research focuses on developing <b class="blue">large AI models</b> and <b class="blue">vision-language-action (VLA) frameworks</b> that enable humanoid and legged robots to autonomously navigate, manipulate, and collaborate in complex real-world environments.
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
Our approach integrates three core pillars:
<ol>
<li><b>Foundation Models for Robotic Perception and Control</b> — We develop vision-language-action models that bridge high-level semantic understanding with low-level motor control, enabling robots to interpret natural language instructions and execute complex manipulation and locomotion tasks. Our models leverage large-scale pre-training on multimodal data (vision, language, proprioception) and are fine-tuned for real-world deployment on humanoid platforms.</li>
<li><b>Bio-Inspired Embodied Intelligence</b> — Drawing inspiration from biological locomotion and sensorimotor systems, we design control architectures that enable robust and adaptive walking, running, climbing, and manipulation on diverse terrains. Our work combines reinforcement learning, model predictive control, and sim-to-real transfer to achieve agile and stable locomotion for legged robots in unstructured environments.</li>
<li><b>Multimodal Learning for Humanoid Robots</b> — We investigate how robots can learn from multimodal sensory inputs (RGB-D cameras, IMUs, tactile sensors, force/torque sensors) to build rich world models that support whole-body planning and contact-rich manipulation. Our research enables humanoid robots to perform tasks in human-centric environments such as homes, offices, and warehouses.</li>
</ol>
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 1em;">
<b>Key Research Directions:</b>
<ul>
<li><b class="blue">Vision-language-action models</b> for robotic task planning and execution</li>
<li><b>Sim-to-real transfer</b> for robust locomotion on diverse terrains</li>
<li><b>Whole-body control</b> and contact-rich manipulation for humanoid platforms</li>
<li><b>Reinforcement learning</b> for adaptive and agile legged locomotion</li>
<li><b>Multimodal perception</b> (vision, tactile, proprioception) for embodied reasoning</li>
</ul>
</div>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "humanoid" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
