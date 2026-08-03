# 실습 254 — rul_prediction_interval

## 1. 학습 목표
장비별 RUL 평균과 HDI를 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
행별 RUL 사후예측 평균과 3~97% 구간을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage13
python examples\ex254_rul_prediction_interval.py
```

## 4. 예상 결과
요청한 베이지안 수명·고장확률·RUL 분석 결과가 출력 또는 저장됩니다.

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
| 8 | `LIFE_FILE = ROOT / "data" / "bayesian_equipment_lifetime.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 9 | `RUL_FILE = ROOT / "data" / "bayesian_rul_snapshots.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 11 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `life_df = pd.read_csv(LIFE_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 14 | `rul_df = pd.read_csv(RUL_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 16 | `features=["cycle","vibration_rms_g","temperature_c","motor_current_a","particle_count"]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 17 | `X=rul_df[features]; mean=X.mean(); std=X.std(); Xs=(X-mean)/std; y=rul_df["rul_cycles"].to_numpy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 18 | `with pm.Model(coords={"feature":features}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 19 | `    a=pm.Normal("a",80,40); beta=pm.Normal("beta",0,20,dims="feature"); sigma=pm.HalfNormal("sigma",20)` | 회귀계수나 그룹 효과의 정규 사전분포를 정의합니다. |
| 20 | `    pm.Normal("rul",a+pm.math.dot(Xs.to_numpy(),beta),sigma,observed=y)` | 회귀계수나 그룹 효과의 정규 사전분포를 정의합니다. |
| 21 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)` | 사후예측 수명 또는 RUL 표본을 생성합니다. |
| 23 | `pred=ppc.posterior_predictive["rul"].values.reshape(-1,len(rul_df))` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 24 | `out=rul_df[["equipment_id","cycle","rul_cycles"]].copy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 25 | `out["pred_mean"]=pred.mean(0); out["pred_p03"]=np.quantile(pred,.03,axis=0); out["pred_p97"]=np.quantile(pred,.97,axis=0)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 26 | `out.to_csv(OUTPUT_DIR/"ex254_rul_intervals.csv",index=False,encoding="utf-8-sig")` | 분석 결과를 CSV로 저장합니다. |
| 27 | `print(out.head(10).round(2))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 검열 데이터가 왜 발생했으며 관측 종료 기준은 무엇인가?
2. 장비별 차이를 계층모형으로 반영했는가?
3. 보수적인 RUL 하한과 정비 비용을 함께 고려했는가?