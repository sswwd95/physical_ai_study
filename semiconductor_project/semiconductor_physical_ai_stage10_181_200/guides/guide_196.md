# 실습 196 — relative_risk_hdi

## 1. 학습 목표
상대위험도의 HDI와 목표 이하 확률을 계산합니다.

## 2. Antigravity용 하네스 프롬프트
```text
pC/pA의 평균·HDI·P(RR<1.2)를 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage10
python examples\ex196_relative_risk_hdi.py
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
| 13 | `g=defect_df.groupby("recipe")[["wafer_count","defect_count"]].sum()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 14 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 15 | `    pA=pm.Beta("pA",1,1); pC=pm.Beta("pC",1,1)` | 0~1 확률용 베타 사전분포를 정의합니다. |
| 16 | `    pm.Binomial("dA",n=int(g.loc["ETCH-A","wafer_count"]),p=pA,observed=int(g.loc["ETCH-A","defect_count"]))` | 불량 개수를 이항분포 관측값으로 연결합니다. |
| 17 | `    pm.Binomial("dC",n=int(g.loc["ETCH-C","wafer_count"]),p=pC,observed=int(g.loc["ETCH-C","defect_count"]))` | 불량 개수를 이항분포 관측값으로 연결합니다. |
| 18 | `    rr=pm.Deterministic("rr",pC/pA)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    idata=pm.sample(1000,tune=1000,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 20 | `s=idata.posterior["rr"].values.ravel(); print("RR mean:",round(s.mean(),4)); print("94% HDI:",az.hdi(s,hdi_prob=.94)); print("P(RR<1.2):",round((s<1.2).mean(),4))` | 최고밀도구간을 계산합니다. |

## 6. 실무 확인 질문
1. 사전분포가 기존 품질 수준을 과도하게 반영하지 않는가?
2. 불량률 차이가 통계적으로뿐 아니라 비용 측면에서도 중요한가?
3. 모델 결과를 자동 정지 기준으로 사용할 때 어떤 안전장치가 필요한가?