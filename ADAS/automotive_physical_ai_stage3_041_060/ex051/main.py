from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 속도 결측값을 제외하고 평균과 표준편차를 계산한다.
df = load_sensor_log()
series = df["vehicle_speed_kmh"]
zscore = (series - series.mean()) / series.std(ddof=0)
# 절댓값 3 이상을 이상값으로 본다.
outliers = df[zscore.abs() >= 3]
print(outliers[["timestamp", "vehicle_speed_kmh"]])
