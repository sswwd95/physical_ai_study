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

group=experiment_df.groupby(["recipe","pressure_level","rf_level"])["uniformity_percent"].agg(["mean","std","count"]).reset_index()
mu=group["mean"].to_numpy(); se=(group["std"]/np.sqrt(group["count"])).fillna(.2).to_numpy()
draws=np.random.default_rng(42).normal(mu,se,size=(4000,len(group)))
winner=np.argmax(draws,axis=1)
group["p_best"]=np.bincount(winner,minlength=len(group))/len(winner)
out=group.sort_values("p_best",ascending=False)
print(out.head(10).round(4))
out.to_csv(OUTPUT_DIR/"ex274_optimal_condition_probability.csv",index=False,encoding="utf-8-sig")
