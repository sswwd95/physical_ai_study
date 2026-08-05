# 실습 340 — automated_bayesian_twin_report

## 1. 학습 목표
자동 베이지안 센서 융합·트윈 보고서를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도·압력 사후요약, 단계요약, 이상스트림 Excel 보고서를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage17
python examples\ex340_automated_bayesian_twin_report.py
```

## 4. 예상 결과
요청한 베이지안 센서 융합·디지털 트윈 불확실성 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_sensor_fusion.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 11 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 12 | `sensor_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `temp_res=(sensor_df["temp_sensor_a_c"]-sensor_df["true_temperature_c"]).dropna().to_numpy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `pressure_res=(sensor_df["pressure_sensor_a_pa"]-sensor_df["true_pressure_pa"]).dropna().to_numpy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `with pm.Model() as temp_model:` | PyMC 확률모형 범위를 시작합니다. |
| 18 | `    temp_mu=pm.Normal("temp_mu",0,2); temp_sigma=pm.HalfNormal("temp_sigma",1)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 19 | `    pm.Normal("temp_r",temp_mu,temp_sigma,observed=temp_res)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 20 | `    temp_idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `with pm.Model() as pressure_model:` | PyMC 확률모형 범위를 시작합니다. |
| 23 | `    pressure_mu=pm.Normal("pressure_mu",0,1); pressure_sigma=pm.HalfNormal("pressure_sigma",.5)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 24 | `    pm.Normal("pressure_r",pressure_mu,pressure_sigma,observed=pressure_res)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 25 | `    pressure_idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 26 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 27 | `temp_summary=az.summary(temp_idata,var_names=["temp_mu","temp_sigma"],hdi_prob=.94)` | 사후요약과 MCMC 진단값을 계산합니다. |
| 28 | `pressure_summary=az.summary(pressure_idata,var_names=["pressure_mu","pressure_sigma"],hdi_prob=.94)` | 사후요약과 MCMC 진단값을 계산합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `stream=sensor_df[["timestamp","process_phase"]].copy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 31 | `temp_b_res=(sensor_df["temp_sensor_b_c"]-sensor_df["true_temperature_c"])` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 32 | `pressure_b_res=(sensor_df["pressure_sensor_b_pa"]-sensor_df["true_pressure_pa"])` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 33 | `stream["temp_anomaly_score"]=np.abs(temp_b_res)/(temp_b_res.dropna().std()+1e-9)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 34 | `stream["pressure_anomaly_score"]=np.abs(pressure_b_res)/(pressure_b_res.dropna().std()+1e-9)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 35 | `stream["review_required"]=(stream["temp_anomaly_score"]>3)\|(stream["pressure_anomaly_score"]>3)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 36 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 37 | `phase_summary=stream.groupby("process_phase")[["temp_anomaly_score","pressure_anomaly_score","review_required"]].mean()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 38 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 39 | `with pd.ExcelWriter(OUTPUT_DIR/"ex340_bayesian_twin_report.xlsx",engine="openpyxl") as w:` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 40 | `    temp_summary.to_excel(w,sheet_name="temperature_posterior")` | 결과를 Excel 보고서로 저장합니다. |
| 41 | `    pressure_summary.to_excel(w,sheet_name="pressure_posterior")` | 결과를 Excel 보고서로 저장합니다. |
| 42 | `    phase_summary.to_excel(w,sheet_name="phase_summary")` | 결과를 Excel 보고서로 저장합니다. |
| 43 | `    stream.to_excel(w,sheet_name="anomaly_stream",index=False)` | 결과를 Excel 보고서로 저장합니다. |
| 44 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 45 | `print("보고서 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 센서 바이어스와 실제 공정 변화를 구분했는가?
2. 사후예측구간이 너무 좁거나 넓지 않은가?
3. 이상확률을 자동 제어에 사용할 때 안전 임계값이 있는가?