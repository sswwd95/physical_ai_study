from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 원본 데이터를 읽는다.
df = load_sensor_log()
# 결측값이 하나라도 있는 행을 삭제한다.
row_dropped = df.dropna()
# 결측률이 5%를 넘는 열만 제거한다.
keep_columns = df.columns[df.isna().mean() <= 0.05]
column_filtered = df[keep_columns]
print("original:", df.shape)
print("drop rows:", row_dropped.shape)
print("filter columns:", column_filtered.shape)
