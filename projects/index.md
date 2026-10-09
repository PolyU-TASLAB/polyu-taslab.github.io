---
title: Projects
published: false
nav:
  order: 3.5
  tooltip: "Government-funded, industry and internal projects"
---

# {% include icon.html icon="fa-solid fa-diagram-project" %}Projects

<p class="section-lead" style="margin: 0 auto 1.6rem; text-align: center;">
  Our research foundation: government-funded projects from Hong Kong and mainland China, industry collaborations
  and PolyU internal projects, spanning trustworthy AI perception, drones, autonomous vehicles and
  legged robots. Click a project for details.
</p>

{% assign n_government = site.projects | where: "type", "government" | size %}
{% assign n_internal = site.projects | where: "type", "internal" | size %}
{% assign n_ongoing = site.projects | where: "status", "ongoing" | size %}
{% assign n_completed = site.projects | where: "status", "completed" | size %}
{% assign n_industry = site.projects | where: "type", "industry" | size %}

{% include section.html %}

<div class="filter-panel">
  <div class="filter-row">
    <span class="filter-label">Type</span>
    <div class="oss-filters" role="group" aria-label="Filter by project type" data-group="type">
      <button type="button" class="oss-filter" data-filter="all" aria-pressed="true">All</button>
      <button type="button" class="oss-filter" data-filter="government" aria-pressed="false">Government-funded ({{ n_government }})</button>
      <button type="button" class="oss-filter" data-filter="industry" aria-pressed="false">Industry collaborations ({{ n_industry }})</button>
      <button type="button" class="oss-filter" data-filter="internal" aria-pressed="false">Internal projects ({{ n_internal }})</button>
    </div>
  </div>
  <div class="filter-row">
    <span class="filter-label">Status</span>
    <div class="oss-filters" role="group" aria-label="Filter by status" data-group="status">
      <button type="button" class="oss-filter" data-filter="all" aria-pressed="true">All</button>
      <button type="button" class="oss-filter" data-filter="ongoing" aria-pressed="false">Ongoing ({{ n_ongoing }})</button>
      <button type="button" class="oss-filter" data-filter="completed" aria-pressed="false">Completed ({{ n_completed }})</button>
    </div>
  </div>
  <div class="filter-row">
    <span class="filter-label">Direction</span>
    <div class="oss-filters" role="group" aria-label="Filter by direction" data-group="direction">
      <button type="button" class="oss-filter" data-filter="all" aria-pressed="true">All</button>
      {% assign direction_keys = "drones,legged,driving,perception" | split: "," %}
      {% for d in direction_keys %}
      {% include project-direction.html direction=d %}
      <button type="button" class="oss-filter" data-filter="{{ d }}" aria-pressed="false">{{ direction_label }}</button>
      {% endfor %}
    </div>
  </div>
</div>

{% assign projects = site.projects | sort: "start" | reverse %}
<div class="oss-grid project-grid">
  {% for p in projects %}{% if p.status == "ongoing" %}
  {% include project-card.html project=p %}
  {% endif %}{% endfor %}
  {% for p in projects %}{% if p.status != "ongoing" %}
  {% include project-card.html project=p %}
  {% endif %}{% endfor %}
</div>
<p class="filter-empty" hidden>No projects match these filters.</p>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var state = { type: "all", status: "all", direction: "all" };
    var cards = document.querySelectorAll(".project-grid .project-card");
    var empty = document.querySelector(".filter-empty");
    document.querySelectorAll(".filter-panel .oss-filters").forEach(function (group) {
      var key = group.dataset.group;
      var buttons = group.querySelectorAll(".oss-filter");
      buttons.forEach(function (button) {
        button.addEventListener("click", function () {
          state[key] = button.dataset.filter;
          buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b === button)); });
          var shown = 0;
          cards.forEach(function (card) {
            card.hidden =
              (state.type !== "all" && card.dataset.type !== state.type) ||
              (state.status !== "all" && card.dataset.status !== state.status) ||
              (state.direction !== "all" && card.dataset.direction !== state.direction);
            if (!card.hidden) shown++;
          });
          empty.hidden = shown > 0;
        });
      });
    });
  });
</script>
