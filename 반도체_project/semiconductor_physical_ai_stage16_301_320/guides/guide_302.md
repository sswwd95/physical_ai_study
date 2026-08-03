# 실습 302 — timestamp_validation

## 1. 학습 목표
시간축 간격과 누락 시점을 검증합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
1초 샘플링 기준으로 시간축 간격 오류를 검증하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage16
python examples\ex302_timestamp_validation.py
```

## 4. 예상 결과
요청한 디지털 트윈·센서 융합 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError(` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 12 | `        "data/digital_twin_sensor_stream.csv 파일이 없습니다."` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 13 | `    )` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 14 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 15 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 디지털 트윈 센서 스트림 CSV를 읽습니다. |
| 16 | `sensor_df = sensor_df.sort_values("timestamp")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 18 | `interval = sensor_df["timestamp"].diff().dt.total_seconds()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `result_df = pd.DataFrame({` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    "timestamp": sensor_df["timestamp"],` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 21 | `    "interval_seconds": interval,` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 22 | `})` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 23 | `result_df["interval_error"] = result_df["interval_seconds"].ne(1.0)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 25 | `print("기대 간격과 다른 행:", int(result_df["interval_error"].sum()))` | 결과를 콘솔에 출력합니다. |
| 26 | `print(result_df["interval_seconds"].describe())` | 결과를 콘솔에 출력합니다. |
| 27 | `result_df.to_csv(` | 결과를 CSV 파일로 저장합니다. |
| 28 | `    OUTPUT_DIR / "ex302_timestamp_validation.csv",` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |
| 29 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `)` | 디지털 트윈·센서 융합 분석 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 센서 시간축과 샘플링 주기가 일치하는가?
2. 트윈 오차가 센서 문제인지 모델 문제인지 구분했는가?
3. 추정값을 제어에 사용할 때 안전한 폴백 조건이 있는가?