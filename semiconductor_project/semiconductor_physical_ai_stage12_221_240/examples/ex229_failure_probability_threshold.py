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

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupShuffleSplit
from sklearn.metrics import precision_score,recall_score,f1_score
pm_df=pd.read_csv(DATA_FILE)
features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]
X=pm_df[features]; y=pm_df["failure_within_20"]; groups=pm_df["equipment_id"]
tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,y,groups))
m=RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1)
m.fit(X.iloc[tr],y.iloc[tr]); prob=m.predict_proba(X.iloc[te])[:,1]
rows=[]
for t in [.2,.3,.4,.5,.6,.7]:
    p=(prob>=t).astype(int)
    rows.append({"threshold":t,"precision":precision_score(y.iloc[te],p,zero_division=0),"recall":recall_score(y.iloc[te],p,zero_division=0),"f1":f1_score(y.iloc[te],p,zero_division=0)})
out=pd.DataFrame(rows); print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex229_thresholds.csv",index=False,encoding="utf-8-sig")
