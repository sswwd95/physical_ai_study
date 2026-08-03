# 실습 178 — hierarchical_recipe_chamber

## 1. 학습 목표
레시피와 챔버 효과를 함께 가진 계층 회귀를 작성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
레시피 고정효과와 챔버 랜덤효과를 함께 포함한 수율 모형을 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex178_hierarchical_recipe_chamber.py
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
| 13 | `r_codes,recipes=pd.factorize(sensor_df["recipe"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `c_codes,chambers=pd.factorize(sensor_df["chamber_id"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `with pm.Model(coords={"recipe":recipes,"chamber":chambers}) as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 16 | `    a=pm.Normal("a",94,5); br=pm.Normal("br",0,1,dims="recipe")` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 17 | `    tau=pm.HalfNormal("tau",1); z=pm.Normal("z",0,1,dims="chamber")` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `    bc=pm.Deterministic("bc",z*tau,dims="chamber")` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 19 | `    s=pm.HalfNormal("s",3)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 20 | `    pm.Normal("y",a+br[r_codes]+bc[c_codes],s,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 21 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,target_accept=0.9,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `print(az.summary(idata,var_names=["a","br","tau","bc"]))` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?