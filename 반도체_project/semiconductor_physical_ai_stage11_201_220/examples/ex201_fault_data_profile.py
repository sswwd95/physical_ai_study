from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "equipment_fault_diagnosis.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/equipment_fault_diagnosis.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE)
print("데이터 크기:", sensor_df.shape)
print(sensor_df["fault_type"].value_counts())
summary = sensor_df.groupby("fault_type")[
    ["temperature_c","pressure_pa","vibration_rms_g","motor_current_a","particle_count"]
].mean()
print(summary.round(3))
summary.to_csv(OUTPUT_DIR/"ex201_fault_summary.csv",encoding="utf-8-sig")
