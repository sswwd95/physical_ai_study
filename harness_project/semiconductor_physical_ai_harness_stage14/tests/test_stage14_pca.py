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

def test_pca_model_created():
    run_script("example_066_train_pca_baseline.py")
    assert (MODELS / "pca_monitoring_bundle.joblib").exists()
    assert (OUTPUTS / "pca_baseline_metadata.json").exists()

def test_pca_score_monitoring():
    run_script("example_066_train_pca_baseline.py")
    run_script("example_067_pca_score_monitoring.py")
    result = pd.read_csv(
        OUTPUTS / "pca_score_monitoring.csv"
    )
    assert "any_pc_score_alert" in result.columns
    assert int(result["any_pc_score_alert"].sum()) > 0

def test_spe_monitoring():
    run_script("example_066_train_pca_baseline.py")
    run_script("example_068_spe_q_statistic.py")
    result = pd.read_csv(
        OUTPUTS / "spe_q_monitoring.csv"
    )
    assert "spe_q_alert" in result.columns
    assert int(result["spe_q_alert"].sum()) > 0

def test_pca_dashboard_created():
    run_script("example_066_train_pca_baseline.py")
    run_script("example_067_pca_score_monitoring.py")
    run_script("example_068_spe_q_statistic.py")
    run_script("example_069_pca_sensor_contributions.py")
    run_script("example_070_pca_monitoring_dashboard.py")
    assert (
        OUTPUTS / "pca_monitoring_dashboard.html"
    ).exists()
