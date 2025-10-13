---
title: Projects
nav:
  order: 3
  tooltip: 
---

# {% include icon.html icon="fa-solid fa-wrench" %}Research Projects

<div class="project-container">
  <div class="search-section">
    <div class="search-box">
      <input type="text" id="project-search" placeholder="Search projects..." oninput="window.onSearchInput(this)">
      <button type="button" onclick="window.onSearchClear()">
        <i class="icon fa-solid fa-magnifying-glass"></i>
      </button>
      <div id="search-suggestions" class="search-suggestions"></div>
    </div>
    
    <div class="tags-wrapper">
      <button class="tags-toggle" onclick="toggleTags()">
        <i class="fa-solid fa-tags"></i> Categories
        <i class="fa-solid fa-chevron-down"></i>
      </button>
      <div class="tags-container collapsed">
        {% include tags.html tags=site.tags %}
      </div>
    </div>
  </div>

  {% include search-info.html %}

  <div class="projects-timeline">
    {% include list.html data="posts" component="post-excerpt" %}
  </div>
</div>

<style>
.project-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 0;
}

.search-section {
  background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
  border-radius: 16px;
  padding: 2rem;
  margin-bottom: 3rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.search-box {
  position: relative;
  max-width: 600px;
  margin: 0 auto 1.5rem;
}

.search-box input {
  width: 100%;
  padding: 1rem 1.5rem;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  background: white;
}

.search-box input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
  outline: none;
}

.search-suggestions {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  border-radius: 0 0 12px 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  z-index: 1000;
  display: none;
}

.tags-wrapper {
  max-width: 600px;
  margin: 0 auto;
}

.tags-toggle {
  width: 100%;
  padding: 1rem;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 12px;
  font-size: 1.1rem;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tags-container {
  margin-top: 1rem;
  transition: all 0.3s ease;
  overflow: hidden;
}

.tags-container.collapsed {
  height: 0;
  margin-top: 0;
}

.projects-timeline {
  position: relative;
  max-width: 800px;
  margin: 4rem auto;
}

.projects-timeline::before {
  content: '';
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  height: 100%;
  background: #e2e8f0;
}

.post-excerpt {
  position: relative;
  width: calc(50% - 30px);
  margin: 2rem 0;
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  transition: transform 0.3s ease;
}

.post-excerpt:hover {
  transform: translateY(-5px);
}

.post-excerpt:nth-child(odd) {
  margin-left: auto;
}

.post-excerpt::before {
  content: '';
  position: absolute;
  top: 20px;
  width: 20px;
  height: 20px;
  background: #3b82f6;
  border-radius: 50%;
}

.post-excerpt:nth-child(odd)::before {
  left: -40px;
}

.post-excerpt:nth-child(even)::before {
  right: -40px;
}
</style>

<script>
function toggleTags() {
  const container = document.querySelector('.tags-container');
  container.classList.toggle('collapsed');
  
  const icon = document.querySelector('.tags-toggle .fa-chevron-down');
  icon.style.transform = container.classList.contains('collapsed') ? 'rotate(0deg)' : 'rotate(180deg)';
}

// Smart search suggestions
const searchInput = document.getElementById('project-search');
const suggestionsContainer = document.getElementById('search-suggestions');
let projectTitles = []; // Populate this with your project titles

searchInput.addEventListener('input', function(e) {
  const value = e.target.value.toLowerCase();
  if (value.length < 2) {
    suggestionsContainer.style.display = 'none';
    return;
  }

  const suggestions = projectTitles.filter(title => 
    title.toLowerCase().includes(value)
  ).slice(0, 5);

  if (suggestions.length) {
    suggestionsContainer.innerHTML = suggestions
      .map(s => `<div class="suggestion-item">${s}</div>`)
      .join('');
    suggestionsContainer.style.display = 'block';
  } else {
    suggestionsContainer.style.display = 'none';
  }
});

// Close suggestions when clicking outside
document.addEventListener('click', function(e) {
  if (!searchInput.contains(e.target)) {
    suggestionsContainer.style.display = 'none';
  }
});
</script>