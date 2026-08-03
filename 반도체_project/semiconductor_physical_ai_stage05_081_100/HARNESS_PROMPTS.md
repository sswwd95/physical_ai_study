# 실습 081~100 Antigravity 하네스 프롬프트

## 실습 081 — anomaly_data_profile
```text
반도체 이상 탐지 CSV의 행·열 수, 이상 라벨 건수와 비율,
정상·이상 그룹별 주요 센서 평균을 계산하는 pandas 예제를 작성하라.
```

## 실습 082 — mad_outlier_detection
```text
온도 센서의 중앙값과 MAD를 계산하라.
modified_z=0.6745*(x-median)/MAD를 구하고 절댓값 3.5 이상을 이상치로 표시하라.
```

## 실습 083 — iqr_multi_sensor_flags
```text
온도, 압력, RF, 가스, 진동, 입자 수에 대해 1.5*IQR 이상치 플래그를 만들라.
행별 이상 센서 개수 anomaly_sensor_count를 계산하고 2개 이상이면 multi_iqr_anomaly로 표시하라.
```

## 실습 084 — contextual_rule_anomaly
```text
purge 상태인데 RF 전력이 900W 이상이거나 stabilize 상태인데 진동이 0.12g 이상이면
contextual_anomaly로 표시하라. 규칙별 탐지 건수를 출력하고 CSV로 저장하라.
```

## 실습 085 — rolling_residual_anomaly
```text
온도 20시점 이동평균과 이동표준편차를 계산하라.
residual=(x-rolling_mean)/rolling_std를 만들고 절댓값 3 이상을 이상으로 표시하라.
```

## 실습 086 — isolation_forest_basic
```text
StandardScaler로 6개 센서를 표준화하고 IsolationForest를 적용하라.
n_estimators=200, contamination=0.1, random_state=42를 사용하고
예측 -1을 anomaly로 변환하여 저장하라.
```

## 실습 087 — isolation_forest_scores
```text
IsolationForest의 score_samples를 사용해 값이 클수록 이상하도록 anomaly_score=-score로 변환하라.
점수가 높은 상위 20행을 출력하고 CSV로 저장하라.
```

## 실습 088 — iforest_contamination_comparison
```text
contamination 0.03, 0.05, 0.1, 0.15로 IsolationForest를 반복 학습하라.
각 설정별 예측 이상 수, precision, recall, f1을 계산하여 CSV로 저장하라.
```

## 실습 089 — local_outlier_factor
```text
StandardScaler 후 LocalOutlierFactor를 적용하라.
n_neighbors=25, contamination=0.1을 사용하고 negative_outlier_factor_를 양의 점수로 변환하라.
```

## 실습 090 — lof_neighbors_comparison
```text
n_neighbors 10, 20, 30, 50에 대해 LOF를 반복 실행하라.
contamination=0.1로 고정하고 precision, recall, f1을 비교하여 저장하라.
```

## 실습 091 — one_class_svm
```text
StandardScaler 후 OneClassSVM을 적용하라.
kernel='rbf', gamma='scale', nu=0.1을 사용하고 -1을 이상으로 변환하라.
decision_function의 음수를 이상점수로 저장하라.
```

## 실습 092 — ocsvm_nu_comparison
```text
nu 0.03, 0.05, 0.1, 0.15로 OneClassSVM을 반복 실행하고
예측 이상 수, precision, recall, f1을 비교하라.
```

## 실습 093 — robust_covariance
```text
MinCovDet를 사용해 6개 센서의 robust Mahalanobis distance를 계산하라.
거리 제곱의 97.5% 분위수를 임계값으로 사용하고 이상 여부를 저장하라.
```

## 실습 094 — pca_reconstruction_error
```text
StandardScaler 후 PCA(n_components=3)를 적용하라.
역변환 결과와 원본 표준화 데이터의 평균제곱오차를 행별 reconstruction_error로 계산하고
97.5% 분위수 이상을 이상으로 표시하라.
```

## 실습 095 — model_metric_comparison
```text
IsolationForest, LOF, OneClassSVM 세 모델을 같은 표준화 데이터에 적용하라.
각 모델의 precision, recall, f1, predicted_count를 한 표로 비교하라.
```

## 실습 096 — confusion_matrix_report
```text
IsolationForest 예측과 true_anomaly를 사용하여 confusion_matrix를 계산하라.
TN, FP, FN, TP와 precision, recall, specificity, f1을 출력하고 CSV로 저장하라.
```

## 실습 097 — threshold_optimization
```text
IsolationForest anomaly_score를 계산하라.
90%부터 99% 분위수까지 1% 간격 임계값을 비교하고 precision, recall, f1을 계산하라.
F1이 가장 높은 임계값을 출력하라.
```

## 실습 098 — anomaly_ensemble_vote
```text
IsolationForest, LOF, OneClassSVM의 이상 예측을 각각 계산하라.
3개 중 2개 이상이 이상이면 ensemble_anomaly로 표시하고 성능을 계산하라.
```

## 실습 099 — anomaly_dashboard_data
```text
IsolationForest 점수, LOF 점수, OneClassSVM 점수, 모델별 이상 플래그,
앙상블 투표 수, true_anomaly를 포함하는 대시보드 CSV를 생성하라.
```

## 실습 100 — automated_anomaly_report
```text
IsolationForest, LOF, OneClassSVM과 2표 이상 앙상블을 계산하라.
model_metrics, anomaly_rows, lot_summary 세 시트의 Excel 보고서와 CSV 요약을 생성하라.
```
