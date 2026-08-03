"""
반도체 Physical AI 하네스 엔지니어링 실습 041~045
Windows 10 / Anaconda / Pandas / scikit-learn
스케일링, 파생 변수, 전처리 파이프라인
"""

from pathlib import Path
import json
import pandas as pd
from sklearn.preprocessing import RobustScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_robust_scaled.csv"
PARAM_PATH = PROJECT_ROOT / "outputs" / "robust_scaler_parameters.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 중앙값과 IQR을 사용하는 RobustScaler를 만든다.
scaler = RobustScaler(
    with_centering=True,
    with_scaling=True,
    quantile_range=(25.0, 75.0),
)

# 2. 이상값에 비교적 강건한 스케일링을 수행한다.
scaled_values = scaler.fit_transform(df[sensor_columns])

scaled_df = df[["timestamp", "lot_id", "recipe_id"]].copy()

for index, sensor in enumerate(sensor_columns):
    scaled_df[f"{sensor}_robust"] = scaled_values[:, index]

# 3. 중앙값과 IQR 규모를 저장한다.
parameters = {
    sensor: {
        "center_median": float(scaler.center_[index]),
        "scale_iqr": float(scaler.scale_[index]),
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

print("[Robust Scaling 결과 중앙값]")
print(scaled_df.filter(like="_robust").median().round(6))
print(f"[완료] 데이터: {OUTPUT_PATH}")
print(f"[완료] 파라미터: {PARAM_PATH}")
