---
title: TAS LAB MPhil Student Xinrui Zhang Delivers Oral Presentation at UPINLBS 2026
subtitle: news
image: images/news/20261108_upinlbs2026/cover.jpg
tags: news
order:
---

On 8 November 2026, Xinrui Zhang, an MPhil student of the Trustworthy AI and Autonomous Systems Laboratory (TAS LAB) at The Hong Kong Polytechnic University (PolyU), attended the 10th International Conference on Ubiquitous Positioning, Indoor Navigation and Location-Based Services (UPINLBS 2026) together with her supervisor, Prof. Weisong Wen. The conference was held at the Qingyuan Campus of Anhui University in Hefei, China, where Xinrui delivered an oral presentation.

UPINLBS 2026 was organized by The Hong Kong Polytechnic University and the PolyU–Hefei Technology and Innovation Research Institute, and locally hosted by Anhui University. The conference took place on 6–8 November 2026 under the theme “Next Generation Positioning.”

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20261108_upinlbs2026/cover.jpg" alt="Xinrui Zhang delivering her oral presentation at UPINLBS 2026, Anhui University, Hefei, China."></figure>
</div>
<p class="news-caption">Xinrui Zhang delivering her oral presentation at UPINLBS 2026, Anhui University, Hefei, China.</p>

Xinrui presented in **Session 04: Multimodal Perception and Intelligent Navigation for Embodied Systems** (8 Nov, 09:00–12:35). Her paper, “A Learned Velocity Factor Improves Tightly-Coupled GNSS/IMU Localization in Urban Canyons” (Paper ID: 142), is co-authored with Qijun Qin, Feng Huang, Jiagui Zhong, and Prof. Weisong Wen. The talk focused on trustworthy GNSS/IMU localization in urban canyons and covered the following key points:

- Motivation: Fixed non-holonomic constraints (NHC) assume near-zero lateral and vertical body-frame velocities with a hand-tuned covariance, which can be too weak or too strong under real urban driving.
- Learned Velocity Factor (LVF): A fine-tuned inertial network predicts lateral and vertical body-frame velocities together with per-epoch uncertainty, and injects the prediction as a soft factor into a tightly-coupled GNSS/IMU factor-graph estimator.
- Training strategy: Two-stage fine-tuning (velocity regression, then uncertainty) with per-platform three-fold sequence-level cross-validation, so every evaluated sequence is predicted by a model that never trained on it.
- Experimental validation: Eighteen real Hong Kong urban driving sequences on two vehicle platforms (Honda and Kia), evaluated under continuous GNSS and controlled 60-second GNSS outages; the oral talk further presented a frozen-transfer study on a third vehicle (Tesla) without retraining, together with operating-envelope and failure-case analysis.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20261108_upinlbs2026/session.jpg" alt="Session 04 board at UPINLBS 2026: Multimodal Perception and Intelligent Navigation for Embodied Systems (8 Nov 09:00–12:35)."></figure>
</div>
<p class="news-caption">Session 04 board at UPINLBS 2026: Multimodal Perception and Intelligent Navigation for Embodied Systems (8 Nov 09:00–12:35).</p>

Xinrui’s participation at UPINLBS 2026 reflects TAS LAB’s commitment to advancing trustworthy AI and autonomous systems through cutting-edge research in urban navigation, multi-sensor fusion, and safety-assured positioning, as well as fostering academic exchange with the global PNT community.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20261108_upinlbs2026/venue.jpg" alt="Outdoor conference backdrop of UPINLBS 2026 at Anhui University, Hefei, China."></figure>
</div>
<p class="news-caption">Outdoor conference backdrop of UPINLBS 2026 at Anhui University, Hefei, China.</p>

More details about the conference can be found on the [UPINLBS 2026 website](https://upinlbs2026.com/).
