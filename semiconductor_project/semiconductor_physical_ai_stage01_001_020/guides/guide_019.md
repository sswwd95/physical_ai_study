# 실습 019 — bayesian_temperature_mean

## 1. 학습 목표
PyMC로 챔버 평균 온도의 사후분포를 추정하는 첫 베이즈 실습을 수행합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
PyMC를 사용해 chamber_temp_c의 평균을 추정하는 정규모형을 작성하라.
mu는 Normal(72, 5), sigma는 HalfNormal(5) 사전분포를 사용하고
draws=1000, tune=1000, chains=2, random_seed=42로 샘플링하라.
arviz.summary로 mu와 sigma의 평균, 표준편차, HDI를 출력하고 CSV로 저장하라.
```

## 3. 실행 방법
```bat
conda activate semi-physical-ai
python examples\ex019_bayesian_temperature_mean.py
```

## 4. 예상 결과
평균 온도 `mu`와 온도 변동 `sigma`의 사후평균, 표준편차, 94% HDI가 출력됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 실습에 필요한 외부 기능을 불러옵니다. |
| 2 | `import pandas as pd` | 실습에 필요한 외부 기능을 불러옵니다. |
| 3 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 4 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 5 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `OUTPUT_DIR = ROOT / "outputs"` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 9 | `import arviz as az` | 실습에 필요한 외부 기능을 불러옵니다. |
| 10 | `import pymc as pm` | 실습에 필요한 외부 기능을 불러옵니다. |
| 11 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 12 | `sensor_df = pd.read_csv(DATA_FILE)` | CSV 파일을 표 형태의 DataFrame으로 읽습니다. |
| 13 | `temperature_data = sensor_df["chamber_temp_c"].to_numpy()` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `with pm.Model() as temperature_model:` | PyMC를 사용해 확률 모형의 구성요소를 만들거나 샘플링합니다. |
| 16 | `    mu = pm.Normal("mu", mu=72.0, sigma=5.0)` | PyMC를 사용해 확률 모형의 구성요소를 만들거나 샘플링합니다. |
| 17 | `    sigma = pm.HalfNormal("sigma", sigma=5.0)` | PyMC를 사용해 확률 모형의 구성요소를 만들거나 샘플링합니다. |
| 18 | `    pm.Normal(` | PyMC를 사용해 확률 모형의 구성요소를 만들거나 샘플링합니다. |
| 19 | `        "temperature_obs",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 20 | `        mu=mu,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 21 | `        sigma=sigma,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `        observed=temperature_data,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `    )` | 실습 흐름에 필요한 명령을 수행합니다. |
| 24 | `    trace = pm.sample(` | PyMC를 사용해 확률 모형의 구성요소를 만들거나 샘플링합니다. |
| 25 | `        draws=1000,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 26 | `        tune=1000,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 27 | `        chains=2,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 28 | `        cores=1,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 29 | `        random_seed=42,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `        progressbar=False,` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 31 | `    )` | 실습 흐름에 필요한 명령을 수행합니다. |
| 32 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 33 | `summary = az.summary(trace, var_names=["mu", "sigma"], hdi_prob=0.94)` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 34 | `print(summary)` | 학습자가 실행 결과를 콘솔에서 확인하도록 출력합니다. |
| 35 | `summary.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 36 | `    OUTPUT_DIR / "ex019_bayesian_temperature_summary.csv",` | 실습 흐름에 필요한 명령을 수행합니다. |
| 37 | `    encoding="utf-8-sig",` | 오른쪽의 값이나 계산 결과를 왼쪽 변수에 저장합니다. |
| 38 | `)` | 실습 흐름에 필요한 명령을 수행합니다. |

## 6. 확인 문제
1. 입력 데이터의 단위가 바뀌면 어느 부분을 수정해야 하는가?
2. 결측값 또는 이상값이 결과에 어떤 영향을 주는가?
3. 이 코드를 실제 반도체 장비 센서에 적용하려면 어떤 컬럼이 더 필요한가?