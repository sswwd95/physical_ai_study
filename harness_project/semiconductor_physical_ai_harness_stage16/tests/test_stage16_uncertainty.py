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

def test_normality_summary_created():
    run_script("example_076_normality_tests.py")
    result = pd.read_csv(OUTPUTS / "normality_test_summary.csv")
    assert len(result) == 2
    assert "normality_rejected_at_0_05" in result.columns

def test_nonnormal_capability_created():
    run_script("example_077_nonnormal_capability.py")
    result = pd.read_csv(OUTPUTS / "nonnormal_capability_summary.csv")
    assert "ppk_percentile_method" in result.columns

def test_bootstrap_intervals_created():
    run_script("example_078_bootstrap_cpk_interval.py")
    result = pd.read_csv(OUTPUTS / "bootstrap_cpk_intervals.csv")
    assert (result["cpk_ci_97_5_percent"] > result["cpk_ci_2_5_percent"]).all()

def test_decision_report_created():
    run_script("example_076_normality_tests.py")
    run_script("example_077_nonnormal_capability.py")
    run_script("example_078_bootstrap_cpk_interval.py")
    run_script("example_079_capability_uncertainty_comparison.py")
    run_script("example_080_capability_decision_report.py")
    assert (OUTPUTS / "capability_decision_report.html").exists()
