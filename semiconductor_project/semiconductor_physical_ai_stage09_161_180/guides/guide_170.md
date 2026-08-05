# 실습 170 — hierarchical_chamber_model

## 1. 학습 목표
챔버별 평균 수율을 부분 풀링하는 계층모형을 작성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
챔버별 효과를 전체 평균 mu_global과 tau로부터 생성하는 비중심 계층모형으로 작성하라.
챔버별 평균 수율의 사후요약을 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex170_hierarchical_chamber_model.py
```

## 4. 예상 결과
챔버별 추정값이 전체 평균 쪽으로 부분 풀링되어 저장됩니다.

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
| 13 | `codes,chambers=pd.factorize(sensor_df["chamber_id"],sort=True)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `with pm.Model(coords={"chamber":chambers}) as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 15 | `    mu_global=pm.Normal("mu_global",94,5)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 16 | `    tau=pm.HalfNormal("tau",2)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 17 | `    z=pm.Normal("z",0,1,dims="chamber")` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 18 | `    mu_chamber=pm.Deterministic("mu_chamber",mu_global+z*tau,dims="chamber")` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 19 | `    sigma=pm.HalfNormal("sigma",3)` | 0보다 큰 표준편차용 사전분포를 정의합니다. |
| 20 | `    pm.Normal("y",mu_chamber[codes],sigma,observed=sensor_df["yield_percent"])` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 21 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False,target_accept=0.9)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 23 | `summary=az.summary(idata,var_names=["mu_global","tau","mu_chamber"],hdi_prob=0.94)` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |
| 24 | `print(summary)` | 결과를 콘솔에 출력합니다. |
| 25 | `summary.to_csv(OUTPUT_DIR/"ex170_hierarchical_chamber.csv",encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?