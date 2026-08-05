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
candidate_df["score"]=m.predict(candidate_df[features])
ranked=candidate_df.sort_values("score",ascending=False)
selected=[]
for _,row in ranked.iterrows():
    if len(selected)>=12:
        break
    if not selected:
        selected.append(row)
        continue
    distance=[
        abs(row["pressure_pa"]-x["pressure_pa"])
        + abs(row["rf_power_w"]-x["rf_power_w"])/20
        + abs(row["gas_flow_sccm"]-x["gas_flow_sccm"])/4
        + (row["recipe"]!=x["recipe"])*1.5
        for x in selected
    ]
    if min(distance)>=1.2:
        selected.append(row)
out=pd.DataFrame(selected)
print(out.round(4))
out.to_csv(OUTPUT_DIR/"ex297_next_batch.csv",index=False,encoding="utf-8-sig")
