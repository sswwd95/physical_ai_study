from pathlib import Path
import json
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

def test_class_balance_summary():
    run_script("example_096_class_imbalance_diagnostics.py")
    data = json.loads(
        (OUTPUTS / "class_balance_summary.json")
        .read_text(encoding="utf-8")
    )
    assert data["defect_count"] > 0
    assert data["normal_count"] > data["defect_count"]

def test_sampling_outputs():
    run_script("example_097_under_over_sampling.py")
    under = pd.read_csv(
        OUTPUTS / "random_undersampled_training.csv"
    )
    over = pd.read_csv(
        OUTPUTS / "random_oversampled_training.csv"
    )
    assert under["defect_flag"].value_counts().nunique() == 1
    assert over["defect_flag"].value_counts().nunique() == 1

def test_cost_sensitive_model_selected():
    run_script("example_099_cost_sensitive_comparison.py")
    result = pd.read_csv(
        OUTPUTS / "cost_sensitive_model_comparison.csv"
    )
    assert result["selected"].sum() == 1
    assert (
        MODELS / "selected_cost_sensitive_model.joblib"
    ).exists()

def test_integrated_project_created():
    run_script("example_096_class_imbalance_diagnostics.py")
    run_script("example_099_cost_sensitive_comparison.py")
    run_script("example_100_integrated_mini_project.py")
    assert (
        OUTPUTS / "integrated_mini_project_dashboard.html"
    ).exists()
    assert (
        OUTPUTS / "integrated_mini_project_predictions.csv"
    ).exists()
