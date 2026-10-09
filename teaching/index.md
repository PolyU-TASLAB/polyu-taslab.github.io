---
title: Teaching
nav:
  order: 5
  tooltip: Teaching philosophy, courses and student pathways
---

# {% include icon.html icon="fa-solid fa-chalkboard-teacher" %}Teaching

<p class="section-lead" style="margin: 0 auto 1.4rem; text-align: center;">
  Teaching is the first job of an academic. We help students move confidently from mathematical and engineering
  foundations to <b>responsible, testable AI and unmanned autonomous systems</b>.
</p>


{% include section.html %}

## Teaching Philosophy

<div class="teach-text">
<p>In safety-relevant autonomous systems, obtaining a result is only the beginning. Students must test their assumptions,
identify failure modes, explain uncertainty and communicate evidence for reliability. Across our subjects we organise
learning as a progression from <b>principles</b> to <b>implementation</b>, <b>validation</b> and <b>reflection</b>: students work with
reproducible code, simulation, real sensor data and open-ended engineering tasks rather than treating AI, navigation or
control as purely abstract topics.</p>
<p>Lectures, demonstrations, code review, project milestones and assessment follow the same cycle we use in research:
specify assumptions, implement a method, evaluate it against evidence, diagnose its limitations and defend the result.
Early low-stakes exercises reveal misconceptions in coordinate frames, sensor models, stability and optimisation before
students commit them to a larger project; annotated examples and guided labs support students from different
backgrounds, while extension tasks stretch experienced programmers. This supports inclusion without lowering standards.</p>
</div>

{% include section.html %}

## Courses

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
  box-shadow: 0 6px 20px rgba(158,36,53,0.16);
  transform: translateY(-2px);
}
.teaching-card-header {
  background: var(--primary, #9e2435);
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
  text-align: left;
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
  color: var(--primary, #9e2435);
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
  border-left: 3.5px solid var(--primary, #9e2435);
  transition: box-shadow 0.2s, transform 0.2s;
  text-align: left;
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
  color: var(--primary, #9e2435);
  margin-bottom: 0.3em;
}
.innovation-desc {
  font-size: 0.87em;
  color: #555;
  line-height: 1.55;
}

.supervision-grid {
  margin: 1em 0 2em 0;
  text-align: left;
}
.supervision-item {
  padding: 0.6em 0;
  border-bottom: 1px solid #eee;
  font-size: 0.92em;
  line-height: 1.55;
  text-align: left;
}
.supervision-item:last-child {
  border-bottom: none;
}
.supervision-badge {
  display: inline-block;
  background: var(--primary, #9e2435);
  color: #fff;
  font-size: 0.75em;
  font-weight: 700;
  padding: 0.15em 0.5em;
  border-radius: 4px;
  margin-right: 0.4em;
  vertical-align: middle;
}

.teach-text p {
  max-width: 900px;
  margin: 0 0 0.9rem;
}
.teach-quotes {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
  margin: 1em 0 1.5em;
  padding: 0;
  list-style: none;
}
.teach-quotes li {
  margin: 0;
  padding: 1rem 1.1rem;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--surface);
}
.teach-quotes blockquote {
  margin: 0 0 0.6rem;
  padding: 0;
  border: none;
  font-size: 0.95rem;
  font-style: italic;
  line-height: 1.55;
}
.teach-quotes span {
  color: var(--primary);
  font-size: 0.8rem;
  font-weight: 700;
}
.teach-vision {
  max-width: 900px;
  margin: 0;
  padding: 1.3rem 1.5rem;
  border-left: 4px solid var(--primary);
  border-radius: var(--radius);
  background: var(--primary-soft);
}
.teach-vision p {
  margin: 0;
}
</style>

<div class="teaching-card-grid">

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE4011</span>
      <span class="teaching-card-semester">S2 2025/26 · S2 2024/25</span>
    </div>
    <div class="teaching-card-body">
      <h4>Artificial Intelligence in Unmanned Autonomous Systems</h4>
      <p class="teaching-card-venue">Undergraduate · Subject leader and key course designer</p>
      <p class="teaching-card-desc">A practice-oriented AI curriculum for drones and unmanned systems: perception, decision-making and autonomous operation, linking current AI advances with real UAV constraints through code examples and hands-on activities.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE5306</span>
      <span class="teaching-card-semester">S1 2025/26 · New course</span>
    </div>
    <div class="teaching-card-body">
      <h4>Electronics Design and Informatics for the Low-Altitude Economy</h4>
      <p class="teaching-card-venue">Postgraduate · Initiated and designed</p>
      <p class="teaching-card-desc">Electronics, circuits, sensing and information processing taught through drone applications and AI tools for intelligent aerial systems, with pathways to low-altitude-economy industry projects.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE4203</span>
      <span class="teaching-card-semester">2021/22 – 2025/26 · 5 offerings</span>
    </div>
    <div class="teaching-card-body">
      <h4>Guidance and Navigation</h4>
      <p class="teaching-card-venue">Undergraduate core subject</p>
      <p class="teaching-card-desc">Linear algebra and probability for state estimation, coordinate frames, satellite navigation, single-point positioning, RTK and multi-sensor integration, taught through code and real GNSS data. Enrolment grew from 9 to 47 students.</p>
      <span class="teaching-card-link-text"><a href="https://www.youtube.com/watch?v=Ob8aM2lTnbk&list=PLiBu9nX8VXKWhdAB6bXbF7klqF0Amwa4j" target="_blank" rel="noopener">› Lecture videos on YouTube</a></span>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE3004</span>
      <span class="teaching-card-semester">S1 2023/24</span>
    </div>
    <div class="teaching-card-body">
      <h4>Dynamical Systems and Control</h4>
      <p class="teaching-card-venue">Undergraduate</p>
      <p class="teaching-card-desc">Modelling, system response, stability and controller design, with ROS-car laboratories that connect control theory to autonomous vehicles, drones and robots.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE4002</span>
      <span class="teaching-card-semester">2021 – present</span>
    </div>
    <div class="teaching-card-body">
      <h4>Capstone Projects and URIS</h4>
      <p class="teaching-card-venue">Final Year Project and undergraduate research supervision</p>
      <p class="teaching-card-desc">Capstone and URIS projects on UAV systems, multi-sensor fusion, autonomous vehicles and robotic perception, including a Merit Award for Best URIS Research Project 2024.</p>
    </div>
  </div>

  <div class="teaching-card">
    <div class="teaching-card-header">
      <span class="teaching-card-code">AAE2004 · AAE6102</span>
      <span class="teaching-card-semester">Earlier and invited teaching</span>
    </div>
    <div class="teaching-card-body">
      <h4>Aviation Systems · Satellite Communication and Navigation</h4>
      <p class="teaching-card-venue">Undergraduate subject and invited postgraduate lectures</p>
      <p class="teaching-card-desc">Path planning and regulation for aviation systems, and invited lectures on advanced GNSS positioning, multi-sensor integration and AI-aided navigation in cities.</p>
    </div>
  </div>

</div>

{% include section.html %}

## Teaching Innovations

<div class="innovation-grid">

  <div class="innovation-card">
    <div class="innovation-title">GitHub-based learning</div>
    <div class="innovation-desc">GenAI-assisted, project-based collaborative learning with 50+ code examples and structured peer review in AAE4203 and AAE4011, extended to partner universities including Wuhan University, Beihang University and UC Berkeley.</div>
  </div>

  <div class="innovation-card">
    <div class="innovation-title">Hands-on project-based learning</div>
    <div class="innovation-desc">ROS-car projects, PX4 and ArduPilot drone-programming workshops, MATLAB/Python demonstrations of GNSS positioning and factor-graph optimisation, and PyTorch/TensorFlow in AI courses.</div>
  </div>

  <div class="innovation-card">
    <div class="innovation-title">MSc in Low-altitude Economy</div>
    <div class="innovation-desc">As Associate Programme Leader, drafted the programme proposal and curriculum framework, connecting UAV systems, airspace management, AI, safety and operations, and led industry consultations.</div>
  </div>

  <div class="innovation-card">
    <div class="innovation-title">Industry in the classroom</div>
    <div class="innovation-desc">Real autonomous-driving case studies, guest speakers from Huawei and Meituan, and field trips to testing facilities, so students see how methods meet real constraints.</div>
  </div>

  <div class="innovation-card">
    <div class="innovation-title">Classroom to Competition to Career</div>
    <div class="innovation-desc">A cross-faculty education scheme proposed with eight co-investigators from four faculties, linking courses with industry challenges, robotics and drone competitions, internships and careers.</div>
  </div>

  <div class="innovation-card">
    <div class="innovation-title">Open teaching resources</div>
    <div class="innovation-desc">Interactive Jupyter notebooks, 3D visualisation of GNSS multipath, video tutorials and recorded lectures, adopted by other universities in Asia.</div>
  </div>

</div>

{% include section.html %}

## What Students Say

<ul class="teach-quotes">
  <li><blockquote>"Dr. Wen is one of the greatest lecturers that I've ever seen."</blockquote><span>AAE4203, 2022/23</span></li>
  <li><blockquote>"He said teaching is his first job as an academic staff; I can personally feel this from his lectures."</blockquote><span>AAE4203, 2023/24</span></li>
  <li><blockquote>"His teaching and learning activities encouraged us to explore more beyond the scope of the course."</blockquote><span>AAE4011, 2024/25</span></li>
  <li><blockquote>"Clear explanation to the reasons behind equations."</blockquote><span>AAE4203, 2022/23</span></li>
</ul>

{% include section.html %}

## From Classroom to Career

<div class="teach-text">
<p>We build a connected pathway from secondary school to research and industry. Through hands-on robotics outreach and
the PolyU Junior Researcher Mentoring Programme, secondary-school students try AI, coding, drones and autonomous vehicles.
At PolyU, courses lead into capstone and URIS projects, and we support the <b>PolyU AI &amp; Robotics Club</b>, where students from engineering,
construction, fashion and design work in mechanical, electronics, perception and AI groups and progress from training
to Robocon and RoboMaster teams, internships and research.</p>
<p>Students have won a Third Prize in the Hong Kong University Student Innovation and Entrepreneurship Competition, a Merit
Award for Best URIS Research Project, the OneRobotics track championship at the 2026 Hong Kong Physical AI Hackathon, and
competed in the China Universities Aircraft Design Competition.</p>
</div>

{% include section.html %}

## Future Teaching Vision

<div class="teach-vision">
<p>Our vision is a <b>vertically integrated education pathway for trustworthy autonomy</b>, from pre-university outreach and
undergraduate foundations to postgraduate specialisation, interdisciplinary projects and lifelong industry engagement.
We will turn the 50+ examples and GitHub learning environment into linked modules through which students progress from
simulated sensor-fusion exercises to supervised validation on ROS, PX4 and ArduPilot platforms, and then to capstone,
club or research projects assessed for <b>reliability as well as performance</b>. The MSc in Low-altitude Economy, the AI &amp;
Robotics Club, our industry partners and international exchanges will carry this forward, always with an emphasis on
experimental design, reproducibility, safety and ethical responsibility.</p>
</div>

{% include section.html %}

## Student Supervision Highlights

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
