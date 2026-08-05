from common.load_data import load_vehicle_log

df = load_vehicle_log()
print(df.dtypes)
print("\n수치형 요약:")
print(df.describe().round(3))
print("\n결측값 수:")
print(df.isna().sum())
