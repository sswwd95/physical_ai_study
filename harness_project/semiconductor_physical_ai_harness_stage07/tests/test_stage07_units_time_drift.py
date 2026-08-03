from pathlib import Path
import subprocess
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = PROJECT_ROOT / "examples"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

def run_script(filename):
    subprocess.run(
        [sys.executable, str(EXAMPLES_DIR / filename)],
        cwd=PROJECT_ROOT,
        check=True,
    )

def test_unit_validation_passes():
    run_script("example_031_validate_sensor_units.py")
    output = OUTPUT_DIR / "sensor_unit_validation.csv"
    result = pd.read_csv(output)
    assert result["validation_passed"].all()

def test_unit_conversion_creates_canonical_columns():
    run_script("example_032_convert_sensor_units.py")
    output = OUTPUT_DIR / "equipment_sensor_log_converted.csv"
    result = pd.read_csv(output)
    required = {
        "temperature_c",
        "pressure_kpa",
        "gas_flow_sccm",
        "vibration_rms",
        "motor_current_a",
    }
    assert required.issubset(result.columns)

def test_time_anomalies_are_detected():
    run_script("example_033_detect_time_interval_anomalies.py")
    output = OUTPUT_DIR / "time_interval_anomalies.csv"
    result = pd.read_csv(output)
    assert len(result) > 0
    assert result["duplicate_timestamp"].any()
    assert result["gap_detected"].any()

def test_duplicate_resolution_removes_duplicates():
    run_script("example_034_resolve_duplicate_timestamps.py")
    output = OUTPUT_DIR / "sensor_log_deduplicated.csv"
    result = pd.read_csv(output, parse_dates=["timestamp"])
    assert result["timestamp"].duplicated().sum() == 0

def test_drift_summary_contains_flags():
    run_script("example_035_detect_sensor_drift.py")
    output = OUTPUT_DIR / "sensor_drift_summary.csv"
    result = pd.read_csv(output)
    assert "drift_detected" in result.columns
    assert len(result) == 5
