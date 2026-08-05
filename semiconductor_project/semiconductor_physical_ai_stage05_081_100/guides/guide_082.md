# 실습 082 — mad_outlier_detection

## 1. 학습 목표
중앙값과 MAD를 사용해 극단값에 강한 단변량 이상치를 탐지합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 센서의 중앙값과 MAD를 계산하라.
modified_z=0.6745*(x-median)/MAD를 구하고 절댓값 3.5 이상을 이상치로 표시하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex082_mad_outlier_detection.py
```

## 4. 예상 결과
극단값에 덜 민감한 MAD 기반 온도 이상치가 탐지됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_anomaly_data.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_anomaly_data.csv 파일이 없습니다.")` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `values = sensor_df["chamber_temp_c"]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `median_value = values.median()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `mad = np.median(np.abs(values - median_value))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 19 | `sensor_df["temp_modified_z"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    0.6745 * (values - median_value) / mad` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 21 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 22 | `sensor_df["mad_anomaly"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `    sensor_df["temp_modified_z"].abs() >= 3.5` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 25 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 26 | `print("MAD 이상치 수:", int(sensor_df["mad_anomaly"].sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 27 | `sensor_df.to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 28 | `    OUTPUT_DIR / "ex082_mad_outliers.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 29 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?