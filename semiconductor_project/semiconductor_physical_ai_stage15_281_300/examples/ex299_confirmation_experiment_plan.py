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

m=make_model()
m.fit(history_df[features],history_df["uniformity_percent"])
candidate_df["predicted_uniformity"]=m.predict(candidate_df[features])
top=candidate_df.sort_values("predicted_uniformity",ascending=False).head(5).copy()
replicated=pd.concat([top.assign(replicate=i+1) for i in range(3)],ignore_index=True)
replicated["random_order"]=np.random.default_rng(42).permutation(np.arange(1,len(replicated)+1))
replicated=replicated.sort_values("random_order")
print(replicated)
replicated.to_csv(OUTPUT_DIR/"ex299_confirmation_plan.csv",index=False,encoding="utf-8-sig")
