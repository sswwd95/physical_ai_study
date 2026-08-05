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

from sklearn.model_selection import GroupShuffleSplit

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(
    columns=["timestamp", "lot_id", "defect", "defect_type"]
)
y = sensor_df["defect"]
groups = sensor_df["lot_id"]

splitter = GroupShuffleSplit(
    n_splits=1,
    test_size=0.25,
    random_state=42,
)

train_index, test_index = next(
    splitter.split(x, y, groups=groups)
)

train_lots = set(groups.iloc[train_index])
test_lots = set(groups.iloc[test_index])

print("학습 LOT 수:", len(train_lots))
print("평가 LOT 수:", len(test_lots))
print("LOT 교집합:", train_lots & test_lots)
print("학습 행 수:", len(train_index))
print("평가 행 수:", len(test_index))
