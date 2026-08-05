from common.health_utils import load_data
df=load_data()
print(df.head())
print(df.describe())
print("failure samples:",int(df["failure_label"].sum()))
