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

predictions=[]
for seed in range(15):
    m=make_model(seed)
    m.fit(history_df[features],history_df["uniformity_percent"])
    predictions.append(m.predict(candidate_df[features]))
mat=np.vstack(predictions)
candidate_df["mean_uniformity"]=mat.mean(0)
candidate_df["std_uniformity"]=mat.std(0)
candidate_df["robust_score"]=candidate_df["mean_uniformity"]-1.64*candidate_df["std_uniformity"]
out=candidate_df.sort_values("robust_score",ascending=False).head(25)
print(out.round(4))
out.to_csv(OUTPUT_DIR/"ex290_robust_scores.csv",index=False,encoding="utf-8-sig")
