---
icon: fas fa-briefcase
order: 2
title: Projects
---

<div class="projects-grid">
{% assign items = site.projects | sort: "order" %}
{% for p in items %}
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

      {% if p.tags and p.tags.size > 0 %}
      <div class="project-tags">
        {% for t in p.tags limit: 5 %}
          <span>{{ t }}</span>
        {% endfor %}
      </div>
      {% endif %}
    </div>
  </a>
{% endfor %}
</div>