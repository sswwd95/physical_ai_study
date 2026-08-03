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

sensor_df = pd.read_csv(DATA_FILE)

print("데이터 크기:", sensor_df.shape)
print("\n불량 클래스 건수:")
print(sensor_df["defect"].value_counts())
print("\n불량 비율:", round(sensor_df["defect"].mean(), 4))
print("\n불량 유형:")
print(sensor_df["defect_type"].value_counts())

summary = (
    sensor_df.groupby("defect")[
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

print("\n정상·불량 그룹 평균:")
print(summary.round(3))
summary.to_csv(
    OUTPUT_DIR / "ex101_defect_group_summary.csv",
    encoding="utf-8-sig",
)
