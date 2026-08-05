# 실습 071 — mean_shift_scan

## 1. 학습 목표
분할점 후보마다 앞뒤 평균 차이를 계산해 변화점 후보를 찾습니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도 시계열에서 후보 인덱스 60부터 len-60까지를 5칸 간격으로 탐색하라.
각 후보에서 앞 구간과 뒤 구간 평균 차이 절댓값을 계산하고 가장 큰 후보 10개를 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex071_mean_shift_scan.py
```

## 4. 예상 결과
앞뒤 평균 차이가 큰 변화점 후보 10개가 출력됩니다.

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
| 15 | `values = sensor_df["chamber_temp_c"].to_numpy()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 18 | `for split_index in range(60, len(values) - 60, 5):` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 19 | `    before_mean = values[:split_index].mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    after_mean = values[split_index:].mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 21 | `    rows.append({` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `        "split_index": split_index,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 23 | `        "before_mean": before_mean,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 24 | `        "after_mean": after_mean,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 25 | `        "absolute_mean_difference": abs(after_mean - before_mean),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 26 | `    })` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 27 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 28 | `scan_df = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 29 | `    pd.DataFrame(rows)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 30 | `    .sort_values(` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 31 | `        "absolute_mean_difference",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 32 | `        ascending=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 33 | `    )` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 34 | `    .head(10)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 36 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 37 | `print(scan_df.round(4))` | 실행 결과를 콘솔에 출력합니다. |
| 38 | `scan_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 39 | `    OUTPUT_DIR / "ex071_mean_shift_candidates.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 41 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?