from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 시간순 로그를 준비한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)
# 카메라 거리 센서가 2프레임 늦게 도착했다고 가정한다.
df["distance_delayed"] = df["front_distance_m"].shift(2)
# 지연 보정을 위해 2프레임 앞으로 이동한다.
df["distance_aligned"] = df["distance_delayed"].shift(-2)
print(df[["front_distance_m", "distance_delayed", "distance_aligned"]].head(8))
