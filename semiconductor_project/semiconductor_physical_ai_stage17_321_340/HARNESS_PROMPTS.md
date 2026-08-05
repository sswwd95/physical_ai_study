## 실습 321 — sensor_bias_posterior
```text
두 온도 센서의 바이어스 사후분포와 94% HDI를 추정하라.
```

## 실습 322 — sensor_noise_posterior
```text
온도 센서 A·B의 노이즈 표준편차 사후분포를 추정하라.
```

## 실습 323 — bayesian_temperature_fusion
```text
잠재 참온도와 센서별 바이어스·노이즈를 둔 베이지안 융합을 작성하라.
```

## 실습 324 — bayesian_pressure_fusion
```text
잠재 참압력과 이중 압력 센서의 베이지안 융합을 작성하라.
```

## 실습 325 — posterior_sensor_weights
```text
센서 노이즈 사후표본의 역분산으로 가중치 분포를 계산하라.
```

## 실습 326 — phase_specific_bias
```text
idle·ramp·process·cooldown 단계별 온도 센서 바이어스를 추정하라.
```

## 실습 327 — hierarchical_sensor_bias
```text
센서별 바이어스를 부분 풀링하는 계층모형을 작성하라.
```

## 실습 328 — robust_student_t_fusion
```text
Student-t 관측모형으로 이상치에 강한 온도 융합을 수행하라.
```

## 실습 329 — latent_temperature_state
```text
GaussianRandomWalk 잠재 온도 상태공간 모형을 작성하라.
```

## 실습 330 — latent_pressure_state
```text
GaussianRandomWalk 잠재 압력 상태공간 모형을 작성하라.
```

## 실습 331 — joint_state_space_model
```text
온도·압력 잠재 상태를 함께 추정하는 모형을 작성하라.
```

## 실습 332 — posterior_predictive_sensor_check
```text
센서 잔차의 관측·사후예측 평균과 표준편차를 비교하라.
```

## 실습 333 — twin_residual_posterior
```text
디지털 트윈 온도 잔차 평균·표준편차의 사후분포를 저장하라.
```

## 실습 334 — sensor_fault_probability
```text
온도 센서 바이어스가 1도·2도를 넘을 사후확률을 계산하라.
```

## 실습 335 — anomaly_probability_stream
```text
시점별 트윈 잔차에서 이상확률 스트림을 생성하라.
```

## 실습 336 — credible_interval_fusion
```text
융합 온도의 사후평균과 94% HDI를 CSV로 저장하라.
```

## 실습 337 — bayesian_confidence_score
```text
HDI 폭을 사용해 0~1 베이지안 신뢰도 점수를 계산하라.
```

## 실습 338 — model_comparison_sensor
```text
Normal과 Student-t 센서 잔차모형을 LOO로 비교하라.
```

## 실습 339 — mcmc_diagnostics_sensor
```text
R-hat·ESS·Divergence와 사후분포 그래프를 저장하라.
```

## 실습 340 — automated_bayesian_twin_report
```text
온도·압력 사후요약, 단계요약, 이상스트림 Excel 보고서를 생성하라.
```