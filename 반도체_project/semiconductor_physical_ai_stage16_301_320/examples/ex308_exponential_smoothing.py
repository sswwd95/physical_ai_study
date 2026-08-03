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

signal = (
    sensor_df["temp_sensor_a_c"]
    .interpolate(limit_direction="both")
)

rows = []
for alpha in [0.05, 0.1, 0.2, 0.4]:
    estimate = signal.ewm(alpha=alpha, adjust=False).mean()
    rmse = np.sqrt(
        np.mean(
            (
                estimate
                - sensor_df["true_temperature_c"]
            ) ** 2
        )
    )
    rows.append({
        "alpha": alpha,
        "rmse": rmse,
    })

result_df = pd.DataFrame(rows).sort_values("rmse")
print(result_df.round(4))
