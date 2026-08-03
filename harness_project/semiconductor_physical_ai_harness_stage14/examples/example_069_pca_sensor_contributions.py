"""
반도체 Physical AI 하네스 엔지니어링 실습 066~070
Windows 10 / Anaconda / Pandas / scikit-learn
PCA 기반 다변량 공정 모니터링
"""

from pathlib import Path
import joblib
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "pca_process_log.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "pca_monitoring_bundle.joblib"
SPE_PATH = PROJECT_ROOT / "outputs" / "spe_q_monitoring.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "pca_sensor_contributions.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
spe_df = pd.read_csv(SPE_PATH, parse_dates=["timestamp"])
bundle = joblib.load(MODEL_PATH)

sensor_columns = bundle["sensor_columns"]
scaler = bundle["scaler"]
pca = bundle["pca"]

# 1. 표준화 데이터와 PCA 복원값을 계산한다.
scaled = scaler.transform(df[sensor_columns])
scores = pca.transform(scaled)
reconstructed = pca.inverse_transform(scores)

# 2. 센서별 제곱 잔차를 SPE 기여도로 사용한다.
squared_residual = (
    scaled - reconstructed
) ** 2

contribution_df = pd.DataFrame(
    squared_residual,
    columns=[
        f"{sensor}_spe_contribution"
        for sensor in sensor_columns
    ],
)

result = df[
    ["timestamp", "lot_id", "recipe_id"]
].copy()

result["spe_q"] = spe_df["spe_q"]
result["spe_q_alert"] = spe_df["spe_q_alert"]

for column in contribution_df.columns:
    result[column] = contribution_df[column]

# 3. 각 행에서 기여도가 가장 큰 센서를 찾는다.
contribution_columns = list(
    contribution_df.columns
)

result["top_contribution_column"] = (
    result[contribution_columns]
    .idxmax(axis=1)
)

result["top_contribution_sensor"] = (
    result["top_contribution_column"]
    .str.replace(
        "_spe_contribution",
        "",
        regex=False,
    )
)

# 4. SPE 경보 행만 저장한다.
alerts = result.loc[
    result["spe_q_alert"]
].copy()

alerts.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[SPE 경보 기여도 상위 센서]")
print(alerts["top_contribution_sensor"].value_counts())
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
