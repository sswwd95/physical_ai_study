from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 자동차 센서의 물리적으로 가능한 범위를 정의한다.
df = load_sensor_log()
ranges = {
    "vehicle_speed_kmh": (0, 130),
    "steering_deg": (-35, 35),
    "front_distance_m": (0.5, 120),
    "battery_v": (10.5, 14.8),
}
# 범위를 벗어난 행 수를 센서별로 계산한다.
for column, (low, high) in ranges.items():
    mask = ~df[column].between(low, high) & df[column].notna()
    print(column, "outliers:", int(mask.sum()))
