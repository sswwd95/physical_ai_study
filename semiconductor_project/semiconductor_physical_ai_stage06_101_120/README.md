# 반도체 Physical AI 하네스 엔지니어링
## 6단계: 101~120제 — 반도체 불량 분류를 위한 지도학습 기초

### 단계 목표
- 분류용 특징과 목표 라벨을 분리한다.
- 층화 분할과 LOT 그룹 분할의 차이를 이해한다.
- 숫자형·범주형 전처리 파이프라인을 구성한다.
- Logistic Regression, Decision Tree, Random Forest를 학습한다.
- 클래스 불균형과 확률 임계값을 조정한다.
- 혼동행렬, ROC-AUC, PR-AUC, 교차검증으로 모델을 평가한다.
- 현업 전달용 예측 파일과 자동 보고서를 생성한다.

### 실행 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- NumPy, pandas, scikit-learn, openpyxl

### 설치 및 실행
```bat
cd semiconductor_physical_ai_stage06_101_120
conda env create -f environment.yml
conda activate semi-physical-ai-stage06
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 101 | defect_data_profile | 불량 분류 데이터의 클래스 비율과 주요 센서 분포를 확인합니다. | `examples/ex101_defect_data_profile.py` |
| 102 | feature_target_split | 입력 특징 X와 목표 라벨 y를 분리하고 사용하지 않을 식별 컬럼을 제외합니다. | `examples/ex102_feature_target_split.py` |
| 103 | stratified_train_test_split | 층화 분할로 학습·평가 데이터의 불량 비율을 유지합니다. | `examples/ex103_stratified_train_test_split.py` |
| 104 | lot_group_split | 같은 LOT가 학습과 평가에 동시에 들어가는 데이터 누수를 방지합니다. | `examples/ex104_lot_group_split.py` |
| 105 | preprocessing_pipeline | 숫자형 표준화와 범주형 One-Hot Encoding을 하나의 전처리기로 구성합니다. | `examples/ex105_preprocessing_pipeline.py` |
| 106 | logistic_regression_basic | 전처리 파이프라인과 Logistic Regression으로 첫 불량 분류 모델을 학습합니다. | `examples/ex106_logistic_regression_basic.py` |
| 107 | logistic_coefficients | Logistic Regression 계수로 센서와 불량 확률의 관계를 해석합니다. | `examples/ex107_logistic_coefficients.py` |
| 108 | decision_tree_basic | Decision Tree로 비선형 규칙 기반 불량 분류를 수행합니다. | `examples/ex108_decision_tree_basic.py` |
| 109 | tree_depth_comparison | Decision Tree 깊이에 따른 과소적합·과적합 변화를 비교합니다. | `examples/ex109_tree_depth_comparison.py` |
| 110 | random_forest_basic | Random Forest로 여러 결정트리의 예측을 결합합니다. | `examples/ex110_random_forest_basic.py` |
| 111 | random_forest_importance | Random Forest 특징 중요도로 불량 판정에 중요한 센서를 확인합니다. | `examples/ex111_random_forest_importance.py` |
| 112 | class_weight_balancing | 클래스 가중치로 희소한 불량 클래스의 재현율을 높입니다. | `examples/ex112_class_weight_balancing.py` |
| 113 | manual_oversampling | 학습 데이터에서 불량 샘플을 단순 복제해 클래스 균형을 맞춥니다. | `examples/ex113_manual_oversampling.py` |
| 114 | probability_threshold_comparison | 불량확률 임계값을 조정해 정밀도와 재현율의 균형을 비교합니다. | `examples/ex114_probability_threshold_comparison.py` |
| 115 | confusion_matrix_analysis | 혼동행렬로 정상 오탐과 불량 미탐을 구분합니다. | `examples/ex115_confusion_matrix_analysis.py` |
| 116 | roc_auc_comparison | ROC-AUC로 여러 모델의 전체 임계값 분류 능력을 비교합니다. | `examples/ex116_roc_auc_comparison.py` |
| 117 | precision_recall_auc | 불균형 데이터에 유용한 PR-AUC를 계산합니다. | `examples/ex117_precision_recall_auc.py` |
| 118 | cross_validation_f1 | 교차검증으로 한 번의 데이터 분할에 따른 성능 변동을 줄입니다. | `examples/ex118_cross_validation_f1.py` |
| 119 | defect_prediction_output | 모델 확률과 예측 결과를 원본 식별정보와 결합해 현업 전달용 파일을 만듭니다. | `examples/ex119_defect_prediction_output.py` |
| 120 | automated_classification_report | 모델별 성능, 혼동행렬, 예측 결과, 특징 중요도를 Excel 보고서로 자동 생성합니다. | `examples/ex120_automated_classification_report.py` |

## 데이터 특징
- 전체 900개 공정 기록
- 30개 LOT
- 3개 레시피와 3개 챔버
- 온도·압력·RF·가스·진동·입자·식각률·균일도 특징
- 이진 불량 라벨 `defect`
- 교육용 불량유형 `defect_type`

## 실무 원칙
1. 라벨 생성 기준과 검사 장비 신뢰도를 먼저 확인한다.
2. 같은 LOT가 학습과 평가에 동시에 들어가지 않도록 주의한다.
3. Accuracy만으로 불균형 분류를 판단하지 않는다.
4. 불량 미탐 비용과 정상 오탐 비용에 따라 임계값을 조정한다.
5. 전처리기와 모델을 하나의 Pipeline으로 저장해야 한다.
