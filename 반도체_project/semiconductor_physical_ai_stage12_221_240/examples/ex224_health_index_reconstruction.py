from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "predictive_maintenance_rul.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/predictive_maintenance_rul.csv 파일이 없습니다."
    )

from sklearn.preprocessing import StandardScaler
pm_df=pd.read_csv(DATA_FILE)
features=["temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count"]
z=StandardScaler().fit_transform(pm_df[features])
risk=z.mean(axis=1)
pm_df["reconstructed_health_index"]=1/(1+np.exp(risk))
print(pm_df[["health_index","reconstructed_health_index"]].corr())
