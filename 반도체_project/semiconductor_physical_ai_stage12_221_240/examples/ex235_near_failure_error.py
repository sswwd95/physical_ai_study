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

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GroupShuffleSplit
pm_df=pd.read_csv(DATA_FILE)
features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]
X=pm_df[features]; y=pm_df["rul_cycles"]; groups=pm_df["equipment_id"]
tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,y,groups))
m=RandomForestRegressor(n_estimators=350,random_state=42,n_jobs=-1); m.fit(X.iloc[tr],y.iloc[tr]); p=m.predict(X.iloc[te])
mask=y.iloc[te]<=20
print("전체 MAE:",round(mean_absolute_error(y.iloc[te],p),4))
print("고장임박 MAE:",round(mean_absolute_error(y.iloc[te][mask],p[mask]),4))
