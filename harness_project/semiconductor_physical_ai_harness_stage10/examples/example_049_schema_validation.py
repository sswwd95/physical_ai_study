"""
반도체 Physical AI 하네스 엔지니어링 실습 046~050
Windows 10 / Anaconda / Pandas / scikit-learn
시계열 분할, 누출 방지, 전처리 재사용, 품질 리포트
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "schema_validation_report.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 기대 스키마를 정의한다.
schema = {
    "timestamp": "datetime64[ns]",
    "lot_id": "object",
    "recipe_id": "object",
    "temperature_c": "float64",
    "pressure_kpa": "float64",
    "gas_flow_sccm": "float64",
    "vibration_rms": "float64",
    "motor_current_a": "float64",
}

issues = []

# 2. 열 존재 여부와 자료형을 검사한다.
for column, expected_dtype in schema.items():
    if column not in df.columns:
        issues.append(
            {
                "column": column,
                "issue": "missing_column",
                "expected": expected_dtype,
                "actual": None,
            }
        )
        continue

    actual_dtype = str(df[column].dtype)

    if actual_dtype != expected_dtype:
        issues.append(
            {
                "column": column,
                "issue": "dtype_mismatch",
                "expected": expected_dtype,
                "actual": actual_dtype,
            }
        )

# 3. 중복 열 이름과 예상 밖 열도 검사한다.
unexpected_columns = [
    column for column in df.columns
    if column not in schema
]

report = {
    "validation_passed": len(issues) == 0,
    "row_count": len(df),
    "column_count": len(df.columns),
    "unexpected_columns": unexpected_columns,
    "issues": issues,
}

OUTPUT_PATH.write_text(
    json.dumps(report, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(report, ensure_ascii=False, indent=2))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
