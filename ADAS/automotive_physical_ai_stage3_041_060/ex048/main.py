from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 데이터를 읽는다.
df = load_sensor_log()
# 조향각 결측값을 평균과 중앙값으로 각각 대체한다.
mean_value = df["steering_deg"].mean()
median_value = df["steering_deg"].median()
df["steering_mean_fill"] = df["steering_deg"].fillna(mean_value)
df["steering_median_fill"] = df["steering_deg"].fillna(median_value)
print("mean:", round(mean_value, 3), "median:", round(median_value, 3))
