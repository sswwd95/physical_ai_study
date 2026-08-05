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

sensor_df = pd.read_csv(DATA_FILE)

print("데이터 크기:", sensor_df.shape)
print("\n수율 요약:")
print(sensor_df["yield_percent"].describe().round(3))
print("\n레시피별 평균 수율:")
print(
    sensor_df.groupby("recipe")["yield_percent"]
    .mean()
    .sort_values(ascending=False)
    .round(3)
)
