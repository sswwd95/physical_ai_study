from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 시간순으로 정렬한다.
df = load_sensor_log().sort_values("timestamp").reset_index(drop=True)
# 배터리 전압은 직전 값으로 채운다.
df["battery_v_ffill"] = df["battery_v"].ffill()
# 기어처럼 상태형 값은 앞뒤 채움을 함께 사용할 수 있다.
df["gear_filled"] = df["gear"].ffill().bfill()
print(df[["timestamp", "battery_v", "battery_v_ffill", "gear_filled"]].head(12))
