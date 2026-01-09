---
layout: page
title: Home
permalink: /
---

# SeongHyun Seo
A short one-liner about what you do.

[GitHub](https://github.com/seonghyunseo-kr){: .btn .btn-primary }
[LinkedIn](https://linkedin.com/in/seonghyun-seo-ms){: .btn .btn-outline-primary }

---

## Projects

<div class="projects-grid">
{% assign featured = site.projects | where: "featured", true | sort: "order" %}
{% for p in featured limit: 6 %}
  <a class="project-card" href="{{ p.url | relative_url }}">
    {% if p.image %}
      <img src="{{ p.image | relative_url }}" alt="{{ p.title }}">
    {% endif %}
    <div class="project-body">
      <h3>{{ p.title }}</h3>

      {% if p.description %}
        <p>{{ p.description }}</p>
      {% else %}
        <p>{{ p.excerpt | strip_html | truncate: 120 }}</p>
      {% endif %}

    </div>
  </a>
{% endfor %}
</div>