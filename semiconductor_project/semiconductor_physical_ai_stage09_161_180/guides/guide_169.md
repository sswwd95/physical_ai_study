# 실습 169 — out_of_sample_prediction

## 1. 학습 목표
새 공정 조건의 수율 사후예측분포를 계산합니다.

## 2. Antigravity용 하네스 프롬프트
```text
입자 표준화 회귀모형에서 particle_mean=8인 새 조건의 mu_new를 deterministic으로 정의하고
사후 평균과 94% HDI를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex169_out_of_sample_prediction.py
```

## 4. 예상 결과
입자 평균 8인 조건의 기대 수율과 불확실성 구간이 출력됩니다.

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
| 13 | `m=sensor_df["particle_mean"].mean(); s=sensor_df["particle_mean"].std()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `x=(sensor_df["particle_mean"]-m)/s` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `x_new=(8.0-m)/s` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 16 | `with pm.Model() as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 17 | `    alpha=pm.Normal("alpha",94,5); beta=pm.Normal("beta",0,2); sigma=pm.HalfNormal("sigma",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `    mu_new=pm.Deterministic("mu_new",alpha+beta*x_new)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 19 | `    pm.Normal("y",alpha+beta*x.to_numpy(),sigma,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 20 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `v=idata.posterior["mu_new"].values.ravel()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 23 | `print("새 조건 평균 예측:",round(v.mean(),3))` | 결과를 콘솔에 출력합니다. |
| 24 | `print("94% HDI:",az.hdi(v,hdi_prob=0.94))` | 지정 확률의 최고밀도구간을 계산합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?