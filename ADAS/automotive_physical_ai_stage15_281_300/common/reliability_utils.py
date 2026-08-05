from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
LIFETIME_PATH = ROOT / "data" / "component_lifetime.csv"
RUL_PATH = ROOT / "data" / "rul_snapshots.csv"
OUTPUTS = ROOT / "outputs"

DRAWS = 500
TUNE = 500
CHAINS = 2
CORES = 1
RANDOM_SEED = 42

def load_lifetime():
    return pd.read_csv(LIFETIME_PATH)

def load_rul():
    return pd.read_csv(RUL_PATH)

def output_path(name):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    return OUTPUTS / name

def standardize(series):
    return (series - series.mean()) / series.std()

def sample_model(model):
    import pymc as pm
    with model:
        return pm.sample(
            draws=DRAWS, tune=TUNE, chains=CHAINS, cores=CORES,
            random_seed=RANDOM_SEED, progressbar=False,
            target_accept=0.9, return_inferencedata=True
        )

def save_summary(idata, var_names, filename):
    import arviz as az
    s = az.summary(idata, var_names=var_names, round_to=6)
    p = output_path(filename)
    s.to_csv(p, encoding="utf-8-sig")
    return s, p

def save_json(data, filename):
    p = output_path(filename)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return p
