# 실습 091~095 라인별 해설

## 실습 091 Decision Tree·Random Forest
1. 트리 모델은 비선형 경계와 센서 상호작용을 학습할 수 있습니다.
2. Decision Tree는 설명이 쉽지만 과적합되기 쉽습니다.
3. Random Forest는 여러 트리의 결과를 평균해 안정성을 높입니다.
4. max_depth와 min_samples_leaf로 복잡도를 제한합니다.
5. class_weight는 불량 클래스의 학습 비중을 높입니다.
6. 모델과 데이터 분할을 함께 고정해야 비교가 공정합니다.

## 실습 092 모델 비교
1. 세 모델을 같은 학습·테스트 데이터에서 비교합니다.
2. Accuracy는 불균형 데이터에서 충분하지 않습니다.
3. Average Precision은 불량 클래스 순위 품질을 평가하는 데 유용합니다.
4. ROC-AUC는 정상과 불량을 구분하는 전체 능력을 봅니다.
5. Recall과 Precision은 운영 비용에 따라 우선순위가 달라집니다.
6. 단일 지표가 아니라 여러 지표를 함께 선택 기준으로 사용합니다.

## 실습 093 확률 보정
1. 분류 모델의 확률이 실제 불량 빈도와 일치하지 않을 수 있습니다.
2. Isotonic calibration은 단조 비선형 함수를 학습합니다.
3. Brier score는 확률 예측의 평균 제곱 오차입니다.
4. Log loss는 틀린 고확신 예측에 큰 벌점을 줍니다.
5. 보정은 순위 성능보다 확률 해석성을 개선하는 목적입니다.
6. 보정 데이터가 적으면 과적합 가능성을 검토해야 합니다.

## 실습 094 Permutation Importance
1. 한 특징을 무작위로 섞어 모델 성능 변화를 측정합니다.
2. 성능이 크게 떨어지면 중요한 특징으로 봅니다.
3. 상관된 특징끼리는 중요도가 분산될 수 있습니다.
4. 테스트 데이터에서 계산해야 일반화 관점의 중요도를 볼 수 있습니다.
5. 반복 횟수로 중요도 변동성을 추정합니다.
6. 중요도는 인과관계의 증거가 아닙니다.

## 실습 095 앙상블 대시보드
1. 모델 비교 표는 후보 모델의 장단점을 보여줍니다.
2. 보정 지표는 확률의 신뢰도를 확인하게 합니다.
3. Permutation Importance는 조사 우선 특징을 보여줍니다.
4. Lot별 보정확률은 우선 검사 Lot을 찾게 합니다.
5. 고위험 Wafer 표는 검사 우선순위 후보입니다.
6. 자동 폐기나 장비 정지는 별도 승인 절차가 필요합니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_091_train_tree_models.py
python examples\example_092_compare_models.py
python examples\example_093_probability_calibration.py
python examples\example_094_permutation_importance.py
python examples\example_095_ensemble_dashboard.py

pytest -q
```
