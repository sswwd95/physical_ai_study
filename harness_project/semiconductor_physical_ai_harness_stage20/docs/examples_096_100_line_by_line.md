# 실습 096~100 라인별 해설

## 실습 096 불균형 진단
1. 정상과 불량 클래스 개수를 먼저 확인합니다.
2. 불량률이 낮으면 Accuracy가 높아도 불량 탐지가 약할 수 있습니다.
3. 다수·소수 클래스 비율은 불균형 정도를 보여줍니다.
4. Precision, Recall, Average Precision을 함께 봐야 합니다.
5. 클래스 분포는 학습·검증·테스트 구간별로 확인합니다.
6. 시간 변화로 불량률이 달라지는지도 점검합니다.

## 실습 097 Under·Over Sampling
1. Under Sampling은 정상 데이터 일부를 제거합니다.
2. 학습은 빨라지지만 정상 패턴 정보를 잃을 수 있습니다.
3. Over Sampling은 불량 데이터를 복제합니다.
4. 정보 손실은 적지만 과적합 가능성이 있습니다.
5. 샘플링은 학습 데이터에만 적용합니다.
6. 테스트 데이터 분포는 실제 운영 분포를 유지해야 합니다.

## 실습 098 SMOTE 유사 합성
1. 불량 샘플의 가까운 이웃을 찾습니다.
2. 두 샘플 사이를 임의 비율로 보간합니다.
3. 숫자 센서는 새로운 중간값을 만듭니다.
4. 범주형 조건은 기준 샘플 값을 유지합니다.
5. 본 코드는 교육용 단순 구현입니다.
6. 실제 프로젝트에서는 검증된 SMOTE 라이브러리와 데이터 의미를 함께 검토합니다.

## 실습 099 비용 민감 학습
1. class_weight로 불량 오류에 더 큰 학습 비용을 부여합니다.
2. 가중치가 커지면 Recall이 높아질 수 있습니다.
3. 동시에 False Positive도 증가할 수 있습니다.
4. 여러 가중치에서 모델 성능과 운영 비용을 비교합니다.
5. FN 비용을 FP보다 5배 크게 둔 교육용 비용함수를 사용합니다.
6. 실제 비용은 폐기·재검사·고객 불량 비용으로 다시 정의합니다.

## 실습 100 통합 미니 프로젝트
1. 불균형 진단으로 문제 구조를 파악합니다.
2. 비용 민감 모델 중 운영 비용이 낮은 모델을 선택합니다.
3. 테스트 Wafer의 불량확률을 계산합니다.
4. Lot별 실제·예측 불량률을 비교합니다.
5. 고위험 Wafer를 검사 우선순위 후보로 제공합니다.
6. 001~100의 데이터 품질·SPC·공정 능력·불량 예측 흐름을 하나로 연결합니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_096_class_imbalance_diagnostics.py
python examples\example_097_under_over_sampling.py
python examples\example_098_simple_smote_like.py
python examples\example_099_cost_sensitive_comparison.py
python examples\example_100_integrated_mini_project.py

pytest -q
```
