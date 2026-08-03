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

models={}
for target in ["uniformity_percent","defect_rate","cycle_time_min"]:
    m=make_model(); m.fit(history_df[features],history_df[target]); models[target]=m
    candidate_df[f"predicted_{target}"]=m.predict(candidate_df[features])

def z(s):
    return (s-s.mean())/s.std()

candidate_df["utility"]=(
    .55*z(candidate_df["predicted_uniformity_percent"])
    -.30*z(candidate_df["predicted_defect_rate"])
    -.15*z(candidate_df["predicted_cycle_time_min"])
)

safe=candidate_df.loc[
    (candidate_df["predicted_defect_rate"]<.04)
    & (candidate_df["predicted_uniformity_percent"]>96)
].copy()

recommendation=safe.sort_values("utility",ascending=False).head(20)
confirmation=pd.concat(
    [recommendation.head(5).assign(replicate=i+1) for i in range(3)],
    ignore_index=True
)
confirmation["random_order"]=np.random.default_rng(42).permutation(np.arange(1,len(confirmation)+1))
feature_importance=[]
for target,m in models.items():
    names=m.named_steps["preprocess"].get_feature_names_out()
    imp=m.named_steps["regressor"].feature_importances_
    feature_importance.extend(
        {"target":target,"feature":name,"importance":value}
        for name,value in zip(names,imp)
    )
importance_df=pd.DataFrame(feature_importance)

with pd.ExcelWriter(OUTPUT_DIR/"ex300_process_optimization_report.xlsx",engine="openpyxl") as w:
    candidate_df.to_excel(w,sheet_name="candidate_predictions",index=False)
    recommendation.to_excel(w,sheet_name="recommendation",index=False)
    confirmation.to_excel(w,sheet_name="confirmation_plan",index=False)
    importance_df.to_excel(w,sheet_name="feature_importance",index=False)

print("보고서 저장 완료")
