# 반도체 Physical AI 하네스 엔지니어링
## 12단계: 221~240제 — 반도체 설비 예지보전과 잔여수명 예측 기초

### 실행
```bat
cd semiconductor_physical_ai_stage12_221_240
conda env create -f environment.yml
conda activate semi-physical-ai-stage12
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 221 | maintenance_data_profile | 장비별 수명과 센서 열화 분포를 확인합니다. | `examples/ex221_maintenance_data_profile.py` |
| 222 | degradation_trend | 장비별 센서 열화 추세를 계산합니다. | `examples/ex222_degradation_trend.py` |
| 223 | rolling_health_features | 이동평균·기울기 기반 건강 특징을 생성합니다. | `examples/ex223_rolling_health_features.py` |
| 224 | health_index_reconstruction | 센서 표준화 점수로 건강지수를 재구성합니다. | `examples/ex224_health_index_reconstruction.py` |
| 225 | failure_horizon_label | 고장 임박 분류 라벨을 생성합니다. | `examples/ex225_failure_horizon_label.py` |
| 226 | group_train_test_split | 장비 단위 학습·평가 분할을 수행합니다. | `examples/ex226_group_train_test_split.py` |
| 227 | failure_classifier_logistic | Logistic Regression으로 고장 임박을 분류합니다. | `examples/ex227_failure_classifier_logistic.py` |
| 228 | failure_classifier_random_forest | Random Forest로 고장 임박을 분류합니다. | `examples/ex228_failure_classifier_random_forest.py` |
| 229 | failure_probability_threshold | 고장확률 임계값별 정책을 비교합니다. | `examples/ex229_failure_probability_threshold.py` |
| 230 | rul_linear_regression | 선형 회귀로 잔여수명을 예측합니다. | `examples/ex230_rul_linear_regression.py` |
| 231 | rul_random_forest | Random Forest로 잔여수명을 예측합니다. | `examples/ex231_rul_random_forest.py` |
| 232 | rul_gradient_boosting | Gradient Boosting으로 잔여수명을 예측합니다. | `examples/ex232_rul_gradient_boosting.py` |
| 233 | rul_model_comparison | 여러 RUL 회귀 모델을 비교합니다. | `examples/ex233_rul_model_comparison.py` |
| 234 | rul_residual_analysis | RUL 예측 잔차를 분석합니다. | `examples/ex234_rul_residual_analysis.py` |
| 235 | near_failure_error | 고장 임박 구간 오차를 별도로 평가합니다. | `examples/ex235_near_failure_error.py` |
| 236 | maintenance_priority_score | 정비 우선순위 점수를 계산합니다. | `examples/ex236_maintenance_priority_score.py` |
| 237 | simple_survival_table | 주기별 생존율 표를 계산합니다. | `examples/ex237_simple_survival_table.py` |
| 238 | remaining_life_interval | 앙상블 기반 RUL 예측구간을 계산합니다. | `examples/ex238_remaining_life_interval.py` |
| 239 | maintenance_schedule_output | 정비 일정 추천 CSV를 생성합니다. | `examples/ex239_maintenance_schedule_output.py` |
| 240 | automated_pm_report | 자동 예지보전 Excel 보고서를 생성합니다. | `examples/ex240_automated_pm_report.py` |

## 데이터 특징
- 장비 12대
- 장비별 전 수명주기 기록
- 온도·진동·전류·압력편차·입자수
- 건강지수, RUL, 20주기 이내 고장 라벨
