"""
반도체 Physical AI 하네스 엔지니어링 실습 041~045
Windows 10 / Anaconda / Pandas / scikit-learn
스케일링, 파생 변수, 전처리 파이프라인
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_engineered_features.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

# 1. 센서의 1초 변화량을 만든다.
df["temperature_delta"] = df["temperature_c"].diff()
df["pressure_delta"] = df["pressure_kpa"].diff()
df["vibration_delta"] = df["vibration_rms"].diff()
df["current_delta"] = df["motor_current_a"].diff()

# 2. 최근 30초 이동평균과 이동표준편차를 만든다.
for sensor in [
    "temperature_c",
    "pressure_kpa",
    "vibration_rms",
    "motor_current_a",
]:
    df[f"{sensor}_ma30"] = (
        df[sensor]
        .rolling(window=30, min_periods=5)
        .mean()
    )

    df[f"{sensor}_std30"] = (
        df[sensor]
        .rolling(window=30, min_periods=5)
        .std()
    )

# 3. 설비 부하를 표현하는 교육용 복합 지표를 만든다.
df["mechanical_load_index"] = (
    df["vibration_rms"] * df["motor_current_a"]
)

# 4. 온도와 압력의 기준점 이탈 정도를 만든다.
df["temperature_deviation_from_65"] = (
    df["temperature_c"] - 65.0
)

df["pressure_deviation_from_101_3"] = (
    df["pressure_kpa"] - 101.3
)

# 5. 시간 특징을 추출한다.
df["hour"] = df["timestamp"].dt.hour
df["minute"] = df["timestamp"].dt.minute
df["second"] = df["timestamp"].dt.second

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[생성된 파생 변수]")
new_columns = [
    column
    for column in df.columns
    if column not in [
        "timestamp",
        "lot_id",
        "recipe_id",
        "temperature_c",
        "pressure_kpa",
        "gas_flow_sccm",
        "vibration_rms",
        "motor_current_a",
    ]
]
print(new_columns)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
