from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data_stage04.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data_stage04.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE)

baseline = sensor_df["chamber_temp_c"].iloc[:120]
mean_value = baseline.mean()
std_value = baseline.std(ddof=1)
z = (
    sensor_df["chamber_temp_c"] - mean_value
) / std_value

rows = []

for k in [0.25, 0.5, 1.0]:
    for h in [4.0, 5.0, 8.0]:
        current = 0.0
        alarm_indices = []

        for index, value in enumerate(z):
            current = max(0.0, current + value - k)
            if current >= h:
                alarm_indices.append(index)

        rows.append({
            "k": k,
            "h": h,
            "first_alarm_index": (
                alarm_indices[0]
                if alarm_indices
                else np.nan
            ),
            "alarm_count": len(alarm_indices),
        })

comparison_df = pd.DataFrame(rows)
print(comparison_df)
comparison_df.to_csv(
    OUTPUT_DIR / "ex066_cusum_parameter_comparison.csv",
    index=False,
    encoding="utf-8-sig",
)
