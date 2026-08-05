# 실습 176 — diagnostic_summary

## 1. 학습 목표
R-hat, ESS, divergence로 MCMC 품질을 점검합니다.

## 2. Antigravity용 하네스 프롬프트
```text
az.summary와 sample_stats.diverging 합계를 출력하고 진단 CSV를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex176_diagnostic_summary.py
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
| 16 | `    pm.Normal("y",mu,sigma,observed=obs)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 17 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 18 | `summary=az.summary(idata,var_names=["mu","sigma"])` | 사후 평균, HDI, R-hat, 유효표본크기를 요약합니다. |
| 19 | `div=int(idata.sample_stats["diverging"].sum())` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 20 | `print(summary); print("divergence:",div)` | 결과를 콘솔에 출력합니다. |
| 21 | `summary.assign(divergence_count=div).to_csv(OUTPUT_DIR/"ex176_diagnostics.csv",encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?