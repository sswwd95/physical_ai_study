# 실습 358 — response_kpi

## 1. 학습 목표
탐지 지연·경보 수·정지 시간을 평가합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
탐지 지연·경보 수·정지 시간을 KPI로 계산하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage18
python examples\ex358_response_kpi.py
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
| 14 | `actual=safe_df["anomaly_type"].ne("normal").to_numpy()` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 15 | `alarm=safe_df["severity_level"].ge(2).to_numpy()` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 16 | `delays=[]` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 17 | `in_event=False` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 18 | `start=None` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 19 | `for i,val in enumerate(actual):` | 여러 시점·임계값·정책을 반복 계산합니다. |
| 20 | `    if val and not in_event:` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 21 | `        in_event=True; start=i` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 22 | `    if in_event and alarm[i]:` | 이상 대응 또는 안전 의사결정 단계를 수행합니다. |
| 23 | `        delays.append(i-start); in_event=False` | 계산 결과나 안전 설정값을 변수에 저장합니다. |
| 24 | `print("사건 수:",int((pd.Series(actual)&~pd.Series(actual).shift(fill_value=False)).sum()))` | 결과를 콘솔에 출력합니다. |
| 25 | `print("평균 탐지 지연(초):",round(float(np.mean(delays)) if delays else np.nan,3))` | 결과를 콘솔에 출력합니다. |
| 26 | `print("경보 시점:",int(alarm.sum()))` | 결과를 콘솔에 출력합니다. |
| 27 | `print("정지 시점:",int((safe_df["severity_level"]>=4).sum()))` | 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 자동 정지 조건이 안전 규정과 일치하는가?
2. 경보 미탐과 오탐의 비용을 별도로 평가했는가?
3. 센서 불확실성·통신지연·수동 개입 절차를 반영했는가?