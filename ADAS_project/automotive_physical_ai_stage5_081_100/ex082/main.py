from common.sync_utils import load_stream
df = load_stream("wheel_20hz.csv")
print("sorted before:", df["timestamp_s"].is_monotonic_increasing)
print("duplicates:", df["timestamp_s"].duplicated().sum())
df = df.drop_duplicates("timestamp_s").sort_values("timestamp_s")
print("sorted after:", df["timestamp_s"].is_monotonic_increasing)
