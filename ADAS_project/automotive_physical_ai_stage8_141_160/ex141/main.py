from common.sensor_utils import load_data
df = load_data()
print(df.head())
print(df.dtypes)
print("rows:", len(df))
