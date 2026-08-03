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

from sklearn.model_selection import train_test_split

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(
    columns=["timestamp", "lot_id", "defect", "defect_type"]
)
y = sensor_df["defect"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

print("전체 불량 비율:", round(y.mean(), 4))
print("학습 불량 비율:", round(y_train.mean(), 4))
print("평가 불량 비율:", round(y_test.mean(), 4))
print("학습 크기:", x_train.shape)
print("평가 크기:", x_test.shape)
