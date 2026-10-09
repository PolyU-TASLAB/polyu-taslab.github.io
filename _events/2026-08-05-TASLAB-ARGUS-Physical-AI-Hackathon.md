---
title: TASLAB Students Win Championship at Hong Kong's Inaugural Physical AI Hackathon OneRobotics Track
subtitle:
# author:
image: images/news/20260805_physical_ai_hackathon/argus_team_award.jpg
tags: news
order:
---

Four PhD students from the Trustworthy AI and Autonomous Systems Laboratory (TASLAB) at The Hong Kong Polytechnic University (PolyU), Xu Ruijie, Feng Yu, Xiao Naigui and Wang Xin, won the championship of the OneRobotics "Third Hand" Track at Hong Kong's inaugural Physical AI Hackathon. The 48-hour competition concluded on 5 August 2026 at the Charles K. Kao Auditorium in Hong Kong Science Park.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20260805_physical_ai_hackathon/argus_team_award.jpg" alt="TASLAB PhD students on stage as OneRobotics Track winners at Hong Kong's inaugural Physical AI Hackathon"></figure>
</div>
<p class="news-caption">TASLAB members and fellow participants celebrate winning the OneRobotics Track championship.</p>

### ARGUS: an AI "third hand" for group photos

During the hackathon, the team developed ARGUS, an embodied AI portrait photography system designed to serve as an autonomous "third hand" for group photography. The project addresses a familiar problem: when friends or family members want to take a group photo, someone is often left behind the camera, while conventional selfies restrict framing, distance and posing. ARGUS turns a camera-equipped robotic arm into an AI photographer that can perceive its subjects, search for suitable viewpoints, give real-time directions and select the best final portraits.

Users start a photography session simply by waving at the camera. MMPose-based perception detects the gesture, tracks the participating subjects and establishes a stable composition target. The robotic arm then explores a safety-constrained set of viewpoints and uses visual feedback to refine the framing. A Qwen3.5-Omni real-time model provides concise voice guidance, such as asking a subject to move slightly or adjust an expression. When pose, eye state, sharpness, exposure and framing meet the required conditions, the system triggers the shutter. It then evaluates the candidate images for visual quality and viewpoint diversity and presents a final Top 3 selection.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20260805_physical_ai_hackathon/argus_robot_demo.jpg" alt="A portrait selected and evaluated by the ARGUS photography system"></figure>
</div>
<p class="news-caption">An example portrait selected and evaluated by ARGUS based on composition, expression and image quality.</p>

[Watch the 58-second ARGUS real-world demonstration.](https://github.com/RuijieXu0408/Opt-in-Hackthon/blob/feat/director-realtime-integration/docs/assets/argus-demo.mp4)

Rather than letting a large model generate robot joint commands directly, the team separated semantic decision-making, geometric control and hardware safety. The AI director chooses only from executable photography actions supplied by the system, while image-based visual servoing, MoveIt and predefined trajectories handle physical motion within constrained operating conditions. The system observes the scene again after each movement, creating a closed loop from perception and composition to guidance, capture and final image curation. This layered architecture enabled the team to turn its concept into a working physical prototype within 48 hours.

<div class="news-photos" data-cols="1">
  <figure><img src="{{ site.baseurl }}/images/news/20260805_physical_ai_hackathon/argus_award_ceremony.jpg" alt="The ARGUS team demonstrating its robotic portrait photography system"></figure>
</div>
<p class="news-caption">The ARGUS team demonstrates its robotic portrait photography system at the Physical AI Hackathon.</p>

### About the hackathon

The hackathon was initiated by Brizan Ventures together with portfolio companies including SpacemiT and alloop.ai. Following 45 days of global recruitment, seven Meet-Ups, more than 1,000 registrations and over 300 interviews, the event brought together more than 150 participants in over 40 teams from Hong Kong, the Greater Bay Area and overseas universities. Twelve teams advanced to the final competition for the overall MVP award, with projects assessed on technical innovation, product value, implementation potential and team performance. The accompanying Physical AI Carnival also connected participating teams with technology companies, investors, researchers and members of the public.

The team's achievement shows how advances in multimodal AI, visual perception, robot control and human-robot interaction can be integrated into a system that acts in the physical world. It also reflects TASLAB's continuing exploration of trustworthy AI and autonomous systems, with an emphasis on connecting intelligent decision-making to safe, observable and practically meaningful physical actions.

The ARGUS source code is publicly available on [GitHub](https://github.com/RuijieXu0408/Opt-in-Hackthon/tree/feat/director-realtime-integration).
