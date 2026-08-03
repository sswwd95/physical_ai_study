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

res=(sensor_df["temp_sensor_b_c"]-sensor_df["true_temperature_c"]).to_numpy()
baseline=res[np.isfinite(res)][:200]
mu=baseline.mean(); sigma=baseline.std()
valid=np.isfinite(res)
z=np.zeros(len(res))
z[valid]=np.abs((res[valid]-mu)/(sigma+1e-9))
sensor_df["anomaly_probability"]=1-np.exp(-0.5*z**2)
sensor_df["anomaly_probability"]=sensor_df["anomaly_probability"].clip(0,1)
out=sensor_df[["timestamp","process_phase","anomaly_probability"]]
print(out.sort_values("anomaly_probability",ascending=False).head(15))
out.to_csv(OUTPUT_DIR/"ex335_anomaly_probability_stream.csv",index=False,encoding="utf-8-sig")
