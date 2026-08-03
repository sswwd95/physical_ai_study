# 실습 278 — loo_interaction_comparison

## 1. 학습 목표
교호작용 포함·제외 모형을 LOO로 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
가법모형과 교호작용 모형을 LOO로 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex278_loo_interaction_comparison.py
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
| 14 | `r_codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `p_codes,pressures=pd.factorize(experiment_df["pressure_level"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `models={}` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `with pm.Model(coords={"recipe":recipes,"pressure":pressures}) as additive:` | PyMC 확률모형 범위를 시작합니다. |
| 18 | `    a=pm.Normal("a",95,3); r=pm.Normal("r",0,1,dims="recipe"); p=pm.Normal("p",0,1,dims="pressure"); s=pm.HalfNormal("s",2)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 19 | `    pm.Normal("y",a+r[r_codes]+p[p_codes],s,observed=experiment_df["uniformity_percent"])` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 20 | `    models["additive"]=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})` | MCMC로 사후분포 표본을 추출합니다. |
| 21 | `with pm.Model(coords={"recipe":recipes,"pressure":pressures}) as interaction_model:` | PyMC 확률모형 범위를 시작합니다. |
| 22 | `    a=pm.Normal("a",95,3); r=pm.Normal("r",0,1,dims="recipe"); p=pm.Normal("p",0,1,dims="pressure")` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 23 | `    inter=pm.Normal("inter",0,.7,dims=("recipe","pressure")); s=pm.HalfNormal("s",2)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 24 | `    pm.Normal("y",a+r[r_codes]+p[p_codes]+inter[r_codes,p_codes],s,observed=experiment_df["uniformity_percent"])` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 25 | `    models["interaction"]=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False,idata_kwargs={"log_likelihood":True})` | MCMC로 사후분포 표본을 추출합니다. |
| 26 | `print(az.compare(models))` | LOO 기반으로 여러 베이지안 모형을 비교합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?