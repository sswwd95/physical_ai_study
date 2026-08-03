"""
반도체 Physical AI 하네스 엔지니어링 실습 066~070
Windows 10 / Anaconda / Pandas / scikit-learn
PCA 기반 다변량 공정 모니터링
"""

from pathlib import Path
import joblib
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "pca_process_log.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "pca_monitoring_bundle.joblib"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "pca_score_monitoring.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
bundle = joblib.load(MODEL_PATH)

sensor_columns = bundle["sensor_columns"]
scaler = bundle["scaler"]
pca = bundle["pca"]

# 1. 저장된 scaler로 전체 데이터를 변환한다.
scaled = scaler.transform(df[sensor_columns])

# 2. PCA 주성분 점수를 계산한다.
scores = pca.transform(scaled)

result = df.copy()

for component_index in range(scores.shape[1]):
    result[
        f"pc{component_index + 1}_score"
    ] = scores[:, component_index]

# 3. 기준 구간 주성분 점수의 평균±3σ 경계를 만든다.
baseline_rows = bundle["baseline_rows"]

for component_index in range(scores.shape[1]):
    column = f"pc{component_index + 1}_score"
    baseline_score = result[column].iloc[:baseline_rows]

    mean_value = float(baseline_score.mean())
    std_value = float(baseline_score.std(ddof=1))

    result[f"{column}_ucl"] = mean_value + 3.0 * std_value
    result[f"{column}_lcl"] = mean_value - 3.0 * std_value
    result[f"{column}_alert"] = (
        (result[column] > result[f"{column}_ucl"])
        | (result[column] < result[f"{column}_lcl"])
    )

alert_columns = [
    column
    for column in result.columns
    if column.endswith("_score_alert")
]

result["any_pc_score_alert"] = (
    result[alert_columns].any(axis=1)
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("주성분 수:", scores.shape[1])
print(
    "주성분 점수 경보 행:",
    int(result["any_pc_score_alert"].sum()),
)
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
