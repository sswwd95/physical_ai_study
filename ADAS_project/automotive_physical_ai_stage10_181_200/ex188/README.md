# 예제 188 — 슬립률 기준 초과 확률

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage10_181_200
conda activate auto_physical_ai
python ex188\main.py
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
| 1 | `import numpy as np` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 2 | `import pymc as pm` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 3 | `from common.bayes_slip_utils import load_data, sample_model` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 4 | `y = load_data()["slip_ratio"].to_numpy()` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 5 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 6 | `    mu = pm.Normal("mu", mu=0.08, sigma=0.08)` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 7 | `    sigma = pm.HalfNormal("sigma", sigma=0.08)` | 양수인 표준편차의 사전분포를 정의합니다. |
| 8 | `    pm.Normal("obs", mu=mu, sigma=sigma, observed=y)` | 정규 사전분포 또는 정규 우도를 정의합니다. |
| 9 | `idata = sample_model(model)` | MCMC 샘플링으로 사후분포를 생성합니다. |
| 10 | `samples = idata.posterior["mu"].values.reshape(-1)` | 사후표본에서 평균·확률·구간을 계산합니다. |
| 11 | `print("P(mean slip > 0.08):", float(np.mean(samples > 0.08)))` | 핵심 추정값·진단값·저장 경로를 출력합니다. |

## 확인 문제
1. 슬립률 평균만 사용하는 것보다 사후분포를 사용하는 장점은 무엇인가?
2. 노면별 계층 모델은 표본이 적은 노면에 어떤 도움을 주는가?
3. 위험확률을 제어기에 연결할 때 히스테리시스가 필요한 이유는 무엇인가?
