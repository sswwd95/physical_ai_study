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
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "spe_q_monitoring.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])
bundle = joblib.load(MODEL_PATH)

sensor_columns = bundle["sensor_columns"]
scaler = bundle["scaler"]
pca = bundle["pca"]
baseline_rows = bundle["baseline_rows"]

# 1. 데이터를 PCA 공간으로 변환한다.
scaled = scaler.transform(df[sensor_columns])
scores = pca.transform(scaled)

# 2. PCA 공간에서 다시 원래 표준화 공간으로 복원한다.
reconstructed = pca.inverse_transform(scores)

# 3. 복원되지 못한 잔차 제곱합을 SPE/Q 통계량으로 계산한다.
residual = scaled - reconstructed
spe_q = np.sum(residual ** 2, axis=1)

# 4. 기준 구간 SPE의 99% 분위수를 경보 임계값으로 사용한다.
threshold = float(
    np.quantile(
        spe_q[:baseline_rows],
        0.99,
    )
)

result = df.copy()
result["spe_q"] = spe_q
result["spe_q_threshold"] = threshold
result["spe_q_alert"] = (
    result["spe_q"]
    > result["spe_q_threshold"]
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("SPE/Q 임계값:", round(threshold, 6))
print("SPE/Q 경보 행:", int(result["spe_q_alert"].sum()))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
