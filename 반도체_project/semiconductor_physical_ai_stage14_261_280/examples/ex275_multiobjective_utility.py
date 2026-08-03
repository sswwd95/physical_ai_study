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

group=experiment_df.groupby(["recipe","pressure_level","rf_level"])[
    ["uniformity_percent","defect_rate","etch_rate_nm_min"]
].mean().reset_index()
group["utility"]=(
    0.5*(group["uniformity_percent"]-group["uniformity_percent"].mean())/group["uniformity_percent"].std()
    -0.35*(group["defect_rate"]-group["defect_rate"].mean())/group["defect_rate"].std()
    +0.15*(group["etch_rate_nm_min"]-group["etch_rate_nm_min"].mean())/group["etch_rate_nm_min"].std()
)
out=group.sort_values("utility",ascending=False)
print(out.head(10).round(4))
out.to_csv(OUTPUT_DIR/"ex275_multiobjective_utility.csv",index=False,encoding="utf-8-sig")
