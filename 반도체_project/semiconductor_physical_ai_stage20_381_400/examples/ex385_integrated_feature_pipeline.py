from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "final_project_data.csv"
CONFIG_FILE = ROOT / "config" / "project_config.json"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "models"
REPORT_DIR = ROOT / "reports"
PORTFOLIO_DIR = ROOT / "portfolio"

for directory in [OUTPUT_DIR, MODEL_DIR, REPORT_DIR, PORTFOLIO_DIR]:
    directory.mkdir(exist_ok=True)

data=pd.read_csv(DATA_FILE)
data["thermal_deviation"]=(data["temperature_c"]-72).abs()
data["pressure_deviation"]=(data["pressure_pa"]-18).abs()
data["rf_deviation"]=(data["rf_power_w"]-850).abs()
data["gas_deviation"]=(data["gas_flow_sccm"]-120).abs()
data["vibration_risk"]=(data["vibration_rms_g"]-.09).clip(lower=0)
data["particle_risk"]=(data["particle_count"]-8).clip(lower=0)
data["health_score"]=np.exp(
    -(.30*data["thermal_deviation"]+.25*data["pressure_deviation"]+
      .01*data["rf_deviation"]+.05*data["gas_deviation"]+
      5*data["vibration_risk"]+.04*data["particle_risk"])
)
print(data[["thermal_deviation","pressure_deviation","health_score"]].describe().round(4))
data.to_csv(OUTPUT_DIR/"ex385_integrated_features.csv",index=False,encoding="utf-8-sig")
