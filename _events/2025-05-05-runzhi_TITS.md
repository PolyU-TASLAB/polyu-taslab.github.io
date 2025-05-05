---
title: Our paper is accpeted by IEEE Transactions on Intelligent Transportation Systems
subtitle: Example news
# author: xxx
image: images/news/runzhi_TITS_train_process.png
tags: news
order: 
---

It is great to share that our paper (*pyrtklib: An open-source package for tightly coupled deep learning and GNSS integration for positioning in urban canyons", by Runzhi Hu, Penghui Xu, Yihan Zhong, Weisong Wen*) is accepted by the *IEEE Transactions on Intelligent Transportation Systems*. Congratulations to Runzhi., etc. The open-source code is available at [Github](https://github.com/IPNL-POLYU/pyrtklib).

## Abstract

Global Navigation Satellite Systems (GNSS) are crucial for intelligent transportation systems (ITS), providing essential positioning capabilities globally. However, in urban canyons, the GNSS performance could significantly degraded due to the blockage of direct GNSS signals. The pseudorange measurements are largely affected and the conventional model of weighting observations is not suitable in urban canyons. This paper addresses these challenges by integrating Artificial Intelligence (AI), specifically deep learning, into GNSS positioning process to enhance positioning accuracy. Traditional methods have primarily focused on pseudorange correction due to the absence of ground truth for weight estimation. In response, we propose an innovative indirect training approach using deep learning to optimize both pseudorange bias and weight estimation, aiming to minimize the positioning errors. To support this integration, we developed pyrtklib, a Python binding for the open-source RTKLIB tool, bridging the gap between traditional GNSS algorithms, typically developed in Fortran or C, and modern Python-based AI frameworks. Comparative analyses demonstrate that our method surpasses established tools like goGPS and RTKLIB in positioning accuracy, marking a significant advancement in the field. The source code of tightly coupled deep learning and GNSS integration, along with pyrtklib, is available on GitHub at [TDL-GNSS](https://github.com/ebhrz/TDL-GNSS) and [pyrtklib](https://github.com/IPNL-POLYU/pyrtklib).


## System Framework

### Training
<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/news/runzhi_TITS_train_process.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

### Prediction
<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/news/runzhi_TITS_predict_process.png" alt="Team Banner" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
</div>

