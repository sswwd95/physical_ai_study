"""
반도체 Physical AI 하네스 엔지니어링 실습 096~100
Windows 10 / Anaconda / Pandas / scikit-learn
불균형 데이터 처리와 001~100 통합 미니 프로젝트
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "imbalanced_wafer_quality.csv"
CSV_OUTPUT = PROJECT_ROOT / "outputs" / "class_balance_summary.csv"
JSON_OUTPUT = PROJECT_ROOT / "outputs" / "class_balance_summary.json"

df = pd.read_csv(INPUT_PATH)

counts = (
    df["defect_flag"]
    .value_counts()
    .sort_index()
)

summary_df = pd.DataFrame({
    "class_label": counts.index,
    "row_count": counts.values,
})

summary_df["rate_percent"] = (
    summary_df["row_count"]
    / len(df)
    * 100.0
)

majority_count = int(summary_df["row_count"].max())
minority_count = int(summary_df["row_count"].min())

imbalance_ratio = (
    majority_count / minority_count
    if minority_count > 0
    else None
)

summary = {
    "total_rows": len(df),
    "normal_count": int((df["defect_flag"] == 0).sum()),
    "defect_count": int((df["defect_flag"] == 1).sum()),
    "defect_rate_percent": float(df["defect_flag"].mean() * 100.0),
    "imbalance_ratio_majority_to_minority": imbalance_ratio,
}

summary_df.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig",
)

JSON_OUTPUT.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(summary_df)
print()
print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] CSV: {CSV_OUTPUT}")
print(f"[완료] JSON: {JSON_OUTPUT}")
