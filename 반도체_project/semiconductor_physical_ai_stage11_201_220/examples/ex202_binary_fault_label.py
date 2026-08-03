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
sensor_df["fault_binary"] = (sensor_df["fault_type"] != "normal").astype(int)
print(sensor_df["fault_binary"].value_counts())
sensor_df[["fault_type","fault_binary"]].drop_duplicates().to_csv(
    OUTPUT_DIR/"ex202_fault_label_mapping.csv",index=False,encoding="utf-8-sig")
