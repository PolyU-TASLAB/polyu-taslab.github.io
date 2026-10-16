---
title: Online Dynamic Model Calibration for Reliable Control of Quadrotor Based on Factor Graph Optimization
authors:
- Peiwen Yang
- Weisong Wen
- Shiyu Bai
- Jiahao Hu
publisher: IEEE Transactions on Aerospace and Electronic Systems
date: '2025-05-01'
doi: https://doi.org/g9hrnt
image: images/papers/cards/2025-yang-online-dynamic-model.jpg
buttons:
- type: manubot
  text: paper
  link: publications/papers/Online_Dynamic_Model_Calibration_for_Reliable_Control_of_Quadrotor_Based_on_Factor_Graph_Optimization.pdf
- type: source
  text: code
  link: https://github.com/RoboticsPolyu/QUAD_DYN
tags:
- Artificial intelligence
- deep learning
- GNSS
- RTKLIB
repo: https://github.com/RoboticsPolyu/QUAD_DYN
citation_id: doi:10.1109/TAES.2025.3566347
---

## Abstract

Precise dynamic model calibration is essential in achieving reliable control of unmanned aerial vehicles (UAV). However, the existing methods tend to use simplified dynamic models and cannot adapt to variations of the dynamic model. To fill this gap, this paper explores an online dynamic model calibration (ODMC) method for the quadrotor based on factor graph optimization (FGO). First, the dynamic model is derived with more error terms, such as the center of gravity (CoG), aerodynamic drag, horizontal velocity-induced thrust (HVT) disturbance, and viscous effect. 
Moreover, the IMU-body extrinsic parameters and the gravity vector are also identified online. Second, the pose is estimated based on the visual-inertial odometry (VIO) together with the dynamic model parameters. The proposed method is validated using open-source and self-collected datasets. The evaluation demonstrates that the ODMC performs even better than the state-of-the-art data-driven methods (DDM) in force and torque prediction when the maximum velocity is less than 9 m/s. Furthermore, the effectiveness of the proposed method is validated by applying the estimated model in the differential-flatness-based controller (DFBC). Finally, we open-source code and datasets at https://github.com/RoboticsPolyu/QUAD_DYN to benefit the research community. 
Authors' addresses: the authors are with the Department of 
Aeronautical and Aviation Engineering, Hong Kong Polytechnic 
University, 
Hong 
Kong (e-mail: peiwen1.yang@connect.polyu.hk; welson.wen@polyu.edu.hk; shiyu.bai@polyu.edu.hk; jiaha.hu@polyu.edu.hk; hc.man@polyu.edu.hk). (Corresponding author: Weisong Wen.) 
 
LIST OF SYMBOLS 
Symbol 
Remarks 

I ,  w , and  b 
The IMU frame 
I , the world frame 
 w , and the body frame  b 
}
{
,
,
, w w w
I
I
I
I
I
= x p
R v
ω
 

I 's state. 
3 w
I  p
, 
3 3 w
I


R
 are translation vector and rotation matrix from 
I to  w , 
3 w
I  v
 is IMU velocity in  w , and 
3
I 
ω
 is angular velocity in 
I 
, b b
T M 
Resultant thrust 
3 b 
T
 and resultant torque 
3 b 
M
 in  b 
P 
Covariance matrix 
T
1
2
3
, 
, d d d


= 
 d
 
3
 d
, the drag coefficients 
T
1
2
3
,
, b b b


= 
 b

## Problem Addressed

Reliable quadrotor control requires precise dynamic model calibration, but existing methods rely on simplified dynamic models and cannot adapt to variations in the vehicle's dynamics.

## Key Contributions

- FGO-based online dynamic model calibration jointly estimating state, IMU-body extrinsics, gravity vector, and dynamic parameters
- Enhanced dynamic model including center of gravity, aerodynamic drag, horizontal velocity-induced thrust disturbance, and viscous effects
- Actuator model mapping motor inputs to rotor velocity, extracting the aerodynamic torque coefficient to resolve joint observability with z-axis inertia
- Open-source code and datasets for calibration and control validation

## Conclusions

Validation on open-source and self-collected datasets shows ODMC outperforms state-of-the-art data-driven methods in force and torque prediction when maximum velocity is below 9 m/s, and torque remains accurately predicted even after changing the center of gravity. Applied within a differential-flatness-based controller, the calibrated model improves trajectory tracking performance. Future work will extend the framework to outdoor scenarios.
