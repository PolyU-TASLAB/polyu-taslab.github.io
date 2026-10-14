---
title: TASLAB and Genvict Conduct Robotic Inspection Data Collection in Shenzhen's Maluanshan Tunnel
subtitle: news
image: images/news/20261014_genvict_tunnel/group_photo.jpg
tags: news
order:
---

From 13 to 14 October 2026, TASLAB visited **Shenzhen Genvict Technologies Co., Ltd. (Genvict, 金溢科技)** for an academic exchange and a field test of unmanned systems in intelligent-transportation scenarios. As part of the visit, the joint team carried out robotic inspection data collection inside the **Maluanshan Tunnel (马峦山隧道)** in Shenzhen, whose right bore is 7,904 m long.

The TASLAB team comprised **Dr. HUANG Feng**, PhD student **XIAO Naigui** and MPhil student **ZHAO Jiaqi**, working together with engineers from Genvict.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20261014_genvict_tunnel/group_photo.jpg" alt="TASLAB and Genvict team members with a quadruped robot and a multi-sensor data-collection platform near the Maluanshan Tunnel"></figure>
</div>
<p class="news-caption">The TASLAB and Genvict team with the quadruped robot and the multi-sensor data-collection platform before entering the Maluanshan Tunnel.</p>

### About Genvict

Founded in 2004 and headquartered in Shenzhen, Genvict was listed on the Shenzhen Stock Exchange in 2017. The company specialises in intelligent transportation and the Internet of Things, with businesses covering electronic toll collection (ETC), vehicle-to-everything (V2X) and vehicle–infrastructure cooperation, and automotive electronics.

### Academic exchange

The visit began with an academic exchange on **high-precision positioning for intelligent connected vehicles and vehicle–infrastructure cooperation**. The two teams discussed the positioning requirements of connected vehicles and roadside infrastructure, as well as the challenges that arise where satellite positioning is unavailable or unreliable.

### Robotic inspection data collection in the tunnel

Long road tunnels are among the most demanding environments for autonomous navigation. GNSS signals are completely blocked, lighting is dim and uneven, and long stretches of near-identical walls offer few distinctive geometric or visual features. Reliable localisation in such settings is essential for robotic tunnel inspection and for connected vehicles that depend on continuous positioning.

During the test, the team deployed a **quadruped robot** and a **mobile multi-sensor data-collection platform** carrying LiDAR and camera sensors. They collected synchronised multi-sensor data through the tunnel entrance and along the tunnel bore, and ran LiDAR–visual mapping and trajectory estimation in real time.

<div class="news-photos" data-cols="2">
  <figure><img src="{{ site.baseurl }}/images/news/20261014_genvict_tunnel/maluanshan_tunnel_sign.jpg" alt="Illuminated sign of the Maluanshan Tunnel, right bore 7,904 m"><figcaption>The Maluanshan Tunnel, with a right bore of 7,904 m.</figcaption></figure>
  <figure><img src="{{ site.baseurl }}/images/news/20261014_genvict_tunnel/team_with_robots.jpg" alt="Team members in safety gear with the robotic platforms beside the tunnel road"><figcaption>Preparing the robotic platforms for the night-time field test.</figcaption></figure>
</div>

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20261014_genvict_tunnel/tunnel_entrance_mapping.jpg" alt="Camera image with projected LiDAR points and real-time 3D map at the tunnel entrance"></figure>
</div>
<p class="news-caption">At the tunnel entrance: camera image overlaid with LiDAR points (left) and the real-time 3D map with the estimated trajectory (right).</p>

<div class="news-photos" data-cols="2">
  <figure><img src="{{ site.baseurl }}/images/news/20261014_genvict_tunnel/tunnel_inside_mapping.jpg" alt="LiDAR-camera overlay and 3D map inside the tunnel"><figcaption>Mapping inside the tunnel, with a stable estimated speed.</figcaption></figure>
  <figure><img src="{{ site.baseurl }}/images/news/20261014_genvict_tunnel/tunnel_degeneration.jpg" alt="Trajectory anomaly flagged during mapping in a geometrically repetitive tunnel section"><figcaption>In feature-poor sections, the system flags a trajectory anomaly, showing the degeneration problem typical of long tunnels.</figcaption></figure>
</div>

The data show both the potential and the difficulty of the task. Near the entrance and in sections with distinctive structures, the robot built consistent 3D maps. Deeper inside the tunnel, the repetitive geometry caused degeneration in LiDAR-based state estimation, which appeared as an abnormal jump in the estimated speed and trajectory. The new dataset provides valuable real-world material for TASLAB's ongoing research on degeneration-aware, multi-sensor fusion localisation for GNSS-denied environments.

### Looking ahead

Following the field test, the two teams will review the results together and explore further collaboration on high-precision positioning, vehicle–infrastructure cooperation and robotic inspection for intelligent transportation infrastructure. TASLAB sincerely thanks Genvict for the invitation and the Genvict engineers for their strong support throughout the night-time field test.
