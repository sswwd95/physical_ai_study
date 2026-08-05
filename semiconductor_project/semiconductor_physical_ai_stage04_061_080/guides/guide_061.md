# 실습 061 — baseline_window_selection

## 1. 학습 목표
초기 정상 구간을 기준선으로 선택하고 평균·표준편차를 계산합니다.

## 2. Antigravity용 하네스 프롬프트
```text
초기 120개 시점을 정상 기준 구간으로 사용하여 온도와 압력의 평균과 표준편차를 계산하라.
기준 구간과 전체 구간 통계를 비교하고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex061_baseline_window_selection.py
```

## 4. 예상 결과
초기 정상 구간과 전체 구간의 평균·표준편차 차이가 출력됩니다.

## 5. 라인별 해설

| 줄 | 코드 | 쉬운 해설 |
|---:|---|---|
| 1 | `from pathlib import Path` | 필요한 라이브러리나 기능을 불러옵니다. |
| 2 | `import numpy as np` | 필요한 라이브러리나 기능을 불러옵니다. |
| 3 | `import pandas as pd` | 필요한 라이브러리나 기능을 불러옵니다. |
| 4 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 5 | `ROOT = Path(__file__).resolve().parents[1]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 6 | `DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 7 | `OUTPUT_DIR = ROOT / "outputs"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 8 | `OUTPUT_DIR.mkdir(exist_ok=True)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 9 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 10 | `if not DATA_FILE.exists():` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 11 | `    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 12 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 13 | `sensor_df = pd.read_csv(DATA_FILE)` | 센서 CSV를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 15 | `baseline_df = sensor_df.iloc[:120].copy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 17 | `rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `for column in ["chamber_temp_c", "chamber_pressure_pa"]:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 19 | `    rows.append({` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `        "sensor": column,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `        "baseline_mean": baseline_df[column].mean(),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `        "baseline_std": baseline_df[column].std(ddof=1),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `        "overall_mean": sensor_df[column].mean(),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 24 | `        "overall_std": sensor_df[column].std(ddof=1),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `    })` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 26 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 27 | `summary_df = pd.DataFrame(rows)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `print(summary_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 29 | `summary_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 30 | `    OUTPUT_DIR / "ex061_baseline_summary.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 31 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?