---
title: Projects
nav:
  order: 3
  tooltip: 
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

<div class="projects-hero">
  <div class="projects-hero-content">
    <h2>Scientific Research & Innovation</h2>
    <p>
      Explore our portfolio of cutting-edge projects at the intersection of trustworthy AI, autonomous systems, and robotics. Each project is driven by scientific rigor, innovation, and a commitment to real-world impact. Our team collaborates across disciplines to advance the state of the art in autonomy, safety, and intelligent systems.
    </p>
  </div>
</div>

<style>
.projects-hero {
  background: linear-gradient(90deg, #f5f7fa 0%, #e9ecef 100%);
  border-radius: 18px;
  margin: 2em 0 2.5em 0;
  padding: 2.5em 1.5em 2em 1.5em;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
  text-align: center;
}
.projects-hero-content h2 {
  font-size: 2em;
  font-weight: 700;
  margin-bottom: 0.4em;
  color: #1a1a1a;
  letter-spacing: 0.01em;
}
.projects-hero-content p {
  font-size: 1.13em;
  color: #444;
  max-width: 700px;
  margin: 0 auto;
}

.projects-search-container {
  display: flex;
  justify-content: center;
  margin: 2em 0 1.5em 0;
}
.search-box {
  width: 100%;
  max-width: 420px;
  position: relative;
}
.search-box input[type="text"] {
  width: 100%;
  padding: 0.85em 2.5em 0.85em 1.1em;
  border-radius: 10px;
  border: 1.5px solid #b6c2d1;
  font-size: 1.08em;
  background: #f8fafc;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  transition: border-color 0.18s, box-shadow 0.18s;
}
.search-box input[type="text"]:focus {
  border-color: #3b82f6;
  outline: none;
  box-shadow: 0 4px 18px rgba(59,130,246,0.08);
}
.search-box button {
  position: absolute;
  right: 0.7em;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #3b82f6;
  font-size: 1.2em;
  cursor: pointer;
}
.search-suggestions {
  position: absolute;
  left: 0;
  right: 0;
  top: 110%;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 0 0 10px 10px;
  box-shadow: 0 4px 18px rgba(0,0,0,0.07);
  z-index: 10;
  max-height: 200px;
  overflow-y: auto;
  display: none;
}
.search-suggestions.active {
  display: block;
}
.search-suggestions li {
  padding: 0.7em 1em;
  cursor: pointer;
  font-size: 1.03em;
  color: #222;
}
.search-suggestions li:hover {
  background: #f1f5f9;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2.2em;
  margin: 2.5em 0;
}

.card {
  background: #fff;
  border-radius: 14px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.07);
  transition: box-shadow 0.18s, transform 0.18s;
  border: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  min-height: 420px;
}
.card:hover {
  box-shadow: 0 6px 24px rgba(0,0,0,0.13);
  transform: translateY(-4px) scale(1.012);
  border-color: #b6c2d1;
}
.card-image img {
  border-radius: 14px 14px 0 0;
  object-fit: cover;
  width: 100%;
  height: 180px;
  background: #f5f5f5;
}
.card-title {
  font-size: 1.13em;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.2em;
}
.card-subtitle {
  color: #888;
  font-size: 0.97em;
}
.card-text {
  padding: 1em 1.1em 1.2em 1.1em;
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
</style>

{% include section.html %}

<div class="projects-search-container">
  <div class="search-box">
    <!-- The input below should be wired to JS for suggestions -->
    <input type="text" placeholder="Search projects..." oninput="window.onSearchInput(this)">
    <button type="button" onclick="window.onSearchClear()">
      <i class="icon fa-solid fa-magnifying-glass"></i>
    </button>
    <ul class="search-suggestions" id="project-search-suggestions"></ul>
  </div>
</div>

{% include tags.html tags=site.tags %}
{% include search-info.html %}

<div class="projects-grid">
  {% include list.html data="posts" component="post-excerpt" %}
</div>