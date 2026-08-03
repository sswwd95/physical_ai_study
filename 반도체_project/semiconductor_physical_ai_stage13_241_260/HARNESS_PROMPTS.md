## 실습 241 — lifetime_data_profile
```text
설비 수명 데이터의 검열 비율, 챔버 유형별 수명, RUL 스냅샷 크기를 요약하라.
```

## 실습 242 — exponential_lifetime_model
```text
고장 관측 장비의 수명을 Exponential 모형으로 추정하라.
```

## 실습 243 — weibull_lifetime_model
```text
Weibull 형상 alpha와 스케일 beta의 사후분포를 추정하라.
```

## 실습 244 — censored_weibull_model
```text
pm.Censored를 사용해 우측 검열된 Weibull 수명모형을 작성하라.
```

## 실습 245 — failure_probability_by_cycle
```text
Weibull 사후표본으로 80·100·120·150주기 이전 고장확률을 계산하라.
```

## 실습 246 — survival_probability_curve
```text
20주기 간격 생존확률 평균과 94% HDI를 CSV로 저장하라.
```

## 실습 247 — median_lifetime_hdi
```text
Weibull 중앙수명을 deterministic으로 정의하고 HDI를 계산하라.
```

## 실습 248 — chamber_type_effect
```text
챔버 유형별 로그수명 효과를 베이지안 회귀로 추정하라.
```

## 실습 249 — maintenance_policy_effect
```text
condition_based 정책이 reactive보다 수명이 길 확률을 계산하라.
```

## 실습 250 — hierarchical_equipment_model
```text
장비별 랜덤효과를 포함한 비중심 계층 수명모형을 작성하라.
```

## 실습 251 — sensor_aft_model
```text
진동·온도·전류·입자수를 포함한 로그수명 회귀를 작성하라.
```

## 실습 252 — posterior_failure_risk
```text
각 장비가 향후 20주기 안에 고장할 조건부 확률을 계산하라.
```

## 실습 253 — bayesian_rul_regression
```text
센서 스냅샷으로 베이지안 RUL 회귀를 작성하라.
```

## 실습 254 — rul_prediction_interval
```text
행별 RUL 사후예측 평균과 3~97% 구간을 저장하라.
```

## 실습 255 — near_failure_probability
```text
각 행의 P(RUL<=20)을 계산하라.
```

## 실습 256 — prior_sensitivity_lifetime
```text
Weibull beta 사전 스케일 80·150·250을 비교하라.
```

## 실습 257 — loo_lifetime_comparison
```text
지수분포와 Weibull 수명모형을 LOO로 비교하라.
```

## 실습 258 — mcmc_diagnostics_lifetime
```text
Weibull 모형의 R-hat·ESS·Divergence를 저장하라.
```

## 실습 259 — maintenance_decision_cost
```text
고장비용 5000, 정비비용 1200으로 행동별 기대비용을 계산하라.
```

## 실습 260 — automated_bayesian_pm_report
```text
수명요약·고장위험·최신RUL·의사결정 Excel 보고서를 생성하라.
```