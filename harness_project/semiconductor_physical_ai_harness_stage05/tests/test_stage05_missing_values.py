from pathlib import Path
import subprocess
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = PROJECT_ROOT / "examples"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
MISSING_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_missing.csv"
)

def run_script(filename):
    subprocess.run(
        [sys.executable, str(EXAMPLES_DIR / filename)],
        cwd=PROJECT_ROOT,
        check=True,
    )

def test_sample_data_contains_missing_values():
    df = pd.read_csv(MISSING_PATH)
    sensor_columns = [
        "temperature_c",
        "pressure_kpa",
        "gas_flow_sccm",
        "vibration_rms",
        "motor_current_a",
    ]
    assert int(df[sensor_columns].isna().sum().sum()) > 0

def test_missing_summary_is_created():
    run_script("example_021_detect_missing_values.py")
    output = OUTPUT_DIR / "missing_value_summary.csv"
    assert output.exists()
    summary = pd.read_csv(output)
    assert "missing_count" in summary.columns
    assert summary["missing_count"].sum() > 0

def test_linear_interpolation_removes_missing_values():
    run_script("example_024_linear_interpolation.py")
    output = OUTPUT_DIR / "sensor_log_linear_interpolation.csv"
    df = pd.read_csv(output)
    sensor_columns = [
        "temperature_c",
        "pressure_kpa",
        "gas_flow_sccm",
        "vibration_rms",
        "motor_current_a",
    ]
    assert int(df[sensor_columns].isna().sum().sum()) == 0

def test_quality_comparison_contains_three_methods():
    run_script("example_025_compare_imputation_quality.py")
    output = OUTPUT_DIR / "imputation_quality_comparison.csv"
    result = pd.read_csv(output)
    assert set(result["method"]) == {
        "ffill_bfill",
        "linear_interpolation",
        "median_fill",
    }
