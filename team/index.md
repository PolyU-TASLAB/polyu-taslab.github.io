---
title: Team
nav:
  order: 4
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-wrench" %}Team

<div style="text-align: center; margin-bottom: 15px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/team/team.png" alt="Team Banner" 
       style="width: 28%; height: auto; object-fit: cover; max-width: 230px; margin: 0 auto; border-radius: 10px;">
</div>

Our lab is made up of a highly engaged and collaborative team of researchers. We recognize that diverse teams do better research. We foster an environment where team members are treated equally, and where we respect and admire our differences. The team includes postdocs, students at all levels, staff, and our lab mascots.

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
  color: var(--primary, #0795d9);
  letter-spacing: 0.01em;
  text-align: center;
  border-bottom: 2px solid var(--primary, #0795d9);
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
  border: 2.5px solid var(--primary, #0795d9);
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

---

#### Inclusion and Diversity

To fulfill our mission to advance collaborative approaches and practical solutions to global poverty challenges, PolyU TAS Lab strives to foster diversity, equity, inclusion, and belonging in all we do.

We strive to do so as a moral imperative and also because:

- Diversity drives richer ideas and solutions.
- Equity ensures that all voices are heard and valued.
- Inclusion results in a seat at the decision-making table.
- Belonging means that we all feel welcome and confident in our roles.

As such, TAS Lab is committed to:

- Dedicating time and creating safe spaces for people to voice diverse perspectives in decision making, teaching, research, and in our work with community partners.
- Acknowledging, working to understand, and repairing the power imbalances that have historically marginalized many voices, including in the field of international development.
- Progressively becoming more diverse, equitable, and inclusive, and ultimately becoming an anti-racist organization.

In this way, we aim for TAS Lab staff, students, and collaborators around the world to be able to design for a more equitable world.

---

#### We are grateful for the continued support we receive from:

<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/polyu_logo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 250px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/aaelogo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 250px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/feng.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 120px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/RIAM_Logo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 130px; margin: 0 auto; vertical-align: middle;">
</div>
<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/RILSlogo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 180px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/UGC_logo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 220px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/itc-logo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 250px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/TD_logo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 150px; margin: 0 auto; vertical-align: middle;">
</div>
<div style="text-align: center; margin-bottom: 20px;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/RGC_logo.jpg"
       style="width: 100%; height: auto; object-fit: cover; max-width: 150px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/guangdong_logo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 170px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/huawei_logo.webp"
       style="width: 100%; height: auto; object-fit: cover; max-width: 180px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/honor-logo-black.svg"
       style="width: 100%; height: auto; object-fit: cover; max-width: 120px; margin: 30px auto; vertical-align: middle;">
  <img src="https://github.com/PolyU-TASLAB/polyu-taslab.github.io/raw/main/images/logo/meituan_logo.png"
       style="width: 100%; height: auto; object-fit: cover; max-width: 120px; margin: 0 auto; vertical-align: middle;">
</div>
