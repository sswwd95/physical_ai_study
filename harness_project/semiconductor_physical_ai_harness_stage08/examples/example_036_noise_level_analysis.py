"""
반도체 Physical AI 하네스 엔지니어링 실습 036~040
Windows 10 / Anaconda / Pandas / SciPy
센서 노이즈 분석과 필터링
"""

from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEAN_PATH = PROJECT_ROOT / "data" / "sensor_signal_clean.csv"
NOISY_PATH = PROJECT_ROOT / "data" / "sensor_signal_noisy.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_noise_summary.csv"

clean_df = pd.read_csv(CLEAN_PATH, parse_dates=["timestamp"])
noisy_df = pd.read_csv(NOISY_PATH, parse_dates=["timestamp"])

sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

rows = []

# 1. 깨끗한 신호와 노이즈 신호의 차이를 노이즈로 정의한다.
for sensor in sensor_columns:
    noise = (
        noisy_df[sensor] - clean_df[sensor]
    ).to_numpy()

    signal = clean_df[sensor].to_numpy()

    # 2. 노이즈 평균, 표준편차, RMS를 계산한다.
    noise_mean = float(np.mean(noise))
    noise_std = float(np.std(noise, ddof=1))
    noise_rms = float(np.sqrt(np.mean(noise ** 2)))

    # 3. 신호 대 잡음비를 dB 단위로 계산한다.
    signal_power = float(np.mean(signal ** 2))
    noise_power = float(np.mean(noise ** 2))

    snr_db = float(
        10.0 * np.log10(signal_power / noise_power)
    )

    rows.append(
        {
            "sensor": sensor,
            "noise_mean": noise_mean,
            "noise_std": noise_std,
            "noise_rms": noise_rms,
            "snr_db": snr_db,
        }
    )

result = pd.DataFrame(rows)
result = result.sort_values(
    "snr_db",
    ascending=True,
).reset_index(drop=True)

result.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig",
)

print("[센서 노이즈 요약]")
print(result.round(5))
print()
print("SNR이 낮을수록 상대적으로 노이즈 영향이 큽니다.")
print(f"[완료] 저장 위치: {OUTPUT_PATH}")
