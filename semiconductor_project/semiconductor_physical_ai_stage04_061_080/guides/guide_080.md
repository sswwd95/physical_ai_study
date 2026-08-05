# 실습 080 — automated_change_report

## 1. 학습 목표
여러 변화 감지 지표와 경보 세그먼트를 Excel 보고서로 자동 생성합니다.

## 2. Antigravity용 하네스 프롬프트
```text
온도 상방 CUSUM, EWMA 경보, 분산비 경보, 다중 센서 change_score를 계산하라.
summary, alarm_rows, segments 세 시트의 Excel 보고서와 CSV 요약을 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex080_automated_change_report.py
```

## 4. 예상 결과
변화 감지 요약, 경보 행, 연속 경보 세그먼트가 Excel 보고서로 저장됩니다.

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
| 13 | `sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])` | 센서 CSV를 DataFrame으로 읽습니다. |
| 14 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 15 | `baseline_temp = sensor_df["chamber_temp_c"].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 16 | `temp_mean = baseline_temp.mean()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 17 | `temp_std = baseline_temp.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 18 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 19 | `z = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 20 | `    sensor_df["chamber_temp_c"] - temp_mean` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 21 | `) / temp_std` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 22 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 23 | `cusum_values = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `current = 0.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `for value in z:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 26 | `    current = max(0.0, current + value - 0.5)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    cusum_values.append(current)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 28 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 29 | `sensor_df["cusum_upper"] = cusum_values` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `sensor_df["cusum_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    sensor_df["cusum_upper"] >= 5.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 32 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 33 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 34 | `lambda_value = 0.2` | 계산 결과나 설정값을 변수에 저장합니다. |
| 35 | `sensor_df["temp_ewma"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 36 | `    sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 37 | `    .ewm(alpha=lambda_value, adjust=False)` | 최근 관측값에 더 큰 가중치를 주는 EWMA를 계산합니다. |
| 38 | `    .mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 41 | `t = np.arange(1, len(sensor_df) + 1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 42 | `ewma_std = temp_std * np.sqrt(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `    lambda_value / (2 - lambda_value)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 44 | `    * (1 - (1 - lambda_value) ** (2 * t))` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 45 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 46 | `sensor_df["ewma_ucl"] = temp_mean + 3 * ewma_std` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `sensor_df["ewma_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    sensor_df["temp_ewma"] > sensor_df["ewma_ucl"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 49 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 50 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 51 | `baseline_variance = baseline_temp.var(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 52 | `sensor_df["variance_ratio"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 53 | `    sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 54 | `    .rolling(window=40, min_periods=15)` | 이동 구간의 통계량을 계산합니다. |
| 55 | `    .var(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 56 | `    / baseline_variance` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 57 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 58 | `sensor_df["variance_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 59 | `    sensor_df["variance_ratio"] >= 2.5` | 계산 결과나 설정값을 변수에 저장합니다. |
| 60 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 61 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 62 | `score = np.zeros(len(sensor_df))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 63 | `for column in [` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 64 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 65 | `    "chamber_pressure_pa",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 66 | `    "vibration_g",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 67 | `]:` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 68 | `    baseline = sensor_df[column].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 69 | `    score += (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 70 | `        (sensor_df[column] - baseline.mean())` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 71 | `        / baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `    ).abs()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 73 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 74 | `sensor_df["change_score"] = score` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `sensor_df["multi_sensor_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 76 | `    sensor_df["change_score"] >= 8.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 77 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 78 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 79 | `sensor_df["any_alarm"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 80 | `    sensor_df["cusum_alarm"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 81 | `    \| sensor_df["ewma_alarm"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 82 | `    \| sensor_df["variance_alarm"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 83 | `    \| sensor_df["multi_sensor_alarm"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 84 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 85 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 86 | `start_flag = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 87 | `    sensor_df["any_alarm"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 88 | `    & ~sensor_df["any_alarm"].shift(1, fill_value=False)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 89 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 90 | `sensor_df["segment_id"] = start_flag.cumsum()` | 계산 결과나 설정값을 변수에 저장합니다. |
| 91 | `sensor_df.loc[` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 92 | `    ~sensor_df["any_alarm"],` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 93 | `    "segment_id",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 94 | `] = 0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 95 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 96 | `segments_df = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 97 | `    sensor_df.loc[sensor_df["segment_id"] > 0]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 98 | `    .groupby("segment_id")` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 99 | `    .agg(` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 100 | `        start_time=("timestamp", "min"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 101 | `        end_time=("timestamp", "max"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 102 | `        length=("timestamp", "size"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 103 | `        max_change_score=("change_score", "max"),` | 계산 결과나 설정값을 변수에 저장합니다. |
| 104 | `    )` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 105 | `    .reset_index()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 106 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 107 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 108 | `summary_df = pd.DataFrame([{` | 계산 결과나 설정값을 변수에 저장합니다. |
| 109 | `    "row_count": len(sensor_df),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 110 | `    "cusum_alarm_count": int(sensor_df["cusum_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 111 | `    "ewma_alarm_count": int(sensor_df["ewma_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 112 | `    "variance_alarm_count": int(sensor_df["variance_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 113 | `    "multi_sensor_alarm_count": int(sensor_df["multi_sensor_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 114 | `    "combined_alarm_count": int(sensor_df["any_alarm"].sum()),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 115 | `    "segment_count": len(segments_df),` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 116 | `}])` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 117 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 118 | `alarm_df = sensor_df.loc[sensor_df["any_alarm"]]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 119 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 120 | `excel_file = OUTPUT_DIR / "ex080_change_detection_report.xlsx"` | 계산 결과나 설정값을 변수에 저장합니다. |
| 121 | `with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:` | 계산 결과나 설정값을 변수에 저장합니다. |
| 122 | `    summary_df.to_excel(writer, sheet_name="summary", index=False)` | 결과를 Excel 파일로 저장합니다. |
| 123 | `    alarm_df.to_excel(writer, sheet_name="alarm_rows", index=False)` | 결과를 Excel 파일로 저장합니다. |
| 124 | `    segments_df.to_excel(writer, sheet_name="segments", index=False)` | 결과를 Excel 파일로 저장합니다. |
| 125 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 126 | `summary_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 127 | `    OUTPUT_DIR / "ex080_change_detection_summary.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 128 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 129 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 130 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 131 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 132 | `print(summary_df)` | 실행 결과를 콘솔에 출력합니다. |
| 133 | `print("보고서 저장:", excel_file)` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?