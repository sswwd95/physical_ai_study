from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_multiclass_defects.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_multiclass_defects.csv 파일이 없습니다."
    )

sensor_df = pd.read_csv(DATA_FILE)

class_count = sensor_df["defect_type"].value_counts()
class_ratio = sensor_df["defect_type"].value_counts(normalize=True)

print("클래스 건수:")
print(class_count)
print("\n클래스 비율:")
print(class_ratio.round(4))

summary = (
    sensor_df.groupby("defect_type")[
        [
            "chamber_temp_c",
            "chamber_pressure_pa",
            "rf_power_w",
            "vibration_g",
            "particle_count",
            "etch_rate_nm_min",
            "uniformity_percent",
        ]
    ]
    .mean()
)

print("\n클래스별 평균:")
print(summary.round(3))
summary.to_csv(
    OUTPUT_DIR / "ex121_multiclass_summary.csv",
    encoding="utf-8-sig",
)
