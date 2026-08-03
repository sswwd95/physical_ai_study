"""
반도체 Physical AI 하네스 엔지니어링 실습 051~055
Windows 10 / Anaconda / Pandas / Matplotlib
SPC 관리도와 경보 규칙
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "temperature_spc_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "western_electric_alerts.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 초기 200개 샘플을 기준으로 평균과 표준편차를 계산한다.
baseline = df["temperature_c"].iloc[:200]
mean_value = float(baseline.mean())
std_value = float(baseline.std(ddof=1))

z = (df["temperature_c"] - mean_value) / std_value

result = df.copy()
result["zscore"] = z

# 2. 규칙 1: 한 점이 3σ 밖에 있음.
result["rule1_beyond_3sigma"] = z.abs() > 3.0

# 3. 규칙 2: 연속 3점 중 2점이 같은 방향 2σ 밖에 있음.
rule2 = pd.Series(False, index=df.index)

for end in range(2, len(df)):
    window = z.iloc[end - 2:end + 1]

    upper_count = int((window > 2.0).sum())
    lower_count = int((window < -2.0).sum())

    if upper_count >= 2 or lower_count >= 2:
        rule2.iloc[end] = True

result["rule2_two_of_three_beyond_2sigma"] = rule2

# 4. 규칙 3: 연속 5점 중 4점이 같은 방향 1σ 밖에 있음.
rule3 = pd.Series(False, index=df.index)

for end in range(4, len(df)):
    window = z.iloc[end - 4:end + 1]

    upper_count = int((window > 1.0).sum())
    lower_count = int((window < -1.0).sum())

    if upper_count >= 4 or lower_count >= 4:
        rule3.iloc[end] = True

result["rule3_four_of_five_beyond_1sigma"] = rule3

# 5. 규칙 4: 8점 연속 같은 쪽에 있음.
rule4 = pd.Series(False, index=df.index)

for end in range(7, len(df)):
    window = z.iloc[end - 7:end + 1]

    if (window > 0).all() or (window < 0).all():
        rule4.iloc[end] = True

result["rule4_eight_on_same_side"] = rule4

rule_columns = [
    "rule1_beyond_3sigma",
    "rule2_two_of_three_beyond_2sigma",
    "rule3_four_of_five_beyond_1sigma",
    "rule4_eight_on_same_side",
]

result["any_alert"] = result[rule_columns].any(axis=1)

alerts = result.loc[
    result["any_alert"],
    [
        "timestamp",
        "lot_id",
        "recipe_id",
        "temperature_c",
        "zscore",
    ] + rule_columns,
].copy()

alerts.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[Western Electric 경보]")
print(alerts.head(30).round(4))
print()
print("총 경보 행 수:", len(alerts))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
