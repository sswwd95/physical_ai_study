# 실습 079 — change_detection_dashboard

## 1. 학습 목표
CUSUM·EWMA·분산비·다중 센서 점수를 한 파일에 통합합니다.

## 2. Antigravity용 하네스 프롬프트
```text
timestamp별 온도, 상방 CUSUM, EWMA, EWMA UCL/LCL, 분산비,
다중 센서 change_score, severity를 포함하는 대시보드 CSV를 생성하라.
```

## 3. 실행 명령
```bat
conda activate semi-physical-ai-stage04
python examples\ex079_change_detection_dashboard.py
```

## 4. 예상 결과
변화 감지 대시보드에서 바로 사용할 통합 CSV가 생성됩니다.

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
| 23 | `cusum = []` | 계산 결과나 설정값을 변수에 저장합니다. |
| 24 | `current = 0.0` | 계산 결과나 설정값을 변수에 저장합니다. |
| 25 | `for value in z:` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 26 | `    current = max(0.0, current + value - 0.5)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 27 | `    cusum.append(current)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 28 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 29 | `lambda_value = 0.2` | 계산 결과나 설정값을 변수에 저장합니다. |
| 30 | `sensor_df["temp_ewma"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 31 | `    sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 32 | `    .ewm(alpha=lambda_value, adjust=False)` | 최근 관측값에 더 큰 가중치를 주는 EWMA를 계산합니다. |
| 33 | `    .mean()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 34 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 35 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 36 | `t = np.arange(1, len(sensor_df) + 1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 37 | `ewma_std = temp_std * np.sqrt(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 38 | `    lambda_value / (2 - lambda_value)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 39 | `    * (1 - (1 - lambda_value) ** (2 * t))` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 40 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 41 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 42 | `sensor_df["ewma_ucl"] = temp_mean + 3 * ewma_std` | 계산 결과나 설정값을 변수에 저장합니다. |
| 43 | `sensor_df["ewma_lcl"] = temp_mean - 3 * ewma_std` | 계산 결과나 설정값을 변수에 저장합니다. |
| 44 | `sensor_df["cusum_upper"] = cusum` | 계산 결과나 설정값을 변수에 저장합니다. |
| 45 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 46 | `baseline_variance = baseline_temp.var(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 47 | `sensor_df["variance_ratio"] = (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 48 | `    sensor_df["chamber_temp_c"]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 49 | `    .rolling(window=40, min_periods=15)` | 이동 구간의 통계량을 계산합니다. |
| 50 | `    .var(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 51 | `    / baseline_variance` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 52 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 53 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 54 | `score = np.zeros(len(sensor_df))` | 계산 결과나 설정값을 변수에 저장합니다. |
| 55 | `for column in [` | 여러 시점 또는 센서에 같은 계산을 반복합니다. |
| 56 | `    "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 57 | `    "chamber_pressure_pa",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 58 | `    "vibration_g",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 59 | `]:` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 60 | `    baseline = sensor_df[column].iloc[:120]` | 계산 결과나 설정값을 변수에 저장합니다. |
| 61 | `    score += (` | 계산 결과나 설정값을 변수에 저장합니다. |
| 62 | `        (sensor_df[column] - baseline.mean())` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 63 | `        / baseline.std(ddof=1)` | 계산 결과나 설정값을 변수에 저장합니다. |
| 64 | `    ).abs()` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 65 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 66 | `sensor_df["change_score"] = score` | 계산 결과나 설정값을 변수에 저장합니다. |
| 67 | `sensor_df["severity"] = pd.cut(` | 계산 결과나 설정값을 변수에 저장합니다. |
| 68 | `    score,` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 69 | `    bins=[-np.inf, 4, 8, 12, np.inf],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 70 | `    labels=["normal", "caution", "warning", "critical"],` | 계산 결과나 설정값을 변수에 저장합니다. |
| 71 | `    right=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 72 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 73 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 74 | `dashboard_df = sensor_df[` | 계산 결과나 설정값을 변수에 저장합니다. |
| 75 | `    [` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 76 | `        "timestamp",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 77 | `        "lot_id",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 78 | `        "chamber_temp_c",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 79 | `        "cusum_upper",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 80 | `        "temp_ewma",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 81 | `        "ewma_ucl",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 82 | `        "ewma_lcl",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 83 | `        "variance_ratio",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 84 | `        "change_score",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 85 | `        "severity",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 86 | `    ]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 87 | `]` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 88 | `` | 코드 구역을 나누는 빈 줄입니다. |
| 89 | `dashboard_df.to_csv(` | 계산 결과를 CSV 파일로 저장합니다. |
| 90 | `    OUTPUT_DIR / "ex079_change_detection_dashboard.csv",` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 91 | `    index=False,` | 계산 결과나 설정값을 변수에 저장합니다. |
| 92 | `    encoding="utf-8-sig",` | 계산 결과나 설정값을 변수에 저장합니다. |
| 93 | `)` | 변화 감지 또는 경보 계산 단계를 수행합니다. |
| 94 | `print(dashboard_df.tail(10).round(3))` | 실행 결과를 콘솔에 출력합니다. |

## 6. 실무 확인 질문
1. 기준 구간이 오염되면 경보 민감도가 어떻게 달라지는가?
2. 민감도와 오경보 사이의 균형을 어떻게 정할 것인가?
3. 변화 감지 후 장비 정지·레시피 확인·재측정 중 무엇을 먼저 할 것인가?