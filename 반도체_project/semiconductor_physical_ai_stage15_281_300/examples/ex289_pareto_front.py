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

values=candidate_df[["uniformity_percent","defect_rate","cycle_time_min"]].to_numpy()
is_pareto=np.ones(len(values),dtype=bool)
for i,v in enumerate(values):
    dominates=(
        (values[:,0]>=v[0])
        & (values[:,1]<=v[1])
        & (values[:,2]<=v[2])
        & ((values[:,0]>v[0]) | (values[:,1]<v[1]) | (values[:,2]<v[2]))
    )
    if dominates.any():
        is_pareto[i]=False
out=candidate_df.loc[is_pareto].copy()
print("Pareto 후보:",len(out))
out.to_csv(OUTPUT_DIR/"ex289_pareto_front.csv",index=False,encoding="utf-8-sig")
