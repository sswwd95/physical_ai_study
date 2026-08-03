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

pm_df = pd.read_csv(DATA_FILE)
rows=[]
for equipment_id, group in pm_df.groupby("equipment_id"):
    group=group.sort_values("cycle")
    rows.append({
        "equipment_id":equipment_id,
        "temp_slope":np.polyfit(group["cycle"],group["temperature_c"],1)[0],
        "vibration_slope":np.polyfit(group["cycle"],group["vibration_rms_g"],1)[0],
        "current_slope":np.polyfit(group["cycle"],group["motor_current_a"],1)[0],
        "health_slope":np.polyfit(group["cycle"],group["health_index"],1)[0],
    })
out=pd.DataFrame(rows)
print(out.round(6))
out.to_csv(OUTPUT_DIR/"ex222_degradation_trends.csv",index=False,encoding="utf-8-sig")
