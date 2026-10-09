---
title: Publications
nav:
  order: 2
  tooltip: Journal and conference papers
---

# {% include icon.html icon="fa-solid fa-book" %}Publications

<p class="section-lead" style="margin: 0 auto 1.4rem; text-align: center;">
  Papers on trustworthy positioning, multi-sensor fusion, safe planning and control, and embodied AI.
  Full list on <a href="https://scholar.google.com/citations?user=N-AFqt8AAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>.
</p>

{% assign pub_journal = 0 %}
{% assign pub_conference = 0 %}
{% assign pub_preprint = 0 %}
{% for citation in site.data.citations %}
  {% capture kind %}{% include pub-kind.html publisher=citation.publisher %}{% endcapture %}
  {% assign kind = kind | strip %}
  {% if kind == "journal" %}{% assign pub_journal = pub_journal | plus: 1 %}
  {% elsif kind == "conference" %}{% assign pub_conference = pub_conference | plus: 1 %}
  {% else %}{% assign pub_preprint = pub_preprint | plus: 1 %}{% endif %}
{% endfor %}
{% assign pub_years = site.data.citations | group_by_exp: "c", "c.date | date: '%Y'" | sort: "name" | reverse %}

<ul class="oss-stats">
  <li class="oss-stat"><span class="oss-stat-value">{{ site.data.citations | size }}</span><span class="oss-stat-label">Papers listed here</span></li>
  <li class="oss-stat"><span class="oss-stat-value">{{ pub_journal }}</span><span class="oss-stat-label">Journal articles</span></li>
  <li class="oss-stat"><span class="oss-stat-value">{{ pub_conference }}</span><span class="oss-stat-label">Conference papers</span></li>
  <li class="oss-stat"><span class="oss-stat-value">{{ pub_years.last.name }}–{{ pub_years.first.name }}</span><span class="oss-stat-label">Years covered</span></li>
</ul>

{% include section.html %}

<div class="filter-panel pub-toolbar">
  <div class="filter-row">
    <span class="filter-label">Search</span>
    <div class="filter-search">{% include search-box.html %}</div>
  </div>
  <div class="filter-row">
    <span class="filter-label">Type</span>
    <div class="oss-filters" role="group" aria-label="Filter by venue type">
      <button type="button" class="oss-filter" data-filter="all" aria-pressed="true">All</button>
      <button type="button" class="oss-filter" data-filter="journal" aria-pressed="false">Journal ({{ pub_journal }})</button>
      <button type="button" class="oss-filter" data-filter="conference" aria-pressed="false">Conference ({{ pub_conference }})</button>
      {% if pub_preprint > 0 %}<button type="button" class="oss-filter" data-filter="preprint" aria-pressed="false">Preprint ({{ pub_preprint }})</button>{% endif %}
    </div>
  </div>
  <div class="filter-row">
    <span class="filter-label">Jump to</span>
    <nav class="pub-years" aria-label="Jump to year">
      {% for year in pub_years %}<a href="#{{ year.name }}">{{ year.name }}</a>{% endfor %}
    </nav>
  </div>
</div>

{% include search-info.html %}

<div class="pub-list">
{% include list.html data="citations" component="citation" style="rich" %}
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll(".pub-toolbar .oss-filter");
    var items = document.querySelectorAll(".pub-list .citation-container");
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        var filter = button.dataset.filter;
        buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b === button)); });
        items.forEach(function (item) {
          item.hidden = filter !== "all" && item.dataset.kind !== filter;
        });
      });
    });
  });
</script>
