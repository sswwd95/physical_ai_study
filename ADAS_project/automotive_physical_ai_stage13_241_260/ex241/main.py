from common.risk_utils import load_data
df=load_data()
print(df.head())
print(df["risk_label"].value_counts())
print("risk ratio:",round(df["risk_label"].mean(),4))
