from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

import numpy as np

sensor_df = pd.read_csv(DATA_FILE)

safe_gas_flow = sensor_df["gas_flow_sccm"].replace(0, np.nan)
sensor_df["process_load"] = sensor_df["rf_power_w"] / safe_gas_flow

result_df = sensor_df[
    ["timestamp", "lot_id", "rf_power_w", "gas_flow_sccm", "process_load"]
]
print(result_df.head(10).round(3))
result_df.to_csv(
    OUTPUT_DIR / "ex006_process_load.csv",
    index=False,
    encoding="utf-8-sig",
)
