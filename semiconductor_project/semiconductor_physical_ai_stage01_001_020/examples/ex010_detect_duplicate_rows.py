from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

duplicated_sample = sensor_df.iloc[:3].copy()
working_df = pd.concat([sensor_df, duplicated_sample], ignore_index=True)

duplicate_count = working_df.duplicated().sum()
clean_df = working_df.drop_duplicates().reset_index(drop=True)

print("처리 전 행 수:", len(working_df))
print("중복 행 수:", duplicate_count)
print("처리 후 행 수:", len(clean_df))
