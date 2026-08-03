# Antigravity 하네스 프롬프트 모음

## 실습 001 — generate_sensor_data
```text
Windows 10과 Anaconda에서 실행할 초보자용 Python 예제를 작성하라.
반도체 식각 장비의 300개 시점 데이터를 합성하라.
컬럼은 timestamp, lot_id, chamber_temp_c, chamber_pressure_pa, rf_power_w,
gas_flow_sccm, vibration_g, particle_count, process_state로 구성하라.
정상 구간과 일부 이상 구간을 포함하고 data/semiconductor_sensor_data.csv에 저장하라.
재현 가능하도록 난수 시드를 고정하고 각 처리 단계에 한국어 주석을 넣어라.
```

## 실습 002 — load_and_inspect
```text
반도체 센서 CSV를 pandas로 읽고 shape, columns, dtypes, head를 출력하는
초보자용 점검 스크립트를 작성하라. 파일이 없으면 실습 001을 먼저 실행하라는
친절한 오류 메시지를 표시하라.
```

## 실습 003 — select_sensor_columns
```text
pandas DataFrame에서 timestamp, chamber_temp_c, chamber_pressure_pa,
rf_power_w만 선택하여 출력하고 outputs/ex003_selected_columns.csv로 저장하는
초보자용 예제를 작성하라.
```

## 실습 004 — basic_statistics
```text
온도, 압력, RF 전력, 가스 유량, 진동 센서에 대해 count, mean, std,
min, max를 계산하고 보기 좋게 출력하는 pandas 예제를 작성하라.
```

## 실습 005 — filter_temperature
```text
chamber_temp_c가 75도 이상인 행만 필터링하고 시점, LOT, 온도, 압력을
출력하는 초보자용 pandas 예제를 작성하라. 필터링된 행 개수도 출력하라.
```

## 실습 006 — create_derived_feature
```text
RF 전력과 가스 유량을 이용해 process_load = rf_power_w / gas_flow_sccm
파생변수를 만들고 상위 10개 행을 출력하라. 0으로 나누는 문제를 방지하라.
```

## 실습 007 — group_by_lot
```text
lot_id로 그룹화하여 온도, 압력, 입자 수의 평균과 표준편차를 계산하는
pandas groupby 예제를 작성하라. 다중 컬럼 이름은 읽기 쉬운 단일 이름으로 바꿔라.
```

## 실습 008 — group_by_process_state
```text
process_state별 chamber_temp_c, chamber_pressure_pa, vibration_g의
평균을 계산하고 가장 진동이 큰 상태를 찾는 pandas 예제를 작성하라.
```

## 실습 009 — handle_missing_values
```text
원본 센서 데이터의 일부 압력값을 의도적으로 NaN으로 바꾸고 결측 개수를
확인한 뒤 중앙값으로 채우는 예제를 작성하라. 원본 CSV는 수정하지 말고 결과를
outputs/ex009_filled_missing.csv에 저장하라.
```

## 실습 010 — detect_duplicate_rows
```text
센서 데이터의 앞 3개 행을 복사해 중복 데이터를 만든 뒤 duplicated로 찾고
drop_duplicates로 제거하는 예제를 작성하라. 처리 전후 행 수를 출력하라.
```

## 실습 011 — sort_by_particle_count
```text
particle_count를 내림차순 정렬하여 상위 15개 시점의 timestamp, lot_id,
particle_count, chamber_temp_c를 출력하고 CSV로 저장하라.
```

## 실습 012 — time_range_filter
```text
timestamp를 datetime으로 읽고 09:02:00부터 09:02:30까지의 행만 선택하여
시간, 온도, 압력, 진동을 출력하는 예제를 작성하라.
```

## 실습 013 — rolling_average
```text
온도 센서에 10개 시점 이동평균 컬럼 temp_ma10을 추가하라.
원본 온도와 이동평균의 마지막 20행을 출력하고 CSV로 저장하라.
```

## 실습 014 — simple_threshold_alarm
```text
온도 75도 이상 또는 압력 20Pa 이상 또는 진동 0.15g 이상이면 alarm을 1로,
아니면 0으로 설정하라. 경보 건수와 경보 행의 주요 컬럼을 출력하라.
```

## 실습 015 — zscore_temperature
```text
scipy.stats.zscore를 사용해 chamber_temp_c의 z-score를 계산하고 절댓값이
3 이상인 행을 이상 후보로 출력하라. z-score 컬럼을 포함하라.
```

## 실습 016 — sensor_correlation
```text
온도, 압력, RF 전력, 가스 유량, 진동, 입자 수의 Pearson 상관계수 행렬을
계산하고 소수 셋째 자리로 출력하라. CSV로도 저장하라.
```

## 실습 017 — plot_temperature_trend
```text
timestamp와 chamber_temp_c를 이용해 12x5 크기의 선 그래프를 작성하라.
75도 기준선을 표시하고 제목, 축 이름, 범례, 격자를 추가한 뒤 PNG로 저장하라.
화면 표시 없이 저장 가능하게 작성하라.
```

## 실습 018 — plot_sensor_histogram
```text
chamber_pressure_pa의 히스토그램을 25개 구간으로 작성하고 평균선을 표시하라.
제목, 축 이름, 범례를 넣고 PNG로 저장하라.
```

## 실습 019 — bayesian_temperature_mean
```text
PyMC를 사용해 chamber_temp_c의 평균을 추정하는 정규모형을 작성하라.
mu는 Normal(72, 5), sigma는 HalfNormal(5) 사전분포를 사용하고
draws=1000, tune=1000, chains=2, random_seed=42로 샘플링하라.
arviz.summary로 mu와 sigma의 평균, 표준편차, HDI를 출력하고 CSV로 저장하라.
```

## 실습 020 — bayesian_alarm_probability
```text
온도 75도 이상 또는 압력 20Pa 이상 또는 진동 0.15g 이상을 경보로 정의하라.
경보 횟수와 전체 횟수를 사용해 Beta(1,1) 사전분포와 Binomial 우도를 가진
PyMC 모형을 작성하라. 경보확률 p의 사후요약과 P(p > 0.05)를 계산해 출력하라.
```
