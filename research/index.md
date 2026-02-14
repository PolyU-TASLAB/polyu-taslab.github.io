---
title: Publications
nav:
  order: 2
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-wrench" %}Publications

<div class="pub-summary" style="text-align:center; margin: 0.5em 0 1.2em 0; font-size: 0.97em; color: #555;">
  More on <a href="https://scholar.google.com/citations?user=N-AFqt8AAAAJ&hl=en" target="_blank" rel="noopener"><strong>Google Scholar</strong></a>
</div>

{% include section.html %}

<style>
/* Override citation styles for academic compact layout */
.citation-container {
  container-type: unset !important;
}
.citation {
  display: flex !important;
  flex-direction: row !important;
  margin: 10px 0 !important;
  padding: 14px 18px !important;
  border-radius: 6px !important;
  background: var(--background) !important;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
  overflow: visible !important;
  border-left: 3px solid var(--primary, #0795d9) !important;
  transition: box-shadow 0.2s, transform 0.15s !important;
  align-items: flex-start !important;
}
.citation:hover {
  box-shadow: 0 3px 12px rgba(0,0,0,0.10) !important;
  transform: translateY(-1px) !important;
}
/* Hide thumbnail images for cleaner academic look */
.citation-image {
  display: none !important;
}
.citation-text {
  padding: 0 !important;
  padding-left: 0 !important;
  gap: 4px !important;
  font-size: 0.93em !important;
}
.citation-text > .icon {
  display: none !important;
}
.citation-title {
  font-size: 1em !important;
  font-weight: 600 !important;
  line-height: 1.4 !important;
  color: var(--primary, #0795d9) !important;
}
.citation-title:hover {
  text-decoration: underline !important;
}
.citation-authors {
  font-size: 0.88em !important;
  color: #444 !important;
  line-height: 1.4 !important;
}
.citation-details {
  font-size: 0.84em !important;
  color: #777 !important;
  line-height: 1.4 !important;
}
.citation-details .citation-publisher {
  font-style: italic !important;
}
.citation-description {
  font-size: 0.85em !important;
  color: #666 !important;
  line-height: 1.45 !important;
  margin-top: 2px !important;
}
.citation-buttons {
  gap: 6px !important;
  margin-top: 2px !important;
}
.citation-buttons .button {
  font-size: 0.82em !important;
  padding: 2px 8px !important;
  border-radius: 4px !important;
  background: #f0f7ff !important;
  color: var(--primary, #0795d9) !important;
  border: 1px solid #d6e8f7 !important;
}
.citation-buttons .button:hover {
  background: var(--primary, #0795d9) !important;
  color: #fff !important;
}
.citation-text > .tags {
  margin-top: 2px !important;
}
.citation-text > .tags .tag {
  font-size: 0.78em !important;
  padding: 1px 8px !important;
}
/* Year headings */
h3 {
  font-size: 1.25rem;
  color: var(--primary, #0795d9);
  border-bottom: 2px solid var(--primary, #0795d9);
  padding-bottom: 0.3em;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}
</style>

## All

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" %}
