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
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report, f1_score, accuracy_score
from sklearn.linear_model import LogisticRegression

sensor_df=pd.read_csv(DATA_FILE)
features=[
"equipment_id","operation_mode","temperature_c","pressure_pa","vibration_rms_g",
"vibration_peak_g","motor_current_a","pump_speed_rpm","gas_flow_sccm",
"particle_count","maintenance_age_hours"]
X=sensor_df[features]; y=(sensor_df["fault_type"]!="normal").astype(int)
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=.25,random_state=42,stratify=y)
num=features[2:]; cat=features[:2]
pre=ColumnTransformer([
    ("num",StandardScaler(),num),
    ("cat",OneHotEncoder(handle_unknown="ignore"),cat)])
model=Pipeline([
    ("preprocess",pre),
    ("classifier",LogisticRegression(max_iter=1500,class_weight="balanced",random_state=42))])
model.fit(X_train,y_train)
pred=model.predict(X_test)
print(classification_report(y_test,pred,zero_division=0))
