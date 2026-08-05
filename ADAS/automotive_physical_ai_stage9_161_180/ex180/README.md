# 예제 180 — IMU 베이즈 추정 통합 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage9_161_180
conda activate auto_physical_ai
python ex180\main.py
```

첫 PyMC 실행은 컴파일 때문에 시간이 더 걸릴 수 있습니다.

## 핵심 개념
사전분포는 데이터 관측 전 가정, 우도는 모수에서 데이터가 생성될 가능성,
사후분포는 두 정보를 결합한 최종 불확실성입니다. R-hat과 ESS로 샘플링 품질을 점검합니다.

## ROS2 연결
추정 바이어스는 IMU 보정값으로, 사후분산은 `sensor_msgs/Imu` 공분산 설정의 참고값으로,
기준 초과 사후확률은 진단·정비 경고로 연결할 수 있습니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import json, numpy as np, pymc as pm, arviz as az` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 2 | `from common.bayes_utils import load_data,sample_model,output_path` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 3 | `d=load_data(); a=d["accel_measurement_mps2"].to_numpy(); g=d["gyro_measurement_rps"].to_numpy()` | 관측값, 모수, 통계량 또는 판정값을 계산합니다. |
| 4 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 5 | `    ab=pm.Normal("accel_bias",0,.1); ass=pm.HalfNormal("accel_sigma",.1); gb=pm.Normal("gyro_bias",0,.05); gs=pm.HalfNormal("gyro_sigma",.03); pm.Normal("a",ab,ass,observed=a); pm.Normal("g",gb,gs,observed=g)` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 6 | `i=sample_model(model); s=az.summary(i,var_names=["accel_bias","accel_sigma","gyro_bias","gyro_sigma"]); sp=output_path("ex180_summary.csv"); s.to_csv(sp)` | MCMC로 사후분포를 샘플링합니다. |
| 7 | `asamp=i.posterior["accel_bias"].values.reshape(-1); gsamp=i.posterior["gyro_bias"].values.reshape(-1); r={"accel_bias_mean":float(asamp.mean()),"gyro_bias_mean":float(gsamp.mean()),"P_abs_accel_gt_0_04":float(np.mean(np.abs(asamp)>.04)),"max_r_hat":float(s["r_hat"].max())}; rp=output_path("ex180_report.json"); rp.write_text(json.dumps(r,indent=2)); print(r); print(sp,rp)` | 사후표본에서 평균·구간·확률을 계산합니다. |

## 확인 문제
1. 사전분포가 지나치게 좁으면 어떤 편향이 생기는가?
2. 95% 신용구간은 어떻게 해석하는가?
3. R-hat과 ESS가 좋지 않을 때 무엇을 조정해야 하는가?
