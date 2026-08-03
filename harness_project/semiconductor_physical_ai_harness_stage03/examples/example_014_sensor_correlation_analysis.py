"""
반도체 Physical AI 하네스 엔지니어링 실습 011~015
Windows 10 / Anaconda / Pandas / PyMC 연계 준비
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
CORR_PATH = PROJECT_ROOT / "outputs" / "sensor_correlation_matrix.csv"
PAIR_PATH = PROJECT_ROOT / "outputs" / "strong_sensor_pairs.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 피어슨 상관계수를 계산한다.
correlation = df[sensor_columns].corr(method="pearson")

# 2. 상관행렬을 CSV로 저장한다.
correlation.to_csv(CORR_PATH, encoding="utf-8-sig")

# 3. 중복되지 않는 센서 쌍만 추출한다.
pairs = []

for index, sensor_a in enumerate(sensor_columns):
    for sensor_b in sensor_columns[index + 1:]:
        value = float(correlation.loc[sensor_a, sensor_b])
        pairs.append({
            "sensor_a": sensor_a,
            "sensor_b": sensor_b,
            "correlation": value,
            "absolute_correlation": abs(value),
        })

pair_df = pd.DataFrame(pairs)

# 4. 절댓값이 큰 순서로 정렬한다.
pair_df = pair_df.sort_values(
    "absolute_correlation",
    ascending=False,
).reset_index(drop=True)

# 5. |상관계수|가 0.5 이상인 쌍을 강한 후보로 표시한다.
pair_df["strong_candidate"] = (
    pair_df["absolute_correlation"] >= 0.5
)

pair_df.to_csv(PAIR_PATH, index=False, encoding="utf-8-sig")

print("[상관행렬]")
print(correlation.round(3))
print("\n[상위 센서 쌍]")
print(pair_df.head(10).round(3))
print("\n주의: 상관관계는 인과관계를 의미하지 않습니다.")
