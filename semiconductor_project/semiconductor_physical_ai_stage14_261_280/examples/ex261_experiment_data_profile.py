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

print("데이터 크기:", experiment_df.shape)
print("조건 조합 수:", experiment_df[["recipe","chamber_id","pressure_level","rf_level"]].drop_duplicates().shape[0])
summary = experiment_df.groupby(["recipe","pressure_level","rf_level"])[
    ["uniformity_percent","etch_rate_nm_min","defect_rate"]
].mean()
print(summary.head(15).round(4))
summary.to_csv(OUTPUT_DIR/"ex261_condition_summary.csv",encoding="utf-8-sig")
