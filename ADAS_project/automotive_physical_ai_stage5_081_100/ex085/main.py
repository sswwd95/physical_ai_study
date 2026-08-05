import numpy as np, pandas as pd
from common.sync_utils import load_stream, out
src = load_stream("range_10hz.csv")
grid = pd.DataFrame({"timestamp_s": np.arange(0,90,0.05)})
grid["front_distance_m"] = np.interp(grid["timestamp_s"], src["timestamp_s"], src["front_distance_m"])
path = out("ex085_range_20hz_interpolated.csv")
grid.to_csv(path,index=False)
print(grid.head())
print("saved:", path)
