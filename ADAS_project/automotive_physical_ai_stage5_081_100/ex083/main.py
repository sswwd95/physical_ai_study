import numpy as np, pandas as pd
from common.sync_utils import out
grid = pd.DataFrame({"timestamp_s": np.arange(0, 90, 0.1)})
path = out("ex083_common_10hz_grid.csv")
grid.to_csv(path, index=False)
print(grid.head())
print("rows:", len(grid), "saved:", path)
