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

phase_twin = (
    sensor_df.groupby("process_phase")[
        [
            "true_temperature_c",
            "true_pressure_pa",
            "true_rf_power_w",
            "true_gas_flow_sccm",
        ]
    ]
    .mean()
)

print(phase_twin.round(3))
phase_twin.to_csv(
    OUTPUT_DIR / "ex312_phase_twin_reference.csv",
    encoding="utf-8-sig",
)
