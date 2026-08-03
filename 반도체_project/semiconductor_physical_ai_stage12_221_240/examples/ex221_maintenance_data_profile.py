from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "predictive_maintenance_rul.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/predictive_maintenance_rul.csv 파일이 없습니다."
    )

pm_df = pd.read_csv(DATA_FILE)
print("데이터 크기:", pm_df.shape)
print("장비 수:", pm_df["equipment_id"].nunique())
life_summary = pm_df.groupby("equipment_id")["cycle"].max().add(1)
print(life_summary.describe())
sensor_summary = pm_df.groupby("failed")[
    ["temperature_c","vibration_rms_g","motor_current_a","particle_count","health_index"]
].mean()
print(sensor_summary.round(4))
