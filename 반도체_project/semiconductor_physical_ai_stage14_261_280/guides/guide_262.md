# 실습 262 — recipe_ab_uniformity

## 1. 학습 목표
두 레시피의 균일도 차이를 베이지안 A/B로 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
ETCH-A와 ETCH-B 균일도 차이의 사후분포와 우월확률을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex262_recipe_ab_uniformity.py
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
| 14 | `data = experiment_df.loc[experiment_df["recipe"].isin(["ETCH-A","ETCH-B"])]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `a = data.loc[data["recipe"]=="ETCH-A","uniformity_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `b = data.loc[data["recipe"]=="ETCH-B","uniformity_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 18 | `    mu_a=pm.Normal("mu_a",95,3); mu_b=pm.Normal("mu_b",95,3)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 19 | `    sigma_a=pm.HalfNormal("sigma_a",2); sigma_b=pm.HalfNormal("sigma_b",2)` | 0보다 큰 표준편차 파라미터를 정의합니다. |
| 20 | `    diff=pm.Deterministic("diff",mu_a-mu_b)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 21 | `    pm.Normal("y_a",mu_a,sigma_a,observed=a)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 22 | `    pm.Normal("y_b",mu_b,sigma_b,observed=b)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 23 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 24 | `s=idata.posterior["diff"].values.ravel()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 25 | `print("평균 차이:",round(s.mean(),4))` | 결과를 콘솔에 출력합니다. |
| 26 | `print("P(A>B):",round((s>0).mean(),4))` | 결과를 콘솔에 출력합니다. |
| 27 | `print("94% HDI:",az.hdi(s,hdi_prob=.94))` | 최고밀도구간을 계산합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?