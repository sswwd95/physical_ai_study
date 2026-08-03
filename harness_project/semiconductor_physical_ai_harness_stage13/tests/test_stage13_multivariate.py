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

def test_multisensor_zscore_output():
    run_script("example_061_multisensor_zscore_monitoring.py")
    result = pd.read_csv(
        OUTPUTS / "multisensor_zscore_monitoring.csv"
    )
    assert "sensor_alarm_count" in result.columns
    assert int(result["any_sensor_alarm"].sum()) > 0

def test_hotelling_t2_output():
    run_script("example_062_hotelling_t2.py")
    result = pd.read_csv(
        OUTPUTS / "hotelling_t2_monitoring.csv"
    )
    assert "hotelling_t2" in result.columns
    assert int(result["t2_alert"].sum()) > 0

def test_combined_alerts_output():
    run_script("example_061_multisensor_zscore_monitoring.py")
    run_script("example_062_hotelling_t2.py")
    run_script("example_063_combine_sensor_alerts.py")
    result = pd.read_csv(
        OUTPUTS / "combined_multisensor_alerts.csv"
    )
    assert "combined_alert_level" in result.columns

def test_dashboard_created():
    run_script("example_061_multisensor_zscore_monitoring.py")
    run_script("example_062_hotelling_t2.py")
    run_script("example_063_combine_sensor_alerts.py")
    run_script("example_064_process_health_score.py")
    run_script("example_065_multivariate_dashboard.py")
    assert (
        OUTPUTS / "multivariate_monitoring_dashboard.html"
    ).exists()
