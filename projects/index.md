---
title: Projects
nav:
  order: 3
  tooltip:
---

<div class="projects-header">
  <h1>{% include icon.html icon="fa-solid fa-wrench" %} Projects</h1>
  <p class="subtitle">Explore our research projects and innovations</p>
</div>

<div class="search-section">
  <div class="search-container">
    <input type="text" id="project-search" placeholder="🔍 Search projects by title or tag..." autocomplete="off">
    <div class="search-suggestions" id="search-suggestions"></div>
  </div>
  <div class="tags-collapsible">
    <button id="tags-toggle-btn" class="tags-toggle-btn">
      <span class="toggle-text">Show Tags</span>
      <i class="fa-solid fa-chevron-down"></i>
    </button>
    <div class="tags-content" id="tags-content">
      <!-- Tags will be rendered here by JS for better control -->
    </div>
  </div>
</div>

<div class="search-info" id="search-info"></div>

<div class="projects-list" id="projects-list">
  {% include list.html data="posts" component="post-excerpt" %}
</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
<script src="https://cdn.jsdelivr.net/npm/fuse.js@6.6.2"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  // --- Collapsible tags ---
  const tagsToggleBtn = document.getElementById('tags-toggle-btn');
  const tagsContent = document.getElementById('tags-content');
  const toggleText = tagsToggleBtn.querySelector('.toggle-text');
  const toggleIcon = tagsToggleBtn.querySelector('i');
  let tagsExpanded = false;

  // --- Gather tags and projects ---
  // Wait for posts to render (in case of async includes)
  setTimeout(() => {
    const projectEls = Array.from(document.querySelectorAll('.post-excerpt'));
    const allTags = new Set();
    const projects = projectEls.map(post => {
      const title = post.querySelector('h3')?.textContent?.trim() || '';
      const tags = Array.from(post.querySelectorAll('.tag')).map(tag => {
        const t = tag.textContent.trim();
        allTags.add(t);
        return t;
      });
      return { title, tags, element: post };
    });
    const tagsArr = Array.from(allTags).sort();

    // --- Render tags as pills ---
    function renderTags() {
      tagsContent.innerHTML = tagsArr.map(tag =>
        `<span class="tag-pill" data-tag="${tag}">${tag}</span>`
      ).join('');
    }
    function clearTags() {
      tagsContent.innerHTML = '';
    }

    // --- Tag click filters projects ---
    tagsContent.addEventListener('click', e => {
      if (e.target.classList.contains('tag-pill')) {
        const tag = e.target.dataset.tag;
        searchInput.value = tag;
        filterProjects(tag);
        suggestionsContainer.classList.remove('active');
      }
    });

    // --- Collapsible tags logic ---
    tagsToggleBtn.addEventListener('click', () => {
      tagsExpanded = !tagsExpanded;
      if (tagsExpanded) {
        tagsContent.classList.add('expanded');
        tagsContent.style.maxHeight = tagsContent.scrollHeight + "px";
        toggleText.textContent = 'Hide Tags';
        toggleIcon.classList.remove('fa-chevron-down');
        toggleIcon.classList.add('fa-chevron-up');
        renderTags();
      } else {
        tagsContent.classList.remove('expanded');
        tagsContent.style.maxHeight = null;
        toggleText.textContent = 'Show Tags';
        toggleIcon.classList.remove('fa-chevron-up');
        toggleIcon.classList.add('fa-chevron-down');
        clearTags();
      }
    });

    // --- Smart search with suggestions ---
    const searchInput = document.getElementById('project-search');
    const suggestionsContainer = document.getElementById('search-suggestions');
    const projectsList = document.getElementById('projects-list');

    // Fuse for projects and tags
    const fuse = new Fuse([
      ...projects.map(p => ({ type: 'project', value: p.title })),
      ...tagsArr.map(t => ({ type: 'tag', value: t }))
    ], {
      keys: ['value'],
      threshold: 0.3,
      includeScore: true
    });

    function filterProjects(query) {
      const q = query.trim().toLowerCase();
      let visibleCount = 0;
      projectEls.forEach(post => {
        post.style.display = '';
        const title = post.querySelector('h3')?.textContent?.toLowerCase() || '';
        const tags = Array.from(post.querySelectorAll('.tag')).map(tag => tag.textContent.toLowerCase());
        if (q && !title.includes(q) && !tags.some(t => t.includes(q))) {
          post.style.display = 'none';
        } else {
          visibleCount++;
        }
      });
      // Show info if no results
      const info = document.getElementById('search-info');
      if (q && visibleCount === 0) {
        info.textContent = 'No projects found.';
      } else {
        info.textContent = '';
      }
    }

    searchInput.addEventListener('input', (e) => {
      const value = e.target.value.trim();
      if (value.length < 1) {
        suggestionsContainer.classList.remove('active');
        filterProjects('');
        return;
      }
      const results = fuse.search(value).slice(0, 8);
      if (results.length > 0) {
        suggestionsContainer.innerHTML = results.map(r =>
          `<div class="suggestion-item" data-type="${r.item.type}" data-value="${r.item.value}">
            ${r.item.type === 'tag' ? '<i class="fa fa-tag"></i> ' : '<i class="fa fa-file-alt"></i> '}
            ${r.item.value}
          </div>`
        ).join('');
        suggestionsContainer.classList.add('active');
      } else {
        suggestionsContainer.classList.remove('active');
      }
      // If user types a tag, filter by tag, else by text
      filterProjects(value);
    });

    suggestionsContainer.addEventListener('mousedown', (e) => {
      if (e.target.classList.contains('suggestion-item')) {
        const val = e.target.dataset.value;
        searchInput.value = val;
        filterProjects(val);
        suggestionsContainer.classList.remove('active');
      }
    });

    document.addEventListener('click', (e) => {
      if (!searchInput.contains(e.target) && !suggestionsContainer.contains(e.target)) {
        suggestionsContainer.classList.remove('active');
      }
    });
  }, 0); // End setTimeout
});
</script>

<style>
.projects-header {
  text-align: center;
  margin-bottom: 2.5rem;
}
.projects-header h1 {
  font-size: 2.7rem;
  font-weight: 700;
  letter-spacing: -1px;
  margin-bottom: 0.5rem;
}
.projects-header .subtitle {
  color: #666;
  font-size: 1.15rem;
  margin-top: 0;
}
.search-section {
  max-width: 650px;
  margin: 0 auto 2.5rem;
}
.search-container {
  position: relative;
  margin-bottom: 0.5rem;
}
#project-search {
  width: 100%;
  padding: 14px 22px;
  border: 1.5px solid #e0e0e0;
  border-radius: 30px;
  font-size: 1.08rem;
  background: #fafbfc;
  transition: border 0.2s;
  box-shadow: 0 2px 8px 0 rgba(0,0,0,0.03);
}
#project-search:focus {
  border: 1.5px solid #0077ff;
  outline: none;
  background: #fff;
}
.search-suggestions {
  position: absolute;
  top: 110%;
  left: 0;
  right: 0;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
  z-index: 1000;
  max-height: 260px;
  overflow-y: auto;
  display: none;
  border: 1px solid #e0e0e0;
}
.search-suggestions.active {
  display: block;
}
.suggestion-item {
  padding: 11px 20px;
  cursor: pointer;
  font-size: 1.04rem;
  display: flex;
  align-items: center;
  gap: 0.6em;
  color: #222;
  transition: background 0.15s;
}
.suggestion-item:hover {
  background: #f3f7fa;
}
.tags-collapsible {
  margin-top: 0.5rem;
  text-align: left;
}
.tags-toggle-btn {
  background: none;
  border: none;
  color: #0077ff;
  font-size: 1.05rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5em;
  margin-bottom: 0.2rem;
  font-weight: 500;
  transition: color 0.2s;
}
.tags-toggle-btn:hover {
  color: #0056b3;
}
.tags-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.35s cubic-bezier(.4,0,.2,1);
  margin-bottom: 0.5rem;
  padding-left: 2px;
}
.tags-content.expanded {
  /* Remove fixed max-height, let JS set it dynamically */
  padding-top: 0.5em;
}
.tag-pill {
  display: inline-block;
  background: linear-gradient(90deg,#e3f0ff 0,#f7faff 100%);
  color: #0077ff;
  border-radius: 18px;
  padding: 6px 16px;
  font-size: 0.98rem;
  margin: 0 7px 7px 0;
  cursor: pointer;
  border: 1px solid #d0e6ff;
  transition: background 0.18s, color 0.18s;
  font-weight: 500;
}
.tag-pill:hover {
  background: #0077ff;
  color: #fff;
}
.projects-list {
  margin-top: 2.5rem;
}
@media (max-width: 600px) {
  .projects-header h1 { font-size: 2rem; }
  .search-section { max-width: 98vw; }
  .tag-pill { font-size: 0.93rem; padding: 5px 12px; }
}
</style>