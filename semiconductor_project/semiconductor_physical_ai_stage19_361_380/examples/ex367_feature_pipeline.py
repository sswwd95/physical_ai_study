from pathlib import Path
import json
import logging
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "operations_stream.csv"
CONFIG_FILE = ROOT / "config" / "app_config.json"
OUTPUT_DIR = ROOT / "outputs"
LOG_DIR = ROOT / "logs"
MODEL_DIR = ROOT / "models"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

ops_df=pd.read_csv(DATA_FILE)
ops_df["thermal_deviation"]=(ops_df["temperature_c"]-72).abs()
ops_df["pressure_deviation"]=(ops_df["pressure_pa"]-18).abs()
ops_df["vibration_risk"]=(ops_df["vibration_rms_g"]-.09).clip(lower=0)
ops_df["particle_risk"]=(ops_df["particle_count"]-8).clip(lower=0)
ops_df["composite_health_score"]=np.exp(
    -(.35*ops_df["thermal_deviation"]+.30*ops_df["pressure_deviation"]+4*ops_df["vibration_risk"]+.05*ops_df["particle_risk"])
)
print(ops_df[["thermal_deviation","pressure_deviation","composite_health_score"]].describe().round(4))
ops_df.to_csv(OUTPUT_DIR/"ex367_feature_pipeline.csv",index=False,encoding="utf-8-sig")
