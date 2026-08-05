from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

sensor_columns = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
    "particle_count",
]
correlation_matrix = sensor_df[sensor_columns].corr(method="pearson")

print(correlation_matrix.round(3))
correlation_matrix.to_csv(
    OUTPUT_DIR / "ex016_sensor_correlation.csv",
    encoding="utf-8-sig",
)
