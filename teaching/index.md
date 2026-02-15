---
title: Teaching
nav:
  order: 5
  tooltip: Courses and student supervision
---

# {% include icon.html icon="fa-solid fa-chalkboard-teacher" %}Teaching

<div style="text-align: justify; font-size: 0.97em; line-height: 1.65; margin-bottom: 0.5em;">
Teaching is one of the most important parts of our academic mission. We are passionate about inspiring young students to explore the frontiers of <b class="blue">aerospace engineering</b>, <b class="blue">AI</b>, and <b class="blue">autonomous systems</b>.
</div>

{% include section.html %}

## 📚 Courses

<style>
.teaching-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.2em;
  margin: 1em 0 2em 0;
}
.teaching-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  overflow: hidden;
  transition: box-shadow 0.25s, transform 0.25s;
}
.teaching-card:hover {
  box-shadow: 0 6px 20px rgba(7,149,217,0.16);
  transform: translateY(-2px);
}
.teaching-card-header {
  background: var(--primary, #0795d9);
  padding: 0.6em 1em;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.3em;
}
.teaching-card-code {
  font-weight: 700;
  font-size: 0.95em;
  color: #fff;
  letter-spacing: 0.5px;
}
.teaching-card-semester {
  font-size: 0.78em;
  color: rgba(255,255,255,0.85);
}
.teaching-card-body {
  padding: 0.9em 1em;
}
.teaching-card-body h4 {
  margin: 0 0 0.3em 0;
  font-size: 1em;
  font-weight: 700;
  color: #222;
  line-height: 1.35;
}
.teaching-card-venue {
  font-size: 0.82em;
  color: #888;
  margin: 0 0 0.4em 0;
}
.teaching-card-desc {
  font-size: 0.88em;
  color: #555;
  line-height: 1.55;
  margin: 0;
}
.teaching-card-link-text {
  display: inline-block;
  margin-top: 0.5em;
  font-size: 0.85em;
  color: var(--primary, #0795d9);
  font-weight: 600;
}

.innovation-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1em;
  margin: 1em 0 2em 0;
}
.innovation-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.07);
  padding: 1em 1.1em;
  border-left: 3.5px solid var(--primary, #0795d9);
  transition: box-shadow 0.2s, transform 0.2s;
}
.innovation-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.13);
  transform: translateY(-2px);
}
.innovation-icon {
  font-size: 1.5em;
  margin-bottom: 0.3em;
}
.innovation-title {
  font-size: 0.95em;
  font-weight: 700;
  color: var(--primary, #0795d9);
  margin-bottom: 0.3em;
}
.innovation-desc {
  font-size: 0.87em;
  color: #555;
  line-height: 1.55;
}

.supervision-grid {
  margin: 1em 0 2em 0;
}
.supervision-item {
  padding: 0.6em 0;
  border-bottom: 1px solid #eee;
  font-size: 0.92em;
  line-height: 1.55;
}
.supervision-item:last-child {
  border-bottom: none;
}
.supervision-badge {
  display: inline-block;
  background: var(--primary, #0795d9);
  color: #fff;
  font-size: 0.75em;
  font-weight: 700;
  padding: 0.15em 0.5em;
  border-radius: 4px;
  margin-right: 0.4em;
  vertical-align: middle;
}
</style>

<div class="teaching-card-grid">

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE4011</span>
      <span class="teaching-card-semester">S2 2024/25</span>
    </div>
    <div class="teaching-card-body">
      <h4>Artificial Intelligence in Unmanned Autonomous Systems</h4>
      <p class="teaching-card-venue">Undergraduate course · PolyU AAE</p>
      <p class="teaching-card-desc">Covers AI fundamentals for autonomous drones and ground robots, including perception, planning, and decision-making using deep learning and reinforcement learning.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE4203</span>
      <span class="teaching-card-semester">S1 2024/25 · S2 2023/24 · S1 2022/23 · S2 2021/22</span>
    </div>
    <div class="teaching-card-body">
      <h4>Guidance and Navigation</h4>
      <p class="teaching-card-venue">Undergraduate course · PolyU AAE</p>
      <p class="teaching-card-desc">GNSS positioning (SPP, DGNSS, RTK), visual navigation, state estimation using Kalman filtering and factor graph optimization. Includes video lectures and hands-on tutorials.</p>
      <span class="teaching-card-link-text"><a href="https://www.youtube.com/watch?v=Ob8aM2lTnbk&list=PLiBu9nX8VXKWhdAB6bXbF7klqF0Amwa4j" target="_blank">› View lecture videos on YouTube</a></span>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE3004</span>
      <span class="teaching-card-semester">S1 2023/24</span>
    </div>
    <div class="teaching-card-body">
      <h4>Dynamical Systems and Control</h4>
      <p class="teaching-card-venue">Undergraduate course · PolyU AAE</p>
      <p class="teaching-card-desc">Fundamentals of dynamical systems modeling, stability analysis, and feedback control design for aerospace and robotics applications.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE2004</span>
      <span class="teaching-card-semester">2022</span>
    </div>
    <div class="teaching-card-body">
      <h4>Introduction to Aviation System and Air Transport Regulation</h4>
      <p class="teaching-card-venue">Undergraduate course · PolyU AAE</p>
      <p class="teaching-card-desc">Path planning for aerospace and aviation systems, introducing foundational concepts in aviation regulation and system design.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE4002</span>
      <span class="teaching-card-semester">2021 – Present</span>
    </div>
    <div class="teaching-card-body">
      <h4>Undergraduate Capstone Project</h4>
      <p class="teaching-card-venue">Final Year Project supervision · PolyU AAE</p>
      <p class="teaching-card-desc">Supervising undergraduate capstone projects on UAV systems, multi-sensor fusion, autonomous vehicles, and robotic perception.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE6102</span>
      <span class="teaching-card-semester">Invited Lecture</span>
    </div>
    <div class="teaching-card-body">
      <h4>Satellite Communication and Navigation</h4>
      <p class="teaching-card-venue">Postgraduate course · PolyU AAE</p>
      <p class="teaching-card-desc">Invited lecture on advanced GNSS positioning techniques, multi-sensor integration, and AI-aided navigation in urban environments.</p>
    </div>
  </div>

</div>

{% include section.html %}

## 💡 Teaching Innovations

<div class="innovation-grid">

  <div class="innovation-card">
    <div class="innovation-icon">🎓</div>
    <div class="innovation-title">Programme Development Leadership</div>
    <div class="innovation-desc">As Associate Programme Leader, drafted MSc in Low-altitude Economy proposal to meet emerging industry needs in drone technology and urban air mobility.</div>
  </div>

  <div class="innovation-card">
    <div class="innovation-icon">💻</div>
    <div class="innovation-title">GitHub-based Learning Pedagogy</div>
    <div class="innovation-desc">Pioneered GitHub-based collaborative learning with 50+ code examples; adopted by Wuhan University, Beihang University, and UC Berkeley.</div>
  </div>

  <div class="innovation-card">
    <div class="innovation-icon">🤖</div>
    <div class="innovation-title">Hands-on Project-Based Learning</div>
    <div class="innovation-desc">ROS car projects, drone programming workshops (PX4/ArduPilot), MATLAB/Python demonstrations, and deep learning frameworks integration.</div>
  </div>

</div>

{% include section.html %}

## 🏅 Student Supervision Highlights

<div class="supervision-grid">

  <div class="supervision-item">
    <span class="supervision-badge">FYP</span>
    <strong>Reliable UAV Perception and Perching Solutions</strong> in Urban Areas — ZHAO Jiaqi, LI Mingjue To, FU Chenlei <span style="color:#888;">(AAE10, 2024/25)</span>
  </div>

  <div class="supervision-item">
    <span class="supervision-badge">FYP</span>
    <strong>Handheld Multi-sensor Fusion Mapping System</strong> — QIN Qijun, WANG Yuteng <span style="color:#888;">(AAE11, 2024/25)</span>
  </div>

  <div class="supervision-item">
    <span class="supervision-badge">URIS</span>
    A High-Definition Map with Traffic Signs Based on <strong>LiDAR-Visual-IMU Fusion SLAM</strong> — QIN Qijun <b class="blue">(Merit Award, Best URIS Research Project 2024)</b>
  </div>

  <div class="supervision-item">
    <span class="supervision-badge">FYP</span>
    An Adaptive Drilling Process for the Aircraft Skin — LAU Chun Ho, LEUNG Cheuk To, CHAN Hei Lam Joshua <span style="color:#888;">(DD01, 2022/23)</span>
  </div>

  <div class="supervision-item">
    <span class="supervision-badge">FYP</span>
    UAS for Situation Awareness and Risk Assessment — LAM Yat Long, CHEN Yat Nam <span style="color:#888;">(AAE39, 2022/23)</span>
  </div>

  <div class="supervision-item">
    <span class="supervision-badge">FYP</span>
    Person-following Mobile Robotics — MOHAMMAD Tamz <span style="color:#888;">(AAE33, 2021/22)</span>
  </div>

</div>
