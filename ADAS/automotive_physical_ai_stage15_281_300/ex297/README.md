# 예제 297 — RUL 사후 예측 분포

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage15_281_300
conda activate auto_physical_ai
python ex297\main.py
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
| 1 | `import pandas as pd, pymc as pm` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 2 | `from common.reliability_utils import load_rul,standardize,sample_model,output_path` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 3 | `df=load_rul()` | 수명 또는 RUL 데이터를 읽습니다. |
| 4 | `x1=standardize(df["age_h"]).to_numpy(); x2=standardize(df["health_score"]).to_numpy(); y=df["observed_rul_h"].to_numpy()` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 5 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 6 | `    a=pm.Normal("intercept",600,500); b1=pm.Normal("age_coef",0,300); b2=pm.Normal("health_coef",0,300); sigma=pm.HalfNormal("sigma",200)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 7 | `    pm.Normal("obs",mu=a+b1*x1+b2*x2,sigma=sigma,observed=y)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 8 | `    idata=sample_model(model)` | MCMC 샘플링으로 사후분포를 생성합니다. |
| 9 | `    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False,return_inferencedata=False)` | 사후표본에서 수명·확률·구간을 계산합니다. |
| 10 | `pred=ppc["obs"].reshape(-1)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 11 | `p=output_path("ex297_rul_posterior_predictive.csv")` | 사후표본에서 수명·확률·구간을 계산합니다. |
| 12 | `pd.DataFrame({"predicted_rul_h":pred}).to_csv(p,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 13 | `print(pred.mean(),pred.std(),p)` | 추정값, 진단값 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 검열 데이터를 버리면 수명추정이 왜 편향될 수 있는가?
2. Weibull shape가 1보다 클 때 어떤 고장 특성을 의미하는가?
3. RUL 평균만 사용하는 것보다 신용구간이 중요한 이유는 무엇인가?
