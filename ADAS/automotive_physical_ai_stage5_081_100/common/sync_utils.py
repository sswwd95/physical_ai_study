
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"

def load_stream(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA / name)

def out(name: str) -> Path:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def nearest_merge(left, right, tolerance=0.06):
    return pd.merge_asof(
        left.sort_values("timestamp_s"),
        right.sort_values("timestamp_s"),
        on="timestamp_s",
        direction="nearest",
        tolerance=tolerance
    )
