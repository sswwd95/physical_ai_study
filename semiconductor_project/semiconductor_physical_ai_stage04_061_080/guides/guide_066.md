# 실습 066 — cusum_parameter_comparison

## 1. 학습 목표
k와 h 조합에 따른 CUSUM 경보 민감도를 비교합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도 상방 CUSUM에서 k=[0.25,0.5,1.0], h=[4,5,8] 조합을 비교하라.
각 조합별 최초 경보 인덱스와 전체 경보 행 수를 표로 만들고 CSV로 저장하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex066_cusum_parameter_comparison.py
```

## 4. 예상 결과
k와 h가 작을수록 민감하지만 경보 수가 늘어나는 경향을 확인합니다.

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
| 15 | `baseline = sensor_df["chamber_temp_c"].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `mean_value = baseline.mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `std_value = baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `z = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 19 | `    sensor_df["chamber_temp_c"] - mean_value` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 20 | `) / std_value` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 22 | `rows = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 23 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 24 | `for k in [0.25, 0.5, 1.0]:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 25 | `    for h in [4.0, 5.0, 8.0]:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 26 | `        current = 0.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `        alarm_indices = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 28 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 29 | `        for index, value in enumerate(z):` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 30 | `            current = max(0.0, current + value - k)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `            if current >= h:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `                alarm_indices.append(index)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 33 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 34 | `        rows.append({` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `            "k": k,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 36 | `            "h": h,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 37 | `            "first_alarm_index": (` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 38 | `                alarm_indices[0]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `                if alarm_indices` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `                else np.nan` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 41 | `            ),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 42 | `            "alarm_count": len(alarm_indices),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 43 | `        })` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 44 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 45 | `comparison_df = pd.DataFrame(rows)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 46 | `print(comparison_df)` | 실행 결과를 콘솔에 출력합니다. |
| 47 | `comparison_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 48 | `    OUTPUT_DIR / "ex066_cusum_parameter_comparison.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 49 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 50 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?