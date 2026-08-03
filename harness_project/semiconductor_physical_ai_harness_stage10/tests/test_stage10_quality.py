from pathlib import Path
import subprocess
import sys
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = PROJECT_ROOT / "examples"
OUTPUTS = PROJECT_ROOT / "outputs"
MODELS = PROJECT_ROOT / "models"

def run_script(filename):
    subprocess.run(
        [sys.executable, str(EXAMPLES / filename)],
        cwd=PROJECT_ROOT,
        check=True,
    )

def test_time_split_files():
    run_script("example_046_time_based_split.py")
    train = pd.read_csv(OUTPUTS / "train.csv", parse_dates=["timestamp"])
    validation = pd.read_csv(OUTPUTS / "validation.csv", parse_dates=["timestamp"])
    test = pd.read_csv(OUTPUTS / "test.csv", parse_dates=["timestamp"])
    assert train["timestamp"].max() < validation["timestamp"].min()
    assert validation["timestamp"].max() < test["timestamp"].min()

def test_leakage_report_passes():
    run_script("example_046_time_based_split.py")
    run_script("example_047_data_leakage_check.py")
    report = pd.read_csv(OUTPUTS / "data_leakage_report.csv")
    assert report["passed"].all()

def test_preprocessor_saved():
    run_script("example_046_time_based_split.py")
    run_script("example_048_save_and_restore_preprocessor.py")
    assert (MODELS / "sensor_preprocessor.joblib").exists()
    assert (OUTPUTS / "test_transformed.csv").exists()

def test_quality_report_created():
    run_script("example_050_data_quality_report.py")
    assert (OUTPUTS / "data_quality_metrics.csv").exists()
    assert (OUTPUTS / "data_quality_report.html").exists()
