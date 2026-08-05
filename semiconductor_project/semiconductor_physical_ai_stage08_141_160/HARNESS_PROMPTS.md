# 실습 141~160 Antigravity 하네스 프롬프트

## 실습 141 — yield_data_profile
```text
반도체 수율 회귀 CSV의 행·열 수, 수율 평균·표준편차·최소·최대,
레시피별 평균 수율을 출력하는 pandas 예제를 작성하라.
```

## 실습 142 — feature_target_split
```text
timestamp, lot_id, yield_percent를 제외하고 입력 특징 X를 만들라.
목표값 y는 yield_percent로 분리하고 입력 컬럼 목록과 크기를 출력하라.
```

## 실습 143 — regression_train_test_split
```text
train_test_split을 test_size=0.25, random_state=42로 적용하라.
학습과 평가 데이터의 수율 평균과 표준편차를 비교하라.
```

## 실습 144 — linear_regression_basic
```text
숫자형 StandardScaler, 범주형 OneHotEncoder, LinearRegression을 Pipeline으로 연결하라.
평가 데이터의 MAE, RMSE, R²를 출력하라.
```

## 실습 145 — linear_coefficients
```text
실습 144 모델을 학습한 뒤 feature_names_out과 회귀계수를 연결하라.
절댓값이 큰 상위 15개 특징을 CSV로 저장하라.
```

## 실습 146 — ridge_regression
```text
Ridge(alpha=1.0)를 전처리 Pipeline과 연결하라.
LinearRegression과 Ridge의 MAE, RMSE, R²를 비교해 CSV로 저장하라.
```

## 실습 147 — lasso_regression
```text
Lasso(alpha=0.01, max_iter=5000)를 학습하라.
0이 아닌 계수 개수와 MAE, RMSE, R²를 출력하고 전체 계수를 CSV로 저장하라.
```

## 실습 148 — elastic_net_regression
```text
ElasticNet(alpha=0.01, l1_ratio=0.5, max_iter=5000)를 학습하라.
Ridge, Lasso, ElasticNet의 MAE와 R²를 비교하라.
```

## 실습 149 — decision_tree_regressor
```text
DecisionTreeRegressor(max_depth=6, min_samples_leaf=10, random_state=42)를 학습하라.
MAE, RMSE, R²를 출력하라.
```

## 실습 150 — random_forest_regressor
```text
RandomForestRegressor를 n_estimators=400, max_depth=10,
min_samples_leaf=4, random_state=42, n_jobs=-1로 학습하라.
MAE, RMSE, R²를 출력하라.
```

## 실습 151 — random_forest_importance
```text
실습 150과 같은 모델을 학습하고 feature_importances_를 특징 이름과 연결하라.
중요도 상위 15개를 CSV로 저장하라.
```

## 실습 152 — gradient_boosting_regressor
```text
GradientBoostingRegressor를 n_estimators=250, learning_rate=0.05,
max_depth=3, random_state=42로 학습하라. MAE, RMSE, R²를 출력하라.
```

## 실습 153 — regression_model_comparison
```text
LinearRegression, Ridge, DecisionTreeRegressor, RandomForestRegressor,
GradientBoostingRegressor를 비교하라. MAE, RMSE, R²를 계산하고 MAE 순으로 저장하라.
```

## 실습 154 — residual_analysis
```text
RandomForestRegressor로 예측하고 residual=actual-prediction을 계산하라.
잔차 평균, 표준편차, MAE를 출력하고 절댓값이 큰 상위 20행을 CSV로 저장하라.
```

## 실습 155 — low_yield_segment_error
```text
RandomForestRegressor 예측 결과에서 실제 수율 92% 미만을 low_yield로 정의하라.
전체 MAE와 저수율 MAE, 고수율 MAE를 비교해 CSV로 저장하라.
```

## 실습 156 — cross_validation_regression
```text
RandomForestRegressor Pipeline에 KFold 5분할 cross_validate를 적용하라.
neg_mean_absolute_error, neg_root_mean_squared_error, r2를 계산하고 fold별 결과와 평균을 저장하라.
```

## 실습 157 — grid_search_random_forest
```text
RandomForestRegressor Pipeline에 GridSearchCV를 적용하라.
n_estimators=[200,400], max_depth=[6,10,None], min_samples_leaf=[2,5],
scoring='neg_mean_absolute_error', cv=3, n_jobs=-1을 사용하라.
```

## 실습 158 — prediction_interval_bootstrap
```text
RandomForestRegressor 20개를 서로 다른 random_state로 학습하라.
평가 데이터 예측의 5%, 50%, 95% 분위수를 계산하고 실제 수율과 함께 CSV로 저장하라.
```

## 실습 159 — yield_prediction_output
```text
튜닝된 RandomForestRegressor로 평가 데이터를 예측하라.
timestamp, lot_id, recipe, chamber_id, actual_yield, predicted_yield,
absolute_error, predicted_low_yield를 포함한 CSV를 생성하라.
predicted_low_yield 기준은 92% 미만으로 하라.
```

## 실습 160 — automated_yield_report
```text
LinearRegression, Ridge, RandomForestRegressor, GradientBoostingRegressor를 비교하라.
model_metrics, predictions, residual_summary, feature_importance 시트의 Excel 보고서를 만들고
모델별 MAE, RMSE, R²를 CSV로 저장하라.
```
