from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "semiconductor_yield_regression.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/semiconductor_yield_regression.csv 파일이 없습니다."
    )

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

sensor_df = pd.read_csv(DATA_FILE)

x = sensor_df.drop(columns=["timestamp", "lot_id", "yield_percent"])
y = sensor_df["yield_percent"]

numeric_features = [
    "temp_mean_c",
    "temp_std_c",
    "pressure_mean_pa",
    "pressure_std_pa",
    "rf_power_mean_w",
    "gas_flow_mean_sccm",
    "vibration_rms_g",
    "particle_mean",
    "downtime_min",
    "maintenance_age_hours",
]
categorical_features = ["recipe", "chamber_id"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)

preprocessor = ColumnTransformer([
    ("num", "passthrough", numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

pipeline = Pipeline([
    ("preprocess", preprocessor),
    (
        "regressor",
        RandomForestRegressor(
            random_state=42,
            n_jobs=-1,
        ),
    ),
])

param_grid = {
    "regressor__n_estimators": [200, 400],
    "regressor__max_depth": [6, 10, None],
    "regressor__min_samples_leaf": [2, 5],
}

search = GridSearchCV(
    pipeline,
    param_grid=param_grid,
    scoring="neg_mean_absolute_error",
    cv=3,
    n_jobs=-1,
)
search.fit(x_train, y_train)

print("최적 파라미터:", search.best_params_)
print("최적 CV MAE:", round(-search.best_score_, 4))
