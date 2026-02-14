---
---

# PolyU TAS LAB's Website

<div align="center">
The <b class="blue">Trustworthy AI and Autonomous Systems (TAS) Laboratory</b> is at the forefront of pioneering advancements in <b class="blue">autonomous systems</b> (such as UAV and self-driving cars) technology, emphasizing the importance of <b class="blue">safety, reliability, and ethical standards</b>. Our laboratory is home to a diverse group of researchers and engineers who specialize in <b class="blue">artificial intelligence</b>, <b class="blue">robotics</b>, cybersecurity, and human-system interaction. Together, we are committed to developing autonomous systems that inspire confidence and trust among users and stakeholders. Through collaborative efforts with industry partners, academic institutions, and policymakers, our team addresses the complex challenges of integrating autonomous systems into society, ensuring they operate transparently and responsibly.
</div>

{% include section.html %}

## Research Topics

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Our research aims to build algorithm foundations for <b class="blue">embodied AI</b> that enable trustworthy perception, navigation, and control of autonomous systems. We develop practical embodied AI-driven autonomous systems — including <b class="blue">drones</b>, <b class="blue">intelligent vehicles</b>, and <b class="blue">legged/humanoid robots</b> — with end-to-end learning and safety certification capabilities, enabling them to perceive, reason, and interact with the physical world safely and reliably for the future society. Our work spans <b class="blue">large AI models</b> for autonomous systems, <b class="blue">foundation models</b> and vision-language-action models for robotic perception and control, <b class="blue">AI-enabled multi-sensor fusion</b>, and software-hardware co-design for efficient embodied AI systems.
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
    <p>AI-driven GNSS positioning (<b class="blue">RTK, PPP, PPP-RTK</b>), 3D LiDAR aided NLOS/multipath mitigation, multi-sensor fusion for robust urban navigation.</p>
  </div>
  <div class="rd-card">
    <h4>🔒 Safety-Certifiable Multi-Sensor Fusion</h4>
    <p>Safety-certifiable AI for autonomous navigation, AI-enabled multi-sensor fusion (<b class="blue">LiDAR/Camera/IMU/GNSS</b>), integrity monitoring and navigation-control joint optimization.</p>
  </div>
  <div class="rd-card">
    <h4>🚗 End-to-End Autonomous Vehicles</h4>
    <p><b class="blue">End-to-end learning</b> for self-driving, safety certification for logistics applications, <b class="blue">V2X-assisted</b> connected autonomous driving.</p>
  </div>
  <div class="rd-card">
    <h4>🤖 Embodied AI for Legged/Humanoid Robotics</h4>
    <p>Large AI models and <b class="blue">vision-language-action models</b> for robotic perception and control, bio-inspired embodied intelligence, multimodal learning for legged/humanoid robots.</p>
  </div>
  <div class="rd-card">
    <h4>🚁 Embodied Drones for City Maintenance</h4>
    <p>Intelligent drones and <b class="blue">UAV swarm systems</b>, aerial manipulation for urban infrastructure, software-hardware co-design for efficient embodied AI drone systems.</p>
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
