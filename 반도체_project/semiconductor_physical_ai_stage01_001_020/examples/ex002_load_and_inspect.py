from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("데이터가 없습니다. 실습 001을 먼저 실행하세요.")

sensor_df = pd.read_csv(DATA_FILE, parse_dates=["timestamp"])

print("행과 열:", sensor_df.shape)
print("\n컬럼 목록:")
print(sensor_df.columns.tolist())
print("\n자료형:")
print(sensor_df.dtypes)
print("\n앞의 5행:")
print(sensor_df.head())
