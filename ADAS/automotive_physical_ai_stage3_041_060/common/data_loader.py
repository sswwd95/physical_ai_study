import pandas as pd
from .path_utils import DATA_DIR


def load_sensor_log() -> pd.DataFrame:
    """Load the shared synthetic automotive sensor log."""
    path = DATA_DIR / "automotive_sensor_dirty.csv"
    df = pd.read_csv(path, parse_dates=["timestamp"])
    return df
