# 예제 243 — 베르누이 위험률 사전분포

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage13_241_260
conda activate auto_physical_ai
python ex243\main.py
```

첫 PyMC 실행은 컴파일 때문에 시간이 더 걸릴 수 있습니다.

## 핵심 개념
위험을 0 또는 1로만 판단하지 않고 사후 위험확률로 표현합니다.
미탐 비용과 오탐 비용을 다르게 설정하면 안전 요구에 맞는 경고 임계값을 선택할 수 있습니다.

## ROS2 연결
- 센서 입력: `/odom`, `/imu`, `/scan`, 모터 진단
- 출력: 위험확률, 위험등급, 권장 감속 또는 정지 플래그
- 진단: `/diagnostics` 또는 사용자 정의 `DrivingRisk` 메시지

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import numpy as np` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 2 | `import matplotlib` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 3 | `matplotlib.use("Agg")` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 4 | `import matplotlib.pyplot as plt` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 5 | `from scipy.stats import beta` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 6 | `from common.risk_utils import output_path` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 7 | `x=np.linspace(.001,.999,500)` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 8 | `y=beta.pdf(x,2,8)` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 9 | `fig,ax=plt.subplots(figsize=(8,4))` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 10 | `ax.plot(x,y); ax.set_title("Prior for Overall Risk Probability"); ax.set_xlabel("Risk probability"); ax.grid(True)` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 11 | `p=output_path("ex243_risk_prior.png")` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 12 | `fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 13 | `print("saved:",p)` | 추정값, 성능, 판정 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 위험확률과 위험 레이블의 차이는 무엇인가?
2. 미탐 비용을 높이면 최적 임계값은 어느 방향으로 움직이는가?
3. 운전자 계층 모델이 표본이 적은 운전자에게 주는 장점은 무엇인가?
