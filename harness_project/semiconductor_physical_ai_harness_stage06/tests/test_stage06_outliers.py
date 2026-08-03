from pathlib import Path
import subprocess
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = PROJECT_ROOT / "examples"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTLIER_PATH = (
    PROJECT_ROOT
    / "data"
    / "equipment_sensor_log_with_outliers.csv"
)

def run_script(filename):
    subprocess.run(
        [sys.executable, str(EXAMPLES_DIR / filename)],
        cwd=PROJECT_ROOT,
        check=True,
    )

def test_sample_data_has_expected_rows():
    df = pd.read_csv(OUTLIER_PATH)
    assert len(df) == 600

def test_physical_range_violations_created():
    run_script("example_026_physical_range_check.py")
    output = OUTPUT_DIR / "physical_range_violations.csv"
    assert output.exists()
    result = pd.read_csv(output)
    assert len(result) >= 3

def test_hampel_output_created():
    run_script("example_029_hampel_filter.py")
    output = OUTPUT_DIR / "sensor_log_hampel_filtered.csv"
    assert output.exists()
    result = pd.read_csv(output)
    flag_columns = [
        column
        for column in result.columns
        if column.endswith("_hampel_outlier")
    ]
    assert len(flag_columns) == 5
    assert int(result[flag_columns].sum().sum()) > 0

def test_quality_comparison_has_three_methods():
    run_script("example_030_compare_outlier_correction.py")
    output = OUTPUT_DIR / "outlier_correction_quality.csv"
    result = pd.read_csv(output)
    assert set(result["method"]) == {
        "median_replace",
        "linear_interpolation",
        "hampel_filter",
    }
