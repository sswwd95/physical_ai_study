"""
반도체 Physical AI 하네스 엔지니어링 실습 066~070
Windows 10 / Anaconda / Pandas / scikit-learn
PCA 기반 다변량 공정 모니터링
"""

from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "pca_process_log.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "pca_monitoring_bundle.joblib"
META_PATH = PROJECT_ROOT / "outputs" / "pca_baseline_metadata.json"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 초기 400개 샘플을 정상 기준 구간으로 사용한다.
baseline = df[sensor_columns].iloc[:400]

# 2. 단위가 다른 센서를 표준화한다.
scaler = StandardScaler()
baseline_scaled = scaler.fit_transform(baseline)

# 3. 누적 설명분산 95%를 만족하는 PCA를 학습한다.
pca = PCA(n_components=0.95, svd_solver="full")
pca.fit(baseline_scaled)

# 4. 운영 재사용을 위해 scaler와 PCA를 함께 저장한다.
bundle = {
    "sensor_columns": sensor_columns,
    "scaler": scaler,
    "pca": pca,
    "baseline_rows": 400,
}

joblib.dump(bundle, MODEL_PATH)

# 5. 설명분산과 주성분 수를 메타데이터로 저장한다.
metadata = {
    "baseline_rows": 400,
    "sensor_columns": sensor_columns,
    "selected_components": int(pca.n_components_),
    "explained_variance_ratio": [
        float(value)
        for value in pca.explained_variance_ratio_
    ],
    "cumulative_explained_variance": float(
        pca.explained_variance_ratio_.sum()
    ),
}

META_PATH.write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(json.dumps(metadata, ensure_ascii=False, indent=2))
print(f"[완료] 모델: {MODEL_PATH}")
print(f"[완료] 메타데이터: {META_PATH}")
