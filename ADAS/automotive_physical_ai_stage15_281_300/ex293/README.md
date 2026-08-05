# 예제 293 — 부품별 계층 수명 모델

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage15_281_300
conda activate auto_physical_ai
python ex293\main.py
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
| 1 | `import numpy as np, pymc as pm` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 2 | `from common.reliability_utils import load_lifetime,sample_model,save_summary` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 3 | `df=load_lifetime().query("failure_event==1")` | 수명 또는 RUL 데이터를 읽습니다. |
| 4 | `cid=df["component_id"].to_numpy()` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 5 | `y=np.log(df["observed_time_h"].to_numpy())` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 6 | `n=int(df["component_id"].nunique())` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 7 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 8 | `    group_mu=pm.Normal("group_mu",7,1)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 9 | `    group_sigma=pm.HalfNormal("group_sigma",1)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 10 | `    comp_mu=pm.Normal("component_mu",group_mu,group_sigma,shape=n)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 11 | `    sigma=pm.HalfNormal("sigma",1)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 12 | `    pm.Normal("obs",mu=comp_mu[cid],sigma=sigma,observed=y)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 13 | `idata=sample_model(model)` | MCMC 샘플링으로 사후분포를 생성합니다. |
| 14 | `s,pth=save_summary(idata,["group_mu","group_sigma","component_mu","sigma"],"ex293_hierarchical_lifetime.csv")` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 15 | `print(s); print(pth)` | 추정값, 진단값 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 검열 데이터를 버리면 수명추정이 왜 편향될 수 있는가?
2. Weibull shape가 1보다 클 때 어떤 고장 특성을 의미하는가?
3. RUL 평균만 사용하는 것보다 신용구간이 중요한 이유는 무엇인가?
