"""
반도체 Physical AI 하네스 엔지니어링 실습 026~030
Windows 10 / Anaconda / Pandas / SciPy
이상값 탐지와 보정 품질 비교
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_outliers.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "iqr_outlier_summary.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

rows = []

# 1. 센서별 1사분위수와 3사분위수를 계산한다.
for sensor in sensor_columns:
    q1 = float(df[sensor].quantile(0.25))
    q3 = float(df[sensor].quantile(0.75))

    # 2. IQR과 이상값 경계를 계산한다.
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    # 3. 경계 밖의 값을 이상값 후보로 표시한다.
    mask = ~df[sensor].between(lower, upper)

    rows.append(
        {
            "sensor": sensor,
            "q1": q1,
            "q3": q3,
            "iqr": iqr,
            "lower_bound": lower,
            "upper_bound": upper,
            "outlier_count": int(mask.sum()),
            "outlier_rate_percent": float(
                mask.mean() * 100.0
            ),
        }
    )

result = pd.DataFrame(rows)

# 4. 이상값 개수가 많은 순서로 정렬한다.
result = result.sort_values(
    "outlier_count",
    ascending=False,
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[IQR 이상값 요약]")
print(result.round(4))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
