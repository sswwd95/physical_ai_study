from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "imu_encoder_log.csv"
OUTPUTS = ROOT / "outputs"

def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)

def output_path(name: str) -> Path:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def rmse(a, b) -> float:
    a = np.asarray(a)
    b = np.asarray(b)
    return float(np.sqrt(np.mean((a - b) ** 2)))

def moving_average(values, window: int):
    return pd.Series(values).rolling(window, min_periods=1, center=True).mean().to_numpy()
