# 실습 329 — latent_temperature_state

## 1. 학습 목표
잠재 온도 상태를 GaussianRandomWalk로 추정합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
GaussianRandomWalk 잠재 온도 상태공간 모형을 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage17
python examples\ex329_latent_temperature_state.py
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
| 14 | `data=sensor_df[["temp_sensor_a_c","temp_sensor_b_c"]].interpolate(limit_direction="both").iloc[:160]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `with pm.Model(coords={"time":np.arange(len(data))}) as model:` | PyMC 확률모형 범위를 시작합니다. |
| 16 | `    sigma_state=pm.HalfNormal("sigma_state",1)` | 0보다 큰 센서 노이즈 표준편차를 정의합니다. |
| 17 | `    latent=pm.GaussianRandomWalk("latent",sigma=sigma_state,init_dist=pm.Normal.dist(25,3),dims="time")` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 18 | `    ba=pm.Normal("ba",0,2); bb=pm.Normal("bb",0,2)` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 19 | `    sa=pm.HalfNormal("sa",1); sb=pm.HalfNormal("sb",1)` | 0보다 큰 센서 노이즈 표준편차를 정의합니다. |
| 20 | `    pm.Normal("a",latent+ba,sa,observed=data["temp_sensor_a_c"],dims="time")` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 21 | `    pm.Normal("b",latent+bb,sb,observed=data["temp_sensor_b_c"],dims="time")` | 센서 바이어스·참값·관측값의 정규분포를 정의합니다. |
| 22 | `    idata=pm.sample(700,tune=700,chains=2,cores=1,target_accept=.9,random_seed=42,progressbar=False)` | MCMC로 사후분포 표본을 추출합니다. |
| 23 | `print(az.summary(idata,var_names=["sigma_state","ba","bb","sa","sb"]))` | 사후요약과 MCMC 진단값을 계산합니다. |

## 6. 실무 확인 질문
1. 센서 바이어스와 실제 공정 변화를 구분했는가?
2. 사후예측구간이 너무 좁거나 넓지 않은가?
3. 이상확률을 자동 제어에 사용할 때 안전 임계값이 있는가?