---
title: EIRM-RL Paper and Video Featured
subtitle: news
image: images/news/20261011_eirm_rl/cover.png
tags: news
order:
---

We are pleased to feature our paper, "**Epistemic Integrity Risk Monitoring Inspired Safe Reinforcement Learning for Trustworthy Autonomous Navigation**", published in the [IEEE Internet of Things Journal](https://doi.org/10.1109/JIOT.2025.3633765).

The paper is authored by **Yuanyuan Zhang, Yingying Wang and Weisong Wen**, with Dr. Yingying Wang as the corresponding author. The work was led by TASLAB PhD student Yuanyuan Zhang at The Hong Kong Polytechnic University.

<div class="news-photos" data-cols="1">
  <figure><a href="https://doi.org/10.1109/JIOT.2025.3633765"><img src="{{ site.baseurl }}/images/news/20261011_eirm_rl/cover.png" alt="EIRM-RL for trustworthy autonomous navigation"></a></figure>
</div>
<p class="news-caption">EIRM-RL brings the protection-level concept from aviation integrity monitoring into safe reinforcement learning.</p>

Learning-based robots can become dangerously confident when sensor observations are noisy or biased. **EIRM-RL** addresses this problem by introducing the protection level (PL) and alert limit (AL) concepts used in GNSS integrity monitoring to safe reinforcement learning.

The framework uses an ensemble world model to estimate epistemic uncertainty. An extended protection level then combines systematic bias, sensor noise and model uncertainty. This integrity risk is incorporated as an adaptive safety constraint through Lagrangian duality, allowing the robot to become more cautious when its information is unreliable.

In static tests under Level-2 noise, EIRM-RL achieved a **0.92 success rate** and a **0.02 collision rate**. In an unseen maze under the most challenging noise condition, it maintained a **0.61 success rate** and a **0.33 collision rate** without retraining. Real-world experiments further demonstrated navigation to consecutive goals after position perturbations and safe operation around pedestrians.

### Video explainer

<video
  controls
  muted
  playsinline
  preload="metadata"
  poster="{{ site.baseurl }}/images/news/20261011_eirm_rl/cover.png"
  style="display:block; width:100%; max-width:850px; margin:1em auto; border-radius:12px;">
  <source src="{{ site.baseurl }}/images/news/20261011_eirm_rl/eirm_rl_explainer.mp4" type="video/mp4">
  Your browser does not support the video element.
</video>

The complete video presents the motivation, integrity-monitoring framework, simulation evaluation and real-world demonstrations. It is also available on [YouTube](https://www.youtube.com/watch?v=khBhRrMxDcc).

Read the full paper via [IEEE](https://doi.org/10.1109/JIOT.2025.3633765).
