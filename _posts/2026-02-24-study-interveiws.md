---
layout: post
title: "[Tech Interviews] "
date: 2026-02-24
tags: [ML, DS, study]
style: border
color: primary
comments: false
# description: 
toc: true
---

### Feature Selection Method, Feature engineering/selection

1. Feature selection experiment(Filter methods , Wrapper methods, Embedded methods)
Filter: 통계 기반의 중요도 판단을 통해 학습 전 단계에서부터 feature selection을 수행하는 방식
Wrapper: 여러번 학습을 반복하며 최적의 변수 조합을 찾는 방식
Embedded: 학습 모델 자체에 feature selection 기능이 포함되어 있는 방식 (Lasso의 L1 Regularization – 중요하지 않은 변수는 가중치를 0으로 만드는 기능, Tree모델들의 feature importance 계산을 통한 feature selection 수행 기능) 

a.	(Feature Selection) What is a good feature? What are some ways to judge good features? (What is feature selection and what methods are there?)
단순히 설명력을 높이는 것을 넘어 타겟 변수와 상관관계는 높으면서, 피처끼리의 상관관계(다중공선성)는 낮은 것
-  mRMR(Minimum Redundancy Maximum Relevance)이 바로 이 원리(중복은 최소화, 관련성은 최대화)를 구현한 알고리즘

2. Missing value handling: (Missing value) There are a lot of missing values in real data. How can we handle them to improve model performance?
가장 단순하고 쉬운 방식은 delete이지만 결측치의 수가 많은 경우 데이터의 정합성에 문제가 발생할 수도 있고, 데이터 설명력이 저하되는 문제가 발생할 수도 있음. 이에 delete가 아니라 데이터의 특성에 따라 대치(Imputation)를 수행. 수치형은 중앙값(Median)이나 평균으로, 범주형은 최빈값(Mode)으로 채우거나, 더 정교하게는 KNN Imputer나 Iterative Imputer를 사용해 다른 변수들과의 관계를 기반으로 예측하여 채울 수 있음.


3. Difference between Random forest and Lasso Regression feature selection
- Random Forest: Information Gain or Gini Impurity-based featrue importance calculation 
- Lasso: L1 Regularization-based feature selection (set the importance as 0)
- Lasso는 선형적인 관계에서 변수를 제거하고, Random Forest는 비선형적인 관계까지 포함하여 "이 변수가 데이터를 나누는 데 얼마나 기여했는가"를 수치화

4. Feature engineering for text data
* (Numeric variable) Why do I need feature normalization for numeric data?

* Normalization vs. Standardization
- Normalization: 데이터의 분포가 정규분포가 아니거나 정확한 분포를 모를 떄 0 ~ 1 사이의 정규분포를 가정하기 위해 사용 (MinMax)
- Standardization: 이상치 등 데이터의 scale이 매우 차이가 많이 날 때 평균 0, 표준편차 1인 표준정규분포로 만드는 방식 (Z-scored)

* (Categorical variable) How should categorical features be handled when performing data preprocessing tasks?

* One-hot encoding, Label encoding, target encoding, etc.
- One-hot encoding: 순서가 없는 범주형 데이터에 사용
- Label encoding: 순서가 있는 범주형 데이터에 사용 (Tree모델에 유리)
- Target encoding: 범주 별 타겟 변수의 평균으로 변환 

* (Text data) The dataset includes numeric and categorical variables, but may also contain text data. Please explain how text data can be used for modeling.
- TF-IDF (단어 빈도 기반), Transformer (BERT), Word Embedding (Word2Vec) 등


### Difference between network types : MLP vs. Convolutional Neural Network vs. Recurrent Neural Network vs. Transformer

1. CNN
a.	Why CNN is well known solution in Computer Vision field
b.	Benefit of ReLU/ Other activation function
* What is an activation function and why is it needed?
* Explain the shortcomings of ReLU

2. RNN
a.	Why RNN is well known solution to Time-series data
- 순서와 시간(Sequential/Temporal)을 고려하여 이전 단계의 출력값이 다음 단계의 입력값으로 들어가는 재귀적 구조로 되어 있어 앞뒤 맥락이 중요한 시계열 데이터나 자연어 처리에 강함. 

b.	Vanishing gradient problem definition and solution
- 기울기 소실 문제는 역전파(Backpropagation) 과정에서 기울기를 계속 곱하다 보니 값이 0에 가까워져 앞부분의 가중치가 업데이트되지 않는 현상으로, 이를 해결하기 위한 방법으로 LSTM과 GRU가 있음. 

c.	GRU, LSTM Architecture: What is the difference between GRU and LSTM?
- 

d.	RNN vs ARIMA

3. Transformer: What is the difference between CNN and Transformer?
a.	Attention mechanism's role
- Self-Attention 매커니즘을 통해 중요한 데이터를 한 번에 파악하는 방식 (Attention은 가중치를 통해 중요한 데이터를 선별하는 알고리즘)
b.	Positional Encoding 
c.	How Attention score is calculated

4. MLP
a.	Limitation of MLP


### Evaluation 방법론 (recall precision, roc curve, etc..)

1. Precision, Recall, F1-Score
* (Precision, Recall, F1-Score) Please explain what evaluation methods can be used in the model validation process and the pros and cons of each method
- Precision: 정밀도. Positive라고 예측한 것 중 실제 Positive인 비율. 
- Recall: 재현율. 실제 Positive인 것 중 모델이 Positive라고 맞춘 비율. 
- F1-score: Precision + Recall / 2 (조화평균) 
* What is the appropriate metric for regression/classification?
- Classification: Accuracy(균형 데이터), F1-Score/AUC-ROC(불균형 데이터), Log Loss(확률적 정밀도 파악).
- Regression: MAE, MSE, R2, MAPE 

2. ROC Curve, Log Loss: (ROC Curve) What are ROC curves and AUC-ROC scores?
- ROC Curve:  임계값(Threshold)을 변화시킬 때 TPR(True Positive Rate)과 FPR(False Positive Rate)의 변화를 나타낸 곡선
- AUC-ROC Curve: ROC곡선 아래의 면적. 1에 가까울수록 모델이 긍정/부정을 구별하는 성능(분별력)이 뛰어남을 의미. 

#### Ways to fighting against overfitting ?
1. Methods or techniques to prevent or reduce overfitting
- Complexity Control: Regularization (L1, L2) 추가
- Early Stopping: 오차가 증가하기 시작하면 학습을 중단
- Pruning: decision tree에서 불필요한 가지를 제거 
- Dropout: 신경망에서 random하게 node를 꺼서 특정 node에 의한 의존도 감소 

2. Data augmentation for tabular data
- SMOTE(Synthetic Minority Over-sampling Technique): 클래스 불균형을 해결하기 위한 방식으로, 기존 데이터 사이의 공간을 knn을 기반으로 찾고, 샘플과 이웃 사이의 선분 위의 임의의 지점에 새로운 데이터를 생성. 
- VAE(Variational Autoencoder): 데이터의 분포를 학습하여 실제 데이터와 통계적으로 유사한 가상 데이터를 생성하는 방식. 딥러닝 기반의 잠재적 분포 기반 규칙을 학습하는 게 특징. 

3. Why Decision Trees and Random Forests are susceptible to overfitting
- Decision Tree: 데이터의 아주 미세한 특징까지 끝까지 나누려 하기 때문에 depth가 깊어져 overfitting이 발생 
- Random Forest: 개별 트리가 과적합될 수 있으나 bagging을 통해 overfitting 완화 가능. 
    - Bagging: 병렬 학습과 복원 추출을 통한 안정성 높은 학습을 수행하는 방식. (variance/분산 감소)
    - Boosting: Bagging과 달리 앞선 모델의 부족함을 뒷 모델이 계속해서 보완하는 방식의 weak learner start method. 오차를 줄이며 점진적으로 강화 (bias 제거)
* Please explain some ways to reduce the risk of overfitting and underfitting (or How should we deal with overfitting)? 

* There is cross validation as a way to prevent overfitting. Can you explain it?
- Cross Validation: 데이터를 M개로 나눠 하나를 검증용, 나머지를 학습용으로 번갈아 사용하는 방식. 특정 데이터셋에 모델이 매몰되는 것을 막아 일반화 성능을 객관적으로 측정하도록 함. 

#### Ways to overcome dataset conditions below ?
1. Small dataset 
2. Imbalanced dataset 
3. Noisy dataset


### 최근 읽은 논문?
If you have recently read the paper and have experience implementing the algorithm in an actual project, please explain.


### Culture
Please describe the most difficult communication experience you had at work. How did you overcome it again?
Tasks you would like to perform if you join the company
Do you have experience explaining analysis results to someone who is unfamiliar with data analysis?


## [Data Scientist specific]

### Data Engineering experience (Tools, SQL, Database)
1. Data pipeline tools: Do you have experience using data pipeline tools (Airflow, etc.)?

2. Data Preprocessing
a. How would you process it if there are 2,000 to 3,000 features?
b. When carrying out a machine learning project, what tasks are performed during data preprocessing?


### Database, SQL
* SQL, MySQL, BigQuery experience
* There have been reports that MySQL is slow these days. What would you check and handle first?
* What should I do if I need to insert a large amount of data (more than 5 million) in MySQL?
* What are Windows functions and how to write them?
* Check knowledge about SQL Join (Inner join, left join, right join, full join)

### Statistics question (pvalue, bayesian, …)
#### Probability and Distribution
1. P-Value, Multicollinearity, 
2. Sampling: Explain how sampling is used in machine learning

#### Estimation
1. Explain Trade-off between bias and variance in estimation
-  Bias는 모델이 너무 단순해서 정답을 못 맞히는 정도(Underfitting)이고, Variance는 모델이 데이터의 노이즈까지 학습하여 결과가 요동치는 정도(Overfitting).
-  하나를 줄이면 다른 하나가 늘어나는 관계이기 때문에, 검증 오차(Validation Error)가 최소가 되는 최적의 복잡도 지점을 찾는 것이 머신러닝 학습의 핵심. 

2. Cautious of when making estimations with a small sample size?


3. Relationship between the width of a confidence interval, the confidence level, and the sample size
- 샘플 사이즈가 커질수록 표준 오차가 줄어들기 때문에 신뢰구간의 폭은 좁아지고 정밀해짐. 반대로 신뢰 수준(Confidence Level)을 95%에서 99%로 높이면, 정답을 포함할 확률을 높여야 하므로 신뢰구간의 폭은 넓어지게 됨. 

#### Multiple Regression
1. Multicollinearity: Explain what multicollinearity is and why it is a problem. How to solve this
- 다중공선성: Regression 문제에서 독립 변수들 간 강한 상관관계가 존재할 때 발생하는 문제로, 어떤 변수가 target에 진짜 영향을 주는지 해석하기가 어려워짐. 이를 해결하기 위해 VIF 지수가 높은 변수를 제거하거나, L1/L2 Regularization을 적용하여 가중치를 억제하여 문제를 해결할 수 있음. 

#### Bayesian statistics
1. Bayes' theorem
a.	Basics: 사전 확률에 새로운 우도(likelihood)를 결합하여 사후 확률을 도출하는 수식으로, 어떤 사건이 발생했다는 조건 하에 가설이 맞을 확률을 사후적으로 계속 업데이트 하는 확률적 추론 방식. 
- (Prior, 사전 확률): 데이터를 보기 전, 우리가 가설 H에 대해 이미 알고 있거나 믿고 있는 확률
- (Likelihood, 우도): 가설 H가 참일 때, 현재 데이터 D가 관측될 확률
- (Posterior, 사후 확률): 데이터 D를 확인한 후, 가설 H가 참일 최종적인 확률
- (Evidence, 증거): 데이터 D 자체가 나타날 전체 확률 (보통 상수로 취급하여 확률의 합을 1로 만드는 역할) 

b.	MLE (Maximum Likelihood Estimation): 최대 우도 추정. 현재 주어진 데이터가 나타날 확률을 최대화하는 파라미터를 찾는 방식. 최대한 주관을 배제. 
c.	MAP (Maximum a Posteriori): 최대 사후 확률 추정. 사전 확률(주관)을 개입시켜 관측된 사실에 집중하여 사후확률을 최대로 추정하는 방법. (과적합 해소에 적합?)

2. MCMC(Markov Chain Monte Carlo)
- 사후 확률의 분포가 너무 복잡해서 수식으로 직접 계산(적분)하기 어려울 때, 무작위 샘플링을 통해 그 분포를 근사적으로 찾아내는 기법. '마르코프 체인' 성질을 이용해 현재 상태에서 다음 상태를 확률적으로 탐색하며 샘플을 추출하고, 이 샘플들이 모여 전체 확률 분포를 형성하게 함으로써 복잡한 베이지안 추론을 가능하도록 함. 

#### Multivariate analysis
1. PCA, LDA(Linear Discriminant Analysis): What is Principal Component Analysis (PCA) and why is it used?
- 

2. Distance metrics in cluster analysis (Euclidean, Manhattan, Cosine, etc.) : Based on your learning and research experience, explain under what circumstances you would use cosine similarity instead of Euclidean distance
- 데이터의 절대적인 크기보다 방향성(패턴)이 중요할 때 사용. 예를 들어 텍스트 데이터에서 문서의 길이는 다르더라도 언급된 단어의 비율(주제)이 비슷하다면 두 문서는 유사하다고 보는데, 이때 유클리드 거리는 문서 길이에 영향을 받지만 코사인 유사도는 벡터의 각도만 보기 때문에 훨씬 정확한 유사도를 산출할 수 있음.

### Time series
#### What characteristics should be considered when processing time series data, and what model should be used?
1. Characteristics: Seasonality, Trend, Cyclicity, irregularity
- Seasonality:
- Trend:
- Cyclicity:
- Irregularity(Non-stationarity): 

2. Time series model: ARIMA, Kalman Filter, LSTM, Prophet, Multivariate Time Series Mdoel (VAR: Vector Autoregression, VARIMA: Vector AutoRegressive Integrated moving Average), etc.
- ARIMA: 자기회귀(AR) + 이동평균(MA) + 차분(I). 선형/통계적 정상성이 유지되는 데이터에서 유효함. 
- Prophet: trend, seasonality, holiday effect를 고려한 비선형적이고 정상성이 없는 데이터에 대해서도 유효하게 작용. 
- LSTM: 딥러닝 기반의 Long memory와 short memory 기반의 과거 데이터를 활용하는 방식. 데이터가 많고 복잡한 비선형 관계가 있을 떄 사용. 
- VAR: 여러 시계열 변수가 서로 영향을 주고받는 다변량 복잡도 높은 시계열 데이터에서 유효함. 

#### How Can Time-Series Data Be Declared As Stationery? -> How to make it stationary? (Differencing, Time series decomposition)
- stationary: 시간이 흘러도 데이터의 평균과 분산이 일정한 상태. (ARIMA와 같은 통계적 시계열 모델이 가정하는 상태)

1. Augmented Dickey-Fuller Test(ADF Test)
