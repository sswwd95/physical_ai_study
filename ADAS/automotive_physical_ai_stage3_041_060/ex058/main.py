from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log

# 시간순 속도 로그를 준비한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)
# 0.1초 간격에서 속도 차이를 가속도로 환산한다.
df["accel_est_mps2"] = df["vehicle_speed_kmh"].diff().div(3.6).div(0.1)
# 승용차 데이터에서 절댓값 8m/s² 초과를 급격한 변화로 표시한다.
mask = df["accel_est_mps2"].abs() > 8
print(df.loc[mask, ["timestamp", "vehicle_speed_kmh", "accel_est_mps2"]])
