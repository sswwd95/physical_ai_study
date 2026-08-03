"""
반도체 Physical AI 하네스 엔지니어링 실습 021~025
Windows 10 / Anaconda / Pandas
결측값 탐지와 처리 품질 비교
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_missing.csv"
)
ROW_OUTPUT = (
    PROJECT_ROOT
    / "outputs"
    / "missing_row_patterns.csv"
)
BLOCK_OUTPUT = (
    PROJECT_ROOT
    / "outputs"
    / "missing_blocks.csv"
)

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 각 행에서 결측인 센서 이름을 문자열로 만든다.
def collect_missing_sensors(row):
    missing = [
        sensor
        for sensor in sensor_columns
        if pd.isna(row[sensor])
    ]
    return ",".join(missing)

df["missing_sensors"] = df.apply(
    collect_missing_sensors,
    axis=1,
)

# 2. 결측 센서 개수를 계산한다.
df["missing_sensor_count"] = (
    df[sensor_columns]
    .isna()
    .sum(axis=1)
)

# 3. 결측이 있는 행만 별도로 저장한다.
missing_rows = df.loc[
    df["missing_sensor_count"] > 0,
    [
        "timestamp",
        "lot_id",
        "recipe_id",
        "missing_sensor_count",
        "missing_sensors",
    ],
].copy()

missing_rows.to_csv(
    ROW_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

# 4. 센서별 연속 결측 블록을 찾는다.
blocks = []

for sensor in sensor_columns:
    is_missing = df[sensor].isna()

    # False→True 전환점마다 새로운 그룹 번호를 만든다.
    group_id = (
        is_missing.ne(is_missing.shift())
        .cumsum()
    )

    for _, block in df.loc[is_missing].groupby(
        group_id[is_missing]
    ):
        start_index = int(block.index.min())
        end_index = int(block.index.max())

        blocks.append(
            {
                "sensor": sensor,
                "start_index": start_index,
                "end_index": end_index,
                "start_time": block["timestamp"].min(),
                "end_time": block["timestamp"].max(),
                "length": len(block),
            }
        )

# 5. 연속 결측 블록을 길이가 긴 순서로 정렬한다.
block_df = pd.DataFrame(blocks)

if not block_df.empty:
    block_df = block_df.sort_values(
        ["length", "sensor"],
        ascending=[False, True],
    ).reset_index(drop=True)

block_df.to_csv(
    BLOCK_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

print("[결측 행 패턴]")
print(missing_rows.head(20))
print()
print("[연속 결측 블록]")
print(block_df)
print(f"[완료] 행 패턴: {ROW_OUTPUT}")
print(f"[완료] 결측 블록: {BLOCK_OUTPUT}")
