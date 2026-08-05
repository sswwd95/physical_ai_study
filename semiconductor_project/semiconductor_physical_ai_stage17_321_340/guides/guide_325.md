# 실습 325 — posterior_sensor_weights

## 1. 학습 목표
센서 노이즈 사후분포로 가중치를 계산합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
센서 노이즈 사후표본의 역분산으로 가중치 분포를 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage17
python examples\ex325_posterior_sensor_weights.py
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
| 14 | `data=sensor_df[["temp_sensor_a_c","temp_sensor_b_c","true_temperature_c"]].dropna()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `ra=data["temp_sensor_a_c"]-data["true_temperature_c"]; rb=data["temp_sensor_b_c"]-data["true_temperature_c"]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 16 | `with pm.Model() as model:` | PyMC 확률모형 범위를 시작합니다. |
| 17 | `    sa=pm.HalfNormal("sa",1); sb=pm.HalfNormal("sb",1)` | 0보다 큰 센서 노이즈 표준편차를 정의합니다. |
| 18 | `    ba=pm.Normal("ba",0,2); bb=pm.Normal("bb",0,2)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 19 | `    pm.Normal("a",ba,sa,observed=ra); pm.Normal("b",bb,sb,observed=rb)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 20 | `    idata=pm.sample(900,tune=900,chains=2,cores=1,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 21 | `sa=idata.posterior["sa"].values.ravel(); sb=idata.posterior["sb"].values.ravel()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 22 | `wa=(1/sa**2)/((1/sa**2)+(1/sb**2))` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 23 | `print("센서 A 평균 가중치:",round(wa.mean(),4))` | 결과를 콘솔에 출력합니다. |
| 24 | `print("94% HDI:",az.hdi(wa,hdi_prob=.94))` | 최고밀도구간을 계산합니다. |

## 6. 실무 확인 질문
1. 센서 바이어스와 실제 공정 변화를 구분했는가?
2. 사후예측구간이 너무 좁거나 넓지 않은가?
3. 이상확률을 자동 제어에 사용할 때 안전 임계값이 있는가?