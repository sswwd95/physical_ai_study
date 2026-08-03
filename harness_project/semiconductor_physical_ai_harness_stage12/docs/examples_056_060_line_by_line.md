# 실습 056~060 라인별 해설

## 실습 056 EWMA 관리도
1. EWMA는 현재값과 이전 EWMA를 가중 평균합니다.
2. lambda가 작을수록 더 많은 과거 정보를 기억합니다.
3. 작은 지속 이동에 개별값 관리도보다 민감할 수 있습니다.
4. 초기에는 EWMA 분산이 작아 관리한계가 좁습니다.
5. 시간이 지나면 관리한계가 정상 상태 값에 접근합니다.
6. lambda와 L은 탐지 속도와 오경보율을 함께 고려해 결정합니다.

## 실습 057 CUSUM 관리도
1. CUSUM은 기준 평균에서 벗어난 편차를 누적합니다.
2. 양의 CUSUM은 상승 이동을, 음의 CUSUM은 하강 이동을 찾습니다.
3. k는 무시할 작은 편차 크기입니다.
4. h는 경보를 발생시키는 누적 한계입니다.
5. 지속적인 작은 편차가 누적되면 빠르게 경보할 수 있습니다.
6. 공정이 정상으로 돌아오면 누적값 초기화 정책도 검토해야 합니다.

## 실습 058 작은 평균 이동 탐지
1. 합성 데이터의 이동 시작 시각을 알고 있으므로 탐지 지연을 계산할 수 있습니다.
2. 첫 경보 시각과 이동 시작 시각의 차이가 탐지 지연입니다.
3. 지연이 짧을수록 빠른 탐지입니다.
4. 경보가 없으면 탐지 실패로 기록합니다.
5. 합성 평가에서는 정답 구간을 알 수 있지만 실제 현장에서는 원인 검증이 필요합니다.
6. 여러 크기의 이동으로 반복 평가해야 합니다.

## 실습 059 관리도 성능 비교
1. 작은 이동과 큰 이동을 따로 평가합니다.
2. 탐지 지연만 비교하면 과민한 관리도가 유리해 보일 수 있습니다.
3. 기준 구간 오경보율을 반드시 함께 봅니다.
4. EWMA와 CUSUM의 파라미터에 따라 결과가 달라집니다.
5. 공정 위험도에 따라 빠른 탐지와 오경보 비용의 균형을 정합니다.
6. 실제 평가는 여러 Lot과 다양한 Recipe에서 수행해야 합니다.

## 실습 060 통합 공정 경보
1. 개별값 관리도는 큰 단일 이상에 민감합니다.
2. EWMA와 CUSUM은 지속적인 작은 이동에 민감합니다.
3. 서로 다른 방법의 동시 경보 수를 투표값으로 사용합니다.
4. 한 방법만 경보하면 WATCH, 두 방법이면 WARNING으로 높입니다.
5. 세 방법 모두 경보하면 CRITICAL로 분류합니다.
6. 교육용 등급이며 실제 자동 정지나 레시피 변경에는 사용하지 않습니다.

## 실행 순서

```bat
conda env create -f environment.yml
conda activate semi-physical-ai

python examples\example_056_ewma_control_chart.py
python examples\example_057_cusum_control_chart.py
python examples\example_058_small_shift_detection.py
python examples\example_059_compare_control_chart_performance.py
python examples\example_060_integrated_process_alerts.py

pytest -q
```
