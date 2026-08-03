"""
반도체 Physical AI 하네스 엔지니어링 실습 041~045
Windows 10 / Anaconda / Pandas / scikit-learn
스케일링, 파생 변수, 전처리 파이프라인
"""

from pathlib import Path
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_minmax_scaled.csv"
PARAM_PATH = PROJECT_ROOT / "outputs" / "minmax_scaler_parameters.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 0~1 범위의 Min-Max 스케일러를 만든다.
scaler = MinMaxScaler(feature_range=(0.0, 1.0))

# 2. 센서별 최솟값과 최댓값을 이용해 정규화한다.
scaled_values = scaler.fit_transform(df[sensor_columns])

scaled_df = df[["timestamp", "lot_id", "recipe_id"]].copy()

for index, sensor in enumerate(sensor_columns):
    scaled_df[f"{sensor}_minmax"] = scaled_values[:, index]

# 3. 재사용을 위해 원래 최솟값과 최댓값을 저장한다.
parameters = {
    sensor: {
        "data_min": float(scaler.data_min_[index]),
        "data_max": float(scaler.data_max_[index]),
    }
    for index, sensor in enumerate(sensor_columns)
}

scaled_df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

PARAM_PATH.write_text(
    json.dumps(parameters, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print("[정규화 열별 최솟값]")
print(scaled_df.filter(like="_minmax").min())
print("[정규화 열별 최댓값]")
print(scaled_df.filter(like="_minmax").max())
print(f"[완료] 데이터: {OUTPUT_PATH}")
print(f"[완료] 파라미터: {PARAM_PATH}")
