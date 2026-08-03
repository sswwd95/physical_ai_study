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

def test_xbar_chart_created():
    run_script("example_052_xbar_control_chart.py")
    csv_path = OUTPUTS / "xbar_control_chart.csv"
    png_path = OUTPUTS / "xbar_control_chart.png"
    assert csv_path.exists()
    assert png_path.exists()
    result = pd.read_csv(csv_path)
    assert "out_of_control" in result.columns

def test_individuals_chart_detects_events():
    run_script("example_053_individuals_chart.py")
    result = pd.read_csv(OUTPUTS / "individuals_control_chart.csv")
    assert int(result["out_of_control"].sum()) > 0

def test_moving_range_chart_created():
    run_script("example_054_moving_range_chart.py")
    result = pd.read_csv(OUTPUTS / "moving_range_chart.csv")
    assert "moving_range" in result.columns
    assert "mr_out_of_control" in result.columns

def test_western_electric_alerts_created():
    run_script("example_055_western_electric_rules.py")
    result = pd.read_csv(OUTPUTS / "western_electric_alerts.csv")
    assert len(result) > 0
