from common.sensor_utils import load_data
df = load_data()
tick_diff = df["encoder_ticks"].diff().fillna(0)
print(tick_diff.describe())
print("zero tick samples:", int((tick_diff == 0).sum()))
