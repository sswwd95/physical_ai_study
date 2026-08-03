# 실습 249 — maintenance_policy_effect

## 1. 학습 목표
정비 정책별 수명 차이의 사후확률을 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
condition_based 정책이 reactive보다 수명이 길 확률을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage13
python examples\ex249_maintenance_policy_effect.py
```

## 4. 예상 결과
요청한 베이지안 수명·고장확률·RUL 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 8 | `LIFE_FILE = ROOT / "data" / "bayesian_equipment_lifetime.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 9 | `RUL_FILE = ROOT / "data" / "bayesian_rul_snapshots.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 11 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `life_df = pd.read_csv(LIFE_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 14 | `rul_df = pd.read_csv(RUL_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 16 | `codes,policies=pd.factorize(life_df["maintenance_policy"],sort=True)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 17 | `y=np.log(life_df["observed_cycles"].to_numpy())` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 18 | `with pm.Model(coords={"policy":policies}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 19 | `    a=pm.Normal("a",np.log(120),1); effect=pm.Normal("effect",0,.5,dims="policy"); sigma=pm.HalfNormal("sigma",.5)` | 회귀계수나 그룹 효과의 정규 사전분포를 정의합니다. |
| 20 | `    pm.Normal("log_life",a+effect[codes],sigma,observed=y)` | 회귀계수나 그룹 효과의 정규 사전분포를 정의합니다. |
| 21 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `arr=idata.posterior["effect"].stack(sample=("chain","draw")).values` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 23 | `cb=list(policies).index("condition_based"); reactive=list(policies).index("reactive")` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 24 | `diff=arr[cb]-arr[reactive]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 25 | `print("P(condition_based > reactive):",round((diff>0).mean(),4))` | 결과를 콘솔에 출력합니다. |
| 26 | `print("94% HDI:",az.hdi(diff,hdi_prob=.94))` | 최고밀도구간을 계산합니다. |

## 6. 실무 확인 질문
1. 검열 데이터가 왜 발생했으며 관측 종료 기준은 무엇인가?
2. 장비별 차이를 계층모형으로 반영했는가?
3. 보수적인 RUL 하한과 정비 비용을 함께 고려했는가?