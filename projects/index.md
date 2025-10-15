---
title: Projects
nav:
  order: 3
  tooltip:
---

<div class="projects-header">
  <h1>{% include icon.html icon="fa-solid fa-wrench" %}Projects</h1>
  <p>Explore our research projects and innovations</p>
</div>

<div class="search-section">
  <div class="search-container">
    <input type="text" id="project-search" placeholder="Search projects by title or tags...">
    <div class="search-suggestions" id="search-suggestions"></div>
  </div>
</div>

<div class="tags-section">
  <div class="tags-toggle">
    <button id="tags-toggle-btn">
      <span class="toggle-text">Show Tags</span>
      <i class="fa-solid fa-chevron-down"></i>
    </button>
  </div>
  <div class="tags-content">
    {% include tags.html tags=site.tags %}
  </div>
</div>

<div class="search-info" id="search-info"></div>

<div class="projects-list">
  {% include list.html data="posts" component="post-excerpt" %}
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@6.6.2"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Tags toggle functionality
  const tagsToggleBtn = document.getElementById('tags-toggle-btn');
  const tagsContent = document.querySelector('.tags-content');
  const toggleText = tagsToggleBtn.querySelector('.toggle-text');
  const toggleIcon = tagsToggleBtn.querySelector('i');
  
  tagsToggleBtn.addEventListener('click', () => {
    tagsContent.classList.toggle('expanded');
    if (tagsContent.classList.contains('expanded')) {
      toggleText.textContent = 'Hide Tags';
      toggleIcon.classList.replace('fa-chevron-down', 'fa-chevron-up');
    } else {
      toggleText.textContent = 'Show Tags';
      toggleIcon.classList.replace('fa-chevron-up', 'fa-chevron-down');
    }
  });

  // Smart search functionality
  const searchInput = document.getElementById('project-search');
  const suggestionsContainer = document.getElementById('search-suggestions');
  
  // Collect all project data
  const projects = Array.from(document.querySelectorAll('.post-excerpt')).map(post => ({
    title: post.querySelector('h3').textContent,
    tags: Array.from(post.querySelectorAll('.tag')).map(tag => tag.textContent),
    element: post
  }));

  const fuse = new Fuse(projects, {
    keys: ['title', 'tags'],
    threshold: 0.3
  });

  searchInput.addEventListener('input', (e) => {
    const value = e.target.value;
    if (value.length < 2) {
      suggestionsContainer.classList.remove('active');
      return;
    }

    const results = fuse.search(value);
    const suggestions = results.slice(0, 5);
    
    if (suggestions.length > 0) {
      suggestionsContainer.innerHTML = suggestions.map(result => 
        `<div class="suggestion-item">${result.item.title}</div>`
      ).join('');
      suggestionsContainer.classList.add('active');
    } else {
      suggestionsContainer.classList.remove('active');
    }
  });

  document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && !suggestionsContainer.contains(e.target)) {
      suggestionsContainer.classList.remove('active');
    }
  });
});
</script>
