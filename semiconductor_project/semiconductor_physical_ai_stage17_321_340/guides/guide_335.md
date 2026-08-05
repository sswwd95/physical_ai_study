# 실습 335 — anomaly_probability_stream

## 1. 학습 목표
시점별 이상확률 스트림을 생성합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
시점별 트윈 잔차에서 이상확률 스트림을 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage17
python examples\ex335_anomaly_probability_stream.py
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
| 14 | `res=(sensor_df["temp_sensor_b_c"]-sensor_df["true_temperature_c"]).to_numpy()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 15 | `baseline=res[np.isfinite(res)][:200]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 16 | `mu=baseline.mean(); sigma=baseline.std()` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 17 | `valid=np.isfinite(res)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 18 | `z=np.zeros(len(res))` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 19 | `z[valid]=np.abs((res[valid]-mu)/(sigma+1e-9))` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 20 | `sensor_df["anomaly_probability"]=1-np.exp(-0.5*z**2)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 21 | `sensor_df["anomaly_probability"]=sensor_df["anomaly_probability"].clip(0,1)` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 22 | `out=sensor_df[["timestamp","process_phase","anomaly_probability"]]` | 계산 결과나 모형 파라미터를 변수에 저장합니다. |
| 23 | `print(out.sort_values("anomaly_probability",ascending=False).head(15))` | 결과를 콘솔에 출력합니다. |
| 24 | `out.to_csv(OUTPUT_DIR/"ex335_anomaly_probability_stream.csv",index=False,encoding="utf-8-sig")` | 결과를 CSV 파일로 저장합니다. |

## 6. 실무 확인 질문
1. 센서 바이어스와 실제 공정 변화를 구분했는가?
2. 사후예측구간이 너무 좁거나 넓지 않은가?
3. 이상확률을 자동 제어에 사용할 때 안전 임계값이 있는가?