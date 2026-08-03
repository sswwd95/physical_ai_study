from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "equipment_fault_diagnosis.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/equipment_fault_diagnosis.csv 파일이 없습니다."
    )

sensor_df=pd.read_csv(DATA_FILE)
sensor_df["peak_to_rms"]=sensor_df["vibration_peak_g"]/sensor_df["vibration_rms_g"].replace(0,np.nan)
sensor_df["pressure_speed_ratio"]=sensor_df["pressure_pa"]/sensor_df["pump_speed_rpm"]
sensor_df["thermal_load"]=sensor_df["temperature_c"]*sensor_df["motor_current_a"]
sensor_df["particle_per_flow"]=sensor_df["particle_count"]/sensor_df["gas_flow_sccm"]
print(sensor_df[["peak_to_rms","pressure_speed_ratio","thermal_load","particle_per_flow"]].describe().round(4))
sensor_df.to_csv(OUTPUT_DIR/"ex204_engineered_features.csv",index=False,encoding="utf-8-sig")
