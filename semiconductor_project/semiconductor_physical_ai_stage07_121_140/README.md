# 반도체 Physical AI 하네스 엔지니어링
## 7단계: 121~140제 — 반도체 다중 불량 유형 분류와 모델 튜닝

### 단계 목표
- normal·particle·uniformity·etch_rate 다중 클래스를 분류한다.
- 다항 Logistic Regression과 One-vs-Rest 계수를 해석한다.
- Decision Tree, Random Forest, Gradient Boosting을 비교한다.
- GridSearchCV와 RandomizedSearchCV로 하이퍼파라미터를 튜닝한다.
- macro F1·weighted F1·클래스별 지표를 구분한다.
- 예측확률 보정과 재검사 정책을 적용한다.
- 오분류 분석과 자동 Excel 보고서를 생성한다.

### 실행 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- NumPy, pandas, scikit-learn, openpyxl

### 설치 및 실행
```bat
cd semiconductor_physical_ai_stage07_121_140
conda env create -f environment.yml
conda activate semi-physical-ai-stage07
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 121 | multiclass_data_profile | 다중 불량 유형의 클래스 분포와 특징 평균을 확인합니다. | `examples/ex121_multiclass_data_profile.py` |
| 122 | label_encoding | 문자열 불량 유형을 정수 라벨로 변환하고 역변환 방법을 익힙니다. | `examples/ex122_label_encoding.py` |
| 123 | multiclass_stratified_split | 다중 클래스 비율을 유지하는 층화 분할을 수행합니다. | `examples/ex123_multiclass_stratified_split.py` |
| 124 | multinomial_logistic_regression | 다항 Logistic Regression으로 기본 다중 클래스 모델을 학습합니다. | `examples/ex124_multinomial_logistic_regression.py` |
| 125 | one_vs_rest_coefficients | One-vs-Rest Logistic Regression의 클래스별 계수를 해석합니다. | `examples/ex125_one_vs_rest_coefficients.py` |
| 126 | multiclass_decision_tree | Decision Tree로 다중 불량 유형의 비선형 분기 규칙을 학습합니다. | `examples/ex126_multiclass_decision_tree.py` |
| 127 | multiclass_random_forest | Random Forest로 안정적인 다중 불량 유형 분류를 수행합니다. | `examples/ex127_multiclass_random_forest.py` |
| 128 | random_forest_feature_importance | Random Forest 특징 중요도를 전체 모델과 클래스 해석에 활용합니다. | `examples/ex128_random_forest_feature_importance.py` |
| 129 | hist_gradient_boosting | HistGradientBoostingClassifier로 비선형 다중 클래스 분류를 수행합니다. | `examples/ex129_hist_gradient_boosting.py` |
| 130 | model_comparison | 여러 다중 클래스 모델을 같은 지표로 비교합니다. | `examples/ex130_model_comparison.py` |
| 131 | grid_search_random_forest | GridSearchCV로 Random Forest 하이퍼파라미터를 탐색합니다. | `examples/ex131_grid_search_random_forest.py` |
| 132 | randomized_search_gradient_boosting | RandomizedSearchCV로 Gradient Boosting 설정을 효율적으로 탐색합니다. | `examples/ex132_randomized_search_gradient_boosting.py` |
| 133 | stratified_cross_validation | StratifiedKFold로 다중 클래스 모델 성능의 변동성을 평가합니다. | `examples/ex133_stratified_cross_validation.py` |
| 134 | classwise_metrics | 클래스별 precision·recall·F1과 support를 표 형태로 저장합니다. | `examples/ex134_classwise_metrics.py` |
| 135 | confusion_matrix_table | 혼동행렬을 라벨이 있는 표로 만들어 오분류 방향을 분석합니다. | `examples/ex135_confusion_matrix_table.py` |
| 136 | probability_calibration | CalibratedClassifierCV로 다중 클래스 예측확률을 보정합니다. | `examples/ex136_probability_calibration.py` |
| 137 | low_confidence_review | 최대 예측확률이 낮은 행을 자동 판정하지 않고 재검사 대상으로 분리합니다. | `examples/ex137_low_confidence_review.py` |
| 138 | misclassification_analysis | 오분류 행을 실제·예측 클래스 쌍별로 집계합니다. | `examples/ex138_misclassification_analysis.py` |
| 139 | multiclass_prediction_output | 클래스별 확률을 포함한 현업 전달용 예측 파일을 생성합니다. | `examples/ex139_multiclass_prediction_output.py` |
| 140 | automated_multiclass_report | 모델 비교, 클래스별 지표, 혼동행렬, 예측, 오분류를 Excel 보고서로 자동 생성합니다. | `examples/ex140_automated_multiclass_report.py` |

## 데이터 특징
- 전체 1,200개 공정 기록
- 40개 LOT
- 4개 클래스: normal, particle, uniformity, etch_rate
- 3개 레시피와 3개 챔버
- 클래스별 원인이 다르게 나타나도록 센서 패턴 구성

## 실무 원칙
1. 전체 정확도보다 희소 불량 클래스의 재현율을 함께 확인한다.
2. macro F1은 각 클래스를 동일하게 중요하게 본다.
3. weighted F1은 데이터가 많은 클래스의 영향을 더 크게 받는다.
4. 낮은 예측확률은 자동 판정보다 재검사 대상으로 분리할 수 있다.
5. 튜닝 결과는 별도 평가 데이터에서 다시 검증해야 한다.
