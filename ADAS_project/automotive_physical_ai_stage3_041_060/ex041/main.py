from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 공통 자동차 센서 로그를 읽는다.
df = load_sensor_log()
# 행과 열의 개수를 확인한다.
print("shape:", df.shape)
# 열별 자료형과 결측 개수를 출력한다.
print(df.dtypes)
print("missing values:", df.isna().sum(), sep="\n")
# 중복 타임스탬프 개수를 확인한다.
print("duplicated timestamps:", df["timestamp"].duplicated().sum())
