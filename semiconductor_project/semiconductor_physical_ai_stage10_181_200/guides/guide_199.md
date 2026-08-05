# 실습 199 — lot_risk_table

## 1. 학습 목표
LOT별 추정 위험점수와 우선순위를 생성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
로지스틱 회귀 사후평균으로 LOT별 불량발생확률을 계산해 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage10
python examples\ex199_lot_risk_table.py
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
| 13 | `features=["temp_abs_deviation","pressure_abs_deviation","particle_mean"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 14 | `X=defect_df[features]; mean=X.mean(); std=X.std(); Xs=(X-mean)/std; y=(defect_df["defect_count"]>0).astype(int)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 15 | `with pm.Model(coords={"feature":features}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 16 | `    a=pm.Normal("a",0,2); beta=pm.Normal("beta",0,1,dims="feature")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `    p=pm.Deterministic("p",pm.math.sigmoid(a+pm.math.dot(Xs.to_numpy(),beta)))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `    pm.Bernoulli("y",p=p,observed=y)` | 개별 정상·불량 라벨을 베르누이분포로 연결합니다. |
| 19 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 20 | `risk=idata.posterior["p"].mean(("chain","draw")).values` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `out=defect_df[["lot_id","recipe","chamber_id","defect_rate"]].copy(); out["posterior_risk"]=risk; out=out.sort_values("posterior_risk",ascending=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `print(out.head(15).round(4)); out.to_csv(OUTPUT_DIR/"ex199_lot_risk.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 사전분포가 기존 품질 수준을 과도하게 반영하지 않는가?
2. 불량률 차이가 통계적으로뿐 아니라 비용 측면에서도 중요한가?
3. 모델 결과를 자동 정지 기준으로 사용할 때 어떤 안전장치가 필요한가?