"""
반도체 Physical AI 하네스 엔지니어링 실습 031~035
Windows 10 / Anaconda / Pandas
단위, 시간축, 중복, 드리프트 데이터 품질
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_mixed_units.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "equipment_sensor_log_converted.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 화씨를 섭씨로 변환한다.
temperature_c = (
    df["temperature_f"] - 32.0
) * 5.0 / 9.0

# 2. Pa를 kPa로 변환한다.
pressure_kpa = df["pressure_pa"] / 1000.0

# 3. slm을 sccm으로 변환한다.
gas_flow_sccm = df["gas_flow_slm"] * 1000.0

# 4. m/s를 mm/s로 변환한다.
vibration_rms = df["vibration_mps"] * 1000.0

# 5. mA를 A로 변환한다.
motor_current_a = df["motor_current_ma"] / 1000.0

# 6. 표준 열 이름과 표준 단위로 새 데이터프레임을 만든다.
converted = pd.DataFrame(
    {
        "timestamp": df["timestamp"],
        "lot_id": df["lot_id"],
        "recipe_id": df["recipe_id"],
        "temperature_c": temperature_c,
        "pressure_kpa": pressure_kpa,
        "gas_flow_sccm": gas_flow_sccm,
        "vibration_rms": vibration_rms,
        "motor_current_a": motor_current_a,
    }
)

# 7. 변환 후 기본 범위를 확인한다.
if not converted["temperature_c"].between(
    -273.15,
    200.0,
).all():
    raise ValueError("온도 단위 변환 결과가 비정상입니다.")

if not converted["pressure_kpa"].between(
    0.0,
    1000.0,
).all():
    raise ValueError("압력 단위 변환 결과가 비정상입니다.")

# 8. 변환 결과를 저장한다.
converted.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(converted.head())
print(f"[완료] 표준 단위 데이터 저장: {OUTPUT_PATH}")
