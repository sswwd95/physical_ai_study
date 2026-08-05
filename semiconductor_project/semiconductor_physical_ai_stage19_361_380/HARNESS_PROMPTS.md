## 실습 361 — project_directory_validation
```text
프로젝트 폴더·데이터·설정·로그·모델 경로 존재 여부를 검증하라.
```

## 실습 362 — config_loader
```text
JSON 설정 파일을 읽고 필수 키와 batch_size 유효성을 검증하라.
```

## 실습 363 — structured_logging
```text
콘솔과 파일에 동시에 기록하는 구조화 로그를 작성하라.
```

## 실습 364 — data_ingestion_pipeline
```text
CSV 입력 로딩·필수컬럼·빈 데이터·시간정렬 검증 함수를 작성하라.
```

## 실습 365 — batch_processing
```text
설정 batch_size로 데이터를 나누고 배치별 수율·고장수를 저장하라.
```

## 실습 366 — data_quality_gate
```text
결측·중복·센서범위·수율범위 품질 게이트를 작성하라.
```

## 실습 367 — feature_pipeline
```text
운영용 센서 편차·위험·건강점수 특징을 생성하라.
```

## 실습 368 — model_training_pipeline
```text
RandomForest 고장 분류 학습 파이프라인을 작성하라.
```

## 실습 369 — model_versioning
```text
학습 모델과 버전 메타데이터를 joblib·JSON으로 저장하라.
```

## 실습 370 — model_loading_inference
```text
최신 모델을 로드해 고장 예측과 확률을 계산하라.
```

## 실습 371 — prediction_monitoring
```text
예측확률 평균·95분위·0.7·0.9 초과 건수를 집계하라.
```

## 실습 372 — data_drift_check
```text
학습구간과 최신구간의 평균·표준편차 드리프트를 점검하라.
```

## 실습 373 — model_performance_monitor
```text
운영 정답 기준 accuracy·precision·recall·F1을 집계하라.
```

## 실습 374 — retry_and_recovery
```text
최대 3회 재시도와 JSON 체크포인트 복구를 구현하라.
```

## 실습 375 — daily_kpi_aggregation
```text
일별 수율·고장·사이클타임·가동비율 KPI를 집계하라.
```

## 실습 376 — equipment_health_summary
```text
장비별 수율·고장률·센서·건강등급 요약을 생성하라.
```

## 실습 377 — operations_alert_output
```text
고장·저수율·지연 경보와 우선순위를 CSV로 생성하라.
```

## 실습 378 — run_manifest
```text
실행ID·입력파일·산출물목록이 포함된 manifest를 생성하라.
```

## 실습 379 — operations_checklist
```text
운영 전 필수 점검 체크리스트를 CSV로 생성하라.
```

## 실습 380 — automated_operations_report
```text
일별KPI·장비건강·경보·데이터품질 Excel 보고서를 생성하라.
```