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

pm_df=pd.read_csv(DATA_FILE).sort_values(["equipment_id","cycle"])
for col in ["temperature_c","vibration_rms_g","motor_current_a","particle_count"]:
    pm_df[f"{col}_roll10_mean"]=pm_df.groupby("equipment_id")[col].transform(
        lambda s:s.rolling(10,min_periods=3).mean())
    pm_df[f"{col}_roll10_std"]=pm_df.groupby("equipment_id")[col].transform(
        lambda s:s.rolling(10,min_periods=3).std())
print(pm_df.filter(regex="roll10").tail().round(4))
pm_df.to_csv(OUTPUT_DIR/"ex223_rolling_features.csv",index=False,encoding="utf-8-sig")
