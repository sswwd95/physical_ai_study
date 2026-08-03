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

def test_tree_models_created():
    run_script("example_091_train_tree_models.py")
    assert (MODELS / "decision_tree_model.joblib").exists()
    assert (MODELS / "random_forest_model.joblib").exists()

def test_model_comparison_created():
    run_script("example_091_train_tree_models.py")
    run_script("example_092_compare_models.py")
    result = pd.read_csv(OUTPUTS / "model_comparison.csv")
    assert set(result["model"]) == {
        "LogisticRegression",
        "DecisionTree",
        "RandomForest",
    }

def test_calibration_created():
    run_script("example_091_train_tree_models.py")
    run_script("example_093_probability_calibration.py")
    result = pd.read_csv(
        OUTPUTS / "probability_calibration_comparison.csv"
    )
    assert len(result) == 2
    assert (MODELS / "calibrated_random_forest.joblib").exists()

def test_dashboard_created():
    run_script("example_091_train_tree_models.py")
    run_script("example_092_compare_models.py")
    run_script("example_093_probability_calibration.py")
    run_script("example_094_permutation_importance.py")
    run_script("example_095_ensemble_dashboard.py")
    assert (OUTPUTS / "ensemble_model_dashboard.html").exists()
