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
    / "physical_range_violations.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 센서별 물리적 허용 범위를 정의한다.
physical_ranges = {
    "temperature_c": (0.0, 150.0),
    "pressure_kpa": (80.0, 130.0),
    "gas_flow_sccm": (0.0, 1000.0),
    "vibration_rms": (0.0, 20.0),
    "motor_current_a": (0.0, 50.0),
}

violations = []

# 2. 각 센서에서 허용 범위를 벗어난 행을 찾는다.
for sensor, (low, high) in physical_ranges.items():
    mask = ~df[sensor].between(low, high)

    for index in df.index[mask]:
        violations.append(
            {
                "row_index": int(index),
                "timestamp": df.loc[index, "timestamp"],
                "lot_id": df.loc[index, "lot_id"],
                "recipe_id": df.loc[index, "recipe_id"],
                "sensor": sensor,
                "value": float(df.loc[index, sensor]),
                "allowed_low": low,
                "allowed_high": high,
            }
        )

# 3. 결과를 표로 만든다.
result = pd.DataFrame(violations)

# 4. 결과를 CSV로 저장한다.
result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[물리 범위 위반]")
print(result)
print()
print("위반 건수:", len(result))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
