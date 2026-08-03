# 실습 187 — hierarchical_recipe_model

## 1. 학습 목표
레시피별 불량률을 계층적으로 부분 풀링합니다.

## 2. Antigravity용 하네스 프롬프트
```text
logit 불량률에 전체 평균과 레시피 랜덤효과를 둔 계층모형을 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage10
python examples\ex187_hierarchical_recipe_model.py
```

## 4. 예상 결과
요청한 베이지안 불량률 분석 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `import pymc as pm` | 필요한 라이브러리를 불러옵니다. |
| 5 | `import arviz as az` | 필요한 라이브러리를 불러옵니다. |
| 6 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 7 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_defect_rate_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 11 | `defect_df = pd.read_csv(DATA_FILE)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `codes,recipes=pd.factorize(defect_df["recipe"],sort=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 14 | `with pm.Model(coords={"recipe":recipes}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 15 | `    a=pm.Normal("a",-3,1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `    tau=pm.HalfNormal("tau",1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `    z=pm.Normal("z",0,1,dims="recipe")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    logit_p=a+z[codes]*tau` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    p=pm.Deterministic("p",pm.math.sigmoid(logit_p))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    pm.Binomial("d",n=defect_df["wafer_count"],p=p,observed=defect_df["defect_count"])` | 불량 개수를 이항분포 관측값으로 연결합니다. |
| 21 | `    idata=pm.sample(900,tune=900,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `print(az.summary(idata,var_names=["a","tau","z"]))` | 사후요약과 MCMC 진단값을 계산합니다. |

## 6. 실무 확인 질문
1. 사전분포가 기존 품질 수준을 과도하게 반영하지 않는가?
2. 불량률 차이가 통계적으로뿐 아니라 비용 측면에서도 중요한가?
3. 모델 결과를 자동 정지 기준으로 사용할 때 어떤 안전장치가 필요한가?