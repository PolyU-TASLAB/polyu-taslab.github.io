---
title: Projects
nav:
  order: 3
  tooltip: Research projects and demos
---

# {% include icon.html icon="fa-solid fa-diagram-project" %}Projects

Our ongoing and completed research projects span <b class="blue">autonomous driving</b>, <b class="blue">drone systems</b>, <b class="blue">GNSS positioning</b>, <b class="blue">multi-sensor fusion</b>, and <b class="blue">embodied AI</b> for robotics.
{:.center}

{% include section.html %}

## Videos

<style>
.video-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin: 16px 0 24px 0;
}
.video-grid iframe {
  width: 100%;
  aspect-ratio: 16/9;
  height: auto;
  border-radius: 8px;
  border: none;
}
@media (max-width: 640px) {
  .video-grid { grid-template-columns: 1fr; }
}
</style>

<div class="video-grid">
  <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114244838299184&bvid=BV1ktZcYdEWD&cid=25777740164&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
  <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115156243711653&bvid=BV1fiaqzNEEm&cid=32199149727&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
  <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115920244638163&bvid=BV1GPkvBdEw9&cid=35479224564&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
  <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114776826971256&bvid=BV1UsgDzeE5J&cid=30968254232&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
</div>

{% include section.html %}

## Research Projects

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}
