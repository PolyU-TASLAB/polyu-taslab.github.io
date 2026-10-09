---
title: Our Paper Is Accepted by IEEE IROS 2025
subtitle: Example news
# author: xxx
image: images/news/IROS2025_RSG_GLIO.png
tags: news
order: 
---

Our paper "*Roadside GNSS Aided Multi-Sensor Integrated System for Vehicle Positioning in Urban Areas*" by Feng Huang\*, Yihan Zhong\*, Hang Chen, Dongzhe Su, Jin Wu, Weisong Wen and Li-Ta Hsu has been accepted by IEEE IROS 2025. The data will be available on [GitHub](https://github.com/DarrenWong/RSG-GLIO).

### Abstract

Global navigation satellite system (GNSS) positioning can be significantly degraded by multipath and non-line-of-sight (NLOS) signals in urban areas. Cellular vehicle-to-everything (C-V2X) technology provides new opportunities to enhance the GNSS performance of a single intelligent vehicle by leveraging roadside GNSS (RSG) and C-V2X. Inspired by this, we propose an RSG-aided GNSS/LiDAR/IMU (RSG-GLIO) method to achieve reliable odometry and mapping, which leverages the high-quality double-differenced (DD) measurements provided by nearby RSG, effectively mitigating shared random errors such as multipath and NLOS. RSG-GLIO first estimates the absolute state of the vehicle using onboard sensors. Using this initial positioning estimate, the proposed method introduces a coarse-to-fine selection scheme to identify consistent DD observations from the available RSG measurements. Finally, the consistent roadside DD constraints are jointly optimized in a factor graph optimization. Static and dynamic data collected with multiple RSG receivers deployed in the Hong Kong C-V2X testbed are extensively evaluated to assess the effectiveness of roadside-aided positioning. The results demonstrate a 36.6% improvement in absolute positioning accuracy compared with the state-of-the-art GLIO method. Furthermore, we show the potential of employing RSG as low-cost base stations in dense urban areas. The data of our work is publicly accessible on [GitHub](https://github.com/DarrenWong/RSG-GLIO).

### System framework

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/IROS2025_RSG_GLIO.png" alt="System framework of RSG-GLIO"></figure>
</div>
<p class="news-caption">System framework of the proposed RSG-GLIO method.</p>
