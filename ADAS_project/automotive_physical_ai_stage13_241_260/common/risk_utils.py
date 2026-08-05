from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "bayesian_driving_risk.csv"
OUTPUTS = ROOT / "outputs"
DRAWS = 500
TUNE = 500
CHAINS = 2
CORES = 1
RANDOM_SEED = 42

def load_data():
    return pd.read_csv(DATA_PATH)

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
    summary = az.summary(idata, var_names=var_names, round_to=6)
    path = output_path(filename)
    summary.to_csv(path, encoding="utf-8-sig")
    return summary, path

def classification_metrics(y_true, prob, threshold=0.5):
    y_true=np.asarray(y_true).astype(int)
    pred=(np.asarray(prob)>=threshold).astype(int)
    tp=int(np.sum((y_true==1)&(pred==1)))
    fp=int(np.sum((y_true==0)&(pred==1)))
    tn=int(np.sum((y_true==0)&(pred==0)))
    fn=int(np.sum((y_true==1)&(pred==0)))
    precision=tp/max(1,tp+fp)
    recall=tp/max(1,tp+fn)
    f1=2*precision*recall/max(1e-12,precision+recall)
    return {"threshold":threshold,"tp":tp,"fp":fp,"tn":tn,"fn":fn,
            "precision":precision,"recall":recall,"f1":f1}

def save_json(data, filename):
    path=output_path(filename)
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    return path
