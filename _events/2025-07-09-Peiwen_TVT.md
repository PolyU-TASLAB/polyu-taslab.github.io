---
title: Our paper is accepted by IEEE Transactions on Vehicular Technology
subtitle: Example news
# author: xxx
image: images/news/peiwen_TVT_system_framework2.png
tags: news
order: 
---

The paper "Tightly Joined Positioning and Control Model for Unmanned Aerial Vehicles Based on Factor Graph Optimization", by Peiwen Yang, Weisong Wen, Shiyu Bai and Li-Ta Hsu of the Trustworthy AI and Autonomous Systems Laboratory (TASLAB), has been accepted by the IEEE Transactions on Vehicular Technology. Congratulations to Peiwen and the co-authors.

### Abstract

The existing motion control pipeline, where the positioning and control are decoupled, struggles to adapt to epistemic and aleatoric uncertainty and nonlinear dynamics. As a result, the motion control reliability of the unmanned aerial vehicle (UAV) is significantly challenged in complex dynamic areas. For example, the ubiquitous global navigation satellite system (GNSS) positioning can be degraded by the signal reflections from surrounding high-rise buildings in complex urban areas, leading to significantly increased positioning uncertainty. Given that positioning and control are highly correlated, this research proposes a tightly joining positioning and control model (JPCM) based on factor graph optimization (FGO). Specifically, the sensor measurements are formulated as the factors in the probabilistic factor graph. In addition, the model predictive control (MPC) is also formulated as the additional factors in the probabilistic factor graph. The factor graph contributed by both the positioning-related factors and the MPC-based factors deeply exploits the complementariness of positioning and control. Finally, we validate the effectiveness and resilience of the proposed method using simulations and real-world experiments that show significantly improved trajectory following performance. To benefit the research community, we open-source our code and make it available at https://github.com/RoboticsPolyu/IPN_MPC.

### System framework

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/peiwen_TVT_system_framework1.png" alt="System framework of the joint positioning and control model"></figure>
</div>

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/peiwen_TVT_system_framework2.png" alt="Factor graph of the joint positioning and control model"></figure>
</div>
<p class="news-caption">System framework of the proposed tightly joined positioning and control model (JPCM).</p>
