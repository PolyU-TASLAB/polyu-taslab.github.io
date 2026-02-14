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

{% assign gnss_posts = site.posts | where: "research_direction", "gnss" %}
{% assign fusion_posts = site.posts | where: "research_direction", "fusion" %}
{% assign vehicles_posts = site.posts | where: "research_direction", "vehicles" %}
{% assign humanoid_posts = site.posts | where: "research_direction", "humanoid" %}
{% assign drones_posts = site.posts | where: "research_direction", "drones" %}

## Research Directions

<style>
.rd-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.2em;
  margin: 1em 0 1.5em 0;
}
.rd-card-link {
  text-decoration: none !important;
  color: inherit !important;
  display: block;
}
.rd-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  padding: 1.2em 1.3em;
  transition: box-shadow 0.25s, transform 0.25s;
  text-align: left;
  border-left: 4px solid var(--primary, #0795d9);
  position: relative;
  min-height: 160px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.rd-card:hover {
  box-shadow: 0 6px 20px rgba(7,149,217,0.18);
  transform: translateY(-3px);
}
.rd-card-icon {
  font-size: 1.6em;
  margin-bottom: 0.3em;
}
.rd-card-title {
  font-size: 1.05em;
  font-weight: 700;
  color: var(--primary, #0795d9);
  margin: 0.2em 0 0.4em 0;
  line-height: 1.35;
}
.rd-card-desc {
  font-size: 0.87em;
  color: #555;
  line-height: 1.5;
  margin: 0 0 0.6em 0;
  flex-grow: 1;
}
.rd-card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 0.3em;
}
.rd-card-count {
  font-size: 0.82em;
  color: #888;
  font-weight: 500;
}
.rd-card-arrow {
  color: var(--primary, #0795d9);
  font-size: 0.9em;
  font-weight: 600;
}
.rd-card-arrow::after {
  content: " →";
}
@media (max-width: 640px) {
  .rd-cards { grid-template-columns: 1fr; }
}
</style>

<div class="rd-cards">

  <a href="{{ 'projects/gnss' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-icon">🛰️</div>
      <div class="rd-card-title">3D LiDAR Aided GNSS Positioning for Robotics Navigation</div>
      <div class="rd-card-desc">AI-driven GNSS positioning (RTK, PPP, PPP-RTK), 3D LiDAR aided NLOS/multipath mitigation, multi-sensor fusion for robust urban navigation.</div>
      <div class="rd-card-footer">
        <span class="rd-card-count">{{ gnss_posts.size }} projects</span>
        <span class="rd-card-arrow">View projects</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/fusion' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-icon">🔒</div>
      <div class="rd-card-title">Safety-certifiable Multi-Sensor Fusion for Robotic Navigation in Urban Scenes</div>
      <div class="rd-card-desc">Safety-certifiable AI for autonomous navigation, AI-enabled multi-sensor fusion (LiDAR/Camera/IMU/GNSS), integrity monitoring and navigation-control joint optimization.</div>
      <div class="rd-card-footer">
        <span class="rd-card-count">{{ fusion_posts.size }} projects</span>
        <span class="rd-card-arrow">View projects</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/vehicles' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-icon">🚗</div>
      <div class="rd-card-title">End-to-End and Safety-Certifiable Autonomous Vehicles for Logistics Applications</div>
      <div class="rd-card-desc">End-to-end learning for self-driving, safety certification for logistics applications, V2X-assisted connected autonomous driving.</div>
      <div class="rd-card-footer">
        <span class="rd-card-count">{{ vehicles_posts.size }} projects</span>
        <span class="rd-card-arrow">View projects</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/humanoid' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-icon">🤖</div>
      <div class="rd-card-title">Embodied AI for Humanoid/Legged Robotics</div>
      <div class="rd-card-desc">Large AI models and vision-language-action models for robotic perception and control, bio-inspired embodied intelligence, multimodal learning for humanoid/legged robots.</div>
      <div class="rd-card-footer">
        <span class="rd-card-count">{{ humanoid_posts.size }} projects</span>
        <span class="rd-card-arrow">View projects</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/drones' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-icon">🚁</div>
      <div class="rd-card-title">Embodied Drones for City Maintenance and Manipulation</div>
      <div class="rd-card-desc">Intelligent drones and UAV swarm systems, aerial manipulation for urban infrastructure, software-hardware co-design for efficient embodied AI drone systems.</div>
      <div class="rd-card-footer">
        <span class="rd-card-count">{{ drones_posts.size }} projects</span>
        <span class="rd-card-arrow">View projects</span>
      </div>
    </div>
  </a>

</div>
