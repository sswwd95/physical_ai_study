from common.bayes_slip_utils import load_data
df = load_data()
print(df.head())
print(df.groupby("surface")["slip_ratio"].agg(["count","mean","std"]))
