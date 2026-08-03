"""
반도체 Physical AI 하네스 엔지니어링 실습 041~045
Windows 10 / Anaconda / Pandas / scikit-learn
스케일링, 파생 변수, 전처리 파이프라인
"""

from pathlib import Path
import json
import pandas as pd
from sklearn.preprocessing import StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_standard_scaled.csv"
PARAM_PATH = PROJECT_ROOT / "outputs" / "standard_scaler_parameters.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 표준화 객체를 만든다.
scaler = StandardScaler()

# 2. 센서값에서 평균을 빼고 표준편차로 나눈다.
scaled_values = scaler.fit_transform(df[sensor_columns])

# 3. 표준화 결과 열을 만든다.
scaled_df = df[["timestamp", "lot_id", "recipe_id"]].copy()

for index, sensor in enumerate(sensor_columns):
    scaled_df[f"{sensor}_z"] = scaled_values[:, index]

# 4. 학습된 평균과 표준편차를 저장한다.
parameters = {
    sensor: {
        "mean": float(scaler.mean_[index]),
        "scale": float(scaler.scale_[index]),
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

print("[표준화 결과 평균]")
print(scaled_df.filter(like="_z").mean().round(6))
print("[표준화 결과 표준편차]")
print(scaled_df.filter(like="_z").std(ddof=0).round(6))
print(f"[완료] 데이터: {OUTPUT_PATH}")
print(f"[완료] 파라미터: {PARAM_PATH}")
