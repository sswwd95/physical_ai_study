from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_process_experiment.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

experiment_df = pd.read_csv(DATA_FILE)

group=experiment_df.groupby(["recipe","pressure_level","rf_level"]).agg(
    uniformity_mean=("uniformity_percent","mean"),
    defect_rate_mean=("defect_rate","mean"),
    etch_rate_mean=("etch_rate_nm_min","mean"),
    n=("lot_id","count")
).reset_index()
group["utility"]=(
    0.5*(group["uniformity_mean"]-group["uniformity_mean"].mean())/group["uniformity_mean"].std()
    -0.35*(group["defect_rate_mean"]-group["defect_rate_mean"].mean())/group["defect_rate_mean"].std()
    +0.15*(group["etch_rate_mean"]-group["etch_rate_mean"].mean())/group["etch_rate_mean"].std()
)
group=group.sort_values("utility",ascending=False)
recipe_summary=experiment_df.groupby("recipe")[["uniformity_percent","defect_rate","etch_rate_nm_min"]].mean()
pairwise=[]
for a in ["ETCH-A","ETCH-B","ETCH-C"]:
    for b in ["ETCH-A","ETCH-B","ETCH-C"]:
        if a<b:
            da=experiment_df.loc[experiment_df["recipe"]==a,"uniformity_percent"].to_numpy()
            db=experiment_df.loc[experiment_df["recipe"]==b,"uniformity_percent"].to_numpy()
            draws_a=np.random.default_rng(42).normal(da.mean(),da.std()/np.sqrt(len(da)),4000)
            draws_b=np.random.default_rng(43).normal(db.mean(),db.std()/np.sqrt(len(db)),4000)
            pairwise.append({"a":a,"b":b,"p_a_better":float((draws_a>draws_b).mean()),"mean_difference":float(draws_a.mean()-draws_b.mean())})
pairwise_df=pd.DataFrame(pairwise)
recommendation=group.head(10).copy()
with pd.ExcelWriter(OUTPUT_DIR/"ex280_bayesian_experiment_report.xlsx",engine="openpyxl") as w:
    recipe_summary.to_excel(w,sheet_name="recipe_summary")
    pairwise_df.to_excel(w,sheet_name="pairwise_probability",index=False)
    group.to_excel(w,sheet_name="condition_utility",index=False)
    recommendation.to_excel(w,sheet_name="recommendation",index=False)
print("보고서 저장 완료")
