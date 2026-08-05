# 예제 300 — 고장확률·잔여수명 통합 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage15_281_300
conda activate auto_physical_ai
python ex300\main.py
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
| 1 | `import json, numpy as np, pymc as pm, arviz as az` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 2 | `from common.reliability_utils import load_lifetime,load_rul,standardize,sample_model,output_path` | PyMC·ArviZ·신뢰성 분석 함수를 불러옵니다. |
| 3 | `life=load_lifetime(); rul=load_rul()` | 수명 또는 RUL 데이터를 읽습니다. |
| 4 | `y_fail=life["failure_event"].to_numpy()` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 5 | `x_age=standardize(rul["age_h"]).to_numpy()` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 6 | `x_health=standardize(rul["health_score"]).to_numpy()` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 7 | `y_rul=rul["observed_rul_h"].to_numpy()` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 8 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 9 | `    failure_p=pm.Beta("failure_probability",2,18)` | 0~1 고장확률에 베타 사전분포를 설정합니다. |
| 10 | `    pm.Bernoulli("failure_obs",p=failure_p,observed=y_fail)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 11 | `    a=pm.Normal("rul_intercept",600,500)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 12 | `    b1=pm.Normal("b_age",0,300)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 13 | `    b2=pm.Normal("b_health",0,300)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 14 | `    sigma=pm.HalfNormal("rul_sigma",200)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 15 | `    pm.Normal("rul_obs",mu=a+b1*x_age+b2*x_health,sigma=sigma,observed=y_rul)` | 회귀계수 또는 관측오차 모델을 정의합니다. |
| 16 | `idata=sample_model(model)` | MCMC 샘플링으로 사후분포를 생성합니다. |
| 17 | `summary=az.summary(idata,var_names=["failure_probability","rul_intercept","b_age","b_health","rul_sigma"],round_to=6)` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 18 | `sp=output_path("ex300_posterior_summary.csv"); summary.to_csv(sp,encoding="utf-8-sig")` | 사후표본에서 수명·확률·구간을 계산합니다. |
| 19 | `fp=idata.posterior["failure_probability"].values.reshape(-1)` | 사후표본에서 수명·확률·구간을 계산합니다. |
| 20 | `report={` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 21 | `    "observed_failure_rate":float(life["failure_event"].mean()),` | 현재 신뢰성 분석 절차를 실행합니다. |
| 22 | `    "posterior_failure_probability_mean":float(fp.mean()),` | 사후표본에서 수명·확률·구간을 계산합니다. |
| 23 | `    "posterior_failure_probability_hdi_95":[float(v) for v in np.quantile(fp,[.025,.975])],` | 사후표본에서 수명·확률·구간을 계산합니다. |
| 24 | `    "prob_failure_probability_gt_0_20":float(np.mean(fp>.20)),` | 현재 신뢰성 분석 절차를 실행합니다. |
| 25 | `    "median_observed_rul_h":float(rul["observed_rul_h"].median()),` | 현재 신뢰성 분석 절차를 실행합니다. |
| 26 | `    "max_r_hat":float(summary["r_hat"].max()),` | 현재 신뢰성 분석 절차를 실행합니다. |
| 27 | `    "min_ess_bulk":float(summary["ess_bulk"].min()),` | 현재 신뢰성 분석 절차를 실행합니다. |
| 28 | `}` | 현재 신뢰성 분석 절차를 실행합니다. |
| 29 | `rp=output_path("ex300_integrated_report.json")` | 수명, 생존확률, RUL 또는 평가값을 계산합니다. |
| 30 | `rp.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 31 | `print(report); print(sp,rp)` | 추정값, 진단값 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 검열 데이터를 버리면 수명추정이 왜 편향될 수 있는가?
2. Weibull shape가 1보다 클 때 어떤 고장 특성을 의미하는가?
3. RUL 평균만 사용하는 것보다 신용구간이 중요한 이유는 무엇인가?
