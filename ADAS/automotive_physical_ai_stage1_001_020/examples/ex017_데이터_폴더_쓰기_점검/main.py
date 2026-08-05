from pathlib import Path
import pandas as pd

out = Path(__file__).resolve().parents[2] / "data"
out.mkdir(exist_ok=True)
path = out / "environment_test.csv"
df = pd.DataFrame({"time_s": [0.0, 0.1, 0.2], "speed_mps": [0.0, 0.1, 0.2]})
df.to_csv(path, index=False, encoding="utf-8-sig")
print(pd.read_csv(path))
print("saved:", path)
