# 반도체 Physical AI 하네스 엔지니어링
## 16단계: 301~320제 — 반도체 공정 디지털 트윈과 센서 융합 기초

### 실행
```bat
cd semiconductor_physical_ai_stage16_301_320
conda env create -f environment.yml
conda activate semi-physical-ai-stage16
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 301 | sensor_stream_profile | 센서 스트림과 공정 단계 분포를 확인합니다. | `examples/ex301_sensor_stream_profile.py` |
| 302 | timestamp_validation | 시간축 간격과 누락 시점을 검증합니다. | `examples/ex302_timestamp_validation.py` |
| 303 | missing_value_interpolation | 센서 결측값을 시간 보간으로 복원합니다. | `examples/ex303_missing_value_interpolation.py` |
| 304 | sensor_bias_estimation | 두 센서 간 바이어스를 추정합니다. | `examples/ex304_sensor_bias_estimation.py` |
| 305 | weighted_sensor_fusion | 센서 분산 기반 가중평균 융합을 수행합니다. | `examples/ex305_weighted_sensor_fusion.py` |
| 306 | median_robust_fusion | 중앙값 기반 강건 센서 융합을 수행합니다. | `examples/ex306_median_robust_fusion.py` |
| 307 | moving_average_filter | 이동평균으로 고주파 노이즈를 완화합니다. | `examples/ex307_moving_average_filter.py` |
| 308 | exponential_smoothing | 지수평활로 실시간 센서 상태를 추정합니다. | `examples/ex308_exponential_smoothing.py` |
| 309 | scalar_kalman_temperature | 1차원 칼만 필터로 온도를 추정합니다. | `examples/ex309_scalar_kalman_temperature.py` |
| 310 | scalar_kalman_pressure | 1차원 칼만 필터로 압력을 추정합니다. | `examples/ex310_scalar_kalman_pressure.py` |
| 311 | multivariable_state_estimation | 온도·압력 상태를 함께 추정합니다. | `examples/ex311_multivariable_state_estimation.py` |
| 312 | phase_based_twin_model | 공정 단계별 디지털 트윈 기준값을 생성합니다. | `examples/ex312_phase_based_twin_model.py` |
| 313 | twin_residual_analysis | 실측과 트윈 간 잔차를 분석합니다. | `examples/ex313_twin_residual_analysis.py` |
| 314 | sensor_fault_detection | 센서 잔차로 바이어스·드리프트 이상을 탐지합니다. | `examples/ex314_sensor_fault_detection.py` |
| 315 | dynamic_threshold_alarm | 이동 평균·표준편차 기반 동적 경보를 생성합니다. | `examples/ex315_dynamic_threshold_alarm.py` |
| 316 | sensor_confidence_score | 센서 신뢰도 점수를 계산합니다. | `examples/ex316_sensor_confidence_score.py` |
| 317 | fallback_sensor_selection | 신뢰도에 따라 주센서·보조센서를 선택합니다. | `examples/ex317_fallback_sensor_selection.py` |
| 318 | twin_health_score | 트윈 오차를 이용해 공정 건강점수를 계산합니다. | `examples/ex318_twin_health_score.py` |
| 319 | realtime_twin_output | 실시간 전달용 상태 추정 CSV를 생성합니다. | `examples/ex319_realtime_twin_output.py` |
| 320 | automated_digital_twin_report | 자동 디지털 트윈 Excel 보고서를 생성합니다. | `examples/ex320_automated_digital_twin_report.py` |

## 데이터 특징
- 1초 주기 센서 스트림 1,800행
- 공정 단계: idle, ramp, process, cooldown
- 온도·압력 이중 센서
- RF·가스유량 센서
- 참값 기반 디지털 트윈 기준 상태
- 결측값·바이어스·이상 구간 포함
