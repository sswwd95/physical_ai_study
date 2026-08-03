# 반도체 Physical AI 하네스 엔지니어링
## 13단계: 241~260제 — PyMC 기반 베이지안 설비 수명·고장확률·RUL 추정

### 실행
```bat
cd semiconductor_physical_ai_stage13_241_260
conda env create -f environment.yml
conda activate semi-physical-ai-stage13
python verify_environment.py
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 241 | lifetime_data_profile | 수명·검열·그룹 분포를 확인합니다. | `examples/ex241_lifetime_data_profile.py` |
| 242 | exponential_lifetime_model | 지수분포 기반 수명모형을 학습합니다. | `examples/ex242_exponential_lifetime_model.py` |
| 243 | weibull_lifetime_model | Weibull 수명분포의 형상·스케일을 추정합니다. | `examples/ex243_weibull_lifetime_model.py` |
| 244 | censored_weibull_model | 우측 검열을 포함한 Weibull 모형을 작성합니다. | `examples/ex244_censored_weibull_model.py` |
| 245 | failure_probability_by_cycle | 특정 주기 이전 고장확률을 계산합니다. | `examples/ex245_failure_probability_by_cycle.py` |
| 246 | survival_probability_curve | 주기별 생존확률 사후분포를 계산합니다. | `examples/ex246_survival_probability_curve.py` |
| 247 | median_lifetime_hdi | 중앙 수명의 사후평균과 HDI를 계산합니다. | `examples/ex247_median_lifetime_hdi.py` |
| 248 | chamber_type_effect | 챔버 유형별 수명 차이를 회귀계수로 추정합니다. | `examples/ex248_chamber_type_effect.py` |
| 249 | maintenance_policy_effect | 정비 정책별 수명 차이의 사후확률을 계산합니다. | `examples/ex249_maintenance_policy_effect.py` |
| 250 | hierarchical_equipment_model | 장비별 수명 차이를 계층적으로 부분 풀링합니다. | `examples/ex250_hierarchical_equipment_model.py` |
| 251 | sensor_aft_model | 센서값을 포함한 가속수명 회귀를 작성합니다. | `examples/ex251_sensor_aft_model.py` |
| 252 | posterior_failure_risk | 장비별 향후 20주기 고장확률을 계산합니다. | `examples/ex252_posterior_failure_risk.py` |
| 253 | bayesian_rul_regression | 센서 스냅샷으로 RUL 사후분포를 추정합니다. | `examples/ex253_bayesian_rul_regression.py` |
| 254 | rul_prediction_interval | 장비별 RUL 평균과 HDI를 생성합니다. | `examples/ex254_rul_prediction_interval.py` |
| 255 | near_failure_probability | RUL이 20 이하일 사후확률을 계산합니다. | `examples/ex255_near_failure_probability.py` |
| 256 | prior_sensitivity_lifetime | 수명 스케일 사전분포 민감도를 비교합니다. | `examples/ex256_prior_sensitivity_lifetime.py` |
| 257 | loo_lifetime_comparison | 지수·Weibull 수명모형을 LOO로 비교합니다. | `examples/ex257_loo_lifetime_comparison.py` |
| 258 | mcmc_diagnostics_lifetime | R-hat·ESS·Divergence를 점검합니다. | `examples/ex258_mcmc_diagnostics_lifetime.py` |
| 259 | maintenance_decision_cost | 정비·고장 비용을 결합해 행동을 선택합니다. | `examples/ex259_maintenance_decision_cost.py` |
| 260 | automated_bayesian_pm_report | 수명·위험·RUL·의사결정 Excel 보고서를 생성합니다. | `examples/ex260_automated_bayesian_pm_report.py` |

## 데이터
- 설비 수명 데이터: 24대
- 우측 검열 데이터 포함
- 챔버 유형·정비 정책·마지막 센서 상태 포함
- 별도 RUL 센서 스냅샷 데이터 포함
