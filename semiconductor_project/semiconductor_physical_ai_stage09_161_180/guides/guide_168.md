# 실습 168 — posterior_predictive_check

## 1. 학습 목표
사후예측분포가 실제 수율 분포를 재현하는지 확인합니다.

## 2. Antigravity용 하네스 프롬프트
```text
다중 회귀 모형을 학습한 뒤 pm.sample_posterior_predictive로 y 예측표본을 만들고
관측 평균과 예측 평균, 관측 표준편차와 예측 표준편차를 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex168_posterior_predictive_check.py
```

## 4. 예상 결과
관측 데이터와 사후예측분포의 중심과 변동성이 비교됩니다.

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
| 13 | `x=(sensor_df["particle_mean"]-sensor_df["particle_mean"].mean())/sensor_df["particle_mean"].std()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `with pm.Model() as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 15 | `    alpha=pm.Normal("alpha",94,5); beta=pm.Normal("beta",0,2); sigma=pm.HalfNormal("sigma",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 16 | `    pm.Normal("y",alpha+beta*x.to_numpy(),sigma,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 17 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 18 | `    ppc=pm.sample_posterior_predictive(idata,random_seed=42,progressbar=False)` | 사후분포에서 새로운 관측값을 생성합니다. |
| 19 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 20 | `pred=ppc.posterior_predictive["y"].values` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 21 | `print("관측 평균:",round(sensor_df["yield_percent"].mean(),3))` | 결과를 콘솔에 출력합니다. |
| 22 | `print("예측 평균:",round(pred.mean(),3))` | 결과를 콘솔에 출력합니다. |
| 23 | `print("관측 표준편차:",round(sensor_df["yield_percent"].std(),3))` | 결과를 콘솔에 출력합니다. |
| 24 | `print("예측 표준편차:",round(pred.std(),3))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?