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

from sklearn.model_selection import GroupShuffleSplit
sensor_df=pd.read_csv(DATA_FILE)
X=sensor_df.drop(columns=["timestamp","fault_type"]); y=sensor_df["fault_type"]; groups=sensor_df["equipment_id"]
split=GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42)
tr,te=next(split.split(X,y,groups))
print("학습 장비:",sorted(groups.iloc[tr].unique()))
print("평가 장비:",sorted(groups.iloc[te].unique()))
print("교집합:",set(groups.iloc[tr]) & set(groups.iloc[te]))
