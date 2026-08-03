# 실습 343 — alarm_priority_queue

## 1. 학습 목표
심각도·지속시간 기반 경보 우선순위를 만듭니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
경보 지속시간과 최대 심각도로 우선순위를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage18
python examples\ex343_alarm_priority_queue.py
```

## 4. 예상 결과
요청한 이상 대응·안전 의사결정 결과가 출력 또는 저장됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리를 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리를 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리를 불러옵니다. |
| 4 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 12 | `` | 코드 구역을 구분하는 빈 줄입니다. |
| 13 | `safe_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])` | 안전 의사결정 센서 스트림을 읽습니다. |
| 14 | `safe_df["alarm"]=safe_df["severity_level"]>=2` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 15 | `group_id=(safe_df["alarm"]!=safe_df["alarm"].shift()).cumsum()` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 16 | `events=safe_df.loc[safe_df["alarm"]].groupby(group_id).agg(` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 17 | `    start=("timestamp","min"),end=("timestamp","max"),` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 18 | `    duration_seconds=("timestamp","count"),` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 19 | `    max_severity=("severity_level","max"),` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 20 | `    equipment_id=("equipment_id","first"),` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 21 | `    anomaly_type=("anomaly_type","first"))` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 22 | `events["priority"]=events["max_severity"]*10+np.log1p(events["duration_seconds"])` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 23 | `events=events.sort_values("priority",ascending=False)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 24 | `print(events.head(15).round(3))` | 결과를 콘솔에 출력합니다. |
| 25 | `events.to_csv(OUTPUT_DIR/"ex343_alarm_priority.csv",encoding="utf-8-sig")` | 결과를 CSV로 저장합니다. |

## 6. 실무 확인 질문
1. 자동 정지 조건이 안전 규정과 일치하는가?
2. 경보 미탐과 오탐의 비용을 별도로 평가했는가?
3. 센서 불확실성·통신지연·수동 개입 절차를 반영했는가?