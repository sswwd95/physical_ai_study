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

def test_ewma_chart_created():
    run_script("example_056_ewma_control_chart.py")
    result = pd.read_csv(OUTPUTS / "ewma_control_chart.csv")
    assert "ewma_alert" in result.columns
    assert int(result["ewma_alert"].sum()) > 0

def test_cusum_chart_created():
    run_script("example_057_cusum_control_chart.py")
    result = pd.read_csv(OUTPUTS / "cusum_control_chart.csv")
    assert "cusum_alert" in result.columns
    assert int(result["cusum_alert"].sum()) > 0

def test_small_shift_summary():
    run_script("example_056_ewma_control_chart.py")
    run_script("example_057_cusum_control_chart.py")
    run_script("example_058_small_shift_detection.py")
    result = pd.read_csv(OUTPUTS / "small_shift_detection_summary.csv")
    assert set(result["method"]) == {"EWMA", "CUSUM"}

def test_integrated_alerts():
    run_script("example_056_ewma_control_chart.py")
    run_script("example_057_cusum_control_chart.py")
    run_script("example_060_integrated_process_alerts.py")
    result = pd.read_csv(OUTPUTS / "integrated_process_alerts.csv")
    assert "integrated_alert_level" in result.columns
    assert set(result["integrated_alert_level"]).issubset(
        {"NORMAL", "WATCH", "WARNING", "CRITICAL"}
    )
