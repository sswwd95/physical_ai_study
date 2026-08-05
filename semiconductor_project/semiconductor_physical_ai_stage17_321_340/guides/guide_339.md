# 실습 339 — mcmc_diagnostics_sensor

## 1. 학습 목표
R-hat·ESS·Divergence와 사후그래프를 저장합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
R-hat·ESS·Divergence와 사후분포 그래프를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage17
python examples\ex339_mcmc_diagnostics_sensor.py
```

## 4. 예상 결과
요청한 베이지안 센서 융합·디지털 트윈 불확실성 결과가 출력 또는 저장됩니다.

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
| 8 | `DATA_FILE = ROOT / "data" / "bayesian_sensor_fusion.csv"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 9 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 10 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 11 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 12 | `sensor_df = pd.read_csv(DATA_FILE)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 13 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 14 | `import matplotlib` | 필요한 라이브러리를 불러옵니다. |
| 15 | `matplotlib.use("Agg")` | 베이지안 센서 융합 또는 트윈 불확실성 분석을 수행합니다. |
| 16 | `import matplotlib.pyplot as plt` | 필요한 라이브러리를 불러옵니다. |
| 17 | `res=(sensor_df["temp_sensor_a_c"]-sensor_df["true_temperature_c"]).dropna().to_numpy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 18 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 19 | `    mu=pm.Normal("mu",0,2); sigma=pm.HalfNormal("sigma",1)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 20 | `    pm.Normal("r",mu,sigma,observed=res)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 21 | `    idata=pm.sample(800,tune=800,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 22 | `summary=az.summary(idata,var_names=["mu","sigma"])` | 사후요약과 MCMC 진단값을 계산합니다. |
| 23 | `div=int(idata.sample_stats["diverging"].sum())` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 24 | `summary.assign(divergence_count=div).to_csv(OUTPUT_DIR/"ex339_mcmc_diagnostics.csv",encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |
| 25 | `az.plot_posterior(idata,var_names=["mu","sigma"],hdi_prob=.94)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 26 | `plt.tight_layout(); plt.savefig(OUTPUT_DIR/"ex339_sensor_posterior.png",dpi=150); plt.close()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 27 | `print(summary)` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 센서 바이어스와 실제 공정 변화를 구분했는가?
2. 사후예측구간이 너무 좁거나 넓지 않은가?
3. 이상확률을 자동 제어에 사용할 때 안전 임계값이 있는가?