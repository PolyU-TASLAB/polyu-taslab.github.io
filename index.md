---
---

# PolyU TAS LAB's Website
<p align="center">
The Trustworthy Autonomous Systems Laboratory is at the forefront of pioneering advancements in autonomous system technology, emphasizing the importance of safety, reliability, and ethical standards. 

Our laboratory is home to a diverse group of researchers and engineers who specialize in artificial intelligence, robotics, cybersecurity, and human-systems interaction. 

Together, we are committed to developing autonomous systems that inspire confidence and trust among users and stakeholders. Through collaborative efforts with industry partners, academic institutions, and policymakers, our team addresses the complex challenges of integrating autonomous systems into society, ensuring they operate transparently and responsibly.
</p>


{% include section.html %}

## Highlights

{% capture text %}

<!-- **Trustworthiness** **Intelligence**  **Innovation**  **Autonomy** -->

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/3DLA-GNSS.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %}



{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/project/all_set.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}



{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/team/team.jpg"
  link="team"
  title="Our Team"
  text=text
%}
