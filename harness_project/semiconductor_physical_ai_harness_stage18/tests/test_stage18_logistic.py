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

def test_model_training():
    run_script("example_086_train_logistic_regression.py")
    assert (MODELS / "logistic_defect_model.joblib").exists()
    assert (OUTPUTS / "test_modeling_data.csv").exists()

def test_model_evaluation():
    run_script("example_086_train_logistic_regression.py")
    run_script("example_087_evaluate_classifier.py")
    metrics = json.loads(
        (OUTPUTS / "logistic_evaluation_metrics.json")
        .read_text(encoding="utf-8")
    )
    assert 0.0 <= metrics["roc_auc"] <= 1.0
    assert 0.0 <= metrics["average_precision"] <= 1.0

def test_threshold_selection():
    run_script("example_086_train_logistic_regression.py")
    run_script("example_087_evaluate_classifier.py")
    run_script("example_088_optimize_threshold.py")
    result = pd.read_csv(
        OUTPUTS / "threshold_performance.csv"
    )
    assert result["selected"].sum() == 1

def test_dashboard_created():
    run_script("example_086_train_logistic_regression.py")
    run_script("example_087_evaluate_classifier.py")
    run_script("example_088_optimize_threshold.py")
    run_script("example_089_logistic_feature_effects.py")
    run_script("example_090_defect_prediction_dashboard.py")
    assert (
        OUTPUTS / "defect_prediction_dashboard.html"
    ).exists()
