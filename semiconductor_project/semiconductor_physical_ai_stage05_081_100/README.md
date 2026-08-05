# 반도체 Physical AI 하네스 엔지니어링
## 5단계: 081~100제 — 반도체 이상 공정 탐지와 통계적 이상치 분석

### 단계 목표
- 점 이상, 집단 이상, 문맥적 이상을 구분한다.
- MAD·IQR·이동잔차 기반 이상 탐지를 수행한다.
- Isolation Forest, LOF, One-Class SVM을 적용한다.
- Robust Covariance와 PCA 재구성 오차를 이해한다.
- 정밀도·재현율·F1으로 모델을 비교한다.
- 임계값 최적화와 앙상블 투표를 적용한다.
- 자동 이상 탐지 보고서를 생성한다.

### 실행 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- NumPy, pandas, SciPy, scikit-learn, openpyxl

### 설치 및 실행
```bat
cd semiconductor_physical_ai_stage05_081_100
conda env create -f environment.yml
conda activate semi-physical-ai-stage05
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 081 | anomaly_data_profile | 정상·이상 라벨과 센서 분포를 먼저 확인하여 탐지 문제를 정의합니다. | `examples/ex081_anomaly_data_profile.py` |
| 082 | mad_outlier_detection | 중앙값과 MAD를 사용해 극단값에 강한 단변량 이상치를 탐지합니다. | `examples/ex082_mad_outlier_detection.py` |
| 083 | iqr_multi_sensor_flags | 여러 센서에 IQR 규칙을 적용하고 행별 이상 센서 수를 계산합니다. | `examples/ex083_iqr_multi_sensor_flags.py` |
| 084 | contextual_rule_anomaly | 공정 상태를 고려한 문맥적 이상을 탐지합니다. | `examples/ex084_contextual_rule_anomaly.py` |
| 085 | rolling_residual_anomaly | 이동평균 잔차로 국소적인 급변 이상을 탐지합니다. | `examples/ex085_rolling_residual_anomaly.py` |
| 086 | isolation_forest_basic | Isolation Forest로 다변량 비지도 이상 탐지를 수행합니다. | `examples/ex086_isolation_forest_basic.py` |
| 087 | isolation_forest_scores | Isolation Forest의 연속형 이상점수를 계산하고 상위 이상을 확인합니다. | `examples/ex087_isolation_forest_scores.py` |
| 088 | iforest_contamination_comparison | contamination 설정에 따른 탐지 건수와 성능 변화를 비교합니다. | `examples/ex088_iforest_contamination_comparison.py` |
| 089 | local_outlier_factor | LOF로 주변 이웃과 밀도가 다른 국소 이상을 탐지합니다. | `examples/ex089_local_outlier_factor.py` |
| 090 | lof_neighbors_comparison | LOF 이웃 수에 따른 민감도와 성능 차이를 비교합니다. | `examples/ex090_lof_neighbors_comparison.py` |
| 091 | one_class_svm | One-Class SVM으로 정상 영역의 경계를 학습합니다. | `examples/ex091_one_class_svm.py` |
| 092 | ocsvm_nu_comparison | nu 설정에 따른 One-Class SVM 이상 비율과 성능을 비교합니다. | `examples/ex092_ocsvm_nu_comparison.py` |
| 093 | robust_covariance | Robust Covariance로 다변량 타원형 정상 영역을 추정합니다. | `examples/ex093_robust_covariance.py` |
| 094 | pca_reconstruction_error | PCA 재구성 오차로 정상 저차원 구조에서 벗어난 시점을 찾습니다. | `examples/ex094_pca_reconstruction_error.py` |
| 095 | model_metric_comparison | 여러 비지도 모델의 예측 결과를 동일한 평가 지표로 비교합니다. | `examples/ex095_model_metric_comparison.py` |
| 096 | confusion_matrix_report | 이상 탐지 결과의 TP·FP·FN·TN과 주요 지표를 계산합니다. | `examples/ex096_confusion_matrix_report.py` |
| 097 | threshold_optimization | 연속형 이상점수의 임계값을 바꾸며 최적 F1 기준을 찾습니다. | `examples/ex097_threshold_optimization.py` |
| 098 | anomaly_ensemble_vote | 여러 탐지 모델의 투표로 단일 모델 의존성을 줄입니다. | `examples/ex098_anomaly_ensemble_vote.py` |
| 099 | anomaly_dashboard_data | 원본 센서와 모델별 이상점수를 하나의 대시보드 CSV로 통합합니다. | `examples/ex099_anomaly_dashboard_data.py` |
| 100 | automated_anomaly_report | 모델 성능, 이상 행, LOT별 이상률을 Excel 보고서로 자동 생성합니다. | `examples/ex100_automated_anomaly_report.py` |

## 데이터 특징
- 전체 420개 시점
- 점 이상: 일부 단일 시점 온도·압력 급변
- 집단 이상: 245~269 시점 다중 센서 동시 변화
- 문맥적 이상: purge 상태의 비정상 고 RF 전력
- 교육용 정답 라벨 true_anomaly 포함

## 실무 원칙
1. 이상 탐지 결과는 곧바로 불량 확정이 아니다.
2. 모델별 점수 방향과 임계값 의미를 확인해야 한다.
3. contamination이나 nu는 실제 이상률을 자동으로 알려주는 값이 아니다.
4. 정밀도와 재현율은 경보 비용에 맞춰 균형을 잡아야 한다.
5. 원본 데이터와 모델 버전, 스케일러, 파라미터를 함께 보관해야 한다.
