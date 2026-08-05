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
from sklearn.model_selection import GroupShuffleSplit
pm_df=pd.read_csv(DATA_FILE)
features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]
X=pm_df[features]; y=pm_df["rul_cycles"]; groups=pm_df["equipment_id"]
tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,y,groups))
preds=[]
for seed in range(20):
    m=RandomForestRegressor(n_estimators=120,max_depth=12,min_samples_leaf=3,random_state=seed,n_jobs=-1)
    m.fit(X.iloc[tr],y.iloc[tr]); preds.append(m.predict(X.iloc[te]))
mat=np.vstack(preds)
out=pm_df.iloc[te][["equipment_id","cycle","rul_cycles"]].copy()
out["rul_p05"]=np.quantile(mat,.05,axis=0); out["rul_p50"]=np.quantile(mat,.5,axis=0); out["rul_p95"]=np.quantile(mat,.95,axis=0)
out.to_csv(OUTPUT_DIR/"ex238_rul_intervals.csv",index=False,encoding="utf-8-sig")
print(out.head(10).round(2))
