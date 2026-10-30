---
layout: page
title: About
permalink: /about/
weight: 1
---

# About

I'm **{{ site.author.name }}**, a researcher at **LG Energy Solution** working on diagnostic algorithms for EV battery fleets. My research interest is forecasting and decision-making under uncertainty in real-world industrial systems: how to forecast the state of complex systems, how far to trust those forecasts, and how to turn them into decisions when failure labels are scarce and arrive late.

I received my B.S. in Data Science and Systems Management Engineering and my M.S. in Industrial Engineering from Sungkyunkwan University. My thesis developed SHIFT, a framework that detects concept drift in deployed manufacturing models and updates their features and training data ([IEEE Access, 2026](https://doi.org/10.1109/ACCESS.2026.3658719); Korean patent). At **Boeing AI (BKETC)**, I built an early-warning system that forecasts quality risks in aircraft manufacturing and traces their root causes with causal discovery.

**Research Interests**
- Uncertainty-aware time-series forecasting
- Learning with scarce and delayed labels
- Decision-making under uncertainty
- Application domains: manufacturing, aerospace, and battery systems (prognostics and health management)


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