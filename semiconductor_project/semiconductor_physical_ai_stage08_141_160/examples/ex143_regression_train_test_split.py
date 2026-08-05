from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_yield_regression.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_yield_regression.csv 파일이 없습니다."
    )

from sklearn.model_selection import train_test_split

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(
    columns=["timestamp", "lot_id", "yield_percent"]
)
y = sensor_df["yield_percent"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42,
)

print("학습 수율 평균:", round(y_train.mean(), 3))
print("평가 수율 평균:", round(y_test.mean(), 3))
print("학습 수율 표준편차:", round(y_train.std(), 3))
print("평가 수율 표준편차:", round(y_test.std(), 3))
