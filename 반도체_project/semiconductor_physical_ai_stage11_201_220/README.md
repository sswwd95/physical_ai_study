# 반도체 Physical AI 하네스 엔지니어링
## 11단계: 201~220제 — 반도체 장비 상태 진단과 고장 분류

### 실행
```bat
cd semiconductor_physical_ai_stage11_201_220
conda env create -f environment.yml
conda activate semi-physical-ai-stage11
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 201 | fault_data_profile | 고장 유형과 센서 분포를 확인합니다. | `examples/ex201_fault_data_profile.py` |
| 202 | binary_fault_label | 정상·고장 이진 라벨을 만듭니다. | `examples/ex202_binary_fault_label.py` |
| 203 | multiclass_split | 다중 고장 유형을 층화 분할합니다. | `examples/ex203_multiclass_split.py` |
| 204 | sensor_feature_engineering | 센서 비율과 복합 특징을 생성합니다. | `examples/ex204_sensor_feature_engineering.py` |
| 205 | logistic_fault_classifier | Logistic Regression으로 정상·고장을 분류합니다. | `examples/ex205_logistic_fault_classifier.py` |
| 206 | multiclass_logistic | 다항 Logistic Regression으로 고장 유형을 분류합니다. | `examples/ex206_multiclass_logistic.py` |
| 207 | decision_tree_faults | Decision Tree로 고장 규칙을 학습합니다. | `examples/ex207_decision_tree_faults.py` |
| 208 | random_forest_faults | Random Forest로 다중 고장을 분류합니다. | `examples/ex208_random_forest_faults.py` |
| 209 | feature_importance | Random Forest 특징 중요도를 계산합니다. | `examples/ex209_feature_importance.py` |
| 210 | gradient_boosting_faults | Gradient Boosting으로 고장 유형을 분류합니다. | `examples/ex210_gradient_boosting_faults.py` |
| 211 | class_weight_comparison | 클래스 가중치 효과를 비교합니다. | `examples/ex211_class_weight_comparison.py` |
| 212 | threshold_review_policy | 고장확률 임계값과 재검사 정책을 비교합니다. | `examples/ex212_threshold_review_policy.py` |
| 213 | confusion_matrix_analysis | 혼동행렬로 고장 유형별 오분류를 분석합니다. | `examples/ex213_confusion_matrix_analysis.py` |
| 214 | classwise_metrics | 클래스별 precision·recall·F1을 저장합니다. | `examples/ex214_classwise_metrics.py` |
| 215 | equipment_group_validation | 장비 단위 그룹 분할을 적용합니다. | `examples/ex215_equipment_group_validation.py` |
| 216 | cross_validation_faults | 층화 교차검증으로 성능 변동을 평가합니다. | `examples/ex216_cross_validation_faults.py` |
| 217 | model_comparison | 여러 고장 분류 모델을 비교합니다. | `examples/ex217_model_comparison.py` |
| 218 | low_confidence_faults | 낮은 확률 예측을 재검사 대상으로 분리합니다. | `examples/ex218_low_confidence_faults.py` |
| 219 | fault_prediction_output | 현업 전달용 고장 예측 CSV를 생성합니다. | `examples/ex219_fault_prediction_output.py` |
| 220 | automated_fault_report | 자동 장비 고장 진단 Excel 보고서를 생성합니다. | `examples/ex220_automated_fault_report.py` |

## 고장 유형
- normal
- bearing_wear
- vacuum_leak
- overheating
- contamination

## 주요 입력
온도, 압력, 진동 RMS·Peak, 모터전류, 펌프속도, 가스유량, 입자수,
정비경과시간, 운전모드, 장비 ID
