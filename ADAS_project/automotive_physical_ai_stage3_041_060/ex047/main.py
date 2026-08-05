from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 타임스탬프를 인덱스로 사용한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp")
df = df.set_index("timestamp")
# 실제 시간 간격을 반영하여 보간한다.
df["distance_time_interp"] = df["front_distance_m"].interpolate(method="time", limit=5)
print(df[["front_distance_m", "distance_time_interp"]].iloc[85:100])
