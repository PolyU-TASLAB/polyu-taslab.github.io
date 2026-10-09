---
---

<div class="home-hero">
  <div class="hero-main">
  <div class="hero-copy">
    <p class="eyebrow">PolyU · Department of Aeronautical and Aviation Engineering</p>
    <h1>Trustworthy AI and Autonomous Systems Lab</h1>
    <p class="hero-tagline">Trustworthy autonomy for dense cities: from satellites to embodied robots.</p>
    <p class="hero-intro">
      We build the algorithmic foundations of <b class="blue">trustworthy embodied AI</b> — perception, navigation and control
      that stay safe and reliable in GNSS-challenged urban canyons — and deploy them on <b class="blue">drones</b>,
      <b class="blue">intelligent vehicles</b> and <b class="blue">legged/humanoid robots</b> together with our industry partners.
    </p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{{ 'research/' | relative_url }}">Our Research</a>
      <a class="btn btn-ghost" href="{{ 'publications/' | relative_url }}">Publications</a>
      <a class="btn btn-ghost" href="{{ 'openings/' | relative_url }}">Join Us</a>
    </div>
  </div>

  <div class="hero-mosaic" aria-label="Our robots">
    <a class="hero-tile" href="{{ 'research/drones.html' | relative_url }}">
      <img src="{{ 'images/home/hero-drone.jpg' | relative_url }}" alt="TAS Lab drone in flight" fetchpriority="high">
      <span>Drones</span>
    </a>
    <a class="hero-tile" href="{{ 'research/humanoid.html' | relative_url }}">
      <img src="{{ 'images/home/hero-legged.jpg' | relative_url }}" alt="TAS Lab quadruped robot on the PolyU campus">
      <span>Legged robots</span>
    </a>
    <a class="hero-tile" href="{{ 'research/vehicles.html' | relative_url }}">
      <img src="{{ 'images/home/hero-wuxi-car.jpg' | relative_url }}" alt="Autonomous passenger car at the PolyU-Wuxi Research Institute">
      <span>Autonomous cars</span>
    </a>
    <a class="hero-tile" href="{{ 'research/vehicles.html' | relative_url }}">
      <img src="{{ 'images/home/hero-vehicle.jpg' | relative_url }}" alt="Autonomous logistics vehicle on the PolyU campus">
      <span>Logistics vehicles</span>
    </a>
  </div>
  </div>

  <ul class="hero-stats" aria-label="Lab highlights">
    {% for item in site.data.highlights %}
    <li>
      <span class="hero-stat-value">{% if item.value == "github-stars" %}{% include oss-total.html %}{% else %}{{ item.value }}{% endif %}</span>
      <span class="hero-stat-label">{{ item.label }}</span>
    </li>
    {% endfor %}
  </ul>
</div>

{% include section.html %}

## Research Directions

<p class="section-lead">
  Algorithm foundations for embodied AI with end-to-end learning and safety certification — spanning large AI models,
  vision-language-action models, AI-enabled multi-sensor fusion and software-hardware co-design.
</p>

<div class="card-grid research-grid">
  <a class="tile tile-accent" href="{{ 'research/gnss.html' | relative_url }}">
    <span class="tile-label">🛰️ 3D LiDAR Aided GNSS Positioning</span>
    <p class="tile-desc">AI-driven GNSS positioning (RTK, PPP, PPP-RTK), 3D LiDAR aided NLOS/multipath mitigation and multi-sensor fusion for robust urban navigation.</p>
  </a>
  <a class="tile tile-accent" href="{{ 'research/fusion.html' | relative_url }}">
    <span class="tile-label">🔒 Safety-Certifiable Multi-Sensor Fusion</span>
    <p class="tile-desc">Safety-certifiable AI for navigation, LiDAR/camera/IMU/GNSS fusion, integrity monitoring and navigation-control joint optimization.</p>
  </a>
  <a class="tile tile-accent" href="{{ 'research/vehicles.html' | relative_url }}">
    <span class="tile-label">🚗 End-to-End Autonomous Vehicles</span>
    <p class="tile-desc">End-to-end learning for self-driving, safety certification for logistics applications and V2X-assisted connected autonomous driving.</p>
  </a>
  <a class="tile tile-accent" href="{{ 'research/humanoid.html' | relative_url }}">
    <span class="tile-label">🤖 Embodied AI for Legged/Humanoid Robots</span>
    <p class="tile-desc">Large AI models and vision-language-action models for perception and control, bio-inspired embodied intelligence and multimodal learning.</p>
  </a>
  <a class="tile tile-accent" href="{{ 'research/drones.html' | relative_url }}">
    <span class="tile-label">🚁 Embodied Drones for City Maintenance</span>
    <p class="tile-desc">Intelligent drones and UAV swarms, aerial manipulation for urban infrastructure and efficient software-hardware co-design.</p>
  </a>
  <a class="tile tile-accent" href="{{ 'research/education.html' | relative_url }}">
    <span class="tile-label">🎓 Embodied AI for Robotics Education</span>
    <p class="tile-desc">AI-powered robotics education platforms, project-based learning with drones and ground robots, and GitHub-based collaborative pedagogy.</p>
  </a>
</div>

{% include section.html %}

<div class="section-head">
  <h2>Latest Updates</h2>
  <a class="link-arrow" href="{{ 'news/' | relative_url }}">All news</a>
</div>

{% assign recent_news = site.events | sort: "date" | reverse %}
<ol class="timeline">
  {% for item in recent_news limit: 5 %}
  <li>
    <span class="timeline-marker" aria-hidden="true"></span>
    <a class="timeline-body" href="{{ item.url | relative_url }}">
      <span>
        <time datetime="{{ item.date | date_to_xmlschema }}">{{ item.date | date: "%b %-d, %Y" }}</time>
        <span class="timeline-title">{{ item.title }}</span>
      </span>
      {% if item.image %}
      <img class="timeline-thumb" src="{{ item.image | relative_url }}" alt="" loading="lazy">
      {% endif %}
    </a>
  </li>
  {% endfor %}
</ol>

{% include section.html %}

## Recognition

<p class="section-lead">Selected honours of the lab and its director.</p>

<div class="card-grid">
  {% for honor in site.data.honors %}
  <div class="tile">
    <span class="tile-year">{{ honor.year }}</span>
    <h3 class="tile-title">{{ honor.title }}</h3>
    <p class="tile-desc">{{ honor.org }}</p>
  </div>
  {% endfor %}
</div>

{% include section.html %}

## Videos

<div class="video-grid">
  <iframe loading="lazy" title="TAS Lab video 1" src="//player.bilibili.com/player.html?isOutside=true&aid=114244838299184&bvid=BV1ktZcYdEWD&cid=25777740164&p=1&autoplay=0" scrolling="no" frameborder="no" allowfullscreen="true"></iframe>
  <iframe loading="lazy" title="TAS Lab video 2" src="//player.bilibili.com/player.html?isOutside=true&aid=115156243711653&bvid=BV1fiaqzNEEm&cid=32199149727&p=1&autoplay=0" scrolling="no" frameborder="no" allowfullscreen="true"></iframe>
  <iframe loading="lazy" title="TAS Lab video 3" src="//player.bilibili.com/player.html?isOutside=true&aid=115920244638163&bvid=BV1GPkvBdEw9&cid=35479224564&p=1&autoplay=0" scrolling="no" frameborder="no" allowfullscreen="true"></iframe>
  <iframe loading="lazy" title="TAS Lab video 4" src="//player.bilibili.com/player.html?isOutside=true&aid=114776826971256&bvid=BV1UsgDzeE5J&cid=30968254232&p=1&autoplay=0" scrolling="no" frameborder="no" allowfullscreen="true"></iframe>
  <iframe loading="lazy" title="TAS Lab video 5" src="//player.bilibili.com/player.html?isOutside=true&aid=116197320362204&bvid=BV1rbPDzgEsT&cid=36567648583&p=1&autoplay=0" scrolling="no" frameborder="no" allowfullscreen="true"></iframe>
</div>

{% include section.html %}

<div class="section-head">
  <h2>Gallery</h2>
  <a class="link-arrow" href="{{ 'team/' | relative_url }}#gallery">All photos</a>
</div>

<p class="section-lead">Life at TAS Lab: our team, competitions, field tests and partner visits.</p>

{% include gallery.html limit=5 %}

{% include section.html %}

<div class="section-head">
  <h2>Funders &amp; Partners</h2>
  <a class="link-arrow" href="{{ 'team/' | relative_url }}#advisory-board">Our advisory board</a>
</div>

<p class="section-lead">
  With gratitude to the government bodies, industry partners and university units whose support turns our research
  into impact for Hong Kong and beyond.
</p>

{% include partners.html %}

{% include section.html %}

## Explore

<div class="card-grid">
  <a class="tile" href="{{ 'research/' | relative_url }}">
    <span class="tile-label">Research</span>
    <p class="tile-desc">Six directions from GNSS positioning to humanoid robots, with projects and demos.</p>
  </a>
  <a class="tile" href="{{ 'publications/' | relative_url }}">
    <span class="tile-label">Publications</span>
    <p class="tile-desc">Journal and conference papers, searchable by year, topic and author.</p>
  </a>
  <a class="tile" href="{{ 'opensource/' | relative_url }}">
    <span class="tile-label">Dataset &amp; Code</span>
    <p class="tile-desc">UrbanNav, GraphGNSSLib, pyrtklib and more — {% include oss-total.html %} GitHub stars.</p>
  </a>
  <a class="tile" href="{{ 'team/' | relative_url }}">
    <span class="tile-label">Team</span>
    <p class="tile-desc">PhD and MPhil students, postdocs, research assistants and alumni.</p>
  </a>
  <a class="tile" href="{{ 'news/' | relative_url }}">
    <span class="tile-label">News</span>
    <p class="tile-desc">Awards, visits, competitions, talks and lab events.</p>
  </a>
  <a class="tile" href="{{ 'openings/' | relative_url }}">
    <span class="tile-label">Openings</span>
    <p class="tile-desc">PhD, MPhil, postdoc and RA positions — we are recruiting.</p>
  </a>
</div>

{% include visitor-map.html %}
