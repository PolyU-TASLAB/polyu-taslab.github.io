---
title: Dataset & Code
nav:
  order: 6
  tooltip: Open-source datasets and code
---

# {% include icon.html icon="fa-solid fa-code" %}Dataset & Code

<p class="section-lead" style="margin: 0 auto 1.6rem; text-align: center;">
  Open science and reproducible research: the datasets, libraries and systems developed by TAS Lab for
  GNSS positioning, multi-sensor fusion, visual localization, HD mapping and UAV control.
  Everything is free on <a href="https://github.com/PolyU-TASLAB" target="_blank" rel="noopener">GitHub</a>.
</p>

{% assign oss_items = site.opensource | sort: "stars" | reverse %}
{% assign oss_datasets = site.opensource | where: "kind", "Dataset" %}
{% assign oss_code = site.opensource | where: "kind", "Code" %}

<ul class="oss-stats">
  <li class="oss-stat"><span class="oss-stat-value">{% include oss-total.html %}</span><span class="oss-stat-label">GitHub stars</span></li>
  <li class="oss-stat"><span class="oss-stat-value">{{ site.opensource | size }}</span><span class="oss-stat-label">Open-source projects</span></li>
  <li class="oss-stat"><span class="oss-stat-value">{{ oss_datasets | size }}</span><span class="oss-stat-label">Public datasets</span></li>
  <li class="oss-stat"><span class="oss-stat-value">{{ oss_code | size }}</span><span class="oss-stat-label">Code libraries &amp; systems</span></li>
</ul>

{% include section.html %}

<div class="oss-filters" role="group" aria-label="Filter projects">
  <button type="button" class="oss-filter" data-filter="all" aria-pressed="true">All ({{ site.opensource | size }})</button>
  <button type="button" class="oss-filter" data-filter="Dataset" aria-pressed="false">Datasets ({{ oss_datasets | size }})</button>
  <button type="button" class="oss-filter" data-filter="Code" aria-pressed="false">Code ({{ oss_code | size }})</button>
</div>

<div class="oss-grid">
  {% for item in oss_items %}
  <article class="oss-card" data-kind="{{ item.kind }}">
    <a class="oss-image" href="{{ item.url | relative_url }}" aria-label="{{ item.title }}">
      {% if item.image %}
      <img src="{{ item.image | relative_url }}" alt="{{ item.title }}" loading="lazy">
      {% else %}
      <span class="oss-placeholder">{{ item.title }}</span>
      {% endif %}
    </a>
    <div class="oss-body">
      <div class="oss-meta">
        <span class="oss-kind" data-kind="{{ item.kind }}">{{ item.kind }}</span>
        {% if item.stars %}<span class="oss-stars" title="GitHub stars (October 2026)">{% include icon.html icon="fa-solid fa-star" %}{{ item.stars }}</span>{% endif %}
      </div>
      <h3 class="oss-title"><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
      <p class="oss-desc">{{ item.subtitle }}</p>
      {% if item.author %}<p class="oss-desc" style="flex-grow: 0; font-size: 0.8rem;">{{ item.author }}</p>{% endif %}
      <div class="oss-actions">
        {% if item.repo %}<a class="btn btn-primary btn-sm" href="https://github.com/{{ item.repo }}" target="_blank" rel="noopener">GitHub</a>{% endif %}
        <a class="btn btn-light btn-sm" href="{{ item.url | relative_url }}">Details</a>
      </div>
    </div>
  </article>
  {% endfor %}
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll(".oss-filter");
    var cards = document.querySelectorAll(".oss-card");
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        var filter = button.dataset.filter;
        buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b === button)); });
        cards.forEach(function (card) {
          card.hidden = filter !== "all" && card.dataset.kind !== filter;
        });
      });
    });
  });
</script>
