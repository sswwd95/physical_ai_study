# 실습 272 — hierarchical_experiment_model

## 1. 학습 목표
챔버별 변동을 부분 풀링하는 계층 실험모형을 작성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
챔버 효과를 부분 풀링하는 계층 실험모형을 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex272_hierarchical_experiment_model.py
```

## 4. 예상 결과
요청한 베이지안 실험분석 결과가 출력 또는 저장됩니다.

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
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 11 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 12 | `experiment_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `c_codes,chambers=pd.factorize(experiment_df["chamber_id"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `r_codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `with pm.Model(coords={"chamber":chambers,"recipe":recipes}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 17 | `    a=pm.Normal("a",95,3); tau=pm.HalfNormal("tau",1); z=pm.Normal("z",0,1,dims="chamber")` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 18 | `    chamber_eff=pm.Deterministic("chamber_eff",z*tau,dims="chamber")` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 19 | `    recipe_eff=pm.Normal("recipe_eff",0,1,dims="recipe")` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 20 | `    sigma=pm.HalfNormal("sigma",2)` | 0보다 큰 표준편차 파라미터를 정의합니다. |
| 21 | `    pm.Normal("y",a+chamber_eff[c_codes]+recipe_eff[r_codes],sigma,observed=experiment_df["uniformity_percent"])` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 22 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 23 | `print(az.summary(idata,var_names=["tau","chamber_eff","recipe_eff"],hdi_prob=.94))` | 사후요약과 MCMC 진단값을 계산합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?