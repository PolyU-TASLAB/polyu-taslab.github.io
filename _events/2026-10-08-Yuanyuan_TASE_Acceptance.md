---
title: Paper on Uncertainty-aware Safe Navigation Accepted by IEEE Transactions on Automation Science and Engineering
subtitle: news
image: images/news/20261008_arspo_tase/cover.jpg
tags: news
order:
---

We are pleased to share that the paper "**Adaptive Robust Safe Policy Optimization with Distributional Risk Modeling for Uncertainty-aware Autonomous Navigation**" has been accepted for publication in the [IEEE Transactions on Automation Science and Engineering (T-ASE)](https://www.ieee-ras.org/publications/t-ase) on 8 October 2026.

The paper is authored by **Yuanyuan Zhang, Yingying Wang and Weisong Wen**, with Dr. Yingying Wang as the corresponding author. The work was led by TASLAB PhD student Yuanyuan Zhang at The Hong Kong Polytechnic University.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20261008_arspo_tase/cover.jpg" alt="ARSPO paper accepted by IEEE Transactions on Automation Science and Engineering"></figure>
</div>
<p class="news-caption">ARSPO develops uncertainty-aware safe reinforcement learning for autonomous navigation.</p>

The proposed **Adaptive Robust Safe Policy Optimization (ARSPO)** framework targets mapless unmanned-ground-vehicle navigation in dynamic environments affected by perception noise and uncertain motion. Rather than treating a policy that is safe only on average as sufficient, ARSPO models the distribution and tail risk of both task returns and safety costs.

Its three main components are:

- **distributional value–cost critics**, which learn the full distributions of performance returns and safety costs;
- a **CVaR-based adaptive risk mechanism**, which adjusts the policy between efficient exploration and cautious behaviour according to the estimated risk; and
- **robust transition augmentation**, which adds physically consistent perturbed states during training to improve generalisation under sensor noise and stochastic dynamics.

The method was evaluated in 1,000 randomised CARLA test cases and through real-world UGV deployment. In noise-free simulation, ARSPO achieved a **90.1% success rate**, a **5.8% collision rate** and the shortest reaching time among the evaluated baselines. Under high perception noise, it retained an **80.8% success rate**, compared with **49.8% for Vanilla-SAC**.

### Real-world demonstration

<video
  controls
  muted
  playsinline
  preload="metadata"
  poster="{{ site.baseurl }}/images/news/20261008_arspo_tase/demo_poster.jpg"
  style="display:block; width:100%; max-width:850px; margin:1em auto; border-radius:12px;">
  <source src="{{ site.baseurl }}/images/news/20261008_arspo_tase/arspo_real_world_demo.mp4" type="video/mp4">
  Your browser does not support the video element.
</video>

The demonstration shows the UGV navigating around static obstacles and moving pedestrians in three outdoor scenes. It is also available on [YouTube](https://www.youtube.com/watch?v=6uTtNyseIl8).

Congratulations to Yuanyuan and all co-authors!
