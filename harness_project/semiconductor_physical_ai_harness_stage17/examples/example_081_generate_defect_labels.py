"""
반도체 Physical AI 하네스 엔지니어링 실습 081~085
Windows 10 / Anaconda / Pandas / SciPy
불량 라벨, 불량률, 교차표, 위험비 분석
"""

from pathlib import Path
import json
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "wafer_process_quality.csv"
RULE_PATH = PROJECT_ROOT / "data" / "defect_rules.json"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "wafer_with_generated_labels.csv"
SUMMARY_PATH = PROJECT_ROOT / "outputs" / "generated_label_summary.json"

df = pd.read_csv(DATA_PATH)
rules = json.loads(RULE_PATH.read_text(encoding="utf-8"))

# 1. 불량 판정 규칙을 읽는다.
quality_threshold = float(rules["quality_score_threshold"])
temperature_low = float(rules["temperature_low"])
temperature_high = float(rules["temperature_high"])
vibration_high = float(rules["vibration_high"])

# 2. 규칙별 boolean 열을 만든다.
df["rule_quality_low"] = (
    df["quality_score"] < quality_threshold
)

df["rule_temperature_outside"] = (
    ~df["temperature_c"].between(
        temperature_low,
        temperature_high,
    )
)

df["rule_vibration_high"] = (
    df["vibration_rms"] > vibration_high
)

# 3. 하나라도 참이면 생성 불량 라벨을 1로 지정한다.
rule_columns = [
    "rule_quality_low",
    "rule_temperature_outside",
    "rule_vibration_high",
]

df["generated_defect_flag"] = (
    df[rule_columns]
    .any(axis=1)
    .astype(int)
)

# 4. 기존 라벨과의 일치 여부를 계산한다.
df["label_agreement"] = (
    df["generated_defect_flag"]
    == df["defect_flag"]
)

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

summary = {
    "total_rows": len(df),
    "generated_defect_count": int(
        df["generated_defect_flag"].sum()
    ),
    "generated_defect_rate_percent": float(
        df["generated_defect_flag"].mean() * 100.0
    ),
    "existing_defect_count": int(df["defect_flag"].sum()),
    "label_agreement_rate_percent": float(
        df["label_agreement"].mean() * 100.0
    ),
}

SUMMARY_PATH.write_text(
    json.dumps(summary, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"[완료] 데이터: {OUTPUT_PATH}")
print(f"[완료] 요약: {SUMMARY_PATH}")
