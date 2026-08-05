from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log
from common.preprocessing import hampel_filter

# 시간순 속도 로그를 준비한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)
# Hampel 필터로 국부 스파이크를 중앙값으로 대체한다.
df["speed_hampel"] = hampel_filter(df["vehicle_speed_kmh"], window=9, n_sigma=3.0)
changed = df[df["vehicle_speed_kmh"] != df["speed_hampel"]]
print(changed[["timestamp", "vehicle_speed_kmh", "speed_hampel"]].dropna())
