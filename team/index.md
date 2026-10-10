---
title: Team
nav:
  order: 4
  tooltip: People, advisors, funders and partners
---

# {% include icon.html icon="fa-solid fa-users" %}Team

<div style="text-align: center; margin-bottom: 15px;">
  <img src="{{ site.baseurl }}/images/team/team.png" alt="Team Banner" 
       style="width: 28%; height: auto; object-fit: cover; max-width: 230px; margin: 0 auto; border-radius: 10px;">
</div>

Our lab is made up of a <b class="blue">highly engaged and collaborative team</b> of researchers. We recognize that diverse teams do better research. We foster an environment where team members are treated equally, and where we respect and admire our differences. The team includes <b class="blue">postdocs</b>, <b class="blue">students at all levels</b>, <b class="blue">staff</b>, and our lab mascots.

---

<style>
.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(155px, 1fr));
  gap: 1em;
  justify-items: center;
  margin: 1em 0 2em 0;
  padding: 0;
}
.team-section-title {
  font-size: 1.15em;
  font-weight: 700;
  margin: 2em 0 0.5em 0;
  padding-bottom: 0.4em;
  color: var(--primary, #9e2435);
  letter-spacing: 0.01em;
  text-align: center;
  border-bottom: 2px solid var(--primary, #9e2435);
}
.portrait-wrapper {
  width: 155px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.portrait {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
  padding: 0.8em 0.5em;
  transition: box-shadow 0.2s, transform 0.2s;
  min-width: 135px;
  max-width: 165px;
  text-decoration: none !important;
}
.portrait:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.13);
  transform: translateY(-2px);
}
.portrait-image {
  width: 88px;
  height: 88px;
  object-fit: cover;
  border-radius: 50%;
  margin-bottom: 0.5em;
  border: 2.5px solid var(--primary, #9e2435);
}
.portrait-name {
  font-size: 0.92em;
  font-weight: 600;
  color: #222;
  text-align: center;
  line-height: 1.3;
  margin-bottom: 0.2em;
}
.display_1 {
  font-size: 0.78em;
  color: #666;
  text-align: center;
  width: 100%;
  display: block;
  line-height: 1.3;
  margin-bottom: 0.1em;
}
.display_2 {
  font-size: 0.75em;
  color: #999;
  text-align: center;
  width: 100%;
  display: block;
  line-height: 1.3;
}
.portrait-desc {
  margin-top: 0.3em;
  text-align: center;
  width: 100%;
  font-size: 0.78em;
  color: #555;
  line-height: 1.3;
}
.portrait-links {
  display: flex;
  justify-content: center;
  gap: 0.5em;
  margin-top: 0.4em;
  padding-top: 0.3em;
  border-top: 1px solid #eee;
  width: 100%;
}
.portrait-link-icon {
  color: #888;
  font-size: 0.85em;
  text-decoration: none !important;
  transition: color 0.2s;
  padding: 2px;
}
.portrait-link-icon:hover {
  color: var(--primary, #9e2435);
}
.pi-bio-card {
  background: #faf7f8;
  border-left: 4px solid var(--primary, #9e2435);
  border-radius: 8px;
  padding: 1.2em 1.4em;
  margin: 0.5em 0 2em 0;
  box-shadow: 0 1px 6px rgba(0,0,0,0.06);
}
</style>

{% assign pi_members = site.members | where: "role", "pi" %}
{% assign postdoc_members = site.members | where: "role", "postdoc" %}
{% assign phd_members = site.members | where: "role", "phd" %}
{% assign ms_members = site.members | where: "role", "ms" %}
{% assign phd_ms_count = phd_members.size | plus: ms_members.size %}
{% assign ra_members = site.members | where: "role", "ra" %}
{% assign under_members = site.members | where: "role", "under" %}
{% assign visiting_members = site.members | where: "role", "visiting" %}
{% assign alumni_members = site.members | where: "role", "alumni" %}

<div class="team-section-title">Faculty / Principal Investigator ({{ pi_members.size }})</div>
<div class="team-grid">
  {% include list_students.html data="members" component="portrait_students" filters="role == 'pi'" %}
</div>

<div class="pi-bio-card">
<h4 style="margin:0 0 0.5em 0; color:var(--primary, #9e2435); font-size:1.05em;">About Dr. Weisong Wen — <a href="https://weisongwen.github.io/" style="color:var(--primary, #9e2435);">Homepage</a></h4>
<p style="text-align:left; margin:0 0 0.6em 0; font-size:0.92em; line-height:1.6;">
<b class="blue">Dr. Weisong Wen</b> is an <b class="blue">Assistant Professor</b> at the Department of Aeronautical and Aviation Engineering, The Hong Kong Polytechnic University, and the <b class="blue">Founding Director of the Trustworthy AI and Autonomous Systems Laboratory (TAS Lab)</b>. He also directs the <b class="blue">PolyU-Wuxi Intelligent Transportation and Unmanned Systems Center</b> and the <b class="blue">PolyU-LinXAI</b> and <b class="blue">PolyU-Simple AI Joint Laboratories</b>, and is the Faculty Advisor of the PolyU AI &amp; Robotics Club (200+ members). Dr. Wen aims to build algorithm foundations for <b class="blue">embodied AI</b> that enable trustworthy perception, navigation, and control of autonomous systems. In particular, he aims to develop practical embodied AI-driven autonomous systems (<b class="blue">drones</b>, <b class="blue">intelligent vehicles</b>, and <b class="blue">humanoid robots</b>) with end-to-end learning and safety certification capabilities, enabling them to perceive, reason, and interact with the physical world safely and reliably for the future society.
</p>
<p style="text-align:left; margin:0 0 0.6em 0; font-size:0.92em; line-height:1.6;">
Dr. Wen received a BEng degree in Mechanical Engineering from <b class="blue">Beijing Information Science and Technology University (BISTU)</b> in 2015, and a MEng degree from the <b class="blue">China Agricultural University (CAU)</b> in 2017. He received a PhD degree from <b class="blue">The Hong Kong Polytechnic University (PolyU)</b> supervised by Dr. Li-ta Hsu in 2020. He was also a visiting PhD student at the <b class="blue">University of California, Berkeley (UC Berkeley)</b> in 2018, supervised by Dr. Zhan and Prof. Tomizuka.
</p>
<p style="text-align:left; margin:0; font-size:0.92em; line-height:1.6;">
He has published <b class="blue">129 papers</b>, including <b class="blue">70 journal papers</b> (51 in JCR Q1) and <b class="blue">59 conference papers</b> (ICRA, IROS, ITSC, ION GNSS+), with <b class="blue">3,800+ citations</b> (Google Scholar h-index: <b class="blue">31</b>). He has led <b class="blue">35 research projects</b> as PI with government and industry partners, tackling trustworthy perception for drones in urban low-altitude airspace, safe end-to-end driving for logistics vehicles, and robust AI navigation for legged and humanoid robots. He was ranked among the <b class="blue">World's Top 2% Most-cited Scientists</b> (Stanford/Elsevier) in 2023, 2024 and 2025. His recognitions include the <b class="blue">Natural Science First Prize of the China Simulation Federation (2026)</b>, the <b class="blue">PolyU Faculty of Engineering Merit Award for Outstanding Early Career Researcher (2026)</b>, the <b class="blue">Faculty of Engineering Research Grant Achievement Award (2025)</b>, the <b class="blue">Best Student Paper Award at ION GNSS+ 2024</b> (co-supervised student Penggao Yan), the <b class="blue">Top Cited Paper Award from NAVIGATION (2022)</b>, the <b class="blue">Innovation Award from TechConnect (2021)</b>, and the <b class="blue">Best Presentation Award from ION (2020)</b>. He serves as <b class="blue">Associate Editor of IEEE Transactions on Intelligent Vehicles</b> (2026–) and <b class="blue">IEEE Transactions on Vehicular Technology</b> (2024–), and as Associate Editor for ICRA and IROS (2025–26).
</p>
</div>

<div class="team-section-title">Postdoctoral Fellows ({{ postdoc_members.size }})</div>
<div class="team-grid">
  {% include list_students.html data="members" component="portrait_students" filters="role == 'postdoc'" %}
</div>

<div class="team-section-title">Ph.D. / MPhil Students ({{ phd_ms_count }})</div>
<div class="team-grid">
  {% include list_students.html data="members" component="portrait_students" filters="role == 'phd'" %}
  {% include list_students.html data="members" component="portrait_students" filters="role == 'ms'" %}
</div>

<div class="team-section-title">Research / Project Assistant ({{ ra_members.size }})</div>
<div class="team-grid">
  {% include list_students.html data="members" component="portrait_students" filters="role == 'ra'" %}
</div>

<div class="team-section-title">Undergraduate Students ({{ under_members.size }})</div>
<div class="team-grid">
  {% include list_students.html data="members" component="portrait_students" filters="role == 'under'" %}
</div>

<div class="team-section-title">Visiting Scholars / Students ({{ visiting_members.size }})</div>
<div class="team-grid">
  {% include list_students.html data="members" component="portrait_students" filters="role == 'visiting'" %}
</div>

<div class="team-section-title">Alumni ({{ alumni_members.size }})</div>
<div class="team-grid">
  {% include list_students.html data="members" component="portrait_students" filters="role == 'alumni'" %}
</div>

<div class="team-section-title" id="gallery">Gallery · Life at TAS Lab</div>
<p class="team-section-lead">Team photos, competitions, field tests and visits. Click a photo to enlarge.</p>
{% include gallery.html %}

<div class="team-section-title" id="inclusion-and-diversity">Inclusion and Diversity</div>
<p class="team-section-lead">
  To advance collaborative, practical solutions to global challenges, TAS Lab fosters diversity, equity,
  inclusion and belonging in everything we do.
</p>

<ul class="values-grid">
  <li><span class="values-title">Diversity</span><span class="values-text">drives richer ideas and solutions.</span></li>
  <li><span class="values-title">Equity</span><span class="values-text">ensures that every voice is heard and valued.</span></li>
  <li><span class="values-title">Inclusion</span><span class="values-text">gives everyone a seat at the decision-making table.</span></li>
  <li><span class="values-title">Belonging</span><span class="values-text">means we all feel welcome and confident in our roles.</span></li>
</ul>

<div class="values-commit">
  <p class="values-commit-title">Our commitments</p>
  <ul>
    <li>Make time and safe space for diverse perspectives in decisions, teaching, research and work with partners.</li>
    <li>Acknowledge and help repair the power imbalances that have marginalised many voices.</li>
    <li>Keep becoming more diverse, equitable and inclusive as a lab.</li>
  </ul>
</div>

<div class="team-section-title" id="advisory-board">With gratitude to our Advisory Board ({{ site.data.advisors.size }})</div>
<p class="team-section-lead">We sincerely thank our advisors, industry and academic leaders who generously share their time
  and experience to guide our research, products and partnerships.</p>
{% include advisors.html %}

<div class="team-section-title" id="funders">With gratitude to our funders and partners</div>
<p class="team-section-lead">Our work is made possible by government, industry and university support.</p>

{% include partners.html %}
