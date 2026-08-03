# 실습 086~090 라인별 해설

## 실습 086 로지스틱 회귀 학습
1. 시계열 순서를 유지해 과거 데이터로 학습하고 미래 데이터로 평가합니다.
2. 숫자형 센서는 중앙값으로 결측을 처리하고 표준화합니다.
3. Recipe와 Tool은 One-Hot Encoding으로 숫자 특징으로 바꿉니다.
4. class_weight='balanced'는 불량 데이터가 적을 때 클래스 가중치를 조정합니다.
5. Pipeline은 전처리와 모델을 같은 순서로 재사용합니다.
6. 모델 파일과 특징 계약을 함께 저장해야 운영 배포가 안전합니다.

## 실습 087 분류 성능 평가
1. 확률 0.5 이상을 기본 불량 예측으로 사용합니다.
2. Accuracy는 클래스 불균형에서 과대평가될 수 있습니다.
3. Precision은 불량 예측 중 실제 불량 비율입니다.
4. Recall은 실제 불량 중 탐지한 비율입니다.
5. ROC-AUC와 Average Precision은 임계값 전반의 구분 성능을 봅니다.
6. 제조 품질에서는 false negative 비용이 특히 클 수 있습니다.

## 실습 088 임계값 최적화
1. 분류 확률을 어떤 임계값에서 경보로 바꿀지 결정합니다.
2. 임계값이 낮으면 Recall은 높아지고 오경보가 늘어날 수 있습니다.
3. 임계값이 높으면 Precision은 높아지고 미탐이 늘어날 수 있습니다.
4. 교육용 비용함수는 FN에 5배 비용을 줍니다.
5. 비용이 같은 경우 F1이 높은 임계값을 선택합니다.
6. 실제 비용은 폐기, 재검사, 고객 불량 비용을 반영해야 합니다.

## 실습 089 특징 영향도
1. 로지스틱 회귀 계수는 불량 로그오즈 변화 방향을 나타냅니다.
2. 양의 계수는 불량 오즈 증가와 연관됩니다.
3. 음의 계수는 불량 오즈 감소와 연관됩니다.
4. 오즈비는 exp(계수)로 계산합니다.
5. 표준화된 숫자 특징 계수는 상대 비교에 도움이 됩니다.
6. 계수는 모델 내 연관성이지 공정 인과관계의 확정이 아닙니다.

## 실습 090 예측 대시보드
1. ROC-AUC와 Average Precision으로 전체 구분 성능을 봅니다.
2. 선택 임계값은 운영 비용 기준을 반영합니다.
3. Lot별 평균 확률과 예측 불량률은 우선 조사 Lot을 찾게 합니다.
4. 고위험 Wafer 목록은 검사 우선순위 후보입니다.
5. 특징 영향도는 공정 분석의 시작점입니다.
6. 자동 폐기나 장비 정지는 독립적인 승인 절차가 필요합니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_086_train_logistic_regression.py
python examples\example_087_evaluate_classifier.py
python examples\example_088_optimize_threshold.py
python examples\example_089_logistic_feature_effects.py
python examples\example_090_defect_prediction_dashboard.py

pytest -q
```
