from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE)

temp_violation = ~sensor_df["chamber_temp_c"].between(69, 75)
pressure_violation = ~sensor_df["chamber_pressure_pa"].between(17, 19)
any_violation = temp_violation | pressure_violation

summary_df = pd.DataFrame([
    {
        "rule": "temperature",
        "violation_count": int(temp_violation.sum()),
        "violation_rate": float(temp_violation.mean()),
    },
    {
        "rule": "pressure",
        "violation_count": int(pressure_violation.sum()),
        "violation_rate": float(pressure_violation.mean()),
    },
    {
        "rule": "any",
        "violation_count": int(any_violation.sum()),
        "violation_rate": float(any_violation.mean()),
    },
])

print(summary_df)
summary_df.to_csv(
    OUTPUT_DIR / "ex056_spec_violation_rate.csv",
    index=False,
    encoding="utf-8-sig",
)
