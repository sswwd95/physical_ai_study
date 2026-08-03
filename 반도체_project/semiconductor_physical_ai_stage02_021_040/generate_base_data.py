from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = DATA_DIR / "semiconductor_sensor_data.csv"

rng = np.random.default_rng(42)
row_count = 300
timestamp = pd.date_range("2026-01-01 09:00:00", periods=row_count, freq="s")
lot_id = np.repeat(["LOT-A", "LOT-B", "LOT-C"], row_count // 3)

temperature = rng.normal(72.0, 0.8, row_count)
pressure = rng.normal(18.0, 0.35, row_count)
rf_power = rng.normal(850.0, 12.0, row_count)
gas_flow = rng.normal(120.0, 2.0, row_count)
vibration = np.abs(rng.normal(0.08, 0.015, row_count))
particle_count = rng.poisson(4, row_count)
process_state = np.repeat(["stabilize", "process", "purge"], 100)

anomaly_index = np.arange(220, 235)
temperature[anomaly_index] += rng.normal(5.0, 0.5, len(anomaly_index))
pressure[anomaly_index] += rng.normal(2.5, 0.2, len(anomaly_index))
vibration[anomaly_index] += rng.normal(0.12, 0.01, len(anomaly_index))
particle_count[anomaly_index] += rng.poisson(12, len(anomaly_index))

sensor_df = pd.DataFrame({
    "timestamp": timestamp,
    "lot_id": lot_id,
    "chamber_temp_c": temperature,
    "chamber_pressure_pa": pressure,
    "rf_power_w": rf_power,
    "gas_flow_sccm": gas_flow,
    "vibration_g": vibration,
    "particle_count": particle_count,
    "process_state": process_state,
})

sensor_df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
print(f"저장 완료: {OUTPUT_FILE}")
