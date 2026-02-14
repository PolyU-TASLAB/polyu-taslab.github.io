---
---

# PolyU TAS LAB's Website

<div align="center">
The Trustworthy AI and Autonomous Systems (TAS) Laboratory is at the forefront of pioneering advancements in autonomous systems (such as UAV and self-driving cars) technology, emphasizing the importance of safety, reliability, and ethical standards. Our laboratory is home to a diverse group of researchers and engineers who specialize in artificial intelligence, robotics, cybersecurity, and human-system interaction. Together, we are committed to developing autonomous systems that inspire confidence and trust among users and stakeholders. Through collaborative efforts with industry partners, academic institutions, and policymakers, our team addresses the complex challenges of integrating autonomous systems into society, ensuring they operate transparently and responsibly.
</div>

{% include section.html %}

## Research Topics

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Our research aims to build algorithm foundations for <strong>embodied AI</strong> that enable trustworthy perception, navigation, and control of autonomous systems. We develop practical embodied AI-driven autonomous systems — including <strong>drones</strong>, <strong>intelligent vehicles</strong>, and <strong>humanoid robots</strong> — with end-to-end learning and safety certification capabilities, enabling them to perceive, reason, and interact with the physical world safely and reliably for the future society. Our work spans large AI models for autonomous systems, foundation models and vision-language-action models for robotic perception and control, AI-enabled multi-sensor fusion, and software-hardware co-design for efficient embodied AI systems.
</div>

<style>
.research-directions {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1em;
  margin: 1em 0 1.5em 0;
}
.rd-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.07);
  padding: 1em 1.1em;
  transition: box-shadow 0.2s, transform 0.2s;
  text-align: left;
  border-left: 3.5px solid var(--primary, #0795d9);
}
.rd-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.13);
  transform: translateY(-2px);
}
.rd-card h4 {
  margin: 0 0 0.4em 0;
  font-size: 0.95em;
  font-weight: 600;
  color: var(--primary, #0795d9);
  text-align: left;
  letter-spacing: 0;
}
.rd-card p {
  margin: 0;
  font-size: 0.88em;
  color: #444;
  line-height: 1.55;
}
</style>

<div class="research-directions">
  <div class="rd-card">
    <h4>🛰️ 3D LiDAR Aided GNSS Positioning</h4>
    <p>AI-driven GNSS positioning (RTK, PPP, PPP-RTK), 3D LiDAR aided NLOS/multipath mitigation, multi-sensor fusion for robust urban navigation.</p>
  </div>
  <div class="rd-card">
    <h4>🔒 Safety-Certifiable Multi-Sensor Fusion</h4>
    <p>Safety-certifiable AI for autonomous navigation, AI-enabled multi-sensor fusion (LiDAR/Camera/IMU/GNSS), integrity monitoring and navigation-control joint optimization.</p>
  </div>
  <div class="rd-card">
    <h4>🚗 End-to-End Autonomous Vehicles</h4>
    <p>End-to-end learning for self-driving, safety certification for logistics applications, V2X-assisted connected autonomous driving.</p>
  </div>
  <div class="rd-card">
    <h4>🤖 Embodied AI for Humanoid Robotics</h4>
    <p>Large AI models and vision-language-action models for robotic perception and control, bio-inspired embodied intelligence, multimodal learning for humanoid robots.</p>
  </div>
  <div class="rd-card">
    <h4>🚁 Embodied Drones for City Maintenance</h4>
    <p>Intelligent drones and UAV swarm systems, aerial manipulation for urban infrastructure, software-hardware co-design for efficient embodied AI drone systems.</p>
  </div>
</div>

---

## Highlights

{% capture text %}
{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/coding.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}
{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/project/all_set.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}
{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="images/team/team.png"
  link="team"
  title="Our Team"
  text=text
%}