---
title: Projects
nav:
  order: 3
  tooltip: 
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

<!-- Add content here -->

<!-- {% include tags.html tags="publication, resource, website" %} -->

{% include section.html %}

{% include search-box.html %}



<button id="toggle-tags" class="toggle-tags-btn">Show/Hide Tags</button>
<div id="tags-section">
  {% include tags.html tags=site.tags %}
</div>
<style>
.toggle-tags-btn {
  margin-bottom: 14px;
  padding: 8px 20px;
  border-radius: 8px;
  border: 1.5px solid #bdbdbd;
  background: #f5f5f5;
  color: #1a73e8;
  font-size: 1.08rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s, border-color 0.2s;
}
.toggle-tags-btn:hover {
  background: var(--light-gray, #eaeaea);
  border-color: #1a73e8;
  color: #1a73e8;
}
</style>
<script>
document.getElementById('toggle-tags').onclick = function() {
  var tags = document.getElementById('tags-section');
  if (tags.style.display === 'none') {
    tags.style.display = 'block';
  } else {
    tags.style.display = 'none';
  }
};
</script>

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}