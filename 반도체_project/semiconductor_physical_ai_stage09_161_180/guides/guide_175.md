# 실습 175 — loo_model_comparison

## 1. 학습 목표
단순 회귀와 다중 회귀를 LOO로 비교합니다.

## 2. Antigravity용 하네스 프롬프트
```text
두 모델을 log_likelihood가 포함된 InferenceData로 적합하고 az.compare를 사용하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex175_loo_model_comparison.py
```

## 4. 예상 결과
요청한 베이지안 결과와 진단 자료가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_yield_data.csv"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 11 | `sensor_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `x1=(sensor_df["particle_mean"]-sensor_df["particle_mean"].mean())/sensor_df["particle_mean"].std()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `X=sensor_df[["particle_mean","maintenance_age_hours"]]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `X=(X-X.mean())/X.std()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `models={}` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `with pm.Model() as m1:` | PyMC 확률모형의 범위를 시작합니다. |
| 18 | `    a=pm.Normal("a",94,5); b=pm.Normal("b",0,2); s=pm.HalfNormal("s",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 19 | `    pm.Normal("y",a+b*x1.to_numpy(),s,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 20 | `    models["simple"]=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})` | MCMC로 사후분포 표본을 추출합니다. |
| 21 | `with pm.Model() as m2:` | PyMC 확률모형의 범위를 시작합니다. |
| 22 | `    a=pm.Normal("a",94,5); b=pm.Normal("b",0,1,shape=2); s=pm.HalfNormal("s",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 23 | `    pm.Normal("y",a+pm.math.dot(X.to_numpy(),b),s,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 24 | `    models["multiple"]=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})` | MCMC로 사후분포 표본을 추출합니다. |
| 25 | `print(az.compare(models))` | LOO 기반으로 여러 베이지안 모델을 비교합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?