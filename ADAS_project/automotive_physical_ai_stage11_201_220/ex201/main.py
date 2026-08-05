from common.anomaly_utils import load_data
df = load_data()
print(df.head())
print(df["event_label"].value_counts())
print("rows:", len(df))
