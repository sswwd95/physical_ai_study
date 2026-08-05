# 실습 167 — multiple_bayesian_regression

## 1. 학습 목표
여러 공정 변수의 회귀계수를 동시에 추정합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도, 압력, 입자, 진동, 정비경과시간을 표준화하고 beta 벡터를 Normal(0,1)로 둔
다중 베이지안 회귀를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex167_multiple_bayesian_regression.py
```

## 4. 예상 결과
각 표준화 공정 변수의 수율 영향 계수와 HDI가 저장됩니다.

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
| 13 | `features=["temp_mean_c","pressure_mean_pa","particle_mean","vibration_rms_g","maintenance_age_hours"]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `X=sensor_df[features]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `X=(X-X.mean())/X.std()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `with pm.Model(coords={"feature":features}) as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 17 | `    alpha=pm.Normal("alpha",94,5)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `    beta=pm.Normal("beta",0,1,dims="feature")` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 19 | `    sigma=pm.HalfNormal("sigma",3)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 20 | `    mu=alpha+pm.math.dot(X.to_numpy(),beta)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 21 | `    pm.Normal("y",mu,sigma,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 22 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `summary=az.summary(idata,var_names=["beta"],hdi_prob=0.94)` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |
| 25 | `print(summary)` | 결과를 콘솔에 출력합니다. |
| 26 | `summary.to_csv(OUTPUT_DIR/"ex167_multiple_regression.csv",encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?