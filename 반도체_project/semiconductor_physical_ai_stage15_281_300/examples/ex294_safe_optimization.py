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

defect_predictions=[]
uniformity_predictions=[]
for seed in range(20):
    md=make_model(seed); md.fit(history_df[features],history_df["defect_rate"])
    mu=make_model(seed+100); mu.fit(history_df[features],history_df["uniformity_percent"])
    defect_predictions.append(md.predict(candidate_df[features]))
    uniformity_predictions.append(mu.predict(candidate_df[features]))
dmat=np.vstack(defect_predictions); umat=np.vstack(uniformity_predictions)
candidate_df["p_defect_below_004"]=(dmat<.04).mean(0)
candidate_df["uniformity_mean"]=umat.mean(0)
safe=candidate_df.loc[candidate_df["p_defect_below_004"]>=.9]
out=safe.sort_values("uniformity_mean",ascending=False).head(25)
print(out.round(4))
out.to_csv(OUTPUT_DIR/"ex294_safe_optimization.csv",index=False,encoding="utf-8-sig")
