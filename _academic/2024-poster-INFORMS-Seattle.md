---
layout: post
type: poster
year: 2024
title: "Steeling Against Time: A Case Study of the Korean Steel Industry"
description: "A case study examining how the Korean steel industry adapts its processes and models to shifting conditions over time."
event: "2024 INFORMS Annual Meeting"
location: "Seattle, WA"
poster_url: "/assets/refs/2024_INFORMS_Poster.pdf"
slides_url:
style: border
color: info
comments: false
toc: true
---

> **2024 INFORMS Annual Meeting** (Seattle, WA)  
> **Session**: Poster Session  
> **Authors**: Jeong-Uk Seo, SeongHyun Seo, Dong-Joon Lim (SKKU Technometrics Lab)  
> **Poster**: [Download PDF](/assets/refs/2024_INFORMS_Poster.pdf)

<br>

#### Overview
This poster presents a focused case study on model degradation and adaptive retraining in Korean steel manufacturing. While the companion talk introduces the full Adaptive Model Update Framework, this poster zooms in on the empirical evidence — showing *why* static models fail in continuous industrial processes and *how* non-periodic, buffer-based retraining restores and maintains performance.

#### Key Takeaways
- **Concept Drift in steel manufacturing**: data patterns shift unpredictably over time; a model trained in 2021 degraded significantly by mid-2023 with no effective update mechanism in place.
- **Double-window CD detection**: three drift patterns are classified using long-term (LW) and short-term (SW) memory models — each triggering a different retraining strategy (expand window / shift window / re-select features).
- **Buffer Period + Differential Weighting**: after drift detection, a buffer collects additional data; weighting functions (Uniform, Stepwise, Linear, Logarithmic) control sensitivity during the update — achieving stable performance gains across all configurations.
- **~74% improvement in CTQ**: the proposed framework outperformed the original model across all evaluated periods, with MAPE dropping from 5.65 → 2.34 and CTQ rising from 53.06% → 92.47%.

<br>

### Abstract
Concept drift (CD) refers to unpredictable changes in the statistical properties of the target variable over time, leading to model performance degradation. This poster proposes an adaptive framework that facilitates CD detection (CDD) and CD adaptation (CDA) through a double-window detection method and a non-periodic model update strategy. During a buffer period following drift detection, various differential weighting functions are applied to structure the retraining data. An empirical case study on return fines prediction in Korean steel sintering demonstrates the necessity and effectiveness of autonomous retraining strategies.

<br>

#### Case Study — Sintering Process, Korean Steel Manufacturing

**Process context**  
Steel production follows sequential stages: Ironmaking → Steelmaking → Casting → Rolling. Within ironmaking, the sintering process converts iron ore into sinter. Return fines — a by-product of sintering — directly predict sinter quality, which cascades into final product quality.

**Data**  
- 50,832 rows restructured from raw plant data  
- Feature discretization: MDLP  
- Feature selection: mRMR  
- Target: return fines occurrence rate (30 input variables)

**Problem**  
CTQ (Critical-to-Quality) degraded from 65% (2021) → 51.86% (Jan–Jun 2023). No effective model update strategy existed to detect or respond to this drift.

<br>

#### Results

| Configuration | MAPE | CTQ (%) |
|---|---|---|
| Original model | 5.65 | 53.06 |
| Proposed (periodic, no buffer) | 3.91 | 72.15 |
| Proposed (non-periodic, no buffer, constant) | 2.35 | 92.39 |
| **Proposed (non-periodic, buffer + various weights)** | **2.34** | **92.47** |

Period-level breakdown:

| Period | Original (MAPE / CTQ) | Proposed (MAPE / CTQ) |
|---|---|---|
| Overall | 7.39 / 7.63 | 4.29 / 40.97 |
| Before Buffer | 6.70 / 0 | 4.88 / 30.76 |
| Buffer | 5.70 / 5.40 | 4.33 / 37.83 |
| After Buffer | 7.84 / 9.37 | 4.03 / 43.75 |

<br>

#### Contribution
- Co-author and presenter (SeongHyun Seo), with Jeong-Uk Seo and Prof. Dong-Joon Lim

#### Related Work
- Companion talk at same conference: [Automating ML Workflow Orchestration](/academic/2024-talk-informs-seattle)
- Extended framework published as: *SHIFT: Self-Healing Intelligence in Feature store and data store Transitions*, IEEE Access (2026)

#### Notes
- Poster available for download above
