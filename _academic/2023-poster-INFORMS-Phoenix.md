---
layout: post
type: poster
year: 2023
title: "Is All Well with Your Models?: Strategies to Deal with Concept Drifts"
description: "Reviewed strategies for detecting and responding to concept drift in deployed machine learning models."
event: "2023 INFORMS Annual Meeting"
location: "Phoenix, AZ"
poster_url: "/assets/refs/2023_INFORMS_Poster.pdf"
slides_url:
style: border
color: warning
comments: false
toc: true
title_kr: "당신의 모델은 안전한가요?: 컨셉 드리프트 대응 전략"
summary_kr: "스판덱스 섬유 생산 공정을 사례로, 컨셉 드리프트를 감지하고 모델을 적응적으로 업데이트하는 전략(피처 선택, 기간 구분, 차등 가중치)을 제안하여 2023 INFORMS 연례총회에서 포스터로 발표했습니다."
---

> **2023 INFORMS Annual Meeting** (Phoenix, AZ)  
> **Session**: Poster Session  
> **Authors**: Seong-Hyun Seo, Ui-Jong Hwang, Dong-Joon Lim (SKKU Technometrics Lab)  
> **Poster**: [Download PDF](/assets/refs/2023_INFORMS_Poster.pdf)  
> **Acknowledgment**: Supported by the National Research Foundation of Korea (NRF) under Grant RS-2023-00239046, and by Hyosung ITX.

<br>

#### Overview
This poster marks the earliest public presentation of what would become the SHIFT framework. Motivated by the limitations of standard Alternating Learner (AL) frameworks for concept drift detection, we introduce model update strategies built around two new concepts — **period** and **weight** — and apply them to a real-world Korean spandex fiber production case study.

#### Key Takeaways
- **Concept drift in continuous manufacturing**: in spandex fiber production, multi-phase chemical reactions make real-time optimization difficult, and data distributions shift unpredictably over time — causing deployed models to degrade.
- **AL framework limitations**: the conventional Alternating Learner approach detects drift by comparing long-window (LW) and short-window (SW) model errors, but cannot modify the model itself or adjust retraining data structure in response.
- **Advanced AL + model update strategy**: the proposed extension adds feature selection (FS) and structured period definitions — Reference, Update, and Buffer — plus differential weighting of buffer-period data, enabling more precise and stable adaptation.
- **74% CTQ improvement**: on spandex dope polymer viscosity prediction, the auto-modeling strategy (AL + Reference Model + Process Variable + FS Period + Q Limit) achieved MAPE = 1.17%, far outperforming periodic retraining (6.48%) and baseline AL + adaptation (4.88%).

<br>

### Abstract
This poster presents concept drift detection methods that address the situation where model performance deteriorates due to concept drift, preventing effective auto-modeling. We adopt feature selection and various model update strategies into the conventional AL framework to detect concept drift more effectively and efficiently. These advanced strategies successfully detect concept drift in real-world scenarios, ensuring consistent performance and reliable predictions in dynamic environments. Results are validated on Korean spandex fiber production data.

<br>

#### Background — Continuous Process in Spandex Fiber Production

Spandex fiber manufacturing involves three sequential reaction phases:
1. Pre-polymer production
2. Polymer reactions
3. Fiber production

Each phase requires chemical quality tests to obtain quality indicators. Real-time process optimization is difficult due to irregular flow times of intermediate products and the need for continuous monitoring.

**Prediction target**: Dope Polymer Viscosity  
**Data**: 691,200 datapoints (Jul 2020 – Dec 2021), 30 features (24 process + 6 derived), Lasso Regression base model  
**Validation**: Rolling origin with 15-day window size and 5-day test period

<br>

#### Proposed Method

**Method 1 — Advanced AL Framework**

The conventional AL framework trains two models — long window (LW) and short window (SW) — and compares errors to detect CD. When CD is detected, LW is replaced with SW + N. However, this approach cannot modify the model itself, making it insufficient when drift is too frequent or hyperparameter-sensitive.

The **Advanced AL** adds:
- **Feature Selection (FS)**: dynamically reconfigures predictor variables upon CD detection, instead of relying on a fixed input set
- Addresses cases where the conventional AL adjusts learning intervals but fails to adapt the model structure

**Method 2 — Model Update Strategy**

Three period types define the update structure:

| Period Type | Description |
|---|---|
| Reference Period | A past period of similar duration used for diagnosing pattern changes |
| Update Period | Minimum duration required to accumulate new data for updates |
| Buffer Period | Additional data collected after detecting pattern changes, before updating |

**Differential Weighting**: assigns varying importance to buffer-period data during model updates, adjusting sensitivity to new distributions.

<br>

#### Results — Spandex Industry

**Optimal configuration**: AL + Reference Model + Process Variable + FS Period + Q Limit  
→ MAPE = **1.17%** (overall period)

| Strategy | Overall MAPE | Rapid Change Period MAPE |
|---|---|---|
| Periodic model update | 6.48% | 2.94% |
| AL + Adaptation | 4.88% | 2.45% |
| **Auto-modeling (proposed)** | **4.69%** | **1.73%** |

**Optimal hyperparameters**:
- Reference Model: 29-day regular model
- Process Variable: Included
- FS Period: 4 days
- Q Length: 11 days
- Buffer Period: 2 days
- Weight: Linear

Key behaviors observed:
- **Downtrend detection**: model updates performed sensitively to the latest data during performance drops
- **Rebound detection**: updates triggered after vulnerable periods to recover stable performance

<br>

#### Contribution
- Co-author and presenter (Seong-Hyun Seo), with Ui-Jong Hwang and Prof. Dong-Joon Lim

#### Related Work
- This work is the conceptual precursor to the full SHIFT framework
- Extended and formalized as: *SHIFT: Self-Healing Intelligence in Feature Store and Data Store Transitions*, IEEE Access (2026)
- See also: [2024 INFORMS Poster — Steeling Against Time](/academic/2024-poster-informs-seatlle)

#### Notes
- Poster available for download above
