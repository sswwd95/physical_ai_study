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
from sklearn.ensemble import RandomForestClassifier,HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
sensor_df=pd.read_csv(DATA_FILE)
features=["equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g","vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm","particle_count","maintenance_age_hours"]
X=sensor_df[features]; y=sensor_df["fault_type"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
lin=ColumnTransformer([("num",StandardScaler(),features[2:]),("cat",OneHotEncoder(handle_unknown="ignore"),features[:2])])
tree=ColumnTransformer([("num","passthrough",features[2:]),("cat",OneHotEncoder(handle_unknown="ignore",sparse_output=False),features[:2])])
models={"Logistic":Pipeline([("preprocess",lin),("classifier",LogisticRegression(max_iter=2000,class_weight="balanced",random_state=42))]),
"RandomForest":Pipeline([("preprocess",tree),("classifier",RandomForestClassifier(n_estimators=350,class_weight="balanced",random_state=42,n_jobs=-1))]),
"HistGB":Pipeline([("preprocess",tree),("classifier",HistGradientBoostingClassifier(max_iter=200,random_state=42))])}
rows=[]
for name,m in models.items():
    m.fit(Xtr,ytr); p=m.predict(Xte); rows.append({"model":name,"accuracy":accuracy_score(yte,p),"macro_f1":f1_score(yte,p,average="macro")})
out=pd.DataFrame(rows).sort_values("macro_f1",ascending=False); print(out.round(4)); out.to_csv(OUTPUT_DIR/"ex217_model_comparison.csv",index=False,encoding="utf-8-sig")
