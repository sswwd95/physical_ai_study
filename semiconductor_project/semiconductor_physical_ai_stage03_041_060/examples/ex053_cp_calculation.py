from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/semiconductor_sensor_data.csv 파일이 없습니다.")

sensor_df = pd.read_csv(DATA_FILE)

lsl = 69.0
usl = 75.0
sigma = sensor_df["chamber_temp_c"].std(ddof=1)

cp = (usl - lsl) / (6 * sigma)

print(f"온도 표준편차: {sigma:.4f}")
print(f"Cp: {cp:.4f}")
print(
    "판정:",
    "잠재 공정능력 양호"
    if cp >= 1.33
    else "잠재 공정능력 개선 필요",
)
