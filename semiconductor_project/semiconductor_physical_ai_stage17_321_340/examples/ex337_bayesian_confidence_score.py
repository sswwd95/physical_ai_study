from pathlib import Path
import numpy as np
import pandas as pd
import pymc as pm
import arviz as az

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "bayesian_sensor_fusion.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sensor_df = pd.read_csv(DATA_FILE)

fusion=pd.read_csv(OUTPUT_DIR/"ex336_credible_interval_fusion.csv") if (OUTPUT_DIR/"ex336_credible_interval_fusion.csv").exists() else None
if fusion is None:
    raise FileNotFoundError("먼저 실습 336을 실행하세요.")
fusion["hdi_width"]=fusion["hdi_high"]-fusion["hdi_low"]
scale=fusion["hdi_width"].median()
fusion["bayesian_confidence"]=np.exp(-fusion["hdi_width"]/(scale+1e-9))
print(fusion.head(10).round(4))
fusion.to_csv(OUTPUT_DIR/"ex337_bayesian_confidence.csv",index=False,encoding="utf-8-sig")
