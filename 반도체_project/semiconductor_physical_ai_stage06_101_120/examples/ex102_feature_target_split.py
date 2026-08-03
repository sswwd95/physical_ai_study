from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_defect_classification.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_defect_classification.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE)

drop_columns = [
    "timestamp",
    "lot_id",
    "defect",
    "defect_type",
]

x = sensor_df.drop(columns=drop_columns)
y = sensor_df["defect"]

print("입력 컬럼:")
print(x.columns.tolist())
print("X 크기:", x.shape)
print("y 클래스 건수:")
print(y.value_counts())
