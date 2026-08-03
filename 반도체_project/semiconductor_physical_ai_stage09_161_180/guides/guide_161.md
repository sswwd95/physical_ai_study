# 실습 161 — prior_predictive_yield

## 1. 학습 목표
사전예측분포로 수율 사전분포의 현실성을 확인합니다.

## 2. Antigravity용 하네스 프롬프트
```text
평균 수율 mu~Normal(94,3), sigma~HalfNormal(2), y~Normal(mu,sigma)인 PyMC 모형을 만들고
사전예측 1000개를 생성하여 범위와 평균을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex161_prior_predictive_yield.py
```

## 4. 예상 결과
수율 사전예측분포가 물리적으로 가능한 범위인지 확인합니다.

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
| 13 | `with pm.Model() as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 14 | `    mu = pm.Normal("mu", mu=94, sigma=3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 15 | `    sigma = pm.HalfNormal("sigma", sigma=2)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 16 | `    y = pm.Normal("y", mu=mu, sigma=sigma)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 17 | `    prior = pm.sample_prior_predictive(samples=1000, random_seed=42)` | 데이터를 보기 전 사전예측분포를 생성합니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `values = prior.prior_predictive["y"].values.ravel()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `print("사전예측 평균:", round(values.mean(), 3))` | 결과를 콘솔에 출력합니다. |
| 21 | `print("사전예측 범위:", round(values.min(), 3), "~", round(values.max(), 3))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?