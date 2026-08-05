from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 속도 센서의 비정상 범위를 제한한다.
df = load_sensor_log()
df["speed_clipped"] = df["vehicle_speed_kmh"].clip(lower=0, upper=130)
# 변경된 행만 확인한다.
changed = df[df["vehicle_speed_kmh"] != df["speed_clipped"]]
print(changed[["timestamp", "vehicle_speed_kmh", "speed_clipped"]])
