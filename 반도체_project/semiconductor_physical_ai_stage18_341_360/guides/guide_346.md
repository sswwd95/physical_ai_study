# 실습 346 — persistence_filter

## 1. 학습 목표
일시적 이상을 제거하는 지속시간 필터를 적용합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
5초 연속 이상인 경우만 경보하는 지속시간 필터를 작성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage18
python examples\ex346_persistence_filter.py
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
| 13 | `safe_df=pd.read_csv(DATA_FILE)` | 안전 의사결정 센서 스트림을 읽습니다. |
| 14 | `raw=safe_df["severity_level"].ge(2)` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 15 | `persistent=raw.rolling(5,min_periods=5).sum().ge(5)` | 최근 구간 기준의 이동 통계량을 계산합니다. |
| 16 | `safe_df["persistent_alarm"]=persistent` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 17 | `print("원시 경보:",int(raw.sum()))` | 결과를 콘솔에 출력합니다. |
| 18 | `print("5초 지속 경보:",int(persistent.sum()))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 자동 정지 조건이 안전 규정과 일치하는가?
2. 경보 미탐과 오탐의 비용을 별도로 평가했는가?
3. 센서 불확실성·통신지연·수동 개입 절차를 반영했는가?