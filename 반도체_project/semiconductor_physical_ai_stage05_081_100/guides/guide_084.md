# 실습 084 — contextual_rule_anomaly

## 1. 학습 목표
공정 상태를 고려한 문맥적 이상을 탐지합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
purge 상태인데 RF 전력이 900W 이상이거나 stabilize 상태인데 진동이 0.12g 이상이면
contextual_anomaly로 표시하라. 규칙별 탐지 건수를 출력하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage05
python examples\ex084_contextual_rule_anomaly.py
```

## 4. 예상 결과
상태를 무시한 단순 임계값으로는 찾기 어려운 문맥적 이상이 탐지됩니다.

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
| 15 | `purge_high_rf = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `    (sensor_df["process_state"] == "purge")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `    & (sensor_df["rf_power_w"] >= 900)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 19 | `stabilize_high_vibration = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    (sensor_df["process_state"] == "stabilize")` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    & (sensor_df["vibration_g"] >= 0.12)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 22 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 23 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 24 | `sensor_df["contextual_anomaly"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    purge_high_rf \| stabilize_high_vibration` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 26 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 27 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 28 | `print("purge 고전력:", int(purge_high_rf.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 29 | `print("stabilize 고진동:", int(stabilize_high_vibration.sum()))` | 실행 결과를 콘솔에 출력합니다. |
| 30 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 31 | `sensor_df.loc[sensor_df["contextual_anomaly"]].to_csv(` | 분석 결과를 CSV로 저장합니다. |
| 32 | `    OUTPUT_DIR / "ex084_contextual_anomalies.csv",` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |
| 33 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 34 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `)` | 이상치 분석 또는 모델 평가 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 이상 비율을 고정하면 실제 공정 변화에 어떤 문제가 생길 수 있는가?
2. 탐지된 이상을 삭제하기 전에 어떤 공정 정보를 확인해야 하는가?
3. 정답 라벨이 부족할 때 모델 성능을 어떻게 검증할 것인가?