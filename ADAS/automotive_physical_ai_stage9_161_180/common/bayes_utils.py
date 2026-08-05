from pathlib import Path
import json, numpy as np, pandas as pd
ROOT=Path(__file__).resolve().parents[1]
DATA_PATH=ROOT/"data"/"bayesian_sensor_calibration.csv"
OUTPUTS=ROOT/"outputs"
DRAWS=500; TUNE=500; CHAINS=2; CORES=1; RANDOM_SEED=42
def load_data(): return pd.read_csv(DATA_PATH)
def output_path(name):
    OUTPUTS.mkdir(parents=True,exist_ok=True); return OUTPUTS/name
def sample_model(model):
    import pymc as pm
    with model:
        return pm.sample(draws=DRAWS,tune=TUNE,chains=CHAINS,cores=CORES,
            random_seed=RANDOM_SEED,progressbar=False,target_accept=0.9,
            return_inferencedata=True)
def save_summary(idata,var_names,filename):
    import arviz as az
    s=az.summary(idata,var_names=var_names,round_to=6)
    p=output_path(filename); s.to_csv(p,encoding="utf-8-sig"); return s,p
def posterior_probability(values,threshold,op="gt"):
    arr=np.asarray(values)
    return float(np.mean(arr>threshold)) if op=="gt" else float(np.mean(arr<threshold))
def save_json(data,filename):
    p=output_path(filename); p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8"); return p
