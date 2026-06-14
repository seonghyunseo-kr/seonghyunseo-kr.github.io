---
layout: post
type: journal
year: 2026
title: "SHIFT: Self-Healing Intelligence in Feature Store and Data Store Transitions"
description: "Introduces SHIFT, a self-healing framework for managing feature store and data store transitions during automated model retraining."
venue: "IEEE Access"
doi: "10.1109/ACCESS.2026.3658719"
paper_url: "/assets/refs/2026-journal-ieee-access.pdf"
style: border
color: danger
comments: false
toc: true
---

> **IEEE Access**, Volume 14, 2026 (Open Access)  
> **DOI**: [10.1109/ACCESS.2026.3658719](https://doi.org/10.1109/ACCESS.2026.3658719)  
> **Authors**: Seong-Hyun Seo, Dong-Joon Lim (Sungkyunkwan University)  
> **Received**: Dec 30, 2025 · **Accepted**: Jan 24, 2026 · **Published**: Jan 28, 2026  
> **Funding**: Ministry of SMEs and Startups of Korea (MSS) · Hyundai Motor Chung Mong-Koo Foundation  
> **Paper**: [Download PDF](/assets/refs/2026-journal-ieee-access.pdf)

<br>

#### Overview
SHIFT (Self-Healing Intelligence in Feature Store and Data Store Transitions) is an AI model management framework designed to sustain the prediction performance of deployed machine learning systems under concept drift. Unlike conventional retraining approaches that rely on fixed feature sets and static data selection, SHIFT autonomously updates both the **feature store** (what variables the model uses) and the **data store** (what data it trains on), enabling continuous, self-correcting model maintenance without manual intervention or model replacement.

The framework was validated on a real-world **virtual metrology (VM) system** in a Korean steel sintering process, recovering predictive accuracy from a degraded state (CTQ 15%) to well above the original deployment target (CTQ 93%), while outperforming 11 existing concept drift detection and adaptation methods.

#### Key Contributions
- **Dual-update strategy**: jointly orchestrates feature store reconfiguration and drift-aware data store construction — the first framework to integrate both within a single automated workflow.
- **Pattern-based CD detection**: classifies drift into three types (stationary, real drift, virtual drift) using a queue-based multi-learner system, enabling tailored retraining responses rather than uniform periodic updates.
- **Buffer Period + Differential Weighting**: collects post-drift data before retraining; applies weighting functions (constant, linear, logarithmic, double) to emphasize recent distributions and distinguish genuine shifts from transient noise.
- **Base-model agnostic**: SHIFT is an operational intelligence layer — it specifies *when* and *how* to retrain, independent of whether the underlying model is Lasso, XGBoost, or a Transformer.
- **Statistically validated**: Wilcoxon signed-rank tests confirm SHIFT significantly outperforms all baseline methods (DDM, ADWIN, PL, AL, STEPD, MDDM, FHDDM, etc.) across the full evaluation period.

<br>

### Abstract
This study presents an AI model management framework for maintaining the prediction performance of virtual metrology (VM) systems in steel manufacturing processes. The proposed method addresses concept drift (CD) — a major threat to long-term model reliability — by employing a dual-update strategy that autonomously updates both the feature store and the data store. Unlike conventional model maintenance approaches based on static inputs and accumulated data, the framework continuously reassesses feature relevance and adapts retraining datasets to reflect evolving process conditions. In a real-world steel sintering process, the method achieved significant recovery in predictive accuracy — from 65% post-deployment to over 93% after updates. The findings contribute to the broader field of AI-enabled asset management by offering a scalable solution for condition monitoring, retraining scheduling, and long-term performance assurance.

**Index Terms**: Operational intelligence, virtual metrology, autonomous model update, concept drift, data store, feature store.

<br>

#### Methodology — SHIFT Algorithm

**CD Detection**  
SHIFT maintains two parallel learners:
- **Long-window model (L)**: learns stable long-term concepts
- **Short-window model (S)**: focuses on recent, temporary patterns

A **queue management system (Q)** accumulates batch-level drift signals (0, 1, or 2) over time, and the final drift decision is made only after sufficient evidence accumulates. This prevents overreaction to transient fluctuations.

Three drift patterns are classified:

| Pattern | Condition | Response |
|---|---|---|
| Stationary (0) | L meets threshold τ | Update L with accumulated data; update S with recent window |
| Real drift (1) | L below τ but better than S; Snew (with FS) outperforms L | Feature store update: re-select optimal predictors |
| Virtual drift (2) | L below τ; S outperforms L | Data store update: retrain on recent window only |

**CD Adaptation**  
Once drift is confirmed:
- **Buffer Period**: collects post-drift data before retraining begins — balancing rapid adaptation vs. robustness to noise
- **Differential Weighting**: assigns greater importance to buffer-period data using linear, logarithmic, or double-weight schemes
- **Feature Selection**: MDLP discretization + mRMR relevance-redundancy optimization to identify the current best predictor set

<br>

#### Case Study — Steel Sintering Process

**Setting**  
A VM model (Lasso regression, 30 variables) was deployed in January 2023 to predict sinter production rate (return fines ratio) in a Korean steel plant. The model, trained on 18 months of data (Jun 2021 – Dec 2022), had no post-deployment update policy.

**Data**: ~1.06M raw instances → 50,832 rows after 10-minute aggregation, 127 features  
**Target**: Sinter production rate (return fines ratio)  
**Metrics**: MAPE (lower = better), CTQ — proportion of predictions within one SD of training data (higher = better)

**Performance Degradation (without SHIFT)**

| Period | MAPE | CTQ (%) |
|---|---|---|
| At development | 4.56 | 65.0 |
| Overall (Jan–Jun 2023) | 9.87 | 15.11 |
| Abnormal period 1 (Jan 31 – Feb 4) | 12.02 | 12.85 |
| Abnormal period 2 (Feb 21 – Feb 27) | 11.44 | 2.07 |
| Abnormal period 3 (Apr 18 – Apr 22) | 9.31 | 12.24 |
| Abnormal period 4 (May 7 – May 10) | 10.87 | 7.71 |

**Performance with SHIFT**

| Period | MAPE | CTQ (%) |
|---|---|---|
| **Overall (Jan–Jun 2023)** | **2.14** | **93.12** |
| Abnormal period 1 | 2.41 | 90.42 |
| Abnormal period 2 | 1.83 | 94.08 |
| Abnormal period 3 | 1.94 | 94.92 |
| Abnormal period 4 | 2.06 | 91.19 |

In total, **621 data store updates** and **395 feature store updates** were performed autonomously. Nine new predictor variables not present in the original model were discovered and incorporated during retraining.

**Hyperparameters (final)**:
- Short window (S): 4 hours
- Batch interval: 2 hours
- τ (MAPE threshold for L): 2
- n (min Q length): 2, δ: 0.3, qmax: 7
- Buffer: 6 hours, Weight: double

<br>

#### Comparison with Existing Methods

SHIFT achieved the **lowest average rank** (5.41) across all evaluation periods, significantly outperforming DDM (6.09), ADWIN (6.25), MDDM (6.30), FHDDM (6.46), STEPD (5.97), and AL (5.94) via Wilcoxon signed-rank test (Bonferroni-adjusted threshold ~0.0045). Only PL (5.63) was not statistically distinguishable — but PL showed notably worse absolute MAPE in failure cases.

**Ablation study**:
- Full SHIFT (both updates): MAPE 2.14 / CTQ 93.12
- Without feature store update: MAPE 2.30 / CTQ 92.71
- Without data store update: MAPE 2.63 / CTQ 88.77

Both components are necessary — neither alone suffices under severe or sudden drift.

<br>

#### Contribution
- First author (Seong-Hyun Seo), co-authored with Prof. Dong-Joon Lim (SKKU)
- This paper is the culmination of the M.S. thesis and the full formalization of research presented at INFORMS 2023 and 2024

#### Related Work
- Precursor poster: [2023 INFORMS — Is All Well with Your Models?](/academic/2023-poster-informs-pheonix)
- Early framework presentation: [2024 INFORMS Talk — Automating ML Workflow Orchestration](/academic/2024-talk-informs-seattle)
- [2024 INFORMS Poster — Steeling Against Time](/academic/2024-poster-informs-seatlle)
- See also: KR Patent No. 10-2941200 (System and Method for AI Model Retraining through Feature Store and Data Store Updates)

#### Notes
- Paper available for download above (Open Access, CC BY 4.0)
