---
layout: post
title: "SHIFT: Self-Healing Model Maintenance under Concept Drift"
category: "Research — Technometrics Lab / POSCO DX"
track: "Research"
topic: "Concept Drift + Feature/Data Store Updates + Adaptive Retraining"
description: "Developed SHIFT, a framework that detects concept drift in deployed manufacturing models and updates their features and training data; began as a POSCO DX PoC that raised accuracy from 15 to 85 (IEEE Access, 2026; KR patent)."
period: "Summer 2023"
year: "2023"
style: border
color: warning
comments: false
toc: true
tools: [Concept Drift Detection, MDLP, mRMR, Adaptive Retraining, Python]
image:
external_url:
featured: true
summary_en: "Developed SHIFT, a framework that detects concept drift in deployed manufacturing models and updates their features and training data. It began as a POSCO DX PoC on steel virtual metrology that raised accuracy from 15 to 85 and won approval for production use, and became the M.S. thesis, an IEEE Access paper (2026), and a Korean patent."
summary_kr: "배포된 제조 모델의 컨셉 드리프트를 감지하고 피처와 학습 데이터를 업데이트하는 프레임워크 SHIFT를 개발했습니다. 철강 가상 계측 POSCO DX PoC에서 정확도를 15에서 85로 높여 실제 적용 승인을 받았고, 석사 학위논문·IEEE Access 논문(2026)·국내 특허로 이어졌습니다."
title_kr: "SHIFT: 컨셉 드리프트 하 자가 치유형 모델 유지보수"
---

#### Problem
- A virtual metrology (VM) model deployed in a Korean steel sintering process had no post-deployment update policy, and its predictive accuracy degraded as process conditions shifted (concept drift).
- Conventional retraining relies on fixed feature sets and accumulated data, so it cannot tell *when* and *how* the model should be updated.

#### My Role
- Led the POSCO DX Proof-of-Concept end-to-end, from research design to the executive presentation.
- Developed SHIFT as my M.S. thesis (Technometrics Lab, SKKU); first author of the IEEE Access paper and co-inventor of the Korean patent.

#### Approach
- Classified real vs. virtual drift using long/short-window learners and a queue-based decision rule.
- Updated the **features** (MDLP + mRMR) and the **training data** (buffer period, weighting), i.e., both the feature store and the data store.

#### Outcome
- PoC: raised accuracy from **15 to 85** (baseline 60–70) and won approval for production use.
- Paper: recovered CTQ from 15% to 93% and outperformed 11 existing concept drift methods.
- Publication: Seo, S., & Lim, D.-J. (2026). SHIFT: Self-Healing Intelligence in Feature store and data store Transitions. *IEEE Access*, 14, 16483–16502. [DOI: 10.1109/ACCESS.2026.3658719](https://doi.org/10.1109/ACCESS.2026.3658719)
- Patent: KR Patent No. 10-2941200.
