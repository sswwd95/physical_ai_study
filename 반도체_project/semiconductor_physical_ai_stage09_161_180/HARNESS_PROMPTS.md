## 실습 161 — prior_predictive_yield
```text
평균 수율 mu~Normal(94,3), sigma~HalfNormal(2), y~Normal(mu,sigma)인 PyMC 모형을 만들고
사전예측 1000개를 생성하여 범위와 평균을 출력하라.
```

## 실습 162 — bayesian_mean_estimation
```text
yield_percent를 관측값으로 사용해 mu~Normal(94,5), sigma~HalfNormal(3)인 정규모형을 작성하라.
draws=1000, tune=1000, chains=2로 표본추출하고 az.summary를 저장하라.
```

## 실습 163 — hdi_and_rope
```text
실습 162 모형에서 mu의 94% HDI와 P(mu>94), ROPE=[93.5,94.5] 안의 사후확률을 계산하라.
```

## 실습 164 — recipe_group_means
```text
recipe를 정수 인덱스로 바꾸고 레시피별 mu를 Normal(94,4), 공통 sigma를 HalfNormal(3)로 두어
그룹 평균 모형을 작성하라. 레시피별 사후요약을 저장하라.
```

## 실습 165 — recipe_difference_probability
```text
ETCH-A와 ETCH-C 평균 차이를 deterministic 변수 diff_A_C로 정의하고
P(diff>0), 평균 차이, 94% HDI를 출력하라.
```

## 실습 166 — simple_bayesian_regression
```text
particle_mean을 표준화하고 yield=alpha+beta*x 모형을 작성하라.
alpha~Normal(94,5), beta~Normal(0,2), sigma~HalfNormal(3)을 사용하라.
```

## 실습 167 — multiple_bayesian_regression
```text
온도, 압력, 입자, 진동, 정비경과시간을 표준화하고 beta 벡터를 Normal(0,1)로 둔
다중 베이지안 회귀를 작성하라.
```

## 실습 168 — posterior_predictive_check
```text
다중 회귀 모형을 학습한 뒤 pm.sample_posterior_predictive로 y 예측표본을 만들고
관측 평균과 예측 평균, 관측 표준편차와 예측 표준편차를 비교하라.
```

## 실습 169 — out_of_sample_prediction
```text
입자 표준화 회귀모형에서 particle_mean=8인 새 조건의 mu_new를 deterministic으로 정의하고
사후 평균과 94% HDI를 출력하라.
```

## 실습 170 — hierarchical_chamber_model
```text
챔버별 효과를 전체 평균 mu_global과 tau로부터 생성하는 비중심 계층모형으로 작성하라.
챔버별 평균 수율의 사후요약을 저장하라.
```

## 실습 171 — prior_sensitivity
```text
약한 사전 beta~Normal(0,5)와 강한 사전 beta~Normal(0,0.5)를 각각 적합하고 beta 평균을 비교하라.
```

## 실습 172 — robust_student_t_model
```text
Normal 대신 StudentT(nu,mu,sigma) 관측모형을 사용하고 nu~Exponential(1/10)+1로 정의하라.
```

## 실습 173 — low_yield_probability
```text
단순 정규모형에서 posterior predictive를 생성하고 P(y_new<92)를 계산하라.
```

## 실습 174 — bayesian_r_squared
```text
다중 회귀의 mu 분산과 잔차분산으로 R2=var(mu)/(var(mu)+sigma^2)를 deterministic으로 정의하라.
```

## 실습 175 — loo_model_comparison
```text
두 모델을 log_likelihood가 포함된 InferenceData로 적합하고 az.compare를 사용하라.
```

## 실습 176 — diagnostic_summary
```text
az.summary와 sample_stats.diverging 합계를 출력하고 진단 CSV를 저장하라.
```

## 실습 177 — trace_and_posterior_plot
```text
az.plot_trace와 az.plot_posterior를 Agg 백엔드로 저장하라.
```

## 실습 178 — hierarchical_recipe_chamber
```text
레시피 고정효과와 챔버 랜덤효과를 함께 포함한 수율 모형을 작성하라.
```

## 실습 179 — bayesian_prediction_table
```text
처음 20행에 대해 posterior predictive 평균, 3%, 97% 분위수를 CSV로 저장하라.
```

## 실습 180 — automated_bayesian_report
```text
summary, diagnostics, recipe_comparison, prediction_interval 네 시트를 생성하라.
```