# 반도체 Physical AI 하네스 엔지니어링
## 17단계: 321~340제 — PyMC 기반 베이지안 센서 융합과 디지털 트윈 불확실성 추정

### 실행
```bat
cd semiconductor_physical_ai_stage17_321_340
conda env create -f environment.yml
conda activate semi-physical-ai-stage17
python verify_environment.py
run_all_windows.bat
```

## 실습 목록
| 번호 | 핵심 주제 | 학습 목표 | 소스 |
|---:|---|---|---|
| 321 | sensor_bias_posterior | 온도 센서 바이어스의 사후분포를 추정합니다. | `examples/ex321_sensor_bias_posterior.py` |
| 322 | sensor_noise_posterior | 온도 센서별 노이즈 크기를 추정합니다. | `examples/ex322_sensor_noise_posterior.py` |
| 323 | bayesian_temperature_fusion | 두 온도 센서를 베이지안 방식으로 융합합니다. | `examples/ex323_bayesian_temperature_fusion.py` |
| 324 | bayesian_pressure_fusion | 두 압력 센서를 베이지안 방식으로 융합합니다. | `examples/ex324_bayesian_pressure_fusion.py` |
| 325 | posterior_sensor_weights | 센서 노이즈 사후분포로 가중치를 계산합니다. | `examples/ex325_posterior_sensor_weights.py` |
| 326 | phase_specific_bias | 공정 단계별 센서 바이어스를 추정합니다. | `examples/ex326_phase_specific_bias.py` |
| 327 | hierarchical_sensor_bias | 센서별 바이어스를 계층적으로 부분 풀링합니다. | `examples/ex327_hierarchical_sensor_bias.py` |
| 328 | robust_student_t_fusion | Student-t 모형으로 이상치에 강한 융합을 수행합니다. | `examples/ex328_robust_student_t_fusion.py` |
| 329 | latent_temperature_state | 잠재 온도 상태를 GaussianRandomWalk로 추정합니다. | `examples/ex329_latent_temperature_state.py` |
| 330 | latent_pressure_state | 잠재 압력 상태를 GaussianRandomWalk로 추정합니다. | `examples/ex330_latent_pressure_state.py` |
| 331 | joint_state_space_model | 온도·압력 잠재 상태를 함께 추정합니다. | `examples/ex331_joint_state_space_model.py` |
| 332 | posterior_predictive_sensor_check | 사후예측으로 센서 분포 재현성을 확인합니다. | `examples/ex332_posterior_predictive_sensor_check.py` |
| 333 | twin_residual_posterior | 트윈 잔차 평균과 변동성의 사후분포를 추정합니다. | `examples/ex333_twin_residual_posterior.py` |
| 334 | sensor_fault_probability | 센서 바이어스가 허용범위를 넘을 확률을 계산합니다. | `examples/ex334_sensor_fault_probability.py` |
| 335 | anomaly_probability_stream | 시점별 이상확률 스트림을 생성합니다. | `examples/ex335_anomaly_probability_stream.py` |
| 336 | credible_interval_fusion | 융합 상태의 평균과 HDI를 CSV로 저장합니다. | `examples/ex336_credible_interval_fusion.py` |
| 337 | bayesian_confidence_score | HDI 폭을 이용한 베이지안 신뢰도 점수를 계산합니다. | `examples/ex337_bayesian_confidence_score.py` |
| 338 | model_comparison_sensor | Normal·Student-t 센서모형을 LOO로 비교합니다. | `examples/ex338_model_comparison_sensor.py` |
| 339 | mcmc_diagnostics_sensor | R-hat·ESS·Divergence와 사후그래프를 저장합니다. | `examples/ex339_mcmc_diagnostics_sensor.py` |
| 340 | automated_bayesian_twin_report | 자동 베이지안 센서 융합·트윈 보고서를 생성합니다. | `examples/ex340_automated_bayesian_twin_report.py` |

## 데이터 특징
- 2초 주기 센서 스트림 420행
- 공정 단계 4개
- 온도·압력 이중 센서
- 센서 바이어스·노이즈·이상 구간·결측값 포함
- 디지털 트윈 참값 포함
