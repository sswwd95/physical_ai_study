"""
반도체 Physical AI 하네스 엔지니어링 실습 096~100
Windows 10 / Anaconda / Pandas / scikit-learn
불균형 데이터 처리와 001~100 통합 미니 프로젝트
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "imbalanced_wafer_quality.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "synthetic_minority_training.csv"
SUMMARY_PATH = PROJECT_ROOT / "outputs" / "synthetic_sampling_summary.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

split_index = int(len(df) * 0.70)
train_df = df.iloc[:split_index].copy()

numeric_features = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

majority = train_df.loc[train_df["defect_flag"] == 0].copy()
minority = train_df.loc[train_df["defect_flag"] == 1].copy()

target_minority_count = len(majority)
synthetic_count = target_minority_count - len(minority)

if len(minority) < 2:
    raise RuntimeError("합성 샘플 생성을 위한 불량 데이터가 부족합니다.")

# 1. 불량 샘플의 최근접 이웃을 학습한다.
neighbor_count = min(6, len(minority))
neighbors = NearestNeighbors(
    n_neighbors=neighbor_count,
)
neighbors.fit(minority[numeric_features])

rng = np.random.default_rng(42)
synthetic_rows = []

# 2. 임의의 불량 샘플과 이웃 사이를 선형 보간한다.
for synthetic_index in range(synthetic_count):
    base_position = rng.integers(0, len(minority))
    base_row = minority.iloc[base_position]

    _, indices = neighbors.kneighbors(
        base_row[numeric_features]
        .to_numpy(dtype=float)
        .reshape(1, -1)
    )

    candidate_positions = indices[0][1:]
    neighbor_position = int(rng.choice(candidate_positions))
    neighbor_row = minority.iloc[neighbor_position]

    gap = float(rng.random())

    new_values = {}
    for feature in numeric_features:
        new_values[feature] = (
            base_row[feature]
            + gap * (
                neighbor_row[feature]
                - base_row[feature]
            )
        )

    new_values.update({
        "timestamp": base_row["timestamp"],
        "wafer_id": f"SYNTH_{synthetic_index + 1:05d}",
        "lot_id": "SYNTHETIC",
        "recipe_id": base_row["recipe_id"],
        "tool_id": base_row["tool_id"],
        "defect_flag": 1,
    })

    synthetic_rows.append(new_values)

synthetic_df = pd.DataFrame(synthetic_rows)

balanced_df = pd.concat(
    [majority, minority, synthetic_df],
    ignore_index=True,
).sample(frac=1.0, random_state=42).reset_index(drop=True)

balanced_df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

summary = pd.DataFrame([
    {
        "dataset": "original_train",
        "row_count": len(train_df),
        "normal_count": len(majority),
        "defect_count": len(minority),
        "synthetic_count": 0,
    },
    {
        "dataset": "synthetic_balanced_train",
        "row_count": len(balanced_df),
        "normal_count": int((balanced_df["defect_flag"] == 0).sum()),
        "defect_count": int((balanced_df["defect_flag"] == 1).sum()),
        "synthetic_count": len(synthetic_df),
    },
])

summary.to_csv(
    SUMMARY_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(summary)
print()
print(
    "주의: 이 코드는 교육용 SMOTE 유사 구현입니다. "
    "범주형 조건과 시간 순서를 엄밀히 보존하는 실제 SMOTE 구현은 아닙니다."
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
