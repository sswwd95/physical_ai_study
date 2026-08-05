from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "vehicle_sensor_log.csv"
OUTPUT_DIR = ROOT / "outputs"

def load_vehicle_data() -> pd.DataFrame:
    """공통 자동차 센서 로그를 읽고 시간 열을 변환한다."""
    df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
    return df

def output_path(filename: str) -> Path:
    """결과 파일 경로를 만들고 outputs 폴더를 보장한다."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR / filename
