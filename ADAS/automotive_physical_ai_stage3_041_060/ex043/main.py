from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 센서 로그를 읽는다.
df = load_sensor_log()
# 각 열의 결측 비율을 백분율로 계산한다.
missing_rate = df.isna().mean().mul(100).sort_values(ascending=False)
# 결측률이 0보다 큰 열만 출력한다.
print(missing_rate[missing_rate > 0].round(2))
# 1% 이상이면 우선 점검 대상으로 표시한다.
priority = missing_rate[missing_rate >= 1.0]
print("priority columns:", priority.index.tolist())
