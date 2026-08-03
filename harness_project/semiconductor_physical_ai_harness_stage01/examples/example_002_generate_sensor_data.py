"""
반도체 Physical AI 하네스 엔지니어링 실습
Windows 10 / Anaconda / PyMC
"""

from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 1. 매번 같은 데이터를 만들 수 있도록 난수 시드를 고정한다.
rng = np.random.default_rng(42)

# 2. 1초 간격으로 600개의 시각을 생성한다.
timestamps = pd.date_range(
    start="2026-08-03 09:00:00",
    periods=600,
    freq="s",
)

# 3. 정상 공정에 가까운 센서 데이터를 생성한다.
temperature_c = rng.normal(65.0, 0.8, size=600)
pressure_kpa = rng.normal(101.3, 0.5, size=600)
gas_flow_sccm = rng.normal(500.0, 4.0, size=600)
vibration_rms = rng.normal(1.8, 0.15, size=600)
motor_current_a = rng.normal(8.0, 0.25, size=600)

# 4. 실제 이상 상황을 흉내 내기 위해 일부 구간에 변화를 넣는다.
temperature_c[420:470] += np.linspace(0, 6, 50)
pressure_kpa[300:315] += 3.5
vibration_rms[500:530] += 1.2
motor_current_a[500:530] += 1.0

# 5. 분석하기 쉬운 표 형태로 묶는다.
df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_c": temperature_c,
    "pressure_kpa": pressure_kpa,
    "gas_flow_sccm": gas_flow_sccm,
    "vibration_rms": vibration_rms,
    "motor_current_a": motor_current_a,
})

# 6. 원본 센서 로그를 CSV 파일로 저장한다.
output_path = DATA_DIR / "equipment_sensor_log.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(df.head())
print(f"[완료] {len(df)}행 저장: {output_path}")
