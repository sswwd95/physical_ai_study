from pathlib import Path
import sys

# 프로젝트 루트를 Python 모듈 검색 경로에 추가한다.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.data_loader import load_sensor_log
from common.preprocessing import robust_zscore

# 중앙값과 MAD를 이용해 조향각의 강건한 점수를 계산한다.
df = load_sensor_log()
score = robust_zscore(df["steering_deg"])
mask = score.abs() > 3.5
print(df.loc[mask, ["timestamp", "steering_deg"]].assign(score=score[mask].round(2)))
