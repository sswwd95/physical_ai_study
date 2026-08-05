from common.load_data import load_vehicle_log

df = load_vehicle_log()
print(df.head())
print("행/열:", df.shape)
print("열 이름:", list(df.columns))
