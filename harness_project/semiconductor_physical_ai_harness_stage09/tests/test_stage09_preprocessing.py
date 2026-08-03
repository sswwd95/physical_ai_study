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

def test_standard_scaling_created():
    run_script("example_041_standard_scaling.py")
    result = pd.read_csv(OUTPUTS / "sensor_standard_scaled.csv")
    z_columns = [c for c in result.columns if c.endswith("_z")]
    assert len(z_columns) == 5
    assert abs(result[z_columns].mean()).max() < 1e-10

def test_minmax_range():
    run_script("example_042_minmax_normalization.py")
    result = pd.read_csv(OUTPUTS / "sensor_minmax_scaled.csv")
    cols = [c for c in result.columns if c.endswith("_minmax")]
    assert result[cols].min().min() >= -1e-12
    assert result[cols].max().max() <= 1.0 + 1e-12

def test_feature_engineering_output():
    run_script("example_044_feature_engineering.py")
    result = pd.read_csv(OUTPUTS / "sensor_engineered_features.csv")
    assert "mechanical_load_index" in result.columns
    assert "temperature_delta" in result.columns

def test_integrated_pipeline_has_no_missing():
    run_script("example_045_integrated_preprocessing_pipeline.py")
    result = pd.read_csv(OUTPUTS / "preprocessed_sensor_features.csv")
    feature_cols = [
        c for c in result.columns
        if c not in ["timestamp", "lot_id", "recipe_id"]
    ]
    assert int(result[feature_cols].isna().sum().sum()) == 0
