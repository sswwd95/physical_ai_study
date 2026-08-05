from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_sensor_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "기본 데이터가 없습니다. 프로젝트 루트에서 "
        "python generate_base_data.py를 먼저 실행하세요."
    )

sensor_df = pd.read_csv(DATA_FILE)
quality_df = sensor_df.copy()

quality_df.loc[[15, 80, 155, 260], "chamber_pressure_pa"] = np.nan
quality_df.loc[[40, 140, 240], "rf_power_w"] = np.nan
quality_df.loc[[35, 135], "process_state"] = "unknown"
quality_df.loc[200, "timestamp"] = quality_df.loc[150, "timestamp"]

duplicate_rows = quality_df.iloc[[20, 21]].copy()
quality_df = pd.concat([quality_df, duplicate_rows], ignore_index=True)

output_file = ROOT / "data" / "sensor_data_with_quality_errors.csv"
quality_df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("오류 연습 데이터 저장:", output_file)
print("행 수:", len(quality_df))
print("압력 결측:", int(quality_df["chamber_pressure_pa"].isna().sum()))
print("RF 결측:", int(quality_df["rf_power_w"].isna().sum()))
print("unknown 상태:", int((quality_df["process_state"] == "unknown").sum()))
print("완전 중복:", int(quality_df.duplicated().sum()))
