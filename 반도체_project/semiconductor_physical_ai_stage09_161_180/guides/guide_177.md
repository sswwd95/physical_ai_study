# 실습 177 — trace_and_posterior_plot

## 1. 학습 목표
트레이스와 사후분포 그래프를 PNG로 저장합니다.

## 2. Antigravity용 하네스 프롬프트
```text
az.plot_trace와 az.plot_posterior를 Agg 백엔드로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage09
python examples\ex177_trace_and_posterior_plot.py
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
| 13 | `import matplotlib` | 필요한 라이브러리를 불러옵니다. |
| 14 | `matplotlib.use("Agg")` | 베이지안 추정 또는 진단 단계를 수행합니다. |
| 15 | `import matplotlib.pyplot as plt` | 필요한 라이브러리를 불러옵니다. |
| 16 | `obs=sensor_df["yield_percent"].to_numpy()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 17 | `with pm.Model() as model:` | PyMC 확률모형의 범위를 시작합니다. |
| 18 | `    mu=pm.Normal("mu",94,5); sigma=pm.HalfNormal("sigma",3)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 19 | `    pm.Normal("y",mu,sigma,observed=obs)` | 정규분포 사전분포 또는 관측모형을 정의합니다. |
| 20 | `    idata=pm.sample(600,tune=600,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 21 | `az.plot_trace(idata,var_names=["mu","sigma"]); plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex177_trace.png",dpi=150); plt.close()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 22 | `az.plot_posterior(idata,var_names=["mu","sigma"],hdi_prob=0.94); plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex177_posterior.png",dpi=150); plt.close()` | 계산 결과나 모형 요소를 변수에 저장합니다. |
| 23 | `print("그래프 저장 완료")` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 사전분포가 실제 공정 지식과 일치하는가?
2. R-hat과 유효표본크기가 충분한가?
3. 점 추정 대신 HDI와 사후예측분포를 함께 전달했는가?