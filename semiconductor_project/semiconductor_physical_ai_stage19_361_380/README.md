# 반도체 Physical AI 하네스 엔지니어링
## 19단계: 361~380제 — 반도체 Physical AI 시스템 통합과 운영 자동화

### 실행
```bat
cd semiconductor_physical_ai_stage19_361_380
conda env create -f environment.yml
conda activate semi-physical-ai-stage19
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 361 | project_directory_validation | 운영 프로젝트 폴더와 필수 파일을 검증합니다. | `examples/ex361_project_directory_validation.py` |
| 362 | config_loader | JSON 설정을 읽고 유효성을 검증합니다. | `examples/ex362_config_loader.py` |
| 363 | structured_logging | 파일·콘솔 구조화 로그를 구성합니다. | `examples/ex363_structured_logging.py` |
| 364 | data_ingestion_pipeline | 입력 데이터 로딩과 기본 검증 파이프라인을 작성합니다. | `examples/ex364_data_ingestion_pipeline.py` |
| 365 | batch_processing | 대용량 데이터를 배치 단위로 처리합니다. | `examples/ex365_batch_processing.py` |
| 366 | data_quality_gate | 결측·범위·중복 기준으로 품질 게이트를 적용합니다. | `examples/ex366_data_quality_gate.py` |
| 367 | feature_pipeline | 운영용 특징공학 파이프라인을 구성합니다. | `examples/ex367_feature_pipeline.py` |
| 368 | model_training_pipeline | 고장 분류 모델 학습 파이프라인을 작성합니다. | `examples/ex368_model_training_pipeline.py` |
| 369 | model_versioning | 모델과 메타데이터 버전을 저장합니다. | `examples/ex369_model_versioning.py` |
| 370 | model_loading_inference | 저장 모델을 로드해 추론합니다. | `examples/ex370_model_loading_inference.py` |
| 371 | prediction_monitoring | 예측 분포와 임계값 초과 건수를 모니터링합니다. | `examples/ex371_prediction_monitoring.py` |
| 372 | data_drift_check | 학습·운영 데이터 분포 차이를 점검합니다. | `examples/ex372_data_drift_check.py` |
| 373 | model_performance_monitor | 운영 정답이 있을 때 모델 성능을 집계합니다. | `examples/ex373_model_performance_monitor.py` |
| 374 | retry_and_recovery | 실패 작업 재시도와 체크포인트 복구를 구현합니다. | `examples/ex374_retry_and_recovery.py` |
| 375 | daily_kpi_aggregation | 일별 수율·고장·사이클타임 KPI를 집계합니다. | `examples/ex375_daily_kpi_aggregation.py` |
| 376 | equipment_health_summary | 장비별 건강 상태 요약을 생성합니다. | `examples/ex376_equipment_health_summary.py` |
| 377 | operations_alert_output | 운영 경보 CSV와 우선순위를 생성합니다. | `examples/ex377_operations_alert_output.py` |
| 378 | run_manifest | 실행 이력과 산출물 manifest를 생성합니다. | `examples/ex378_run_manifest.py` |
| 379 | operations_checklist | 운영 점검 체크리스트를 자동 생성합니다. | `examples/ex379_operations_checklist.py` |
| 380 | automated_operations_report | 자동 운영 통합 Excel 보고서를 생성합니다. | `examples/ex380_automated_operations_report.py` |

## 운영 구성요소
- 설정 관리
- 구조화 로그
- 데이터 품질 게이트
- 배치 처리
- 모델 학습·버전관리·추론
- 드리프트·성능 모니터링
- 재시도·체크포인트
- KPI·경보·보고서
