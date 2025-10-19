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


<button id="toggle-tags" style="margin-bottom:10px;">Show/Hide Tags</button>
<div id="tags-section">
  {% include tags.html tags=site.tags %}
</div>

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