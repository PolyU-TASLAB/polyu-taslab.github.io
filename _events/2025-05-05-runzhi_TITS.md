---
title: Our Paper Is Accepted by IEEE Transactions on Intelligent Transportation Systems
subtitle: Example news
# author: xxx
image: images/news/runzhi_TITS_train_process.png
tags: news
order: 
---

Our paper "*pyrtklib: An open-source package for tightly coupled deep learning and GNSS integration for positioning in urban canyons*" by Runzhi Hu, Penghui Xu, Yihan Zhong and Weisong Wen has been accepted by the *IEEE Transactions on Intelligent Transportation Systems*. Congratulations to Runzhi and the co-authors. The open-source code is available on [GitHub](https://github.com/IPNL-POLYU/pyrtklib).

### Abstract

Global Navigation Satellite Systems (GNSS) are crucial for intelligent transportation systems (ITS), providing essential positioning capabilities globally. However, in urban canyons, GNSS performance can be significantly degraded due to the blockage of direct GNSS signals. The pseudorange measurements are strongly affected, and the conventional model of weighting observations is not suitable in urban canyons. This paper addresses these challenges by integrating Artificial Intelligence (AI), specifically deep learning, into the GNSS positioning process to enhance positioning accuracy. Traditional methods have primarily focused on pseudorange correction due to the absence of ground truth for weight estimation. In response, we propose an indirect training approach using deep learning to optimize both pseudorange bias and weight estimation, aiming to minimize the positioning errors. To support this integration, we developed pyrtklib, a Python binding for the open-source RTKLIB tool, bridging the gap between traditional GNSS algorithms, typically developed in Fortran or C, and modern Python-based AI frameworks. Comparative analyses demonstrate that our method surpasses established tools like goGPS and RTKLIB in positioning accuracy. The source code of the tightly coupled deep learning and GNSS integration, along with pyrtklib, is available on GitHub at [TDL-GNSS](https://github.com/ebhrz/TDL-GNSS) and [pyrtklib](https://github.com/IPNL-POLYU/pyrtklib).

### System framework

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/runzhi_TITS_train_process.png" alt="Training process of the proposed method"></figure>
</div>
<p class="news-caption">Training process.</p>

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/runzhi_TITS_predict_process.png" alt="Prediction process of the proposed method"></figure>
</div>
<p class="news-caption">Prediction process.</p>
