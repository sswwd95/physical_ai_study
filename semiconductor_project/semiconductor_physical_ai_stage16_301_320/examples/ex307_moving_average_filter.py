from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "digital_twin_sensor_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/digital_twin_sensor_stream.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE)

sensor_df["temp_sensor_a_c"] = (
    sensor_df["temp_sensor_a_c"]
    .interpolate(limit_direction="both")
)

for window in [3, 5, 15, 30]:
    sensor_df[f"temp_ma_{window}"] = (
        sensor_df["temp_sensor_a_c"]
        .rolling(window, min_periods=1)
        .mean()
    )

columns = [
    "true_temperature_c",
    "temp_sensor_a_c",
    "temp_ma_3",
    "temp_ma_5",
    "temp_ma_15",
    "temp_ma_30",
]

rmse_rows = []
for column in columns[1:]:
    rmse_rows.append({
        "signal": column,
        "rmse": np.sqrt(
            np.mean(
                (
                    sensor_df[column]
                    - sensor_df["true_temperature_c"]
                ) ** 2
            )
        ),
    })

result_df = pd.DataFrame(rmse_rows).sort_values("rmse")
print(result_df.round(4))
