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

def test_generated_labels_created():
    run_script("example_081_generate_defect_labels.py")
    result = pd.read_csv(
        OUTPUTS / "wafer_with_generated_labels.csv"
    )
    assert "generated_defect_flag" in result.columns
    assert set(result["generated_defect_flag"]).issubset({0, 1})

def test_feature_bin_rates_created():
    run_script("example_082_feature_bin_defect_rates.py")
    result = pd.read_csv(
        OUTPUTS / "feature_bin_defect_rates.csv"
    )
    assert len(result) >= 15
    assert "defect_rate_percent" in result.columns

def test_chi_square_summary_created():
    run_script("example_083_chi_square_crosstab.py")
    result = pd.read_csv(
        OUTPUTS / "chi_square_crosstab_summary.csv"
    )
    assert set(result["condition"]) == {"recipe_id", "tool_id"}

def test_dashboard_created():
    run_script("example_082_feature_bin_defect_rates.py")
    run_script("example_083_chi_square_crosstab.py")
    run_script("example_084_condition_risk_ratio.py")
    run_script("example_085_defect_analysis_dashboard.py")
    assert (
        OUTPUTS / "defect_analysis_dashboard.html"
    ).exists()
