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

from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
pm_df=pd.read_csv(DATA_FILE)
features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]
X=pm_df[features]; y=pm_df["rul_cycles"]; groups=pm_df["equipment_id"]
tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,y,groups))
models={"Linear":Pipeline([("scale",StandardScaler()),("regressor",LinearRegression())]),
"RandomForest":RandomForestRegressor(n_estimators=300,random_state=42,n_jobs=-1),
"GradientBoosting":GradientBoostingRegressor(n_estimators=250,learning_rate=.05,random_state=42)}
rows=[]
for name,m in models.items():
    m.fit(X.iloc[tr],y.iloc[tr]); p=m.predict(X.iloc[te])
    rows.append({"model":name,"mae":mean_absolute_error(y.iloc[te],p),"r2":r2_score(y.iloc[te],p)})
out=pd.DataFrame(rows).sort_values("mae"); print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex233_rul_model_comparison.csv",index=False,encoding="utf-8-sig")
