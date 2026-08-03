# 반도체 Physical AI 하네스 엔지니어링
## 10단계: 181~200제 — PyMC 기반 베이지안 불량률·공정 비교·의사결정 분석

### 실행
```bat
cd semiconductor_physical_ai_stage10_181_200
conda env create -f environment.yml
conda activate semi-physical-ai-stage10
python verify_environment.py
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 목표 | 소스 |
|---:|---|---|---|
| 181 | beta_binomial_basic | 전체 불량률을 베타-이항 모형으로 추정합니다. | `examples/ex181_beta_binomial_basic.py` |
| 182 | informative_prior | 기존 공정 지식을 반영한 정보성 사전분포를 적용합니다. | `examples/ex182_informative_prior.py` |
| 183 | target_exceedance_probability | 불량률이 관리 목표를 초과할 확률을 계산합니다. | `examples/ex183_target_exceedance_probability.py` |
| 184 | recipe_defect_rates | 레시피별 불량률 사후분포를 추정합니다. | `examples/ex184_recipe_defect_rates.py` |
| 185 | recipe_rate_difference | 레시피 간 불량률 차이의 사후확률을 계산합니다. | `examples/ex185_recipe_rate_difference.py` |
| 186 | chamber_defect_rates | 챔버별 불량률을 추정합니다. | `examples/ex186_chamber_defect_rates.py` |
| 187 | hierarchical_recipe_model | 레시피별 불량률을 계층적으로 부분 풀링합니다. | `examples/ex187_hierarchical_recipe_model.py` |
| 188 | hierarchical_chamber_model | 챔버별 불량률을 계층적으로 추정합니다. | `examples/ex188_hierarchical_chamber_model.py` |
| 189 | bayesian_logistic_regression | 공정 변수로 LOT 불량 발생확률을 예측합니다. | `examples/ex189_bayesian_logistic_regression.py` |
| 190 | logistic_coefficient_probability | 회귀계수의 양수 확률을 계산합니다. | `examples/ex190_logistic_coefficient_probability.py` |
| 191 | posterior_predictive_defects | 새 LOT의 불량 개수 사후예측분포를 계산합니다. | `examples/ex191_posterior_predictive_defects.py` |
| 192 | probability_of_zero_defects | 다음 LOT에서 무불량일 확률을 계산합니다. | `examples/ex192_probability_of_zero_defects.py` |
| 193 | decision_cost_matrix | 검사 강화와 유지의 기대비용을 비교합니다. | `examples/ex193_decision_cost_matrix.py` |
| 194 | optimal_action_probability | 각 사후표본에서 더 저렴한 의사결정을 선택합니다. | `examples/ex194_optimal_action_probability.py` |
| 195 | bayesian_ab_test | 두 레시피 불량률을 베이지안 A/B 테스트로 비교합니다. | `examples/ex195_bayesian_ab_test.py` |
| 196 | relative_risk_hdi | 상대위험도의 HDI와 목표 이하 확률을 계산합니다. | `examples/ex196_relative_risk_hdi.py` |
| 197 | model_diagnostics | R-hat·ESS·Divergence를 점검합니다. | `examples/ex197_model_diagnostics.py` |
| 198 | posterior_plot | 불량률 사후분포 그래프를 저장합니다. | `examples/ex198_posterior_plot.py` |
| 199 | lot_risk_table | LOT별 추정 위험점수와 우선순위를 생성합니다. | `examples/ex199_lot_risk_table.py` |
| 200 | automated_defect_decision_report | 사후요약·그룹비교·의사결정·LOT위험을 Excel 보고서로 생성합니다. | `examples/ex200_automated_defect_decision_report.py` |

## 핵심 개념
- 베타-이항 모형: 불량률 p와 불량 개수의 기본 모형
- 그룹 비교: 레시피·챔버별 불량률 차이와 상대위험도
- 계층모형: 데이터가 적은 그룹을 전체 평균 정보로 부분 풀링
- 베이지안 로지스틱 회귀: 공정 변수와 불량 발생확률의 관계 추정
- 의사결정 분석: 사후확률과 비용함수를 결합해 행동 선택
