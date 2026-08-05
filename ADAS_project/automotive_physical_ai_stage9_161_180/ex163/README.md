# 예제 163 — 정규 사전분포 시각화

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage9_161_180
conda activate auto_physical_ai
python ex163\main.py
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
| 1 | `import numpy as np` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 2 | `import matplotlib` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 3 | `matplotlib.use("Agg")` | 현재 분석 절차를 실행합니다. |
| 4 | `import matplotlib.pyplot as plt` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 5 | `from scipy.stats import norm` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 6 | `from common.bayes_utils import output_path` | 필요한 PyMC·ArviZ·공통 함수를 불러옵니다. |
| 7 | `x=np.linspace(-.15,.15,500); y=norm.pdf(x,0,.05)` | 관측값, 모수, 통계량 또는 판정값을 계산합니다. |
| 8 | `fig,ax=plt.subplots(figsize=(8,4)); ax.plot(x,y); ax.grid(True); ax.set_title("Accelerometer Bias Prior")` | 관측값, 모수, 통계량 또는 판정값을 계산합니다. |
| 9 | `p=output_path("ex163_accel_bias_prior.png"); fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig); print("saved:",p)` | 결과 파일을 저장합니다. |

## 확인 문제
1. 사전분포가 지나치게 좁으면 어떤 편향이 생기는가?
2. 95% 신용구간은 어떻게 해석하는가?
3. R-hat과 ESS가 좋지 않을 때 무엇을 조정해야 하는가?
