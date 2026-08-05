from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 중복 시각을 제거하고 타임스탬프를 인덱스로 설정한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").set_index("timestamp")
# 200ms 간격으로 평균 리샘플링한다.
numeric = df.select_dtypes(include="number")
resampled = numeric.resample("200ms").mean().interpolate("time")
print(resampled.head(10))
