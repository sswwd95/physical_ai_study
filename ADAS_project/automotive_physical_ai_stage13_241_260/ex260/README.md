# 예제 260 — 이상 주행 확률·위험도 통합 리포트

## 실행
```bat
cd /d C:\work\automotive_physical_ai_stage13_241_260
conda activate auto_physical_ai
python ex260\main.py
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
| 1 | `import json, numpy as np, pandas as pd, pymc as pm, arviz as az` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 2 | `from common.risk_utils import load_data,standardize,sample_model,classification_metrics,output_path` | PyMC·ArviZ·데이터 처리 함수를 불러옵니다. |
| 3 | `df=load_data()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 4 | `x1=standardize(df["speed_mps"]).to_numpy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 5 | `x2=standardize(df["abs_accel_mps2"]).to_numpy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 6 | `x3=standardize(df["ttc_s"]).to_numpy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 7 | `x4=standardize(df["slip_ratio"]).to_numpy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 8 | `y=df["risk_label"].to_numpy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 9 | `with pm.Model() as model:` | 확률 모델 정의를 시작합니다. |
| 10 | `    a=pm.Normal("intercept",0,2)` | 회귀계수 또는 계층 효과의 정규 사전분포를 정의합니다. |
| 11 | `    b1=pm.Normal("b_speed",0,2); b2=pm.Normal("b_accel",0,2)` | 회귀계수 또는 계층 효과의 정규 사전분포를 정의합니다. |
| 12 | `    b3=pm.Normal("b_ttc",0,2); b4=pm.Normal("b_slip",0,2)` | 회귀계수 또는 계층 효과의 정규 사전분포를 정의합니다. |
| 13 | `    p=pm.Deterministic("risk_probability",pm.math.sigmoid(a+b1*x1+b2*x2+b3*x3+b4*x4))` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 14 | `    pm.Bernoulli("obs",p=p,observed=y)` | 이상 여부 관측값의 베르누이 우도를 정의합니다. |
| 15 | `idata=sample_model(model)` | MCMC 샘플링으로 사후분포를 생성합니다. |
| 16 | `summary=az.summary(idata,var_names=["intercept","b_speed","b_accel","b_ttc","b_slip"],round_to=6)` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 17 | `summary_path=output_path("ex260_posterior_summary.csv"); summary.to_csv(summary_path,encoding="utf-8-sig")` | 사후표본에서 위험확률이나 계수 확률을 계산합니다. |
| 18 | `prob=idata.posterior["risk_probability"].mean(dim=("chain","draw")).values` | 사후표본에서 위험확률이나 계수 확률을 계산합니다. |
| 19 | `best=None` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 20 | `for th in [i/100 for i in range(5,96,5)]:` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 21 | `    m=classification_metrics(y,prob,th); m["cost"]=m["fn"]*10+m["fp"]*2` | 임계값에 따른 분류 성능과 비용을 계산합니다. |
| 22 | `    if best is None or m["cost"]<best["cost"]: best=m` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 23 | `pred=df[["sample_id","driver","surface","risk_label","severity"]].copy()` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 24 | `pred["posterior_risk_probability"]=prob` | 사후표본에서 위험확률이나 계수 확률을 계산합니다. |
| 25 | `pred["predicted_risk"]=(prob>=best["threshold"]).astype(int)` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 26 | `pred_path=output_path("ex260_risk_predictions.csv"); pred.to_csv(pred_path,index=False,encoding="utf-8-sig")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 27 | `report={` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 28 | `    "samples":len(df),` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 29 | `    "observed_risk_rate":float(df["risk_label"].mean()),` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 30 | `    "best_threshold":best["threshold"],` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 31 | `    "cost_metrics":best,` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 32 | `    "max_r_hat":float(summary["r_hat"].max()),` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 33 | `    "min_ess_bulk":float(summary["ess_bulk"].min()),` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 34 | `    "coef_probability":{` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 35 | `        "speed_positive":float(np.mean(idata.posterior["b_speed"].values.reshape(-1)>0)),` | 사후표본에서 위험확률이나 계수 확률을 계산합니다. |
| 36 | `        "accel_positive":float(np.mean(idata.posterior["b_accel"].values.reshape(-1)>0)),` | 사후표본에서 위험확률이나 계수 확률을 계산합니다. |
| 37 | `        "ttc_negative":float(np.mean(idata.posterior["b_ttc"].values.reshape(-1)<0)),` | 사후표본에서 위험확률이나 계수 확률을 계산합니다. |
| 38 | `        "slip_positive":float(np.mean(idata.posterior["b_slip"].values.reshape(-1)>0))` | 사후표본에서 위험확률이나 계수 확률을 계산합니다. |
| 39 | `    }` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 40 | `}` | 현재 베이지안 위험 분석 절차를 실행합니다. |
| 41 | `report_path=output_path("ex260_integrated_report.json")` | 데이터, 모델 모수, 위험확률 또는 평가값을 계산합니다. |
| 42 | `report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")` | 분석 결과를 outputs 폴더에 저장합니다. |
| 43 | `print(report)` | 추정값, 성능, 판정 또는 저장 경로를 출력합니다. |
| 44 | `print("saved:",summary_path,pred_path,report_path)` | 추정값, 성능, 판정 또는 저장 경로를 출력합니다. |

## 확인 문제
1. 위험확률과 위험 레이블의 차이는 무엇인가?
2. 미탐 비용을 높이면 최적 임계값은 어느 방향으로 움직이는가?
3. 운전자 계층 모델이 표본이 적은 운전자에게 주는 장점은 무엇인가?
