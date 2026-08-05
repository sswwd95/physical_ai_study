## 실습 181 — beta_binomial_basic
```text
전체 wafer_count와 defect_count를 합산하고 p~Beta(1,1), defects~Binomial(n,p) 모형을 작성하라.
사후 평균과 94% HDI를 출력하라.
```

## 실습 182 — informative_prior
```text
과거 불량률 3%에 해당하는 Beta(3,97) 사전분포와 Beta(1,1)를 비교하라.
두 모형의 사후 평균과 HDI를 표로 출력하라.
```

## 실습 183 — target_exceedance_probability
```text
전체 불량률 모형에서 P(p>0.04), P(p>0.05)를 계산하라.
```

## 실습 184 — recipe_defect_rates
```text
recipe별 wafer_count와 defect_count를 집계하고 레시피별 p를 Beta(1,1)로 둔
벡터화 베타-이항 모형을 작성하라.
```

## 실습 185 — recipe_rate_difference
```text
ETCH-C와 ETCH-A의 불량률 차이 diff_C_A를 deterministic으로 정의하고
P(diff>0), 평균 차이, HDI를 출력하라.
```

## 실습 186 — chamber_defect_rates
```text
chamber_id별 베타-이항 모형을 작성하고 사후요약을 저장하라.
```

## 실습 187 — hierarchical_recipe_model
```text
logit 불량률에 전체 평균과 레시피 랜덤효과를 둔 계층모형을 작성하라.
```

## 실습 188 — hierarchical_chamber_model
```text
챔버 효과를 비중심 모수화한 계층 로지스틱 모형으로 작성하라.
```

## 실습 189 — bayesian_logistic_regression
```text
LOT defect_count>0을 목표로 온도편차·압력편차·입자수를 표준화한 베이지안 로지스틱 회귀를 작성하라.
```

## 실습 190 — logistic_coefficient_probability
```text
각 beta에 대해 P(beta>0)와 94% HDI를 표로 저장하라.
```

## 실습 191 — posterior_predictive_defects
```text
wafer_count=100, p 사후표본을 사용해 Binomial posterior predictive를 생성하라.
```

## 실습 192 — probability_of_zero_defects
```text
wafer_count=100일 때 P(defect_count=0)를 사후예측으로 계산하라.
```

## 실습 193 — decision_cost_matrix
```text
불량 1건 비용, 검사 강화 비용, 감소효과를 가정해 사후표본별 기대비용을 계산하라.
```

## 실습 194 — optimal_action_probability
```text
강화검사가 더 유리한 사후확률과 기대 절감액을 계산하라.
```

## 실습 195 — bayesian_ab_test
```text
ETCH-A와 ETCH-B의 상대위험도 pB/pA와 P(pB<pA)를 계산하라.
```

## 실습 196 — relative_risk_hdi
```text
pC/pA의 평균·HDI·P(RR<1.2)를 출력하라.
```

## 실습 197 — model_diagnostics
```text
계층모형의 az.summary와 divergence 수를 CSV로 저장하라.
```

## 실습 198 — posterior_plot
```text
레시피별 p의 az.plot_posterior 그래프를 PNG로 저장하라.
```

## 실습 199 — lot_risk_table
```text
로지스틱 회귀 사후평균으로 LOT별 불량발생확률을 계산해 CSV로 저장하라.
```

## 실습 200 — automated_defect_decision_report
```text
summary, recipe_rates, decision_analysis, lot_risk 네 시트를 생성하라.
```