---
title: Projects
nav:
  order: 3
  tooltip: 
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

<div style="text-align: center; margin-bottom: 2em;">
  <span style="font-size: 1.15em; color: #444;">
    Explore our ongoing and completed projects in trustworthy AI, autonomous systems, and robotics. Click on each project for more details.
  </span>
</div>

<style>
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2em;
  margin: 2em 0;
  align-items: stretch;
}
.projects-section-title {
  font-size: 1.15em;
  font-weight: 700;
  margin: 2em 0 1em 0;
  color: #1a1a1a;
  letter-spacing: 0.01em;
  text-align: center;
}
</style>

{% include section.html %}

<div class="projects-section-title">Browse Projects</div>
<div class="projects-grid">
  {% include list.html data="posts" component="post-excerpt" %}
</div>

<div style="margin-top: 2em;">
  {% include search-box.html %}
  {% include tags.html tags=site.tags %}
  {% include search-info.html %}
</div>