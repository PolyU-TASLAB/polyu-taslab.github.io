---
title: Our Autonomous Platforms
# subtitle: End-to-End AI-Powered Self-Driving Systems
# author: Zhang Ziqi
image: images/project/Vehicle/ADV.png
tags: Autonomous-Driving
research_direction: vehicles
order: 
---

Our cutting-edge research platforms for end-to-end AI self-driving, where neural networks learn to drive directly from sensor data to control outputs.

## What is End-to-End AI Self-Driving?

End-to-end AI self-driving represents a paradigm shift in autonomous vehicle technology. Unlike traditional modular pipelines that break down driving into separate perception, prediction, planning, and control modules, end-to-end approaches use deep neural networks to learn the entire driving task holistically—directly mapping raw sensor inputs to vehicle control commands.

This revolutionary approach offers several key advantages:

**Direct Sensor-to-Control Learning**: Neural networks process multi-modal sensor data (cameras, LiDAR, GNSS) and output steering angles, throttle, and brake commands in a single forward pass, eliminating the error propagation inherent in modular systems.

**Learned Representations**: Rather than hand-crafting features and rules, the network automatically discovers optimal internal representations of the driving environment, capturing subtle patterns that human engineers might miss.

**Data-Driven Adaptation**: End-to-end models continuously improve through exposure to diverse driving scenarios, learning complex behaviors like defensive driving, traffic flow prediction, and context-aware decision-making from demonstration data.

**Unified Optimization**: The entire driving pipeline is optimized jointly using gradient-based learning, ensuring that perception and control work synergistically rather than as isolated components.

Our research explores multiple end-to-end architectures—from imitation learning systems that mimic expert drivers to reinforcement learning agents that discover optimal policies through trial and error in simulation, then transfer to real-world deployment.

## Introduction

Autonomous vehicles represent the future of intelligent transportation, leveraging end-to-end AI architectures to transform raw sensor data into safe, human-like driving decisions. Our laboratory develops and deploys advanced self-driving systems that embody the latest breakthroughs in deep learning, computer vision, and robotics.

At the core of our autonomous platforms is an integrated AI pipeline that processes multi-modal sensor streams—LiDAR point clouds, camera images, and GNSS/INS data—through sophisticated neural network architectures. These systems learn to simultaneously perceive the environment, predict future trajectories, and execute driving maneuvers in real-time, handling complex urban scenarios with human-level performance.

The autonomous driving vehicle operates under comprehensive CANBUS control integrated with ROS2 middleware. Our AI control stack communicates seamlessly with the vehicle's MCU, translating high-level neural network outputs into low-level CAN signals for precise actuation. This architecture enables full drive-by-wire control including:

- **Longitudinal control**: Acceleration and braking commands derived from learned policies
- **Lateral control**: Steering angles predicted by end-to-end neural networks  
- **Mode management**: Automated gear shifting (D/P/R/N) based on mission planning
- **Safety systems**: AI-monitored lighting, indicators, and fail-safe mechanisms

This platform serves as our testbed for advancing AI-powered autonomous driving, from imitation learning and reinforcement learning to vision-language models for natural language navigation.

## End-to-End AI Architecture Components

Our autonomous driving system implements a comprehensive end-to-end AI architecture comprising the following key components:

### 1. Multi-Modal Perception Network
**Function**: Fuses data from cameras, LiDAR, and GNSS/INS into unified spatial-temporal representations

**Architecture**: Vision backbone (ResNet, EfficientNet, or Vision Transformers) for image feature extraction; PointNet++/VoxelNet for 3D point cloud processing; Multi-scale feature pyramid networks for detecting objects at various distances; Temporal fusion modules (ConvLSTM, 3D CNNs) for motion prediction

**Outputs**: Bird's-eye-view (BEV) semantic maps, 3D object detections, drivable area segmentation, lane boundary predictions

### 2. World Model & Prediction
**Function**: Learns predictive models of how the environment evolves over time

**Architecture**: Recurrent neural networks (GRU/LSTM) or Transformers for sequential prediction; Probabilistic trajectory forecasting for surrounding vehicles and pedestrians; Occupancy grid prediction for future scene states; Attention mechanisms for modeling agent-agent interactions

**Outputs**: Multi-modal future trajectory distributions, predicted collision risks, uncertainty estimates

### 3. Planning & Decision-Making Network
**Function**: Generates safe, comfortable, and efficient driving trajectories

**Architecture**: Hierarchical planning with high-level route planning and low-level trajectory optimization; Imitation learning from expert demonstrations (Behavioral Cloning, GAIL, DAgger); Reinforcement learning for reward-driven policy optimization (PPO, SAC, TD3); Cost volume networks for evaluating trajectory candidates; Attention-based reasoning for traffic rule compliance

**Outputs**: Reference trajectories (waypoints with velocity profiles), discrete actions (lane changes, stops)

### 4. Control Network
**Function**: Executes planned trajectories through precise vehicle control

**Architecture**: PID controllers enhanced with learned gain scheduling; Model Predictive Control (MPC) with learned dynamics models; Direct end-to-end control networks (steering/throttle/brake prediction); Residual learning to compensate for model uncertainties

**Outputs**: Low-level commands (steering angle, throttle percentage, brake pressure)

### 5. Safety & Verification Layer
**Function**: Ensures AI decisions meet safety constraints and override when necessary

**Components**: Learned safety filters using reachability analysis; Rule-based fallback systems for edge cases; Uncertainty-aware decision-making (epistemic and aleatoric uncertainty); Real-time monitoring and anomaly detection; Redundant sensor validation and fault diagnosis

**Outputs**: Safety scores, intervention flags, fail-safe commands

### 6. Continuous Learning Pipeline
**Function**: Enables the system to improve from real-world deployment data

**Components**: On-vehicle data logging (sensor streams, AI decisions, interventions); Offline reinforcement learning from logged experience; Active learning for identifying informative scenarios; Sim-to-real transfer learning using domain adaptation; Federated learning across vehicle fleet

**Outputs**: Updated model weights, identified edge cases, performance metrics

## Sensor Platform

Our laboratory operates two autonomous vehicle testbeds—one at PolyU Main Campus and another at PolyU-Wuxi Research Institute—both equipped with production-grade sensor suites for multi-modal AI training and validation.

The sensor configuration enables comprehensive environmental perception:

| Sensor Type | Brand/Model | Specifications | AI Application |
|-------------|-------------|----------------|----------------|
| **LiDAR**   | Robosense RS-LiDAR-32 | 32 channels, 200m range, 360° FOV, 30° vertical FOV, 10-20Hz | 3D point cloud processing for obstacle detection, semantic segmentation, and occupancy prediction |
| **Cameras** | HikRobot Event Camera | 1280×720 resolution, 120dB HDR, 60fps, global shutter | Vision-based perception, lane detection, traffic sign recognition, end-to-end driving policy learning |
| **GNSS/INS**| CHCNav GNSS/INS | Dual-frequency RTK, integrated IMU, cm-level accuracy | Ground-truth localization for supervised learning, map-based planning, sensor fusion validation |

This sensor fusion architecture provides redundant, complementary data streams that feed our end-to-end AI models, enabling robust perception under diverse weather and lighting conditions.

## AI-Driven Autonomous Driving Demonstrations

### Real-World Testing: Campus Deployment

<div style="max-width: 850px; margin: 0 auto; border-radius: 15px; overflow: hidden;">
  <iframe width="850" height="480" src="https://www.youtube.com/embed/Q0nq1vHeinM" frameborder="0" allowfullscreen></iframe>
  <p style="text-align: center; margin-top: 10px;"><strong>End-to-End AI Navigation</strong> — PolyU Campus</p>
</div>

<div style="max-width: 850px; margin: 0 auto; border-radius: 15px; overflow: hidden;">
  <iframe width="850" height="480" src="https://www.youtube.com/embed/xPd1KiWvAK8" frameborder="0" allowfullscreen></iframe>
  <p style="text-align: center; margin-top: 10px;"><strong>Autonomous Operation</strong> — PolyU-Wuxi Research Institute</p>
</div>

### AI Training Pipeline: CARLA Simulation

Our AI models are pre-trained and validated in high-fidelity simulation environments before real-world deployment. Using CARLA simulator, we generate diverse driving scenarios for imitation learning, reinforcement learning, and domain adaptation research.

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vehicle/Carla.gif" alt="CARLA Simulation" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
  <p style="margin-top: 10px; text-align: center;"><strong>CARLA Simulation Environment</strong> — End-to-End AI Policy Learning</p>
</div>

<!-- Pedestrian avoidance demonstration -->
<!-- <div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/project/Vehicle/EgoVehicle.gif" alt="Pedestrian Avoidance" 
       style="width: 100%; height: auto; object-fit: cover; max-width: 850px; margin: 0 auto; border-radius: 15px;">
  <p style="margin-top: 10px; text-align: center;">Autonomous Driving with AI-Based Pedestrian Avoidance</p>
</div> -->

## Research Team

**Principal Investigator:**  
[Dr. Wen Weisong](https://polyu-taslab.github.io/members/Wen_Weisong.html) — Assistant Professor, Department of Aeronautical and Aviation Engineering, The Hong Kong Polytechnic University

**Core Researchers:**  
[Mr. Zhang Ziqi](https://polyu-taslab.github.io/members/Zhang_Ziqi.html) — PhD Student, End-to-End Learning & Sensor Fusion  
[Dr. Huang Feng](https://polyu-taslab.github.io/members/Huang_Feng.html) — Postdoctoral Researcher, Navigation & Localization

---

**Research Focus:** End-to-End Deep Learning, Vision-Language Navigation, Multi-Modal Sensor Fusion, Sim-to-Real Transfer, Safe Reinforcement Learning, Imitation Learning, World Models for Autonomous Driving