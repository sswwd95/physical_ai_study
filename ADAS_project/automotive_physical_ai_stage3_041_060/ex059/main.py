from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import matplotlib.pyplot as plt
from common.data_loader import load_sensor_log
from common.path_utils import OUTPUT_DIR
from common.preprocessing import hampel_filter

# 속도 데이터를 정렬하고 보간한다.
df = load_sensor_log().sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)
df["speed_clean"] = df["vehicle_speed_kmh"].interpolate(limit=5)
df["speed_clean"] = hampel_filter(df["speed_clean"], window=9)
# 원본과 정제 결과를 한 그래프에 표시한다.
plt.figure(figsize=(10, 4))
plt.plot(df["timestamp"], df["vehicle_speed_kmh"], label="raw", alpha=0.6)
plt.plot(df["timestamp"], df["speed_clean"], label="clean")
plt.xlabel("time")
plt.ylabel("speed (km/h)")
plt.legend()
plt.tight_layout()
path = OUTPUT_DIR / "ex059_speed_before_after.png"
plt.savefig(path, dpi=150)
print("saved:", path)
