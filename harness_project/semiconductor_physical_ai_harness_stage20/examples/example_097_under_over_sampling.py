"""
반도체 Physical AI 하네스 엔지니어링 실습 096~100
Windows 10 / Anaconda / Pandas / scikit-learn
불균형 데이터 처리와 001~100 통합 미니 프로젝트
"""

from pathlib import Path
import pandas as pd
from sklearn.utils import resample

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "imbalanced_wafer_quality.csv"
UNDER_PATH = PROJECT_ROOT / "outputs" / "random_undersampled_training.csv"
OVER_PATH = PROJECT_ROOT / "outputs" / "random_oversampled_training.csv"
SUMMARY_PATH = PROJECT_ROOT / "outputs" / "sampling_comparison.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
df = df.sort_values("timestamp").reset_index(drop=True)

split_index = int(len(df) * 0.70)
train_df = df.iloc[:split_index].copy()

majority = train_df.loc[train_df["defect_flag"] == 0]
minority = train_df.loc[train_df["defect_flag"] == 1]

# 1. Random Under Sampling
majority_under = resample(
    majority,
    replace=False,
    n_samples=len(minority),
    random_state=42,
)

under_df = pd.concat(
    [majority_under, minority],
    ignore_index=True,
).sample(frac=1.0, random_state=42).reset_index(drop=True)

# 2. Random Over Sampling
minority_over = resample(
    minority,
    replace=True,
    n_samples=len(majority),
    random_state=42,
)

over_df = pd.concat(
    [majority, minority_over],
    ignore_index=True,
).sample(frac=1.0, random_state=42).reset_index(drop=True)

under_df.to_csv(
    UNDER_PATH,
    index=False,
    encoding="utf-8-sig",
)

over_df.to_csv(
    OVER_PATH,
    index=False,
    encoding="utf-8-sig",
)

summary = pd.DataFrame([
    {
        "dataset": "original_train",
        "row_count": len(train_df),
        "normal_count": int((train_df["defect_flag"] == 0).sum()),
        "defect_count": int((train_df["defect_flag"] == 1).sum()),
    },
    {
        "dataset": "undersampled_train",
        "row_count": len(under_df),
        "normal_count": int((under_df["defect_flag"] == 0).sum()),
        "defect_count": int((under_df["defect_flag"] == 1).sum()),
    },
    {
        "dataset": "oversampled_train",
        "row_count": len(over_df),
        "normal_count": int((over_df["defect_flag"] == 0).sum()),
        "defect_count": int((over_df["defect_flag"] == 1).sum()),
    },
])

summary.to_csv(
    SUMMARY_PATH,
    index=False,
    encoding="utf-8-sig",
)

print(summary)
print(f"[완료] Under Sampling: {UNDER_PATH}")
print(f"[완료] Over Sampling: {OVER_PATH}")
