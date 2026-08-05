# 반도체 Physical AI 하네스 엔지니어링
## 18단계: 341~360제 — 반도체 공정 이상 대응과 안전 의사결정 시스템

### 실행
```bat
cd semiconductor_physical_ai_stage18_341_360
conda env create -f environment.yml
conda activate semi-physical-ai-stage18
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 341 | safety_stream_profile | 이상 유형·심각도·인터록 상태를 확인합니다. | `examples/ex341_safety_stream_profile.py` |
| 342 | severity_rule_engine | 센서 임계값으로 심각도 등급을 계산합니다. | `examples/ex342_severity_rule_engine.py` |
| 343 | alarm_priority_queue | 심각도·지속시간 기반 경보 우선순위를 만듭니다. | `examples/ex343_alarm_priority_queue.py` |
| 344 | interlock_validation | 문·냉각·진공 인터록 위반을 검증합니다. | `examples/ex344_interlock_validation.py` |
| 345 | safety_state_machine | 정상·주의·감속·정지 상태기계를 구현합니다. | `examples/ex345_safety_state_machine.py` |
| 346 | persistence_filter | 일시적 이상을 제거하는 지속시간 필터를 적용합니다. | `examples/ex346_persistence_filter.py` |
| 347 | alarm_hysteresis | 경보 진입·해제 히스테리시스를 구현합니다. | `examples/ex347_alarm_hysteresis.py` |
| 348 | sensor_vote_logic | 다중 센서 투표로 경보를 결정합니다. | `examples/ex348_sensor_vote_logic.py` |
| 349 | risk_score | 온도·압력·진동·입자 위험점수를 계산합니다. | `examples/ex349_risk_score.py` |
| 350 | action_policy | 관찰·재검사·감속·정지 행동을 선택합니다. | `examples/ex350_action_policy.py` |
| 351 | false_alarm_cost | 오탐·미탐 비용을 계산합니다. | `examples/ex351_false_alarm_cost.py` |
| 352 | threshold_cost_optimization | 임계값별 기대비용을 비교합니다. | `examples/ex352_threshold_cost_optimization.py` |
| 353 | random_forest_risk_model | Random Forest로 위험상태 확률을 예측합니다. | `examples/ex353_random_forest_risk_model.py` |
| 354 | probability_action_policy | 위험확률 기반 행동 정책을 생성합니다. | `examples/ex354_probability_action_policy.py` |
| 355 | uncertainty_review_zone | 중간 확률 구간을 재검사 대상으로 분리합니다. | `examples/ex355_uncertainty_review_zone.py` |
| 356 | safe_fallback_policy | 센서·인터록 이상 시 안전 폴백을 적용합니다. | `examples/ex356_safe_fallback_policy.py` |
| 357 | incident_timeline | 이상사건별 시작·종료·지속시간을 생성합니다. | `examples/ex357_incident_timeline.py` |
| 358 | response_kpi | 탐지 지연·경보 수·정지 시간을 평가합니다. | `examples/ex358_response_kpi.py` |
| 359 | operator_handoff_output | 작업자 인계용 안전 이벤트 CSV를 생성합니다. | `examples/ex359_operator_handoff_output.py` |
| 360 | automated_safety_report | 자동 안전 의사결정 Excel 보고서를 생성합니다. | `examples/ex360_automated_safety_report.py` |

## 안전 상태
- NORMAL
- CAUTION
- SLOWDOWN
- STOP

## 행동 정책
- CONTINUE
- MONITOR
- REINSPECT
- SLOWDOWN
- EMERGENCY_STOP
