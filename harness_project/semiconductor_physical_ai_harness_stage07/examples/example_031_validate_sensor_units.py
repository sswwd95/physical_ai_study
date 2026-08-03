"""
반도체 Physical AI 하네스 엔지니어링 실습 031~035
Windows 10 / Anaconda / Pandas
단위, 시간축, 중복, 드리프트 데이터 품질
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_mixed_units.csv"
)
UNIT_CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "sensor_units.json"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "outputs"
    / "sensor_unit_validation.csv"
)

df = pd.read_csv(INPUT_PATH)

# 1. 센서 단위 계약을 읽는다.
unit_config = json.loads(
    UNIT_CONFIG_PATH.read_text(encoding="utf-8")
)

# 2. 입력 열과 실제 단위의 대응 관계를 정의한다.
source_columns = {
    "temperature_c": {
        "column": "temperature_f",
        "source_unit": "degF",
    },
    "pressure_kpa": {
        "column": "pressure_pa",
        "source_unit": "Pa",
    },
    "gas_flow_sccm": {
        "column": "gas_flow_slm",
        "source_unit": "slm",
    },
    "vibration_rms": {
        "column": "vibration_mps",
        "source_unit": "m/s",
    },
    "motor_current_a": {
        "column": "motor_current_ma",
        "source_unit": "mA",
    },
}

rows = []

# 3. 입력 열 존재 여부와 허용 단위 여부를 검사한다.
for canonical_sensor, source_info in source_columns.items():
    source_column = source_info["column"]
    source_unit = source_info["source_unit"]
    contract = unit_config[canonical_sensor]

    column_exists = source_column in df.columns
    unit_allowed = (
        source_unit
        in contract["allowed_source_units"]
    )

    rows.append(
        {
            "canonical_sensor": canonical_sensor,
            "source_column": source_column,
            "source_unit": source_unit,
            "expected_unit": contract["expected_unit"],
            "column_exists": column_exists,
            "unit_allowed": unit_allowed,
            "validation_passed": (
                column_exists and unit_allowed
            ),
        }
    )

# 4. 검증 결과를 저장한다.
result = pd.DataFrame(rows)
result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[센서 단위 계약 검사]")
print(result)
print()

if not result["validation_passed"].all():
    raise ValueError(
        "센서 단위 계약 검사가 실패했습니다."
    )

print("[검사 통과] 모든 입력 단위가 허용 목록에 있습니다.")
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
