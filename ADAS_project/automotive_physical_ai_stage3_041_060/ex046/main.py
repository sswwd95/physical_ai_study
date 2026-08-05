from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 데이터를 시간순으로 정렬한다.
df = load_sensor_log().sort_values("timestamp").reset_index(drop=True)
# 속도와 거리 센서의 짧은 결측 구간을 선형 보간한다.
for column in ["vehicle_speed_kmh", "front_distance_m"]:
    df[column + "_interp"] = df[column].interpolate(method="linear", limit=5)
print(df[["vehicle_speed_kmh", "vehicle_speed_kmh_interp"]].iloc[20:32])
