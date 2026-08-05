# 실습 165 — recipe_difference_probability

## 1. 학습 목표
두 레시피 평균 차이의 사후확률을 계산합니다.

## 2. Antigravity용 하네스 프롬프트
```text
ETCH-A와 ETCH-C 평균 차이를 deterministic 변수 diff_A_C로 정의하고
P(diff>0), 평균 차이, 94% HDI를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex165_recipe_difference_probability.py
```

## 4. 예상 결과
ETCH-A가 ETCH-C보다 높은 수율을 가질 사후확률이 계산됩니다.

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
| 13 | `codes, recipes = pd.factorize(sensor_df["recipe"], sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `a_idx = list(recipes).index("ETCH-A")` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `c_idx = list(recipes).index("ETCH-C")` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `with pm.Model(coords={"recipe": recipes}) as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 17 | `    mu_recipe = pm.Normal("mu_recipe", 94, 4, dims="recipe")` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `    sigma = pm.HalfNormal("sigma", 3)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 19 | `    diff_A_C = pm.Deterministic("diff_A_C", mu_recipe[a_idx]-mu_recipe[c_idx])` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `    pm.Normal("y", mu_recipe[codes], sigma, observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 21 | `    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `d = idata.posterior["diff_A_C"].values.ravel()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 24 | `print("평균 차이:", round(d.mean(),4))` | 결과를 콘솔에 출력합니다. |
| 25 | `print("P(A>C):", round((d>0).mean(),4))` | 결과를 콘솔에 출력합니다. |
| 26 | `print("94% HDI:", az.hdi(d,hdi_prob=0.94))` | 지정 확률의 최고밀도구간을 계산합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?