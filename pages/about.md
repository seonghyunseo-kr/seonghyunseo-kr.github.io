---
layout: page
title: About
permalink: /about/
weight: 1
---

# About

Hi, I’m **{{ site.author.name }}**!

Through multiple projects in the manufacturing sector, I’ve become deeply motivated by solving real-world problems with field-generated data. This has been the main driver of my professional growth.

My current research interests focus on **reliable AI/ML for real-world operations**, including time-series forecasting, multimodal time series, control & planning, and post-deployment model maintenance (e.g., monitoring and retraining).

I was an **AI/ML Researcher Intern at Boeing AI (BKETC, Seoul, South Korea)** where I focused on building sustainable and autonomous ML systems for industrial applications.

Currently, I am seeking opportunities to contribute to the R&D journey within the industry.


Check out my latest [CV (PDF)](/assets/pdf/cv.pdf) ! 


<h2 data-en="{{ site.data.i18n.about.education.en | escape }}" data-kr="{{ site.data.i18n.about.education.kr | escape }}">{{ site.data.i18n.about.education.en }}</h2>

<div class="row">
  {% include education.html %}
</div>

<h2 data-en="{{ site.data.i18n.about.experience.en | escape }}" data-kr="{{ site.data.i18n.about.experience.kr | escape }}">{{ site.data.i18n.about.experience.en }}</h2>

<div class="row">
  {% include about/timeline.html %}
</div>

<h2 data-en="{{ site.data.i18n.about.publications_patents.en | escape }}" data-kr="{{ site.data.i18n.about.publications_patents.kr | escape }}">{{ site.data.i18n.about.publications_patents.en }}</h2>

<div class="row">
  {% include about/publications-patent.html %}
</div>

<div class="d-flex justify-content-end">
  <a class="btn btn-link p-0" href="{{ site.baseurl }}/academic/" data-en="{{ site.data.i18n.about.for_more_academic.en | escape }}" data-kr="{{ site.data.i18n.about.for_more_academic.kr | escape }}">{{ site.data.i18n.about.for_more_academic.en }}</a>
</div>

<h2 data-en="{{ site.data.i18n.about.honors_awards.en | escape }}" data-kr="{{ site.data.i18n.about.honors_awards.kr | escape }}">{{ site.data.i18n.about.honors_awards.en }}</h2>

<div class="row">
  {% include about/honors-awards.html %}
</div>

<div class="row">
  {% include about/skills.html title="Programming Skills" title_kr=site.data.i18n.about.programming_skills.kr source=site.data.programming-skills %}
  {% include about/languages-certifications.html %}
</div>