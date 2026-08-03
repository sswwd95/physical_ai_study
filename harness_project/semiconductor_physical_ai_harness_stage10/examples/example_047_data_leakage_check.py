"""
반도체 Physical AI 하네스 엔지니어링 실습 046~050
Windows 10 / Anaconda / Pandas / scikit-learn
시계열 분할, 누출 방지, 전처리 재사용, 품질 리포트
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "outputs"
REPORT_PATH = OUTPUT_DIR / "data_leakage_report.csv"

train_df = pd.read_csv(
    OUTPUT_DIR / "train.csv",
    parse_dates=["timestamp"],
)
validation_df = pd.read_csv(
    OUTPUT_DIR / "validation.csv",
    parse_dates=["timestamp"],
)
test_df = pd.read_csv(
    OUTPUT_DIR / "test.csv",
    parse_dates=["timestamp"],
)

rows = []

# 1. 데이터셋 간 시간 범위가 겹치는지 검사한다.
checks = [
    (
        "train_before_validation",
        train_df["timestamp"].max()
        < validation_df["timestamp"].min(),
    ),
    (
        "validation_before_test",
        validation_df["timestamp"].max()
        < test_df["timestamp"].min(),
    ),
]

for name, passed in checks:
    rows.append({
        "check_name": name,
        "passed": bool(passed),
        "details": "",
    })

# 2. 동일 timestamp가 데이터셋 사이에 중복되는지 검사한다.
dataset_pairs = [
    ("train_validation", train_df, validation_df),
    ("train_test", train_df, test_df),
    ("validation_test", validation_df, test_df),
]

for name, left, right in dataset_pairs:
    overlap = set(left["timestamp"]).intersection(
        set(right["timestamp"])
    )

    rows.append({
        "check_name": f"timestamp_overlap_{name}",
        "passed": len(overlap) == 0,
        "details": f"overlap_count={len(overlap)}",
    })

# 3. 메타데이터 열이 특징 목록에 포함되지 않았는지 검사한다.
feature_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

for forbidden in ["timestamp", "lot_id", "recipe_id"]:
    rows.append({
        "check_name": f"forbidden_feature_{forbidden}",
        "passed": forbidden not in feature_columns,
        "details": ",".join(feature_columns),
    })

result = pd.DataFrame(rows)
result.to_csv(
    REPORT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(result)

if not result["passed"].all():
    raise RuntimeError(
        "데이터 누출 검사에서 실패 항목이 발견되었습니다."
    )

print("[검사 통과] 명백한 시계열 누출이 없습니다.")
