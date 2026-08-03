# 실습 334 — sensor_fault_probability

## 1. 학습 목표
센서 바이어스가 허용범위를 넘을 확률을 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 센서 바이어스가 1도·2도를 넘을 사후확률을 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage17
python examples\ex334_sensor_fault_probability.py
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
| 14 | `res=(sensor_df["temp_sensor_b_c"]-sensor_df["true_temperature_c"]).dropna().to_numpy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 16 | `    bias=pm.Normal("bias",0,2); sigma=pm.HalfNormal("sigma",1)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 17 | `    pm.Normal("r",bias,sigma,observed=res)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 18 | `    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 19 | `s=idata.posterior["bias"].values.ravel()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 20 | `print("P(\|bias\|>1.0):",round((np.abs(s)>1.0).mean(),4))` | 결과를 콘솔에 출력합니다. |
| 21 | `print("P(\|bias\|>2.0):",round((np.abs(s)>2.0).mean(),4))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 센서 바이어스와 실제 공정 변화를 구분했는가?
2. 사후예측구간이 너무 좁거나 넓지 않은가?
3. 이상확률을 자동 제어에 사용할 때 안전 임계값이 있는가?