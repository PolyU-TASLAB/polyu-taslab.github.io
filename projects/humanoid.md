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

<p align="center">
  <img width="700" src="{{ 'images/project/E2EHL.png' | relative_url }}" alt="Embodied AI for Humanoid/Legged Robotics">
</p>
<center><i>Embodied AI for Humanoid/Legged Robotics</i></center>

<a href="{{ 'projects' | relative_url }}" style="font-size: 0.9em;">← Back to all Research Directions</a>

{% include section.html %}

## Demo Video

<p align="center">
  <iframe src="//player.bilibili.com/player.html?bvid=BV1GPkvBdEw9&page=1&autoplay=0" width="560" height="315" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</p>
<center><i>Embodied AI for Humanoid/Legged Robotics — TAS Lab, PolyU</i></center>

{% include section.html %}

## Key Research Directions

<ul>
<li><b class="blue">Vision-language-action models</b> for robotic task planning and execution</li>
<li><b class="blue">Sim-to-real transfer</b> for robust locomotion on diverse terrains</li>
<li><b class="blue">Whole-body control</b> and contact-rich manipulation for humanoid platforms</li>
<li><b class="blue">Reinforcement learning</b> for adaptive and agile legged locomotion</li>
<li><b class="blue">Multimodal perception</b> (vision, tactile, proprioception) for embodied reasoning</li>
<li><b class="blue">Human-robot interaction</b> and collaborative task execution</li>
</ul>

{% include section.html %}

## Target Applications

<ul>
<li><b class="blue">Logistics and warehousing</b>: Humanoid robots for package handling, sorting, and delivery</li>
<li><b class="blue">Urban maintenance</b>: Legged robots for inspection and maintenance in complex environments</li>
<li><b class="blue">Healthcare and assistive robotics</b>: Service robots for elderly care and rehabilitation</li>
<li><b class="blue">Search and rescue</b>: Legged robots operating in disaster-stricken environments</li>
</ul>

{% include section.html %}

## Selected Publications (*: Corresponding author)

<style>
p[align="center"] { text-align: center !important; }
p[align="center"] img, p[align="center"] iframe { display: inline-block; max-width: 100%; }
center { text-align: center; font-size: 0.88em; color: #555; margin-top: 4px; }
.pub-list { list-style: none; padding-left: 0; }
.pub-item { margin: 10px 0; padding: 10px 14px; border-left: 3px solid var(--primary, #0795d9); background: #f9fbfd; font-size: 0.92em; line-height: 1.55; }
.pub-title { font-weight: 600; color: var(--primary, #0795d9); }
.pub-authors { font-size: 0.9em; color: #444; }
.pub-venue { font-size: 0.88em; color: #555; font-style: italic; }
.pub-meta { font-size: 0.85em; color: #888; }
</style>

<ul class="pub-list">

<li class="pub-item"><span class="pub-title">Integrated Planning and Control on Manifolds: Factor Graph Representation and Toolkit.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>., Yang, R., Zhang, Y., Hu, J., Chen, Y., Xiao, N., Zhao, J.</span><br><span class="pub-venue">IEEE International Conference on Robotics &amp; Automation (ICRA), 2026.</span></li>

<li class="pub-item"><span class="pub-title">Unified Sufficient Conditions for Exact Convex Relaxation of Nonconvex Optimal Control Problems.</span><br><span class="pub-authors">Yang, R., <strong>Wen, W</strong>., Yang, P., Zhao, Z. and Huang, F.</span><br><span class="pub-venue">IEEE Transactions on Aerospace and Electronic Systems, 2025.</span> <span class="pub-meta">(IF: 5.7, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">EIRM-RL: Epistemic Integrity Risk Monitoring Inspired Safe Reinforcement Learning for Trustworthy Autonomous Navigation.</span><br><span class="pub-authors">Zhang, Y., Wang, Y., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Internet of Things Journal, 13(2), 3500-3512, 2025.</span> <span class="pub-meta">(IF: 8.9, JCR Q1)</span></li>

<li class="pub-item"><span class="pub-title">Learning Safe, Optimal, Real-Time Flight Interaction with Deep Confidence-enhanced Reachability Guarantee.</span><br><span class="pub-authors">Zhang, Y., Wang, Y., Yan, P., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE Transactions on Intelligent Transportation Systems, 2025.</span> <span class="pub-meta">(IF: 8.4, JCR Q1, Citations: 2)</span></li>

<li class="pub-item"><span class="pub-title">Tightly Joined Positioning and Control Model for Unmanned Aerial Vehicles Based on Factor Graph Optimization.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>.*, Bai, S., Hsu, L.T.</span><br><span class="pub-venue">IEEE Transactions on Vehicular Technology, 2025.</span> <span class="pub-meta">(IF: 7.1, JCR Q1, Citations: 4)</span></li>

<li class="pub-item"><span class="pub-title">Online Dynamic Model Calibration for Reliable Control of Quadrotor Based on Factor Graph Optimization.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>.*, Bai, S., Hu, J.</span><br><span class="pub-venue">IEEE Transactions on Aerospace and Electronic Systems, 2025.</span> <span class="pub-meta">(IF: 5.7, JCR Q1, Citations: 2)</span></li>

<li class="pub-item"><span class="pub-title">Safe-Assured Learning-Based Deep SE(3) Motion Joint Planning and Control for UAV Interactions with Dynamic Environments.</span><br><span class="pub-authors">Zhang, Y., <strong>Wen, W</strong>., Yan, P.</span><br><span class="pub-venue">IEEE ITSC 2024.</span> <span class="pub-meta">(Citations: 4)</span></li>

<li class="pub-item"><span class="pub-title">Tightly Joining Positioning and Control for Trustworthy Unmanned Aerial Vehicles Based on Factor Graph Optimization in Urban Transportation.</span><br><span class="pub-authors">Yang, P., <strong>Wen, W</strong>.</span><br><span class="pub-venue">IEEE ITSC 2023.</span> <span class="pub-meta">(Citations: 7)</span></li>

</ul>

<p style="text-align:right;font-size:0.88em;margin-top:8px;"><a href="{{ 'research' | relative_url }}" style="color:var(--primary, #1a73e8);">→ Full publication list</a></p>

{% include section.html %}

## Acknowledgement and Collaborators

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
This research is supported by <b class="blue">The Hong Kong Polytechnic University</b> and industry partners. We collaborate with leading research groups in embodied AI and robotics worldwide.
</div>

{% include section.html %}

{% assign posts = site.posts | where: "research_direction", "humanoid" | sort: "date" | reverse %}

## Projects ({{ posts.size }})

{% for post in posts %}
  {% include post-excerpt.html title=post.title url=post.url image=post.image content=post.content excerpt=post.excerpt date=post.date author=post.author tags=post.tags last_modified_at=post.last_modified_at %}
{% endfor %}
