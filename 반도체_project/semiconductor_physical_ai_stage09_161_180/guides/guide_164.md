# 실습 164 — recipe_group_means

## 1. 학습 목표
레시피별 평균 수율의 사후분포를 각각 추정합니다.

## 2. Antigravity용 하네스 프롬프트
```text
recipe를 정수 인덱스로 바꾸고 레시피별 mu를 Normal(94,4), 공통 sigma를 HalfNormal(3)로 두어
그룹 평균 모형을 작성하라. 레시피별 사후요약을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex164_recipe_group_means.py
```

## 4. 예상 결과
ETCH-A/B/C의 평균 수율 사후분포가 비교됩니다.

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
| 14 | `with pm.Model(coords={"recipe": recipes}) as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 15 | `    mu_recipe = pm.Normal("mu_recipe", 94, 4, dims="recipe")` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 16 | `    sigma = pm.HalfNormal("sigma", 3)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 17 | `    pm.Normal("y", mu=mu_recipe[codes], sigma=sigma, observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `    idata = pm.sample(1000, tune=1000, chains=2, cores=1, random_seed=42, progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 19 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 20 | `summary = az.summary(idata, var_names=["mu_recipe"], hdi_prob=0.94)` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |
| 21 | `print(summary)` | 결과를 콘솔에 출력합니다. |
| 22 | `summary.to_csv(OUTPUT_DIR/"ex164_recipe_means.csv",encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?