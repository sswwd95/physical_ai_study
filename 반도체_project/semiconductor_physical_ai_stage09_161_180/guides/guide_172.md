# 실습 172 — robust_student_t_model

## 1. 학습 목표
Student-t 관측모형으로 극단값에 강한 수율 추정을 수행합니다.

## 2. Antigravity용 하네스 프롬프트
```text
Normal 대신 StudentT(nu,mu,sigma) 관측모형을 사용하고 nu~Exponential(1/10)+1로 정의하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex172_robust_student_t_model.py
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
| 13 | `obs=sensor_df["yield_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 14 | `with pm.Model() as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 15 | `    mu=pm.Normal("mu",94,5); sigma=pm.HalfNormal("sigma",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 16 | `    nu_minus_one=pm.Exponential("nu_minus_one",1/10)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `    nu=pm.Deterministic("nu",nu_minus_one+1)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 18 | `    pm.StudentT("y",nu=nu,mu=mu,sigma=sigma,observed=obs)` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 19 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 20 | `print(az.summary(idata,var_names=["mu","sigma","nu"]))` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?