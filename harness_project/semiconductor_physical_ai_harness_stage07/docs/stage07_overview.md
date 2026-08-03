# 7단계 개요: 단위·시간축·중복·드리프트 품질 관리

| 실습 | 주제 | 주요 출력 |
|---:|---|---|
|031|센서 단위 계약 검증|`sensor_unit_validation.csv`|
|032|표준 단위 변환|`equipment_sensor_log_converted.csv`|
|033|시간 간격 이상 탐지|`time_interval_anomalies.csv`|
|034|중복 timestamp 통합|정리 데이터·중복 리포트|
|035|센서 드리프트 기초 탐지|`sensor_drift_summary.csv`|

## 실무 핵심
단위와 시간축 오류는 값 자체가 정상처럼 보여도 분석 전체를 무너뜨릴 수 있습니다. 센서 데이터는 값, 단위, timestamp, 샘플링 간격, Lot·Recipe 문맥을 하나의 데이터 계약으로 관리해야 합니다.
