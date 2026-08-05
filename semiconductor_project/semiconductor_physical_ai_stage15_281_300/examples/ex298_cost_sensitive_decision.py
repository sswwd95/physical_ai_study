from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
HISTORY_FILE = ROOT / "data" / "process_optimization_history.csv"
CANDIDATE_FILE = ROOT / "data" / "optimization_candidates.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

history_df = pd.read_csv(HISTORY_FILE)
candidate_df = pd.read_csv(CANDIDATE_FILE)

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

features=["recipe","chamber_id","pressure_pa","rf_power_w","gas_flow_sccm","temperature_c"]
numeric=features[2:]
categorical=features[:2]

preprocessor=ColumnTransformer([
    ("num","passthrough",numeric),
    ("cat",OneHotEncoder(handle_unknown="ignore"),categorical)
])

def make_model(seed=42):
    return Pipeline([
        ("preprocess",preprocessor),
        ("regressor",RandomForestRegressor(
            n_estimators=300,
            max_depth=14,
            min_samples_leaf=3,
            random_state=seed,
            n_jobs=-1,
        ))
    ])

for target in ["uniformity_percent","defect_rate","cycle_time_min"]:
    m=make_model(); m.fit(history_df[features],history_df[target])
    candidate_df[target]=m.predict(candidate_df[features])

candidate_df["expected_quality_loss"]=(97-candidate_df["uniformity_percent"]).clip(lower=0)*500
candidate_df["expected_defect_cost"]=candidate_df["defect_rate"]*100*200
candidate_df["time_cost"]=candidate_df["cycle_time_min"]*8
candidate_df["experiment_cost"]=150
candidate_df["total_expected_cost"]=(
    candidate_df["expected_quality_loss"]
    +candidate_df["expected_defect_cost"]
    +candidate_df["time_cost"]
    +candidate_df["experiment_cost"]
)
out=candidate_df.sort_values("total_expected_cost").head(25)
print(out.round(2))
out.to_csv(OUTPUT_DIR/"ex298_cost_sensitive_decision.csv",index=False,encoding="utf-8-sig")
