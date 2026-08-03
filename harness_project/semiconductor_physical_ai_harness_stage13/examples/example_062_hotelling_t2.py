"""
반도체 Physical AI 하네스 엔지니어링 실습 061~065
Windows 10 / Anaconda / Pandas / NumPy / Matplotlib
다변량 공정 모니터링
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import chi2

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "multisensor_process_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "hotelling_t2_monitoring.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 1. 초기 300개 샘플로 평균 벡터와 공분산 행렬을 계산한다.
baseline = df[sensor_columns].iloc[:300]

mean_vector = baseline.mean().to_numpy()
covariance = baseline.cov().to_numpy()

# 2. 수치 안정성을 위해 작은 ridge 값을 추가한다.
ridge = 1e-6
covariance_regularized = (
    covariance
    + ridge * np.eye(len(sensor_columns))
)

inverse_covariance = np.linalg.inv(
    covariance_regularized
)

# 3. 각 행에 대해 Hotelling T²를 계산한다.
values = df[sensor_columns].to_numpy()
centered = values - mean_vector

t2_values = np.einsum(
    "ij,jk,ik->i",
    centered,
    inverse_covariance,
    centered,
)

# 4. 교육용으로 카이제곱 99% 임계값을 사용한다.
alpha = 0.99
threshold = float(
    chi2.ppf(
        alpha,
        df=len(sensor_columns),
    )
)

result = df.copy()
result["hotelling_t2"] = t2_values
result["t2_threshold"] = threshold
result["t2_alert"] = (
    result["hotelling_t2"]
    > result["t2_threshold"]
)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("T² 임계값:", round(threshold, 4))
print("T² 경보 행 수:", int(result["t2_alert"].sum()))
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
