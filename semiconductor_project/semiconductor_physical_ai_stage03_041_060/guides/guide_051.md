# 실습 051 — trend_rule_detection

## 1. 학습 목표
연속 상승 또는 연속 하락 추세를 감지합니다.

## 2. Antigravity용 예제 소스 생성 하네스 프롬프트
```text
온도 데이터에서 6개 연속 관측값이 계속 상승하거나 계속 하락하는 구간을 탐지하라.
diff의 부호를 이용하고 trend_violation 플래그를 추가하여 결과를 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage03
python examples\ex051_trend_rule_detection.py
```

## 4. 예상 결과
6개 연속 상승 또는 하락 추세가 끝나는 시점이 탐지됩니다.

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
| 15 | `temperature_diff = sensor_df["chamber_temp_c"].diff()` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 16 | `direction = np.sign(temperature_diff)` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 17 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 18 | `window_size = 5` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 19 | `direction_sum = direction.rolling(window=window_size).sum()` | 지정한 구간의 이동통계를 계산합니다. |
| 20 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 21 | `sensor_df["trend_violation"] = (` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 22 | `    direction_sum.abs() == window_size` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 23 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 24 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 25 | `violation_df = sensor_df.loc[` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 26 | `    sensor_df["trend_violation"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 27 | `    ["timestamp", "chamber_temp_c"],` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 28 | `]` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 29 | `` | 코드 구역을 보기 좋게 나누는 빈 줄입니다. |
| 30 | `print("추세 규칙 위반 행 수:", len(violation_df))` | 실행 결과를 콘솔에 출력합니다. |
| 31 | `violation_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 32 | `    OUTPUT_DIR / "ex051_trend_rule_violations.csv",` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |
| 33 | `    index=False,` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 34 | `    encoding="utf-8-sig",` | 오른쪽 계산 결과를 왼쪽 변수에 저장합니다. |
| 35 | `)` | 공정 모니터링 또는 SPC 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 관리한계와 규격한계는 어떻게 다른가?
2. 공정 조건이나 레시피가 바뀌면 기준선을 다시 계산해야 하는가?
3. 경보가 발생했을 때 자동 정지와 작업자 확인 중 어떤 절차가 필요한가?