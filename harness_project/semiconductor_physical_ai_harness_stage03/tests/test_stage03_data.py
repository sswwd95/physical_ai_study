from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "equipment_sensor_log.csv"

def test_sensor_log_has_expected_rows():
    df = pd.read_csv(DATA_PATH)
    assert len(df) == 600

def test_required_columns_exist():
    df = pd.read_csv(DATA_PATH)
    required = {
        "timestamp", "lot_id", "recipe_id",
        "temperature_c", "pressure_kpa",
        "gas_flow_sccm", "vibration_rms",
        "motor_current_a",
    }
    assert required.issubset(df.columns)

def test_timestamp_is_monotonic():
    df = pd.read_csv(DATA_PATH, parse_dates=["timestamp"])
    assert df["timestamp"].is_monotonic_increasing
