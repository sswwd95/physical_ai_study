# 반도체 Physical AI 하네스 엔지니어링
## 9단계: 161~180제 — PyMC 기반 베이지안 수율 추정과 불확실성 분석

### 실행
```bat
cd semiconductor_physical_ai_stage09_161_180
conda env create -f environment.yml
conda activate semi-physical-ai-stage09
python verify_environment.py
run_all_windows.bat
```

공식 PyMC는 호환되는 패키지 조합을 얻기 위해 conda-forge 기반의 별도 Conda 환경 사용을 권장합니다.
ArviZ의 HDI는 사후분포에서 지정 확률 질량을 포함하는 최고밀도구간을 계산합니다.

## 실습 목록
| 번호 | 핵심 주제 | 목표 | 소스 |
|---:|---|---|---|
| 161 | prior_predictive_yield | 사전예측분포로 수율 사전분포의 현실성을 확인합니다. | `examples/ex161_prior_predictive_yield.py` |
| 162 | bayesian_mean_estimation | 전체 수율 평균과 표준편차의 사후분포를 추정합니다. | `examples/ex162_bayesian_mean_estimation.py` |
| 163 | hdi_and_rope | HDI와 ROPE로 목표 수율 충족 가능성을 판단합니다. | `examples/ex163_hdi_and_rope.py` |
| 164 | recipe_group_means | 레시피별 평균 수율의 사후분포를 각각 추정합니다. | `examples/ex164_recipe_group_means.py` |
| 165 | recipe_difference_probability | 두 레시피 평균 차이의 사후확률을 계산합니다. | `examples/ex165_recipe_difference_probability.py` |
| 166 | simple_bayesian_regression | 입자 수와 수율의 베이지안 선형관계를 추정합니다. | `examples/ex166_simple_bayesian_regression.py` |
| 167 | multiple_bayesian_regression | 여러 공정 변수의 회귀계수를 동시에 추정합니다. | `examples/ex167_multiple_bayesian_regression.py` |
| 168 | posterior_predictive_check | 사후예측분포가 실제 수율 분포를 재현하는지 확인합니다. | `examples/ex168_posterior_predictive_check.py` |
| 169 | out_of_sample_prediction | 새 공정 조건의 수율 사후예측분포를 계산합니다. | `examples/ex169_out_of_sample_prediction.py` |
| 170 | hierarchical_chamber_model | 챔버별 평균 수율을 부분 풀링하는 계층모형을 작성합니다. | `examples/ex170_hierarchical_chamber_model.py` |
| 171 | prior_sensitivity | 사전분포 폭에 따른 회귀계수 변화를 비교합니다. | `examples/ex171_prior_sensitivity.py` |
| 172 | robust_student_t_model | Student-t 관측모형으로 극단값에 강한 수율 추정을 수행합니다. | `examples/ex172_robust_student_t_model.py` |
| 173 | low_yield_probability | 각 LOT의 수율이 92% 미만일 사후예측확률을 계산합니다. | `examples/ex173_low_yield_probability.py` |
| 174 | bayesian_r_squared | 베이지안 R²의 사후분포를 계산합니다. | `examples/ex174_bayesian_r_squared.py` |
| 175 | loo_model_comparison | 단순 회귀와 다중 회귀를 LOO로 비교합니다. | `examples/ex175_loo_model_comparison.py` |
| 176 | diagnostic_summary | R-hat, ESS, divergence로 MCMC 품질을 점검합니다. | `examples/ex176_diagnostic_summary.py` |
| 177 | trace_and_posterior_plot | 트레이스와 사후분포 그래프를 PNG로 저장합니다. | `examples/ex177_trace_and_posterior_plot.py` |
| 178 | hierarchical_recipe_chamber | 레시피와 챔버 효과를 함께 가진 계층 회귀를 작성합니다. | `examples/ex178_hierarchical_recipe_chamber.py` |
| 179 | bayesian_prediction_table | 평가 행별 사후예측 평균과 HDI를 표로 만듭니다. | `examples/ex179_bayesian_prediction_table.py` |
| 180 | automated_bayesian_report | 사후요약·진단·예측·그룹비교를 Excel 보고서로 생성합니다. | `examples/ex180_automated_bayesian_report.py` |

## 실행 시간
MCMC 예제는 각 파일에서 2개 체인과 수백~수천 번의 표본추출을 수행하므로 일반 pandas 예제보다 오래 걸립니다.
초기 수업에서는 draws와 tune을 300~500으로 낮춘 뒤 최종 분석에서 늘릴 수 있습니다.
