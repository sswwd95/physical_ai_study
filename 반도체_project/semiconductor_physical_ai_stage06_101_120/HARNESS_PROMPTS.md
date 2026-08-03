# 실습 101~120 Antigravity 하네스 프롬프트

## 실습 101 — defect_data_profile
```text
반도체 불량 분류 CSV의 행·열 수, defect 클래스 건수와 비율,
defect_type 건수, 정상·불량별 주요 센서 평균을 출력하는 pandas 예제를 작성하라.
```

## 실습 102 — feature_target_split
```text
timestamp, lot_id, defect_type은 모델 입력에서 제외하고 defect를 목표값 y로 분리하라.
입력 컬럼 목록, X 크기, y 클래스 건수를 출력하라.
```

## 실습 103 — stratified_train_test_split
```text
train_test_split을 사용해 테스트 비율 0.25, random_state=42로 분할하라.
stratify=y를 적용하고 전체·학습·평가 데이터의 불량 비율을 비교하라.
```

## 실습 104 — lot_group_split
```text
GroupShuffleSplit을 사용하여 lot_id 단위로 학습과 평가 데이터를 분리하라.
test_size=0.25, random_state=42를 사용하고 두 집합의 LOT 교집합이 비어 있는지 확인하라.
```

## 실습 105 — preprocessing_pipeline
```text
숫자형 컬럼에는 StandardScaler, recipe와 chamber_id에는 OneHotEncoder를 적용하는
ColumnTransformer를 작성하라. 학습 데이터에 fit_transform하고 변환 후 배열 크기를 출력하라.
```

## 실습 106 — logistic_regression_basic
```text
ColumnTransformer와 LogisticRegression을 Pipeline으로 연결하라.
max_iter=1000, random_state=42를 사용하고 테스트 accuracy, precision, recall, f1을 출력하라.
```

## 실습 107 — logistic_coefficients
```text
실습 106과 같은 모델을 학습한 뒤 전처리된 feature_names_out과 LogisticRegression 계수를
연결하여 절댓값이 큰 상위 15개 특징을 출력하고 CSV로 저장하라.
```

## 실습 108 — decision_tree_basic
```text
범주형은 OneHotEncoder로 변환하고 DecisionTreeClassifier를 학습하라.
max_depth=5, min_samples_leaf=10, random_state=42를 사용하고 주요 성능 지표를 출력하라.
```

## 실습 109 — tree_depth_comparison
```text
max_depth 2, 3, 5, 8, None을 비교하라.
각 깊이별 train_f1과 test_f1을 계산하고 CSV로 저장하라.
```

## 실습 110 — random_forest_basic
```text
RandomForestClassifier를 n_estimators=300, max_depth=8, min_samples_leaf=5,
random_state=42, n_jobs=-1로 학습하라. accuracy, precision, recall, f1을 출력하라.
```

## 실습 111 — random_forest_importance
```text
실습 110과 같은 RandomForest를 학습하고 feature_importances_를 특징 이름과 연결하라.
중요도가 높은 상위 15개를 출력하고 CSV로 저장하라.
```

## 실습 112 — class_weight_balancing
```text
LogisticRegression에서 class_weight=None과 'balanced'를 비교하라.
각 설정의 precision, recall, f1, predicted_defect_count를 표로 저장하라.
```

## 실습 113 — manual_oversampling
```text
외부 라이브러리 없이 pandas로 불량 클래스 행을 복원추출하여 정상 클래스 수와 같게 만들라.
오버샘플링 전후 클래스 건수를 출력하고 LogisticRegression으로 성능을 평가하라.
```

## 실습 114 — probability_threshold_comparison
```text
balanced LogisticRegression의 predict_proba를 사용하라.
임계값 0.2, 0.3, 0.4, 0.5, 0.6을 비교하여 precision, recall, f1, 예측 불량 수를 저장하라.
```

## 실습 115 — confusion_matrix_analysis
```text
RandomForest 모델의 confusion_matrix를 계산하라.
TN, FP, FN, TP를 한 행의 DataFrame으로 만들고 specificity, false_negative_rate를 함께 저장하라.
```

## 실습 116 — roc_auc_comparison
```text
LogisticRegression, DecisionTree, RandomForest의 불량확률을 계산하고
각 모델의 roc_auc_score를 비교하여 CSV로 저장하라.
```

## 실습 117 — precision_recall_auc
```text
LogisticRegression, DecisionTree, RandomForest의 average_precision_score를 계산하라.
모델별 ROC-AUC와 PR-AUC를 함께 비교하여 저장하라.
```

## 실습 118 — cross_validation_f1
```text
StratifiedKFold 5분할과 cross_validate를 사용해 balanced LogisticRegression의
precision, recall, f1을 평가하라. 각 fold와 평균·표준편차를 CSV로 저장하라.
```

## 실습 119 — defect_prediction_output
```text
balanced RandomForest를 학습하고 평가 데이터의 defect_probability와 predicted_defect를 계산하라.
timestamp, lot_id, recipe, chamber_id, actual_defect와 함께 CSV로 저장하라.
```

## 실습 120 — automated_classification_report
```text
LogisticRegression, DecisionTree, RandomForest를 학습하라.
model_metrics, confusion_matrices, predictions, feature_importance 네 시트의 Excel 보고서를 만들고
모델별 accuracy, precision, recall, f1, roc_auc, pr_auc를 CSV로도 저장하라.
```
