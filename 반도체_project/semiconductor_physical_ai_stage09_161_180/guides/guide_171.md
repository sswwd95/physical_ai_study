# 실습 171 — prior_sensitivity

## 1. 학습 목표
사전분포 폭에 따른 회귀계수 변화를 비교합니다.

## 2. Antigravity용 하네스 프롬프트
```text
약한 사전 beta~Normal(0,5)와 강한 사전 beta~Normal(0,0.5)를 각각 적합하고 beta 평균을 비교하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex171_prior_sensitivity.py
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
| 13 | `x=(sensor_df["particle_mean"]-sensor_df["particle_mean"].mean())/sensor_df["particle_mean"].std()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `rows=[]` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 15 | `for prior_sigma in [5.0,0.5]:` | 여러 그룹이나 모형에 같은 작업을 반복합니다. |
| 16 | `    with pm.Model() as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 17 | `        a=pm.Normal("a",94,5); b=pm.Normal("b",0,prior_sigma); s=pm.HalfNormal("s",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `        pm.Normal("y",a+b*x.to_numpy(),s,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 19 | `        idata=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 20 | `    rows.append({"prior_sigma":prior_sigma,"beta_mean":float(idata.posterior["b"].mean())})` | 베이지안 추정 또는 진단 단계를 수행합니다. |
| 21 | `print(pd.DataFrame(rows))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?