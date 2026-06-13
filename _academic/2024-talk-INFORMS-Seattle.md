---
layout: post
type: talk
year: 2024
title: "Automating ML Workflow Orchestration: Strategies for Autonomous Post-Deployment Model Updates"
event: "2024 INFORMS Annual Meeting"
location: "Seattle, WA"
slides_url: "/assets/refs/2024_INFORMS_Presentation.pdf"
style: border
color: primary
comments: false
toc: true
---

> **2024 INFORMS Annual Meeting** (Seattle, WA)  
> **Session**: Oral Session — Recent Advances in Stochastic Optimization (Contributed)  
> **Slides**: [Download PDF](/assets/refs/2024_INFORMS_Presentation.pdf)

<br>

#### Overview
Modern manufacturing relies on continuous AI-driven automation, yet existing MLOps frameworks lack robust answers to a core question: *when and how* should a deployed model be retrained? This talk presents an **Adaptive Model Update Framework** that addresses concept drift through non-periodic, pattern-based retraining — integrating feature store and data store updates into a closed-loop MLOps workflow.

#### Key Takeaways
- **Beyond periodic retraining**: conventional approaches risk missing degradation points by retraining on a fixed schedule; the proposed framework detects drift dynamically using a double-window method and classifies it into 3 patterns.
- **Pattern-based CD detection**: a multi-learner queue system (LW/SW) monitors performance over time and triggers one of three retraining strategies — extend the training window, shift to a short window, or re-select optimal feature combinations.
- **Buffer Period + Differential Weighting**: after drift is detected, a buffer collects additional data before retraining; differential weighting (Constant, Amplified, Linear, Log) controls sensitivity to new distributions.
- **Industrial validation**: applied to a Korean steel sintering process (30 variables, return fines prediction) — CTQ improved from 53.06% to 92.47%, MAPE from 5.65 to 2.34.

<br>

### Abstract
This presentation focuses on autonomous model update strategies aimed at improving the performance and stability of machine learning models after deployment. Unlike traditional approaches that rely on periodic retraining or fixed performance thresholds, the proposed adaptive framework makes informed decisions about *when* and *how* to retrain — integrating concept drift detection, feature/data store refresh, and differential weighting into a unified MLOps workflow. An empirical case study from the Korean steel industry demonstrates both the necessity and effectiveness of autonomous post-deployment retraining strategies.

<br>

#### Proposed Method — Three Core Components

**1. Non-Periodic Retraining via Double-Window CD Detection**  
A queue management system monitors long-term (LW) and short-term (SW) memory models in parallel. Based on error comparisons and queue thresholds (τ, δ, maxq), drift is classified into three patterns:
- Pattern 1: Expand LW → maintain current model
- Pattern 2: Shift LW → SW → maintain current model  
- Pattern 3: Shift LW → SW → re-select optimal feature combinations

**2. Feature & Data Store Updates**  
mRMR-based feature selection is triggered on Pattern 3 detections, ensuring the model adapts to shifts in feature importance — not just distributional changes in the target.

**3. Buffer Period with Differential Weighting**  
Post-detection, a buffer period collects data before retraining. Four weighting schemes (Constant, Amplified, Linear, Logarithmic) control how much influence new-distribution data has on the updated model, balancing adaptation speed against stability.

<br>

#### Case Study — Korean Steel Manufacturing
- **Process**: sintering (ironmaking stage) — return fines ratio predicts sinter and final product quality
- **Data**: 50,832 rows, 30 variables; MDLP discretization + mRMR feature selection
- **Problem**: CTQ degraded from 65% (2021) → 51.86% (Jan–Jun 2023) with no effective update strategy

| Configuration | MAPE | CTQ (%) |
|---|---|---|
| Original model | 5.65 | 53.06 |
| Proposed (no buffer, constant weight) | 2.35 | 92.39 |
| **Proposed (buffer + double weight)** | **2.34** | **92.47** |

The proposed framework achieved ~74% improvement in CTQ performance compared to the original, with stable predictions maintained even during abnormal periods (Feb and Mar 2023).

<br>

#### Contribution
- Presenter (SeongHyun Seo), co-authored with Prof. Dong-Joon Lim (SKKU)

#### Related Work
- This talk is an early presentation of the framework later published as: *SHIFT: Self-Healing Intelligence in Feature store and data store Transitions*, IEEE Access (2026)
- See also: [2024 INFORMS Poster — Steeling Against Time](/academic/2024-poster-informs-seatlle)

#### Notes
- Slides available for download above
- The framework forms the core of the M.S. thesis and KR Patent No. 10-2941200
