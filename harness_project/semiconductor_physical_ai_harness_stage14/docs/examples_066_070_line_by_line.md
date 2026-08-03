# 실습 066~070 라인별 해설

## 실습 066 PCA 기준 모델
1. 기준 구간은 정상 다중 센서 패턴을 학습하는 데이터입니다.
2. 센서 단위가 다르므로 PCA 전에 표준화합니다.
3. PCA는 센서 상관관계를 적은 수의 축으로 요약합니다.
4. 누적 설명분산 95%는 대부분의 정상 변동을 보존하는 교육용 기준입니다.
5. scaler와 PCA를 함께 저장해야 운영 데이터에 같은 변환을 적용할 수 있습니다.
6. 기준 구간이 오염되면 PCA 정상 공간도 왜곡됩니다.

## 실습 067 주성분 점수 모니터링
1. PC 점수는 각 샘플이 주성분 축에서 어디에 위치하는지 나타냅니다.
2. 정상 기준 구간의 점수 평균과 표준편차를 계산합니다.
3. 평균±3σ를 교육용 경보선으로 사용합니다.
4. PC 점수 경보는 정상 상관 구조 안에서 큰 방향 이동을 찾습니다.
5. 여러 PC 중 하나라도 경보하면 any_pc_score_alert가 참입니다.
6. PC 축은 원시 센서보다 해석이 어려울 수 있습니다.

## 실습 068 SPE/Q 통계량
1. PCA는 정상 변동을 주성분 공간으로 압축합니다.
2. inverse_transform은 PCA 정보로 원래 표준화 센서를 복원합니다.
3. 원본과 복원값의 차이가 PCA가 설명하지 못한 잔차입니다.
4. 잔차 제곱합이 SPE 또는 Q 통계량입니다.
5. SPE가 크면 정상 상관 구조에서 벗어난 새로운 패턴일 수 있습니다.
6. 기준 구간 99% 분위수는 교육용 경험 임계값입니다.

## 실습 069 센서 기여도
1. 센서별 잔차 제곱은 SPE 전체값에 대한 기여도를 나타냅니다.
2. 가장 큰 기여 센서는 조사 우선순위 후보입니다.
3. 기여도가 높다고 해당 센서가 반드시 고장 원인은 아닙니다.
4. 공통 원인 때문에 여러 센서 기여도가 함께 커질 수 있습니다.
5. Lot·Recipe·장비 이벤트와 함께 확인해야 합니다.
6. 기여도 표는 유지보수와 원인 분석의 출발점입니다.

## 실습 070 PCA 모니터링 대시보드
1. PC 점수 경보는 정상 주성분 방향의 큰 이동을 보여줍니다.
2. SPE/Q 경보는 정상 모델이 설명하지 못하는 패턴을 보여줍니다.
3. 두 경보가 동시에 발생하면 우선순위를 높일 수 있습니다.
4. Lot별 요약은 이상이 집중된 생산 단위를 보여줍니다.
5. 센서 기여도 집계는 반복되는 이상 패턴을 찾게 합니다.
6. HTML과 JSON을 함께 제공해 사람과 시스템이 모두 사용할 수 있습니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_066_train_pca_baseline.py
python examples\example_067_pca_score_monitoring.py
python examples\example_068_spe_q_statistic.py
python examples\example_069_pca_sensor_contributions.py
python examples\example_070_pca_monitoring_dashboard.py

pytest -q
```
