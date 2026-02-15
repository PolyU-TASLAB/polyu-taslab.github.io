---
title: Research
nav:
  order: 3
  tooltip: Research projects and directions
---

# {% include icon.html icon="fa-solid fa-flask" %}Research Topics

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Our research aims to <b>build algorithm foundations for embodied AI</b> that enable <b>trustworthy perception, navigation, and control</b> of autonomous systems. We develop practical <b>embodied AI-driven autonomous systems</b> — including <b class="blue">drones</b>, <b class="blue">intelligent vehicles</b>, and <b class="blue">legged/humanoid robots</b> — with <b>end-to-end learning</b> and <b>safety certification</b> capabilities, enabling them to perceive, reason, and interact with the physical world safely and reliably for the future society. Our work spans large AI models for autonomous systems, foundation models and vision-language-action models for robotic perception and control, AI-enabled multi-sensor fusion, and software-hardware co-design for efficient embodied AI systems.
</div>

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
<b>Research Directions:</b><br>
1) <b>3D LiDAR Aided GNSS Positioning</b> — AI-driven GNSS positioning (RTK, PPP, PPP-RTK), 3D LiDAR aided NLOS/multipath mitigation, multi-sensor fusion for robust urban navigation;<br>
2) <b>Safety-certifiable Multi-Sensor Fusion</b> — safety-certifiable AI for autonomous navigation, AI-enabled multi-sensor fusion (LiDAR/Camera/IMU/GNSS), integrity monitoring and navigation-control joint optimization;<br>
3) <b>End-to-End and Safety-Certifiable Autonomous Vehicles</b> — end-to-end learning for self-driving, safety certification for logistics applications, V2X-assisted connected autonomous driving;<br>
4) <b>Embodied AI for Humanoid/Legged Robotics</b> — large AI models and vision-language-action models for robotic perception and control, bio-inspired embodied intelligence, multimodal learning for humanoid/legged robots;<br>
5) <b>Embodied Drones for City Maintenance and Manipulation</b> — intelligent drones and UAV swarm systems, aerial manipulation for urban infrastructure, software-hardware co-design for efficient embodied AI drone systems;<br>
6) <b>Embodied AI for Robotics Education</b> — AI-powered robotics education platforms, hands-on project-based learning with drones and ground robots, GitHub-based collaborative learning pedagogy, bridging academic research and industry-ready skills.
</div>

{% include section.html %}

<style>
.rd-cards {
  display: flex;
  flex-direction: column;
  gap: 2em;
  margin: 1em 0 2em 0;
}
.rd-card-link {
  text-decoration: none !important;
  color: inherit !important;
  display: block;
}
.rd-card {
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0,0,0,0.10);
  transition: box-shadow 0.3s, transform 0.3s;
  background: #fff;
}
.rd-card:hover {
  box-shadow: 0 6px 24px rgba(0,0,0,0.18);
  transform: translateY(-3px);
}
.rd-card-img {
  width: 100%;
  height: 220px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}
.rd-card-img-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 4em;
  color: rgba(255,255,255,0.7);
}
.rd-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}
.rd-card-img-1 { background: linear-gradient(135deg, #1a5276 0%, #2e86c1 50%, #85c1e9 100%); }
.rd-card-img-2 { background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 50%, #74c69d 100%); }
.rd-card-img-3 { background: linear-gradient(135deg, #4a235a 0%, #7d3c98 50%, #c39bd3 100%); }
.rd-card-img-4 { background: linear-gradient(135deg, #7e2811 0%, #ca6702 50%, #e9c46a 100%); }
.rd-card-img-5 { background: linear-gradient(135deg, #1b3a4b 0%, #006d77 50%, #83c5be 100%); }
.rd-card-img-6 { background: linear-gradient(135deg, #2c3e50 0%, #3498db 50%, #85c1e9 100%); }
.rd-card-body {
  background: #0b6e7f;
  padding: 1em 1.2em;
}
.rd-card-body h3 {
  margin: 0 0 0.3em 0;
  font-size: 1.1em;
  font-weight: 700;
  color: #fff;
  line-height: 1.35;
}
.rd-card-body .rd-find-more {
  font-size: 0.9em;
  color: rgba(255,255,255,0.85);
  text-decoration: none;
}
.rd-card-body .rd-find-more:hover {
  color: #fff;
  text-decoration: underline;
}
@media (min-width: 700px) {
  .rd-cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5em;
  }
  .rd-card-img {
    height: 200px;
  }
}
@media (min-width: 1000px) {
  .rd-card-img {
    height: 240px;
  }
}
</style>

<div class="rd-cards">

  <a href="{{ 'projects/gnss' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-img">
        <img src="{{ 'images/project/3DLA-GNSS.jpg' | relative_url }}" alt="3D LiDAR Aided GNSS Positioning for Robotics Navigation">
      </div>
      <div class="rd-card-body">
        <h3>3D LiDAR Aided GNSS Positioning for Robotics Navigation</h3>
        <span class="rd-find-more">› Find out more</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/fusion' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-img">
        <img src="{{ 'images/project/multi-sensor.jpg' | relative_url }}" alt="Safety-certifiable Multi-Sensor Fusion">
      </div>
      <div class="rd-card-body">
        <h3>Safety-certifiable Multi-Sensor Fusion for Robotic Navigation in Urban Scenes</h3>
        <span class="rd-find-more">› Find out more</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/vehicles' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-img">
        <img src="{{ 'images/project/E2ELV.png' | relative_url }}" alt="End-to-End Autonomous Vehicles">
      </div>
      <div class="rd-card-body">
        <h3>End-to-End and Safety-Certifiable Autonomous Vehicles for Logistics Applications</h3>
        <span class="rd-find-more">› Find out more</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/humanoid' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-img">
        <img src="{{ 'images/project/E2EHL.png' | relative_url }}" alt="Embodied AI for Humanoid/Legged Robotics">
      </div>
      <div class="rd-card-body">
        <h3>Embodied AI for Humanoid/Legged Robotics</h3>
        <span class="rd-find-more">› Find out more</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/drones' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-img">
        <img src="{{ 'images/project/E2EDrone.png' | relative_url }}" alt="Embodied Drones for City Maintenance and Manipulation">
      </div>
      <div class="rd-card-body">
        <h3>Embodied Drones for City Maintenance and Manipulation</h3>
        <span class="rd-find-more">› Find out more</span>
      </div>
    </div>
  </a>

  <a href="{{ 'projects/education' | relative_url }}" class="rd-card-link">
    <div class="rd-card">
      <div class="rd-card-img">
        <img src="{{ 'images/project/EBAIEdu.png' | relative_url }}" alt="Embodied AI for Robotics Education">
      </div>
      <div class="rd-card-body">
        <h3>Embodied AI for Robotics Education</h3>
        <span class="rd-find-more">› Find out more</span>
      </div>
    </div>
  </a>

</div>
