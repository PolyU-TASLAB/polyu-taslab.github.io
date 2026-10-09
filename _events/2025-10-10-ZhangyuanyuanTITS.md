---
title: Our paper is accepted by IEEE Transactions on Intelligent Transportation Systems
subtitle: news
# author: XIAO Naigui
image: images/news/1010ZYYTITIS/1.png
tags: news
order:
---

We are pleased to share that our paper "Learning Safe, Optimal, and Real-Time Flight Interaction With Deep Confidence-Enhanced Reachability Guarantee", by Yuanyuan Zhang, Yingying Wang, Penggao Yan and Weisong Wen, has been accepted by the IEEE Transactions on Intelligent Transportation Systems. Congratulations to Yuanyuan and our colleagues.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/1010ZYYTITIS/1.png" alt="Title and authors of the accepted paper"></figure>
</div>
<p class="news-caption">The accepted paper in IEEE Transactions on Intelligent Transportation Systems.</p>

### Abstract

In the low-altitude economy, ensuring the safe and agile flight of unmanned aerial vehicles (UAVs) in dynamic obstacle environments is essential for expanding interactive applications like parcel delivery. While deep reinforcement learning (DRL) shows promise for UAV motion planning and control, its trial-and-error exploration often struggles to ensure both agility and safety, especially under uncertain observational noise. Therefore, this paper proposes a deep confidence-enhanced reachability policy optimization (DCRPO) framework. By integrating safe DRL with nonlinear model predictive control (NMPC), DCRPO achieves high-level safety decisions, complex real-time joint planning and control for UAVs. Furthermore, we develop a deep confidence-enhanced reachability guarantee that constructs a set of stochastically forward-reachable planned trajectories under uncertainty, enabling robust safety collision probability certifications. This safe reachability mechanism adaptively selects belief space actions from planned actions to interact with the environment, further enhancing safety and reducing training time. In extensive experiments of UAVs traversing a fast-moving rectangular gate, the proposed method outperforms other state-of-the-art baseline methods under varying environments in terms of operational robustness. Furthermore, the proposed method significantly reduces overall collision violations and training time, greatly improving both training safety and efficiency. The demonstration video ([https://youtu.be/7xkp9U7FSJg](https://youtu.be/7xkp9U7FSJg)) and the source code ([https://github.com/ZyyFLY/DCRPO](https://github.com/ZyyFLY/DCRPO)) are also provided.

### System framework

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/1010ZYYTITIS/framework.jpg" alt="DCRPO system framework diagram"></figure>
</div>
<p class="news-caption">System framework.</p>

### Test evaluation

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/1010ZYYTITIS/test.jpg" alt="Test evaluation results"></figure>
</div>
<p class="news-caption">Test evaluation.</p>
