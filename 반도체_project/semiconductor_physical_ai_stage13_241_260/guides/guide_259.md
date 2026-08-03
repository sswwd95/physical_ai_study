# 실습 259 — maintenance_decision_cost

## 1. 학습 목표
정비·고장 비용을 결합해 행동을 선택합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
고장비용 5000, 정비비용 1200으로 행동별 기대비용을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage13
python examples\ex259_maintenance_decision_cost.py
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
| 16 | `obs=life_df.loc[life_df["event_observed"]==1,"observed_cycles"].to_numpy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 17 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 18 | `    alpha=pm.HalfNormal("alpha",3); beta=pm.HalfNormal("beta",150); pm.Weibull("life",alpha=alpha,beta=beta,observed=obs)` | 설비 수명을 Weibull 분포로 모델링합니다. |
| 19 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 20 | `a=idata.posterior["alpha"].values.ravel(); b=idata.posterior["beta"].values.ravel()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 21 | `rows=[]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 22 | `failure_cost=5000; maintenance_cost=1200` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 23 | `for _,r in life_df.iterrows():` | 여러 장비·그룹·정책을 반복 분석합니다. |
| 24 | `    t=r["observed_cycles"]; p=1-np.exp(-(((t+20)/b)**a-(t/b)**a))` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 25 | `    wait_cost=p*failure_cost; maintain=np.full_like(p,maintenance_cost)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 26 | `    rows.append({"equipment_id":r["equipment_id"],"p_maintain_better":float((maintain<wait_cost).mean()),"expected_wait_cost":wait_cost.mean(),"maintenance_cost":maintenance_cost})` | 베이지안 수명·고장확률·RUL 분석 단계를 수행합니다. |
| 27 | `out=pd.DataFrame(rows).sort_values("p_maintain_better",ascending=False)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 28 | `print(out.head(10).round(2)); out.to_csv(OUTPUT_DIR/"ex259_maintenance_decision.csv",index=False,encoding="utf-8-sig")` | 분석 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 검열 데이터가 왜 발생했으며 관측 종료 기준은 무엇인가?
2. 장비별 차이를 계층모형으로 반영했는가?
3. 보수적인 RUL 하한과 정비 비용을 함께 고려했는가?