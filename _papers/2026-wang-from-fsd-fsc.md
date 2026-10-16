---
title: 'From FSD to FSC: Enabling Full Smart-Communication in Autonomous Vehicles Through Full Self-Driving Models'
authors:
- Zhicheng Wang
- Shihan Zhao
- Donghui Dai
- Lei Yang
- Feng Huang
- Li-Ta Hsu
- Weisong Wen
publisher: IEEE INFOCOM 2026 - IEEE Conference on Computer Communications
date: '2026-05-18'
doi: https://doi.org/hcb4mk
image: images/papers/cards/2026-wang-from-fsd-fsc.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/From_FSD_to_FSC_Enabling_Full_Smart-Communication_in_Autonomous_Vehicles_Through_Full_Self-Driving_Models.pdf
citation_id: doi:10.1109/INFOCOM59046.2026.11571492
---

## Abstract

In-vehicle wireless systems, such as vehicle-tosatellite communication, face challenges in adapting to rapidly changing environments due to the inherent latency of aligning high-precision beamforming with distant base stations (e.g., satellites). Motivated by the robust sensing capabilities of today's autonomous vehicles, we propose modeling the radio environment in parallel. This allows the in-vehicle communication subsystem to predict channel conditions along the vehicle's planned trajectory and precompute optimal beamforming parameters in advance, effectively addressing rapid environmental changes. To this end, we introduce Full Smart-Communication (FSC), a novel framework that repurposes intermediate feature representations—such as planned trajectories, occupancy maps, and posture estimates—from a vehicle's end-to-end Full SelfDriving (FSD) model to derive spatio-temporal stochastic radio radiance fields. This approach avoids direct access to raw sensor streams while effectively correlating kinematic and environmental states with radio propagation dynamics. Our comprehensive experiments demonstrate that FSC achieves a mean gain of 15 dB and maintains less than one-degree beamforming error at direct upcoming positions. Additionally, FSC reduces power consumption by 70% and GPU memory usage by 94% through the hitchhiking approach. By leveraging FSD-derived environmental awareness for communication, our work bridges the gap between autonomous navigation and robust connectivity, unlocking the synergy of perception and radio resource management in nextgeneration self-driving vehicles.

## Problem Addressed

In-vehicle wireless systems such as vehicle-to-satellite communication struggle to adapt to rapidly changing environments, because aligning high-precision beamforming with distant base stations incurs inherent latency.

## Key Contributions

- Full Smart-Communication (FSC) framework repurposing intermediate Full Self-Driving model features for radio environment modeling
- Spatio-temporal stochastic radio radiance fields derived from planned trajectories, occupancy maps, and posture estimates without raw sensor access
- Channel prediction along the planned trajectory enabling precomputed optimal beamforming parameters
- Hitchhiking execution approach that drastically reduces power consumption and GPU memory usage

## Conclusions

Comprehensive experiments show FSC achieves a mean gain of 15 dB and maintains less than one-degree beamforming error at direct upcoming positions. The hitchhiking approach reduces power consumption by 70% and GPU memory usage by 94%. By combining hitchhiking execution with progressive ray tracing, the framework bridges autonomous navigation and robust connectivity for next-generation self-driving vehicles.
