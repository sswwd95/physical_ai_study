# 실습 266 — effect_size_rope

## 1. 학습 목표
효과크기와 ROPE로 실질적 차이를 판단합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
ETCH-A와 ETCH-C의 표준화 효과크기와 ROPE 확률을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage14
python examples\ex266_effect_size_rope.py
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
| 15 | `c=experiment_df.loc[experiment_df["recipe"]=="ETCH-C","uniformity_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 17 | `    mu_a=pm.Normal("mu_a",95,3); mu_c=pm.Normal("mu_c",95,3)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 18 | `    sigma=pm.HalfNormal("sigma",2)` | 0보다 큰 표준편차 파라미터를 정의합니다. |
| 19 | `    effect=pm.Deterministic("effect",(mu_a-mu_c)/sigma)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `    pm.Normal("a",mu_a,sigma,observed=a); pm.Normal("c",mu_c,sigma,observed=c)` | 평균·효과·회귀계수에 정규 사전분포를 정의합니다. |
| 21 | `    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `s=idata.posterior["effect"].values.ravel()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 23 | `print("표준화 효과크기:",round(s.mean(),4))` | 결과를 콘솔에 출력합니다. |
| 24 | `print("P(\|effect\|<0.1):",round((np.abs(s)<.1).mean(),4))` | 결과를 콘솔에 출력합니다. |
| 25 | `print("94% HDI:",az.hdi(s,hdi_prob=.94))` | 최고밀도구간을 계산합니다. |

## 6. 실무 확인 질문
1. 실험 조건이 무작위화·반복·블로킹 원칙을 만족하는가?
2. 통계적 우월성과 공정상 의미 있는 효과크기를 구분했는가?
3. 최적 조건 선정 시 수율·불량률·안전·원가를 함께 고려했는가?