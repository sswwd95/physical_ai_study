# 반도체 Physical AI 하네스 엔지니어링
## 20단계: 381~400제 — 종합 프로젝트와 포트폴리오 완성

### 실행
```bat
cd semiconductor_physical_ai_stage20_381_400
conda env create -f environment.yml
conda activate semi-physical-ai-stage20
python verify_environment.py
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 381 | project_charter | 종합 프로젝트 목표·범위·성과지표를 정의합니다. | `examples/ex381_project_charter.py` |
| 382 | requirements_traceability | 요구사항과 구현·검증 항목을 연결합니다. | `examples/ex382_requirements_traceability.py` |
| 383 | data_contract | 입력 데이터 컬럼·형식·품질 규칙을 정의합니다. | `examples/ex383_data_contract.py` |
| 384 | integrated_data_validation | 종합 데이터 품질 검증을 수행합니다. | `examples/ex384_integrated_data_validation.py` |
| 385 | integrated_feature_pipeline | 수율·고장·RUL 공통 특징을 생성합니다. | `examples/ex385_integrated_feature_pipeline.py` |
| 386 | yield_model_training | 수율 예측 모델을 학습·평가합니다. | `examples/ex386_yield_model_training.py` |
| 387 | fault_model_training | 고장 확률 모델을 학습·평가합니다. | `examples/ex387_fault_model_training.py` |
| 388 | rul_model_training | RUL 예측 모델을 학습·평가합니다. | `examples/ex388_rul_model_training.py` |
| 389 | model_registry | 세 모델과 메타데이터를 등록합니다. | `examples/ex389_model_registry.py` |
| 390 | integrated_inference | 수율·고장확률·RUL 통합 추론을 수행합니다. | `examples/ex390_integrated_inference.py` |
| 391 | decision_engine | 통합 예측으로 운영 행동을 결정합니다. | `examples/ex391_decision_engine.py` |
| 392 | safety_gate | 안전 게이트가 모델보다 우선하도록 검증합니다. | `examples/ex392_safety_gate.py` |
| 393 | end_to_end_pipeline | 입력부터 결과 저장까지 전체 파이프라인을 실행합니다. | `examples/ex393_end_to_end_pipeline.py` |
| 394 | integration_tests | 핵심 통합 테스트를 자동 실행합니다. | `examples/ex394_integration_tests.py` |
| 395 | kpi_scorecard | 프로젝트 KPI 스코어카드를 생성합니다. | `examples/ex395_kpi_scorecard.py` |
| 396 | error_analysis | 수율·고장·RUL 오차를 통합 분석합니다. | `examples/ex396_error_analysis.py` |
| 397 | portfolio_case_study | 포트폴리오용 문제·접근·결과 문서를 생성합니다. | `examples/ex397_portfolio_case_study.py` |
| 398 | presentation_summary | 최종 발표용 1페이지 요약을 생성합니다. | `examples/ex398_presentation_summary.py` |
| 399 | deployment_checklist | 배포·운영·안전 체크리스트를 생성합니다. | `examples/ex399_deployment_checklist.py` |
| 400 | final_project_package | 최종 종합 Excel·문서·manifest를 생성합니다. | `examples/ex400_final_project_package.py` |

## 최종 프로젝트 구조
- 데이터 계약과 품질 검증
- 공통 특징공학
- 수율·고장확률·RUL 모델
- 모델 레지스트리
- 통합 추론·의사결정
- 안전 게이트
- 통합 테스트·KPI·오차분석
- 포트폴리오·발표·배포 체크리스트
- 최종 Excel 보고서와 manifest
