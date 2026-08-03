from pathlib import Path
import subprocess
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = PROJECT_ROOT / "examples"
OUTPUTS = PROJECT_ROOT / "outputs"

def run_script(filename):
    subprocess.run(
        [sys.executable, str(EXAMPLES / filename)],
        cwd=PROJECT_ROOT,
        check=True,
    )

def test_noise_summary_created():
    run_script("example_036_noise_level_analysis.py")
    output = OUTPUTS / "sensor_noise_summary.csv"
    result = pd.read_csv(output)
    assert len(result) == 5
    assert "snr_db" in result.columns

def test_moving_average_output_created():
    run_script("example_037_moving_average_filter.py")
    output = OUTPUTS / "sensor_moving_average.csv"
    result = pd.read_csv(output)
    ma_columns = [
        column for column in result.columns
        if column.endswith("_ma11")
    ]
    assert len(ma_columns) == 5

def test_savgol_output_created():
    run_script("example_039_savgol_filter.py")
    output = OUTPUTS / "sensor_savgol_filtered.csv"
    result = pd.read_csv(output)
    savgol_columns = [
        column for column in result.columns
        if column.endswith("_savgol")
    ]
    assert len(savgol_columns) == 5

def test_filter_comparison_has_three_methods():
    run_script("example_040_compare_filter_performance.py")
    output = OUTPUTS / "filter_performance_comparison.csv"
    result = pd.read_csv(output)
    assert set(result["method"]) == {
        "moving_average",
        "exponential_smoothing",
        "savgol_filter",
    }
