from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

state_summary = (
    sensor_df.groupby("process_state")[
        ["chamber_temp_c", "chamber_pressure_pa", "vibration_g"]
    ]
    .mean()
    .sort_values("vibration_g", ascending=False)
)

print(state_summary.round(4))
print("\n진동 평균이 가장 큰 상태:", state_summary.index[0])
