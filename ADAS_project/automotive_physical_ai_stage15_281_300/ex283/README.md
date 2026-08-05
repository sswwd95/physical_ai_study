# 예제 283 — 고장률 베타 사전분포

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage15_281_300
conda activate auto_physical_ai
python ex283\main.py
```

## 핵심 개념
- 고장확률: 관측 기간에 고장이 발생할 가능성
- 수명분포: 고장시간 자체의 확률분포
- 생존확률: 특정 시간까지 고장 없이 동작할 가능성
- 검열: 관측이 끝났지만 아직 고장하지 않은 데이터
- RUL: 현재 상태에서 남은 사용시간의 확률적 추정

## ROS2 연결
- 상태 입력: `/diagnostics`, 모터·배터리·진동 상태 토픽
- 출력: 부품별 고장확률, 생존확률, RUL 분포, 정비 권고
- 실제 시스템에서는 정비 이력과 부품 교체 시점을 함께 기록해야 합니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import numpy as np` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 2 | `import matplotlib` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 3 | `matplotlib.use("Agg")` | 현재 신뢰성 분석 절차를 실행합니다. |
| 4 | `import matplotlib.pyplot as plt` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 5 | `from scipy.stats import beta` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 6 | `from common.reliability_utils import output_path` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 7 | `x=np.linspace(.001,.999,500); y=beta.pdf(x,2,18)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 8 | `fig,ax=plt.subplots(figsize=(8,4)); ax.plot(x,y); ax.set_title("Prior for Failure Probability"); ax.grid(True)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 9 | `p=output_path("ex283_failure_probability_prior.png")` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 10 | `fig.tight_layout(); fig.savefig(p,dpi=140); plt.close(fig)` | 분석 결과를 outputs 폴더에 저장합니다. |
| 11 | `print(p)` | 추정값, 진단값 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 검열 데이터를 버리면 수명추정이 왜 편향될 수 있는가?
2. Weibull shape가 1보다 클 때 어떤 고장 특성을 의미하는가?
3. RUL 평균만 사용하는 것보다 신용구간이 중요한 이유는 무엇인가?
