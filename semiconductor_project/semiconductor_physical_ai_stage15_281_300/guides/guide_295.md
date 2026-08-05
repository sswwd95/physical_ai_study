# 실습 295 — bayesian_linear_surrogate

## 1. 학습 목표
PyMC 베이지안 회귀 대리모델을 작성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
PyMC 다중 선형 회귀로 균일도 베이지안 대리모델을 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage15
python examples\ex295_bayesian_linear_surrogate.py
```

## 4. 예상 결과
요청한 공정 최적화·베이지안 의사결정 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `HISTORY_FILE = ROOT / "data" / "process_optimization_history.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `CANDIDATE_FILE = ROOT / "data" / "optimization_candidates.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 11 | `history_df = pd.read_csv(HISTORY_FILE)` | 과거 공정 기록 또는 후보 조건 CSV를 읽습니다. |
| 12 | `candidate_df = pd.read_csv(CANDIDATE_FILE)` | 과거 공정 기록 또는 후보 조건 CSV를 읽습니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `import pymc as pm` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 15 | `import arviz as az` | 필요한 라이브러리나 최적화 모델을 불러옵니다. |
| 16 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 17 | `features=["pressure_pa","rf_power_w","gas_flow_sccm","temperature_c"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `X=history_df[features]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `X=(X-X.mean())/X.std()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `y=history_df["uniformity_percent"].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 22 | `with pm.Model(coords={"feature":features}) as model:` | 베이지안 최적화용 확률모형을 정의합니다. |
| 23 | `    alpha=pm.Normal("alpha",96,3)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `    beta=pm.Normal("beta",0,1,dims="feature")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    sigma=pm.HalfNormal("sigma",2)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 26 | `    mu=alpha+pm.math.dot(X.to_numpy(),beta)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    pm.Normal("y",mu,sigma,observed=y)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 29 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 30 | `summary=az.summary(idata,var_names=["alpha","beta","sigma"],hdi_prob=.94)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `print(summary)` | 결과를 콘솔에 출력합니다. |
| 32 | `summary.to_csv(OUTPUT_DIR/"ex295_bayesian_surrogate.csv",encoding="utf-8-sig")` | 추천 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 목적함수와 제약조건이 실제 품질·안전 기준을 반영하는가?
2. 추천 조건이 과거 운전 범위를 벗어나지 않는가?
3. 최적 조건을 바로 양산에 적용하지 않고 확인 실험을 거치는가?