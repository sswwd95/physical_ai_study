# 실습 044 — ewma_monitoring

## 1. 학습 목표
EWMA를 이용해 최근 공정 변화에 민감한 추세 지표를 만듭니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 센서에 대해 span=20인 EWMA를 계산하라.
원본 온도와 EWMA를 CSV로 저장하고 마지막 20행을 출력하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex044_ewma_monitoring.py
```

## 4. 예상 결과
원본 온도보다 부드럽지만 최근 변화에 빠르게 반응하는 EWMA가 생성됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 9 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 12 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | CSV 센서 데이터를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 15 | `sensor_df["temp_ewma_20"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `    sensor_df["chamber_temp_c"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 17 | `    .ewm(span=20, adjust=False)` | 최근 데이터에 더 큰 가중치를 주는 지수이동통계를 계산합니다. |
| 18 | `    .mean()` | 데이터의 평균을 계산합니다. |
| 19 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 20 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 21 | `result_df = sensor_df[` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `    ["timestamp", "chamber_temp_c", "temp_ewma_20"]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 23 | `]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 24 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 25 | `print(result_df.tail(20).round(3))` | 실행 결과를 콘솔에 출력합니다. |
| 26 | `result_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 27 | `    OUTPUT_DIR / "ex044_temperature_ewma.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 28 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 29 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 30 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?