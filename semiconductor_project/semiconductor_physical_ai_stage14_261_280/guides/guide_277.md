# 실습 277 — sequential_experiment_update

## 1. 학습 목표
1차·2차 데이터로 사후분포 갱신을 비교합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
1차 데이터와 전체 데이터로 사후분포 갱신 폭을 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex277_sequential_experiment_update.py
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
| 14 | `a=experiment_df.loc[experiment_df["recipe"]=="ETCH-A","uniformity_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `first=a[:len(a)//2]; second=a` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `rows=[]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `for name,data in [("phase1",first),("phase1_plus_phase2",second)]:` | 여러 조건이나 그룹을 반복 분석합니다. |
| 18 | `    with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 19 | `        mu=pm.Normal("mu",95,3); sigma=pm.HalfNormal("sigma",2)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 20 | `        pm.Normal("y",mu,sigma,observed=data)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 21 | `        idata=pm.sample(700,tune=700,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `    s=idata.posterior["mu"].values.ravel()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 23 | `    h=az.hdi(s,hdi_prob=.94)` | 최고밀도구간을 계산합니다. |
| 24 | `    rows.append({"phase":name,"posterior_mean":s.mean(),"hdi_low":h[0],"hdi_high":h[1]})` | 베이지안 실험분석 단계를 수행합니다. |
| 25 | `out=pd.DataFrame(rows)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 26 | `print(out.round(4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?