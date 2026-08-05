from common.safety_utils import load_data
df=load_data()
print(df.head())
print(df[["distance_m","ttc_s","safe_distance_m","risk_label"]].describe())
