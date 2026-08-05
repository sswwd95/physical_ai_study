# 반도체 Physical AI 하네스 엔지니어링
## 8단계: 141~160제 — 반도체 수율 예측을 위한 회귀분석 기초

### 단계 목표
- 수율 예측용 특징과 목표값을 분리한다.
- Linear Regression과 정규화 회귀를 적용한다.
- Decision Tree, Random Forest, Gradient Boosting 회귀를 비교한다.
- MAE, RMSE, R²를 구분한다.
- 잔차와 저수율 구간 오차를 분석한다.
- 교차검증, GridSearchCV, 예측구간을 적용한다.
- 현업 전달용 예측 파일과 자동 보고서를 생성한다.

### 실행 환경
- Windows 10
- Anaconda 또는 Miniconda
- Python 3.11
- NumPy, pandas, scikit-learn, openpyxl

### 설치 및 실행
```bat
cd semiconductor_physical_ai_stage08_141_160
conda env create -f environment.yml
conda activate semi-physical-ai-stage08
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 141 | yield_data_profile | 수율 분포와 공정 변수의 기본 통계를 확인합니다. | `examples/ex141_yield_data_profile.py` |
| 142 | feature_target_split | 수율 예측 입력 특징 X와 목표 y를 분리합니다. | `examples/ex142_feature_target_split.py` |
| 143 | regression_train_test_split | 학습·평가 데이터로 분할하고 수율 분포를 비교합니다. | `examples/ex143_regression_train_test_split.py` |
| 144 | linear_regression_basic | 전처리 파이프라인과 Linear Regression으로 첫 수율 예측 모델을 학습합니다. | `examples/ex144_linear_regression_basic.py` |
| 145 | linear_coefficients | 선형 회귀 계수로 수율에 영향을 주는 공정 변수를 해석합니다. | `examples/ex145_linear_coefficients.py` |
| 146 | ridge_regression | Ridge 정규화로 다중공선성과 과적합을 완화합니다. | `examples/ex146_ridge_regression.py` |
| 147 | lasso_regression | Lasso 정규화로 중요하지 않은 특징의 계수를 0에 가깝게 만듭니다. | `examples/ex147_lasso_regression.py` |
| 148 | elastic_net_regression | Elastic Net으로 Ridge와 Lasso의 특성을 결합합니다. | `examples/ex148_elastic_net_regression.py` |
| 149 | decision_tree_regressor | Decision Tree Regressor로 비선형 수율 관계를 학습합니다. | `examples/ex149_decision_tree_regressor.py` |
| 150 | random_forest_regressor | Random Forest Regressor로 여러 트리의 예측을 결합합니다. | `examples/ex150_random_forest_regressor.py` |
| 151 | random_forest_importance | Random Forest 특징 중요도로 수율 영향 변수를 확인합니다. | `examples/ex151_random_forest_importance.py` |
| 152 | gradient_boosting_regressor | Gradient Boosting Regressor로 잔차를 순차적으로 개선합니다. | `examples/ex152_gradient_boosting_regressor.py` |
| 153 | regression_model_comparison | 여러 회귀 모델을 동일한 지표로 비교합니다. | `examples/ex153_regression_model_comparison.py` |
| 154 | residual_analysis | 예측 잔차의 평균·표준편차·극단값을 분석합니다. | `examples/ex154_residual_analysis.py` |
| 155 | low_yield_segment_error | 저수율 구간에서 모델 오차를 별도로 평가합니다. | `examples/ex155_low_yield_segment_error.py` |
| 156 | cross_validation_regression | 교차검증으로 회귀 성능의 변동성을 평가합니다. | `examples/ex156_cross_validation_regression.py` |
| 157 | grid_search_random_forest | GridSearchCV로 Random Forest 회귀 파라미터를 튜닝합니다. | `examples/ex157_grid_search_random_forest.py` |
| 158 | prediction_interval_bootstrap | 부트스트랩 모델 앙상블로 간단한 예측구간을 계산합니다. | `examples/ex158_prediction_interval_bootstrap.py` |
| 159 | yield_prediction_output | 실제 수율·예측 수율·오차·저수율 경보를 포함한 현업 전달 파일을 만듭니다. | `examples/ex159_yield_prediction_output.py` |
| 160 | automated_yield_report | 모델 비교, 잔차, 예측, 특징 중요도를 Excel 보고서로 자동 생성합니다. | `examples/ex160_automated_yield_report.py` |

## 데이터 특징
- 전체 1,000개 공정 기록
- 100개 LOT
- 3개 레시피와 3개 챔버
- 평균·변동성·입자·정지시간·정비경과시간 특징
- 목표값: yield_percent
- 교육용 수율 범위: 약 75~99.8%

## 실무 원칙
1. 수율 계산 기준과 검사 시점을 명확히 한다.
2. 평균 오차와 저수율 구간 오차를 함께 평가한다.
3. R²가 높아도 특정 LOT에서 큰 오차가 발생할 수 있다.
4. 예측값만 제공하지 말고 불확실성 또는 예측구간을 함께 제공한다.
5. 회귀 모델은 공정 조건 추천 전에 별도 안전 검증이 필요하다.
