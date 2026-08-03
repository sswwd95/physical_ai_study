# 실습 265 — pairwise_superiority

## 1. 학습 목표
모든 레시피 쌍의 우월확률을 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
모든 레시피 쌍의 우월확률과 평균 차이를 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex265_pairwise_superiority.py
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
| 14 | `codes,recipes=pd.factorize(experiment_df["recipe"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `with pm.Model(coords={"recipe":recipes}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 16 | `    mu=pm.Normal("mu",95,3,dims="recipe"); sigma=pm.HalfNormal("sigma",2)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 17 | `    pm.Normal("y",mu[codes],sigma,observed=experiment_df["uniformity_percent"])` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 18 | `    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 19 | `arr=idata.posterior["mu"].stack(sample=("chain","draw")).values` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `rows=[]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 21 | `for i in range(len(recipes)):` | 여러 조건이나 그룹을 반복 분석합니다. |
| 22 | `    for j in range(i+1,len(recipes)):` | 여러 조건이나 그룹을 반복 분석합니다. |
| 23 | `        d=arr[i]-arr[j]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 24 | `        rows.append({"condition_a":recipes[i],"condition_b":recipes[j],"p_a_better":float((d>0).mean()),"mean_difference":float(d.mean())})` | 베이지안 실험분석 단계를 수행합니다. |
| 25 | `out=pd.DataFrame(rows)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 26 | `print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex265_pairwise_superiority.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?