from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log
from common.path_utils import OUTPUT_DIR
from common.preprocessing import hampel_filter

# 1. 원본 로그를 읽고 시간순 정렬 및 중복 제거를 수행한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)
# 2. 연속 센서의 짧은 결측 구간을 보간한다.
continuous = ["vehicle_speed_kmh", "steering_deg", "yaw_rate_dps", "front_distance_m", "imu_ax_mps2", "imu_ay_mps2", "battery_v"]
df[continuous] = df[continuous].interpolate(method="linear", limit=5).ffill().bfill()
# 3. 물리 범위를 벗어난 값을 제한한다.
df["vehicle_speed_kmh"] = df["vehicle_speed_kmh"].clip(0, 130)
df["steering_deg"] = df["steering_deg"].clip(-35, 35)
df["front_distance_m"] = df["front_distance_m"].clip(0.5, 120)
# 4. 속도와 거리의 국부 스파이크를 Hampel 필터로 완화한다.
df["vehicle_speed_kmh"] = hampel_filter(df["vehicle_speed_kmh"], window=9)
df["front_distance_m"] = hampel_filter(df["front_distance_m"], window=9)
# 5. 정제된 CSV와 품질 요약을 저장한다.
out_path = OUTPUT_DIR / "ex060_clean_sensor_log.csv"
df.to_csv(out_path, index=False)
print("saved:", out_path)
print("remaining missing:", int(df.isna().sum().sum()))
print("rows:", len(df))
