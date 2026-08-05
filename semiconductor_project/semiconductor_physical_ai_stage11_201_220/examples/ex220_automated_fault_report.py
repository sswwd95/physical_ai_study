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

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
sensor_df=pd.read_csv(DATA_FILE,parse_dates=["timestamp"])
features=["equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g","vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm","particle_count","maintenance_age_hours"]
X=sensor_df[features]; y=sensor_df["fault_type"]; idx=np.arange(len(sensor_df)); tr,te=train_test_split(idx,test_size=.25,random_state=42,stratify=y)
pre=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])
m=Pipeline([("preprocess",pre),("classifier",RandomForestClassifier(n_estimators=400,class_weight="balanced",random_state=42,n_jobs=-1))])
m.fit(X.iloc[tr],y.iloc[tr]); pred=m.predict(X.iloc[te]); prob=m.predict_proba(X.iloc[te]); classes=m.classes_
metrics=pd.DataFrame(classification_report(y.iloc[te],pred,output_dict=True,zero_division=0)).T
matrix=pd.DataFrame(confusion_matrix(y.iloc[te],pred,labels=classes),index=[f"actual_{c}" for c in classes],columns=[f"pred_{c}" for c in classes])
pred_df=sensor_df.iloc[te][["timestamp","equipment_id","operation_mode","fault_type"]].copy(); pred_df["predicted_fault"]=pred; pred_df["max_probability"]=prob.max(1); pred_df["review_required"]=pred_df["max_probability"]<.65
names=m.named_steps["preprocess"].get_feature_names_out(); imp=m.named_steps["classifier"].feature_importances_; importance=pd.DataFrame({"feature":names,"importance":imp}).sort_values("importance",ascending=False)
with pd.ExcelWriter(OUTPUT_DIR/"ex220_fault_diagnosis_report.xlsx",engine="openpyxl") as w:
    metrics.to_excel(w,sheet_name="class_metrics"); matrix.to_excel(w,sheet_name="confusion_matrix"); pred_df.to_excel(w,sheet_name="predictions",index=False); importance.to_excel(w,sheet_name="feature_importance",index=False)
print("보고서 저장 완료")
