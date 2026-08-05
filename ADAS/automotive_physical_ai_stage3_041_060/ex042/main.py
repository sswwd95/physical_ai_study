from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 원본 로그를 읽는다.
df = load_sensor_log()
# 타임스탬프 기준으로 정렬한다.
df = df.sort_values("timestamp")
# 같은 시각의 중복 행은 마지막 행만 남긴다.
df = df.drop_duplicates(subset="timestamp", keep="last")
# 인덱스를 0부터 다시 부여한다.
df = df.reset_index(drop=True)
print(df.head())
print("monotonic:", df["timestamp"].is_monotonic_increasing)
