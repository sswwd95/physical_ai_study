# 실습 166 — simple_bayesian_regression

## 1. 학습 목표
입자 수와 수율의 베이지안 선형관계를 추정합니다.

## 2. Antigravity용 하네스 프롬프트
```text
particle_mean을 표준화하고 yield=alpha+beta*x 모형을 작성하라.
alpha~Normal(94,5), beta~Normal(0,2), sigma~HalfNormal(3)을 사용하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex166_simple_bayesian_regression.py
```

## 4. 예상 결과
입자 수가 수율에 미치는 회귀계수의 사후분포가 출력됩니다.

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
| 13 | `x = (sensor_df["particle_mean"]-sensor_df["particle_mean"].mean())/sensor_df["particle_mean"].std()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `y_obs = sensor_df["yield_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `with pm.Model() as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 16 | `    alpha = pm.Normal("alpha",94,5)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 17 | `    beta = pm.Normal("beta",0,2)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `    sigma = pm.HalfNormal("sigma",3)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 19 | `    mu = alpha + beta*x.to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `    pm.Normal("y",mu,sigma,observed=y_obs)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 21 | `    idata = pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `summary=az.summary(idata,var_names=["alpha","beta","sigma"],hdi_prob=0.94)` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |
| 24 | `print(summary)` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?