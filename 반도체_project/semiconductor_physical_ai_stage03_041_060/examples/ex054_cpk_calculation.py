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
mean_value = sensor_df["chamber_temp_c"].mean()
sigma = sensor_df["chamber_temp_c"].std(ddof=1)

cpu = (usl - mean_value) / (3 * sigma)
cpl = (mean_value - lsl) / (3 * sigma)
cpk = min(cpu, cpl)

near_side = "USL" if cpu < cpl else "LSL"

print(f"평균={mean_value:.4f}, 표준편차={sigma:.4f}")
print(f"CPU={cpu:.4f}, CPL={cpl:.4f}, Cpk={cpk:.4f}")
print("평균이 더 가까운 규격:", near_side)
