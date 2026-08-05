from common.bayes_slip_utils import load_data
df = load_data()
print(df["slip_ratio"].describe())
print("risk ratio:", round(df["risk_label"].mean(), 4))
