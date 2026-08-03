# 실습 021~040 Antigravity 하네스 프롬프트

## 실습 021 — schema_validation
```text
반도체 센서 CSV의 필수 컬럼 9개가 모두 존재하는지 검사하는 Python 예제를 작성하라.
누락 컬럼, 예상하지 않은 컬럼, 현재 컬럼 순서를 출력하고 검사 결과를 PASS/FAIL로 표시하라.
원본 파일은 수정하지 말고 한국어 주석을 사용하라.
```

## 실습 022 — dtype_normalization
```text
timestamp는 datetime, 연속형 센서는 float, particle_count는 정수,
lot_id와 process_state는 category로 변환하라. 변환 전후 dtypes를 출력하고
정규화된 CSV를 저장하라.
```

## 실습 023 — unit_conversion
```text
온도 °C를 K로, 압력 Pa를 kPa로, 진동 g를 m/s²로 변환하는 파생 컬럼을 추가하라.
원본 컬럼을 유지하고 변환 공식을 주석으로 설명하며 결과를 CSV로 저장하라.
```

## 실습 024 — allowed_range_check
```text
센서별 허용 범위를 딕셔너리로 정의하라.
온도 65~80°C, 압력 15~22Pa, RF 780~920W, 가스 105~135sccm,
진동 0~0.25g, 입자 수 0~40으로 검사하라.
각 센서별 범위 위반 건수와 전체 품질 플래그를 출력하고 CSV로 저장하라.
```

## 실습 025 — inject_quality_errors
```text
원본 센서 데이터를 복사하여 품질 오류 연습용 CSV를 생성하라.
압력 결측 4건, RF 전력 결측 3건, 중복 행 2건, timestamp 역순 1건,
잘못된 process_state 값 unknown 2건을 삽입하라.
원본은 수정하지 말고 오류 삽입 내역을 출력하라.
```

## 실습 026 — missing_value_profile
```text
sensor_data_with_quality_errors.csv를 읽고 컬럼별 결측 개수와 결측 비율을 계산하라.
결측 비율이 높은 순으로 정렬하고 quality_missing_profile.csv로 저장하라.
파일이 없으면 실습 025를 먼저 실행하라는 메시지를 표시하라.
```

## 실습 027 — time_interpolation
```text
오류 연습 데이터를 timestamp 순서로 정렬하고 chamber_pressure_pa와 rf_power_w의
결측값을 시간 기반 선형보간으로 채워라. 보간 전후 결측 개수와 수정된 행을 출력하고
새 CSV로 저장하라.
```

## 실습 028 — duplicate_key_check
```text
오류 연습 데이터에서 완전 중복과 timestamp+lot_id 복합키 중복을 각각 검사하라.
중복 행을 모두 출력하고 별도 CSV로 저장하라.
```

## 실습 029 — remove_duplicates_with_audit
```text
오류 연습 데이터에서 완전 중복 행을 제거하라.
제거되는 행은 duplicate_audit.csv에, 정제 데이터는 cleaned_no_duplicates.csv에 저장하라.
처리 전후 행 수와 제거 수를 출력하라.
```

## 실습 030 — timestamp_monotonicity
```text
오류 연습 데이터의 timestamp를 datetime으로 변환하라.
원래 행 순서에서 시간이 이전 행보다 작거나 같은 위치를 찾고
timestamp_monotonic 플래그와 시간 차이 초를 계산하라.
문제 행을 출력하고 CSV로 저장하라.
```

## 실습 031 — sampling_interval_check
```text
timestamp를 정렬한 뒤 인접 행 시간 차이를 계산하라.
예상 주기는 1초이며 1초가 아닌 간격을 gap_type으로 분류하라.
0초 이하는 duplicate_or_reverse, 1초 초과는 missing_or_delay로 표시하라.
```

## 실습 032 — category_validation
```text
lot_id 허용값은 LOT-A, LOT-B, LOT-C이고 process_state 허용값은
stabilize, process, purge이다. 허용되지 않은 값을 컬럼별로 찾고
invalid_category 플래그를 생성하여 문제 행을 저장하라.
```

## 실습 033 — iqr_outlier_flags
```text
온도, 압력, RF 전력, 가스 유량, 진동에 대해 Q1, Q3, IQR을 계산하고
1.5*IQR 바깥 값을 이상 후보로 표시하라. 컬럼별 이상 후보 수와 경계값을 출력하고
플래그가 포함된 CSV를 저장하라.
```

## 실습 034 — winsorize_outliers
```text
온도와 압력 컬럼의 1% 및 99% 분위수를 구하고 clip으로 경계 밖 값을 제한하라.
원본 컬럼은 유지하고 _winsorized 컬럼을 추가하라.
변경된 행 수와 전후 최솟값·최댓값을 출력하라.
```

## 실습 035 — lot_consistency_check
```text
각 lot_id별 행 수, 첫 시각, 마지막 시각, process_state 고유값을 요약하라.
LOT별 행 수가 100이 아니면 lot_count_error를 True로 표시하라.
결과를 CSV로 저장하라.
```

## 실습 036 — state_transition_check
```text
허용 전이는 stabilize→stabilize/process, process→process/purge,
purge→purge/stabilize로 정의하라. 현재 행과 다음 행의 process_state를 비교해
허용되지 않은 전이를 찾고 CSV로 저장하라.
```

## 실습 037 — cross_sensor_rule_check
```text
process_state가 process인데 RF 전력이 800W 미만이거나 가스 유량이 110sccm 미만이면
cross_sensor_violation으로 표시하라. 또한 purge 상태에서 RF 전력이 900W를 넘으면
위반으로 표시하라. 규칙별 위반 건수와 문제 행을 저장하라.
```

## 실습 038 — quality_score
```text
오류 연습 데이터에 대해 결측, 범주 오류, 범위 위반, 중복 여부를 검사하라.
각 오류는 25점 감점하고 100점에서 시작하는 quality_score를 계산하라.
90 이상 A, 75 이상 B, 50 이상 C, 나머지는 D로 등급화하여 저장하라.
```

## 실습 039 — quality_report
```text
오류 연습 데이터의 행 수, 컬럼 수, 결측 셀 수, 완전 중복 수,
잘못된 상태 수, 범위 위반 행 수를 한 행의 품질 요약표로 작성하라.
컬럼별 결측표와 함께 Excel의 summary, missing_by_column 시트로 저장하라.
```

## 실습 040 — cleaning_pipeline
```text
오류 연습 데이터를 입력으로 받는 clean_sensor_data 함수를 작성하라.
필수 컬럼 검사, timestamp 변환, 정렬, 완전 중복 제거, 숫자형 변환,
압력과 RF 결측 시간 보간, 잘못된 process_state를 NaN으로 변경,
품질 플래그 추가, 정제 CSV와 감사 요약 CSV 저장을 수행하라.
각 단계의 처리 건수를 audit 딕셔너리에 기록하라.
```
