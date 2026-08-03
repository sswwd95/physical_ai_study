# 반도체 Physical AI 하네스 엔지니어링
## 15단계: 281~300제 — 반도체 공정 최적화와 베이지안 의사결정

### 실행
```bat
cd semiconductor_physical_ai_stage15_281_300
conda env create -f environment.yml
conda activate semi-physical-ai-stage15
python verify_environment.py
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 281 | optimization_data_profile | 최적화 이력과 후보 공간을 확인합니다. | `examples/ex281_optimization_data_profile.py` |
| 282 | single_objective_uniformity | 균일도 최대 조건을 탐색합니다. | `examples/ex282_single_objective_uniformity.py` |
| 283 | single_objective_defect_rate | 불량률 최소 조건을 탐색합니다. | `examples/ex283_single_objective_defect_rate.py` |
| 284 | cycle_time_optimization | 사이클타임 최소 조건을 탐색합니다. | `examples/ex284_cycle_time_optimization.py` |
| 285 | constraint_filtering | 안전·품질 제약조건으로 후보를 필터링합니다. | `examples/ex285_constraint_filtering.py` |
| 286 | surrogate_models | 균일도·불량률·시간 대리모델을 학습합니다. | `examples/ex286_surrogate_models.py` |
| 287 | candidate_prediction | 전체 후보 조건의 결과를 예측합니다. | `examples/ex287_candidate_prediction.py` |
| 288 | weighted_utility | 가중 효용함수로 조건을 순위화합니다. | `examples/ex288_weighted_utility.py` |
| 289 | pareto_front | 다목적 Pareto 후보를 계산합니다. | `examples/ex289_pareto_front.py` |
| 290 | robust_condition_score | 예측 변동을 고려한 강건 점수를 계산합니다. | `examples/ex290_robust_condition_score.py` |
| 291 | expected_improvement | 균일도 기대개선량을 계산합니다. | `examples/ex291_expected_improvement.py` |
| 292 | probability_of_improvement | 현재 최고값 초과확률을 계산합니다. | `examples/ex292_probability_of_improvement.py` |
| 293 | lower_confidence_bound | 보수적 신뢰하한으로 후보를 선택합니다. | `examples/ex293_lower_confidence_bound.py` |
| 294 | safe_optimization | 불량률 제약을 만족할 확률로 안전 후보를 선택합니다. | `examples/ex294_safe_optimization.py` |
| 295 | bayesian_linear_surrogate | PyMC 베이지안 회귀 대리모델을 작성합니다. | `examples/ex295_bayesian_linear_surrogate.py` |
| 296 | posterior_candidate_ranking | 후보별 최적일 사후확률을 계산합니다. | `examples/ex296_posterior_candidate_ranking.py` |
| 297 | sequential_batch_selection | 다음 실험 배치를 다양성 있게 선택합니다. | `examples/ex297_sequential_batch_selection.py` |
| 298 | cost_sensitive_decision | 품질·불량·시간·실험비용을 결합합니다. | `examples/ex298_cost_sensitive_decision.py` |
| 299 | confirmation_experiment_plan | 추천 조건의 확인 실험 계획을 생성합니다. | `examples/ex299_confirmation_experiment_plan.py` |
| 300 | automated_optimization_report | 자동 공정 최적화 Excel 보고서를 생성합니다. | `examples/ex300_automated_optimization_report.py` |

## 최적화 목표
- 균일도 최대화
- 불량률 최소화
- 사이클타임 최소화
- 안전 제약 만족
- 확인 실험 가능한 후보 추천
