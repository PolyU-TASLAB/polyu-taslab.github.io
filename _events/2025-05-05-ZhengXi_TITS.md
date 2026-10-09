---
title: Our paper is accepted by IEEE Transactions on Intelligent Transportation Systems
subtitle: Example news
# author: xxx
image: images/news/Zheng2024TITS_feature.png
tags: news
order: 
---

Our paper "Safety-quantifiable Line Feature-based Monocular Visual Localization with 3D Prior Map" by Xi Zheng, Weisong Wen and Li-Ta Hsu has been accepted by the *IEEE Transactions on Intelligent Transportation Systems*. Congratulations to Xi Zheng and the co-authors. The open-source code is available on [GitHub](https://github.com/ZHENGXi-git/PriorLineVisualLocalization).

### System framework

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/Zheng2024TITS.jpg" alt="System framework of the safety-quantifiable line feature-based visual localization method"></figure>
</div>
<p class="news-caption">System framework of the proposed localization method.</p>

### Abstract

Accurate and safety-quantifiable localization is of great significance for safety-critical autonomous systems, such as unmanned ground vehicles (UGV) and unmanned aerial vehicles (UAV). Visual odometry-based methods can provide accurate positioning over a short period but are subject to drift over time. Moreover, quantifying the safety of the localization solution (i.e. that the error is bounded by a certain value) is still a challenge. To fill these gaps, this paper proposes a safety-quantifiable line feature-based visual localization method with a prior map. Visual-inertial odometry provides a high-frequency local pose estimate, which serves as the initial guess for the visual localization. By obtaining visual line feature pair associations, a foot point-based constraint is proposed to construct the cost function between the 2D lines extracted from the real-time image and the 3D lines extracted from the high-precision prior 3D point cloud map. Moreover, a method inspired by global navigation satellite systems (GNSS) receiver autonomous integrity monitoring (RAIM) is employed to quantify the safety of the derived localization solution. An outlier rejection (also known as fault detection and exclusion) strategy is employed via the weighted sum of squares residual with a Chi-squared probability distribution. A protection level (PL) scheme considering multiple outliers is derived and used to quantify the potential error bound of the localization solution in both the position and rotation domains. The effectiveness of the proposed safety-quantifiable localization system is verified using datasets collected in UAV indoor and UGV outdoor environments. The open-source code is available on [GitHub](https://github.com/ZHENGXi-git/PriorLineVisualLocalization).
