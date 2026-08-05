from __future__ import annotations
import pandas as pd
from .paths import DATA_DIR


def load_vehicle_log() -> pd.DataFrame:
    """공통 자동차 센서 CSV를 DataFrame으로 읽어 반환한다."""
    path = DATA_DIR / "vehicle_sensor_log.csv"
    if not path.exists():
        raise FileNotFoundError(f"센서 로그를 찾을 수 없습니다: {path}")
    return pd.read_csv(path)
