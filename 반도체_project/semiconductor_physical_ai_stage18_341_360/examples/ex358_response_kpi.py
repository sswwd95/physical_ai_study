from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "safety_decision_stream.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_FILE.exists():
    raise FileNotFoundError("data/safety_decision_stream.csv 파일이 없습니다.")

safe_df=pd.read_csv(DATA_FILE)
actual=safe_df["anomaly_type"].ne("normal").to_numpy()
alarm=safe_df["severity_level"].ge(2).to_numpy()
delays=[]
in_event=False
start=None
for i,val in enumerate(actual):
    if val and not in_event:
        in_event=True; start=i
    if in_event and alarm[i]:
        delays.append(i-start); in_event=False
print("사건 수:",int((pd.Series(actual)&~pd.Series(actual).shift(fill_value=False)).sum()))
print("평균 탐지 지연(초):",round(float(np.mean(delays)) if delays else np.nan,3))
print("경보 시점:",int(alarm.sum()))
print("정지 시점:",int((safe_df["severity_level"]>=4).sum()))
