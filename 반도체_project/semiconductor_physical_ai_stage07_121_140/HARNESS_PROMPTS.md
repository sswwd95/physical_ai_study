# 실습 121~140 Antigravity 하네스 프롬프트

## 실습 121 — multiclass_data_profile
```text
반도체 다중 불량 유형 CSV에서 클래스별 건수와 비율,
클래스별 주요 센서 평균을 출력하는 pandas 예제를 작성하라.
```

## 실습 122 — label_encoding
```text
LabelEncoder로 defect_type을 정수 라벨로 변환하라.
classes_, 원본과 정수 라벨의 매핑, inverse_transform 예시를 출력하라.
```

## 실습 123 — multiclass_stratified_split
```text
defect_type을 목표값으로 하고 train_test_split에서 stratify=y를 사용하라.
테스트 비율 0.25, random_state=42로 분할하고 전체·학습·평가 클래스 비율을 비교하라.
```

## 실습 124 — multinomial_logistic_regression
```text
숫자형 StandardScaler, 범주형 OneHotEncoder, LogisticRegression을 Pipeline으로 연결하라.
max_iter=2000, class_weight='balanced', random_state=42를 사용하고 macro F1과 weighted F1을 출력하라.
```

## 실습 125 — one_vs_rest_coefficients
```text
OneVsRestClassifier(LogisticRegression)을 사용해 클래스별 분류기를 학습하라.
각 클래스에서 절댓값이 큰 상위 8개 계수를 CSV로 저장하라.
```

## 실습 126 — multiclass_decision_tree
```text
DecisionTreeClassifier를 max_depth=6, min_samples_leaf=8,
class_weight='balanced', random_state=42로 학습하라.
macro F1, weighted F1, confusion matrix를 출력하라.
```

## 실습 127 — multiclass_random_forest
```text
RandomForestClassifier를 n_estimators=400, max_depth=10,
min_samples_leaf=4, class_weight='balanced', random_state=42, n_jobs=-1로 학습하라.
classification_report를 출력하라.
```

## 실습 128 — random_forest_feature_importance
```text
실습 127과 같은 RandomForest를 학습하고 feature_importances_를 특징 이름과 연결하라.
중요도 상위 20개를 출력하고 CSV로 저장하라.
```

## 실습 129 — hist_gradient_boosting
```text
범주형은 OneHotEncoder, 숫자형은 passthrough로 전처리하고
HistGradientBoostingClassifier를 max_iter=200, learning_rate=0.08,
max_depth=6, random_state=42로 학습하라. macro F1을 출력하라.
```

## 실습 130 — model_comparison
```text
LogisticRegression, DecisionTree, RandomForest, HistGradientBoosting을 비교하라.
accuracy, macro_f1, weighted_f1을 계산하고 macro_f1 순으로 정렬해 CSV로 저장하라.
```

## 실습 131 — grid_search_random_forest
```text
RandomForest Pipeline에 GridSearchCV를 적용하라.
n_estimators=[200,400], max_depth=[6,10,None], min_samples_leaf=[2,5],
scoring='f1_macro', cv=3, n_jobs=-1을 사용하고 최적 파라미터와 점수를 출력하라.
```

## 실습 132 — randomized_search_gradient_boosting
```text
HistGradientBoosting Pipeline에 RandomizedSearchCV를 적용하라.
learning_rate, max_iter, max_depth, l2_regularization 후보를 정의하고
n_iter=8, scoring='f1_macro', cv=3, random_state=42로 탐색하라.
```

## 실습 133 — stratified_cross_validation
```text
RandomForest Pipeline에 StratifiedKFold 5분할과 cross_validate를 적용하라.
accuracy, f1_macro, f1_weighted를 계산하고 fold별 결과와 평균·표준편차를 CSV로 저장하라.
```

## 실습 134 — classwise_metrics
```text
RandomForest를 학습하고 classification_report(..., output_dict=True)를 사용하라.
클래스별 precision, recall, f1-score, support를 DataFrame으로 저장하라.
```

## 실습 135 — confusion_matrix_table
```text
RandomForest 예측으로 confusion_matrix를 계산하라.
행은 actual_, 열은 predicted_ 접두사를 붙인 DataFrame으로 저장하라.
```

## 실습 136 — probability_calibration
```text
RandomForest Pipeline을 CalibratedClassifierCV(method='sigmoid', cv=3)로 감싸 학습하라.
평가 데이터의 log_loss와 각 클래스 평균 예측확률을 출력하라.
```

## 실습 137 — low_confidence_review
```text
보정된 다중 클래스 모델의 predict_proba를 사용하라.
최대 확률이 0.55 미만이면 review_required=True로 표시하고
상위 두 클래스와 확률 차이도 계산하여 CSV로 저장하라.
```

## 실습 138 — misclassification_analysis
```text
RandomForest 평가 결과에서 actual_class != predicted_class인 행만 추출하라.
실제→예측 클래스 조합별 건수를 집계하고 상세 오분류 행과 함께 CSV 두 개로 저장하라.
```

## 실습 139 — multiclass_prediction_output
```text
튜닝된 RandomForest를 학습하고 평가 데이터에 대해 각 클래스 확률,
predicted_class, actual_class, max_probability를 포함하는 CSV를 생성하라.
```

## 실습 140 — automated_multiclass_report
```text
LogisticRegression, RandomForest, HistGradientBoosting을 학습하라.
model_metrics, class_metrics, confusion_matrix, predictions, misclassified_rows,
feature_importance 시트의 Excel 보고서를 생성하고 모델 비교 CSV도 저장하라.
```
