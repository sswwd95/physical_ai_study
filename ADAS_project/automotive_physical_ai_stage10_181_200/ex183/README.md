# 예제 183 — 슬립률 사전분포 시각화

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage10_181_200
conda activate auto_physical_ai
python ex183\main.py
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
| 2 | `import matplotlib` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 3 | `matplotlib.use("Agg")` | 현재 베이즈 분석 절차를 실행합니다. |
| 4 | `import matplotlib.pyplot as plt` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 5 | `from scipy.stats import beta` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 6 | `from common.bayes_slip_utils import output_path` | PyMC·ArviZ 또는 공통 함수를 불러옵니다. |
| 7 | `x = np.linspace(0.001, 0.40, 400)` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 8 | `y = beta.pdf(x/0.4, a=2, b=8) / 0.4` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 9 | `fig, ax = plt.subplots(figsize=(8,4))` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 10 | `ax.plot(x, y)` | 현재 베이즈 분석 절차를 실행합니다. |
| 11 | `ax.set_title("Prior Distribution of Slip Ratio")` | 현재 베이즈 분석 절차를 실행합니다. |
| 12 | `ax.set_xlabel("Slip ratio")` | 현재 베이즈 분석 절차를 실행합니다. |
| 13 | `ax.set_ylabel("Density")` | 현재 베이즈 분석 절차를 실행합니다. |
| 14 | `ax.grid(True)` | 현재 베이즈 분석 절차를 실행합니다. |
| 15 | `path = output_path("ex183_slip_prior.png")` | 데이터, 모델 모수, 통계량 또는 판정값을 계산합니다. |
| 16 | `fig.tight_layout()` | 현재 베이즈 분석 절차를 실행합니다. |
| 17 | `fig.savefig(path, dpi=140)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 18 | `plt.close(fig)` | 현재 베이즈 분석 절차를 실행합니다. |
| 19 | `print("saved:", path)` | 핵심 추정값·진단값·저장 경로를 출력합니다. |

## 확인 문제
1. 슬립률 평균만 사용하는 것보다 사후분포를 사용하는 장점은 무엇인가?
2. 노면별 계층 모델은 표본이 적은 노면에 어떤 도움을 주는가?
3. 위험확률을 제어기에 연결할 때 히스테리시스가 필요한 이유는 무엇인가?
