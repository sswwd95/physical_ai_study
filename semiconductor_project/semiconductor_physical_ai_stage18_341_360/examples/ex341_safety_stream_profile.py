from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")

safe_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])
print("데이터 크기:",safe_df.shape)
print("\n이상 유형:")
print(safe_df["anomaly_type"].value_counts())
print("\n심각도:")
print(safe_df["severity_level"].value_counts().sort_index())
print("\n인터록 위반:")
print((safe_df[["door_closed","cooling_ok","vacuum_ok"]]==0).sum())
