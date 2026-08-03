"""
반도체 Physical AI 하네스 엔지니어링 실습 011~015
Windows 10 / Anaconda / Pandas / PyMC 연계 준비
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"
OUTPUT_PATH = PROJECT_ROOT / "outputs" / "sensor_descriptive_statistics.csv"

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

# 1. 통계 요약을 만들 센서 열을 선택한다.
sensor_columns = [
    "temperature_c",
    "pressure_kpa",
    "gas_flow_sccm",
    "vibration_rms",
    "motor_current_a",
]

# 2. 개수, 평균, 표준편차, 사분위수, 최솟값, 최댓값을 계산한다.
summary = df[sensor_columns].describe().T

# 3. 공정 변동을 비교하기 위해 변동계수(CV)를 추가한다.
summary["cv_percent"] = (
    summary["std"] / summary["mean"] * 100.0
)

# 4. 중앙값과 결측 개수를 추가한다.
summary["median"] = df[sensor_columns].median()
summary["missing_count"] = df[sensor_columns].isna().sum()

# 5. 보기 쉬운 열 순서로 재배치한다.
summary = summary[
    [
        "count",
        "mean",
        "median",
        "std",
        "cv_percent",
        "min",
        "25%",
        "50%",
        "75%",
        "max",
        "missing_count",
    ]
]

# 6. 결과를 CSV로 저장하고 출력한다.
summary.to_csv(OUTPUT_PATH, encoding="utf-8-sig")

print("[센서 기술통계]")
print(summary.round(4))
print(f"\n[완료] 저장 위치: {OUTPUT_PATH}")
