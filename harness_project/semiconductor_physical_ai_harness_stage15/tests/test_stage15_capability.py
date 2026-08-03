from pathlib import Path
import json
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

def test_cp_cpk_created():
    run_script("example_071_cp_cpk.py")
    data = json.loads(
        (OUTPUTS / "cp_cpk_summary.json").read_text(
            encoding="utf-8"
        )
    )
    assert data["cp"] > 0
    assert data["cpk"] > 0

def test_pp_ppk_created():
    run_script("example_072_pp_ppk.py")
    data = json.loads(
        (OUTPUTS / "pp_ppk_summary.json").read_text(
            encoding="utf-8"
        )
    )
    assert data["pp"] > 0
    assert data["ppk"] > 0

def test_spec_violations_detected():
    run_script("example_073_spec_violation_rate.py")
    result = pd.read_csv(OUTPUTS / "spec_violation_rows.csv")
    assert len(result) > 0

def test_dashboard_created():
    run_script("example_071_cp_cpk.py")
    run_script("example_072_pp_ppk.py")
    run_script("example_073_spec_violation_rate.py")
    run_script("example_074_lot_capability_comparison.py")
    run_script("example_075_capability_dashboard.py")
    assert (
        OUTPUTS / "process_capability_dashboard.html"
    ).exists()
