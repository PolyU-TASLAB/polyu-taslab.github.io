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
  top: calc(100% + 5px);
  left: 0;
  right: 0;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  border: 1px solid #e2e8f0;
  z-index: 1000;
  max-height: 400px;
  overflow-y: auto;
  display: none;
}

.suggestion-category {
  padding: 8px 12px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #64748b;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
}

.suggestion-item {
  padding: 10px 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s ease;
}

.suggestion-item:hover,
.suggestion-item.selected {
  background: #f1f5f9;
}

.suggestion-item i {
  font-size: 0.9rem;
  color: #64748b;
}

.suggestion-item .tag-suggestion {
  color: #3b82f6;
  font-size: 0.9rem;
}

.suggestion-item .title-suggestion {
  color: #1e293b;
}

.no-results {
  padding: 12px 16px;
  color: #64748b;
  font-style: italic;
  text-align: center;
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
  max-width: 1000px;
  margin: 4rem auto;
  padding: 20px 0;
}

.projects-timeline::before {
  content: '';
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: 3px;
  height: 100%;
  background: linear-gradient(to bottom, transparent, #e2e8f0 10%, #e2e8f0 90%, transparent);
  border-radius: 3px;
}

.post-excerpt {
  position: relative;
  width: calc(50% - 50px);
  margin: 2rem 0;
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.post-excerpt:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.1);
}

.post-excerpt::before {
  content: '';
  position: absolute;
  top: 24px;
  width: 16px;
  height: 16px;
  background: #3b82f6;
  border: 3px solid #fff;
  border-radius: 50%;
  box-shadow: 0 0 0 3px rgba(59,130,246,0.2);
  z-index: 1;
}

.post-excerpt::after {
  content: '';
  position: absolute;
  top: 32px;
  width: 50px;
  height: 2px;
  background: #e2e8f0;
}

.post-excerpt:nth-child(odd) {
  float: left;
  clear: left;
}

.post-excerpt:nth-child(even) {
  float: right;
  clear: right;
}

.post-excerpt:nth-child(odd)::before {
  right: -58px;
}

.post-excerpt:nth-child(even)::before {
  left: -58px;
}

.post-excerpt:nth-child(odd)::after {
  right: -50px;
}

.post-excerpt:nth-child(even)::after {
  left: -50px;
}

.post-date {
  position: absolute;
  top: 0;
  font-size: 0.9rem;
  color: #64748b;
  padding: 4px 12px;
  background: #f8fafc;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.post-excerpt:nth-child(odd) .post-date {
  right: -110px;
}

.post-excerpt:nth-child(even) .post-date {
  left: -110px;
}

.post-excerpt:nth-child(odd) {
  animation: slideInLeft 0.5s ease-out;
}

.post-excerpt:nth-child(even) {
  animation: slideInRight 0.5s ease-out;
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Clear fix for the timeline */
.projects-timeline::after {
  content: '';
  display: table;
  clear: both;
}

/* Make timeline responsive */
@media (max-width: 768px) {
  .projects-timeline::before {
    left: 30px;
  }
  
  .post-excerpt {
    width: calc(100% - 80px);
    float: right;
    clear: both;
  }
  
  .post-excerpt::before {
    left: -45px !important;
  }
  
  .post-excerpt::after {
    left: -37px !important;
    width: 37px;
  }
  
  .post-date {
    left: -85px !important;
    font-size: 0.85rem;
  }
}
</style>

<script>
// Get all project data
const getAllProjects = () => {
  const projects = document.querySelectorAll('.post-excerpt');
  return Array.from(projects).map(project => ({
    title: project.querySelector('h3')?.textContent || '',
    tags: Array.from(project.querySelectorAll('.tag')).map(tag => tag.textContent.trim()),
    element: project
  }));
};

// Get all unique tags
const getAllTags = () => {
  const tags = new Set();
  document.querySelectorAll('.tag').forEach(tag => {
    tags.add(tag.textContent.trim());
  });
  return Array.from(tags);
};

const projects = getAllProjects();
const allTags = getAllTags();

function showSuggestions(query) {
  if (!query || query.length < 1) {
    suggestionsContainer.style.display = 'none';
    return;
  }

  const lcQuery = query.toLowerCase();
  
  // Find matching tags
  const matchingTags = allTags.filter(tag => 
    tag.toLowerCase().includes(lcQuery)
  );

  // Find matching titles
  const matchingTitles = projects.filter(project => 
    project.title.toLowerCase().includes(lcQuery)
  );

  // Build suggestion HTML
  let html = '';
  
  if (matchingTags.length > 0) {
    html += `<div class="suggestion-category">Tags</div>`;
    html += matchingTags.slice(0, 3).map(tag => `
      <div class="suggestion-item" data-type="tag" data-value="${tag}">
        <i class="fa-solid fa-tag"></i>
        <span class="tag-suggestion">${tag}</span>
      </div>
    `).join('');
  }

  if (matchingTitles.length > 0) {
    html += `<div class="suggestion-category">Projects</div>`;
    html += matchingTitles.slice(0, 5).map(project => `
      <div class="suggestion-item" data-type="title" data-value="${project.title}">
        <i class="fa-solid fa-file-lines"></i>
        <span class="title-suggestion">${project.title}</span>
      </div>
    `).join('');
  }

  if (!html) {
    html = '<div class="no-results">No matching results found</div>';
  }

  suggestionsContainer.innerHTML = html;
  suggestionsContainer.style.display = 'block';
}

// Handle keyboard navigation
let selectedIndex = -1;

searchInput.addEventListener('keydown', function(e) {
  const items = suggestionsContainer.querySelectorAll('.suggestion-item');
  
  if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
    e.preventDefault();
    
    if (e.key === 'ArrowDown') {
      selectedIndex = (selectedIndex + 1) % items.length;
    } else {
      selectedIndex = selectedIndex <= 0 ? items.length - 1 : selectedIndex - 1;
    }
    
    items.forEach((item, index) => {
      item.classList.toggle('selected', index === selectedIndex);
    });
  }
  
  if (e.key === 'Enter' && selectedIndex >= 0) {
    const selectedItem = items[selectedIndex];
    handleSuggestionClick(selectedItem);
  }
});

searchInput.addEventListener('input', function(e) {
  selectedIndex = -1;
  showSuggestions(e.target.value);
});

// Handle suggestion clicks
function handleSuggestionClick(element) {
  const type = element.dataset.type;
  const value = element.dataset.value;
  
  if (type === 'tag') {
    // Find and click the corresponding tag element
    document.querySelector(`.tag[data-tooltip="${value}"]`)?.click();
  } else {
    // Filter to show only the selected project
    searchInput.value = value;
    window.onSearchInput(searchInput);
  }
  
  suggestionsContainer.style.display = 'none';
}

suggestionsContainer.addEventListener('click', function(e) {
  const item = e.target.closest('.suggestion-item');
  if (item) {
    handleSuggestionClick(item);
  }
});
</script>