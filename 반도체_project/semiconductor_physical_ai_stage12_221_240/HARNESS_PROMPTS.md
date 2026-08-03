## 실습 221 — maintenance_data_profile
```text
장비별 수명, 고장 수, 정상·고장 센서 평균을 요약하라.
```

## 실습 222 — degradation_trend
```text
장비별 온도·진동·전류·건강지수의 선형 기울기를 계산하라.
```

## 실습 223 — rolling_health_features
```text
장비별 10주기 이동평균과 이동표준편차 특징을 생성하라.
```

## 실습 224 — health_index_reconstruction
```text
센서 표준화 점수로 0~1 건강지수를 재구성하라.
```

## 실습 225 — failure_horizon_label
```text
RUL 기준 10·20·30주기 고장임박 라벨을 생성하라.
```

## 실습 226 — group_train_test_split
```text
equipment_id 단위 GroupShuffleSplit을 수행하라.
```

## 실습 227 — failure_classifier_logistic
```text
Logistic Regression으로 20주기 이내 고장 여부를 분류하라.
```

## 실습 228 — failure_classifier_random_forest
```text
Random Forest로 20주기 이내 고장 여부를 분류하라.
```

## 실습 229 — failure_probability_threshold
```text
고장확률 임계값별 precision·recall·F1을 비교하라.
```

## 실습 230 — rul_linear_regression
```text
선형 회귀로 RUL을 예측하고 MAE·RMSE·R²를 출력하라.
```

## 실습 231 — rul_random_forest
```text
Random Forest로 RUL을 예측하라.
```

## 실습 232 — rul_gradient_boosting
```text
Gradient Boosting으로 RUL을 예측하라.
```

## 실습 233 — rul_model_comparison
```text
Linear·RandomForest·GradientBoosting RUL 모델을 비교하라.
```

## 실습 234 — rul_residual_analysis
```text
RUL 잔차와 큰 오차 상위 20개를 저장하라.
```

## 실습 235 — near_failure_error
```text
전체 MAE와 RUL 20 이하 구간 MAE를 비교하라.
```

## 실습 236 — maintenance_priority_score
```text
건강지수와 RUL로 정비 우선순위 점수를 계산하라.
```

## 실습 237 — simple_survival_table
```text
장비 수명으로 10주기 간격 생존율 표를 생성하라.
```

## 실습 238 — remaining_life_interval
```text
20개 Random Forest로 RUL 5·50·95% 구간을 계산하라.
```

## 실습 239 — maintenance_schedule_output
```text
최신 장비 상태에서 정비 권고와 예정 주기를 생성하라.
```

## 실습 240 — automated_pm_report
```text
분류·회귀 성능, 예측, 정비 우선순위 Excel 보고서를 생성하라.
```