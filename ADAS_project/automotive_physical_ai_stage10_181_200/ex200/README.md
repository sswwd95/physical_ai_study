# 예제 200 — 휠 슬립·오도메트리 불확실성 통합 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage10_181_200
conda activate auto_physical_ai
python ex200\main.py
```

## 핵심 개념
휠 슬립률과 오도메트리 오차를 하나의 고정값으로 보지 않고 확률분포로 추정합니다.
사후분포를 이용하면 평균 오차뿐 아니라 기준 초과 가능성도 계산할 수 있습니다.

## ROS2 연결
- 휠 엔코더 → `/joint_states`
- IMU → `/imu`
- 적분 위치와 자세 → `/odom`
- 슬립 위험확률 → `/diagnostics` 또는 사용자 정의 경고 토픽
- 노면별 사후분포 → 주행 제어기의 속도·가속도 제한값 조정

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import json` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 2 | `import numpy as np` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 3 | `import pymc as pm` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 4 | `import arviz as az` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 5 | `from common.bayes_slip_utils import load_data, sample_model, output_path` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 6 | `df = load_data()` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 7 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 8 | `    slip_mu = pm.Normal("slip_mu", 0.08, 0.08)` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 9 | `    slip_sigma = pm.HalfNormal("slip_sigma", 0.08)` | 양수인 표준편차의 사전분포를 정의합니다. |
| 10 | `    dist_bias = pm.Normal("dist_bias", 0.0, 0.20)` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 11 | `    dist_sigma = pm.HalfNormal("dist_sigma", 0.20)` | 양수인 표준편차의 사전분포를 정의합니다. |
| 12 | `    yaw_bias = pm.Normal("yaw_bias", 0.0, 0.20)` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 13 | `    yaw_sigma = pm.HalfNormal("yaw_sigma", 0.20)` | 양수인 표준편차의 사전분포를 정의합니다. |
| 14 | `    pm.Normal("slip_obs", slip_mu, slip_sigma, observed=df["slip_ratio"].to_numpy())` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 15 | `    pm.Normal("dist_obs", dist_bias, dist_sigma, observed=df["distance_error_m"].to_numpy())` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 16 | `    pm.Normal("yaw_obs", yaw_bias, yaw_sigma, observed=df["yaw_error_rad"].to_numpy())` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 17 | `idata = sample_model(model)` | MCMC 샘플링으로 사후분포를 생성합니다. |
| 18 | `summary = az.summary(` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 19 | `    idata,` | 현재 베이즈 분석 절차를 실행합니다. |
| 20 | `    var_names=["slip_mu","slip_sigma","dist_bias","dist_sigma","yaw_bias","yaw_sigma"],` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 21 | `    round_to=6` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 22 | `)` | 현재 베이즈 분석 절차를 실행합니다. |
| 23 | `summary_path = output_path("ex200_integrated_summary.csv")` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 24 | `summary.to_csv(summary_path, encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 25 | `slip_samples = idata.posterior["slip_mu"].values.reshape(-1)` | 사후표본에서 평균·확률·구간을 계산합니다. |
| 26 | `dist_samples = idata.posterior["dist_bias"].values.reshape(-1)` | 사후표본에서 평균·확률·구간을 계산합니다. |
| 27 | `yaw_samples = idata.posterior["yaw_bias"].values.reshape(-1)` | 사후표본에서 평균·확률·구간을 계산합니다. |
| 28 | `report = {` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 29 | `    "slip_mean": float(slip_samples.mean()),` | 현재 베이즈 분석 절차를 실행합니다. |
| 30 | `    "slip_hdi_95": [float(v) for v in np.quantile(slip_samples,[0.025,0.975])],` | 현재 베이즈 분석 절차를 실행합니다. |
| 31 | `    "distance_bias_mean_m": float(dist_samples.mean()),` | 현재 베이즈 분석 절차를 실행합니다. |
| 32 | `    "yaw_bias_mean_rad": float(yaw_samples.mean()),` | 현재 베이즈 분석 절차를 실행합니다. |
| 33 | `    "prob_mean_slip_gt_0_08": float(np.mean(slip_samples > 0.08)),` | 현재 베이즈 분석 절차를 실행합니다. |
| 34 | `    "prob_distance_bias_gt_0_05": float(np.mean(dist_samples > 0.05)),` | 현재 베이즈 분석 절차를 실행합니다. |
| 35 | `    "max_r_hat": float(summary["r_hat"].max()),` | 현재 베이즈 분석 절차를 실행합니다. |
| 36 | `    "min_ess_bulk": float(summary["ess_bulk"].min()),` | 현재 베이즈 분석 절차를 실행합니다. |
| 37 | `}` | 현재 베이즈 분석 절차를 실행합니다. |
| 38 | `report_path = output_path("ex200_integrated_report.json")` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 39 | `report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 40 | `print(report)` | 핵심 추정값·진단값·저장 경로를 출력합니다. |
| 41 | `print("saved:", summary_path, report_path)` | 핵심 추정값·진단값·저장 경로를 출력합니다. |

## 확인 문제
1. 슬립률 평균만 사용하는 것보다 사후분포를 사용하는 장점은 무엇인가?
2. 노면별 계층 모델은 표본이 적은 노면에 어떤 도움을 주는가?
3. 위험확률을 제어기에 연결할 때 히스테리시스가 필요한 이유는 무엇인가?
