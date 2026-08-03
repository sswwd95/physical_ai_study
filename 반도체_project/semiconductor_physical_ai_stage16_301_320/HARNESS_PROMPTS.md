## 실습 301 — sensor_stream_profile
```text
공정 단계별 센서 데이터 크기·결측값·기본 통계를 출력하라.
```

## 실습 302 — timestamp_validation
```text
1초 샘플링 기준으로 시간축 간격 오류를 검증하라.
```

## 실습 303 — missing_value_interpolation
```text
다중 센서 결측값을 선형 시간 보간하고 전후 결측 수를 비교하라.
```

## 실습 304 — sensor_bias_estimation
```text
온도·압력 이중 센서 간 평균 바이어스와 표준편차를 계산하라.
```

## 실습 305 — weighted_sensor_fusion
```text
센서 오차분산의 역수를 가중치로 온도 센서를 융합하라.
```

## 실습 306 — median_robust_fusion
```text
이중 온도 센서의 중앙값으로 강건 융합을 수행하라.
```

## 실습 307 — moving_average_filter
```text
3·5·15·30 구간 이동평균의 RMSE를 비교하라.
```

## 실습 308 — exponential_smoothing
```text
지수평활 alpha별 온도 추정 RMSE를 비교하라.
```

## 실습 309 — scalar_kalman_temperature
```text
1차원 칼만 필터로 온도 상태를 추정하라.
```

## 실습 310 — scalar_kalman_pressure
```text
1차원 칼만 필터로 압력 상태를 추정하라.
```

## 실습 311 — multivariable_state_estimation
```text
온도와 압력을 2차원 상태벡터로 칼만 추정하라.
```

## 실습 312 — phase_based_twin_model
```text
공정 단계별 디지털 트윈 기준값을 생성하라.
```

## 실습 313 — twin_residual_analysis
```text
실측 센서와 트윈 기준값의 잔차를 단계별로 분석하라.
```

## 실습 314 — sensor_fault_detection
```text
센서 잔차 임계값으로 바이어스·드리프트 고장을 탐지하라.
```

## 실습 315 — dynamic_threshold_alarm
```text
60초 이동 평균·표준편차로 동적 3시그마 경보를 생성하라.
```

## 실습 316 — sensor_confidence_score
```text
센서 절대오차와 결측 여부로 0~1 신뢰도 점수를 계산하라.
```

## 실습 317 — fallback_sensor_selection
```text
신뢰도가 높은 온도 센서를 시점별로 자동 선택하라.
```

## 실습 318 — twin_health_score
```text
온도·압력·RF·가스 오차를 결합한 트윈 건강점수를 계산하라.
```

## 실습 319 — realtime_twin_output
```text
융합 센서값·잔차·경보가 포함된 실시간 전달 CSV를 생성하라.
```

## 실습 320 — automated_digital_twin_report
```text
센서품질·단계요약·경보행·전체스트림 Excel 보고서를 생성하라.
```