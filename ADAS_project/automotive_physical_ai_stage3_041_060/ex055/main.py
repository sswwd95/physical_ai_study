from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 거리 센서를 시간순으로 정렬한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)
# 5개 샘플 이동 중앙값을 계산한다.
df["distance_median5"] = df["front_distance_m"].rolling(5, center=True, min_periods=1).median()
print(df[["front_distance_m", "distance_median5"]].head(15))
