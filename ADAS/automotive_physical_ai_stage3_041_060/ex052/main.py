from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log
from common.preprocessing import iqr_bounds

# 전방 거리의 사분위 범위를 계산한다.
df = load_sensor_log()
low, high = iqr_bounds(df["front_distance_m"].dropna())
# IQR 경계 밖의 값을 추출한다.
mask = ~df["front_distance_m"].between(low, high) & df["front_distance_m"].notna()
print("bounds:", round(low, 2), round(high, 2))
print(df.loc[mask, ["timestamp", "front_distance_m"]])
