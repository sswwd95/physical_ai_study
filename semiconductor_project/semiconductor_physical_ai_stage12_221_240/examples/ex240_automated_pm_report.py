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

from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.metrics import classification_report,mean_absolute_error,r2_score
from sklearn.model_selection import GroupShuffleSplit
pm_df=pd.read_csv(DATA_FILE)
features=["cycle","temperature_c","vibration_rms_g","motor_current_a","pressure_deviation","particle_count","health_index"]
X=pm_df[features]; groups=pm_df["equipment_id"]
tr,te=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=42).split(X,pm_df["rul_cycles"],groups))
clf=RandomForestClassifier(n_estimators=300,class_weight="balanced",random_state=42,n_jobs=-1)
clf.fit(X.iloc[tr],pm_df["failure_within_20"].iloc[tr]); cp=clf.predict(X.iloc[te]); cprob=clf.predict_proba(X.iloc[te])[:,1]
reg=RandomForestRegressor(n_estimators=350,random_state=42,n_jobs=-1)
reg.fit(X.iloc[tr],pm_df["rul_cycles"].iloc[tr]); rp=reg.predict(X.iloc[te])
class_metrics=pd.DataFrame(classification_report(pm_df["failure_within_20"].iloc[te],cp,output_dict=True,zero_division=0)).T
reg_metrics=pd.DataFrame([{"mae":mean_absolute_error(pm_df["rul_cycles"].iloc[te],rp),"r2":r2_score(pm_df["rul_cycles"].iloc[te],rp)}])
pred=pm_df.iloc[te][["equipment_id","cycle","health_index","rul_cycles","failure_within_20"]].copy(); pred["predicted_rul"]=rp; pred["failure_probability"]=cprob
latest=pm_df.sort_values("cycle").groupby("equipment_id").tail(1).copy(); latest["priority_score"]=(1-latest["health_index"])*50+(20-latest["rul_cycles"]).clip(lower=0)*2
with pd.ExcelWriter(OUTPUT_DIR/"ex240_predictive_maintenance_report.xlsx",engine="openpyxl") as w:
    class_metrics.to_excel(w,sheet_name="classification_metrics"); reg_metrics.to_excel(w,sheet_name="regression_metrics",index=False); pred.to_excel(w,sheet_name="predictions",index=False); latest.to_excel(w,sheet_name="maintenance_priority",index=False)
print("보고서 저장 완료")
