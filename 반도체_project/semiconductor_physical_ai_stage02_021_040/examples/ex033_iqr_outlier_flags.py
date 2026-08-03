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

sensor_columns = [
    "chamber_temp_c",
    "chamber_pressure_pa",
    "rf_power_w",
    "gas_flow_sccm",
    "vibration_g",
]

flag_columns = []
for column in sensor_columns:
    q1 = sensor_df[column].quantile(0.25)
    q3 = sensor_df[column].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    flag_column = f"{column}_iqr_outlier"
    sensor_df[flag_column] = ~sensor_df[column].between(lower, upper)
    flag_columns.append(flag_column)

    print(
        column,
        f"하한={lower:.3f}",
        f"상한={upper:.3f}",
        f"이상 후보={int(sensor_df[flag_column].sum())}",
    )

sensor_df["any_iqr_outlier"] = sensor_df[flag_columns].any(axis=1)
sensor_df.to_csv(
    OUTPUT_DIR / "ex033_iqr_outlier_flags.csv",
    index=False,
    encoding="utf-8-sig",
)
