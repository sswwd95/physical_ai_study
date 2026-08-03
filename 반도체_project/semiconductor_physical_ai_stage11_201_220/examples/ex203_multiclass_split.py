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

from sklearn.model_selection import train_test_split
sensor_df = pd.read_csv(DATA_FILE)
X=sensor_df.drop(columns=["timestamp","fault_type"])
y=sensor_df["fault_type"]
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=.25,random_state=42,stratify=y)
print(pd.DataFrame({
    "overall":y.value_counts(normalize=True),
    "train":y_train.value_counts(normalize=True),
    "test":y_test.value_counts(normalize=True)
}).fillna(0).round(4))
