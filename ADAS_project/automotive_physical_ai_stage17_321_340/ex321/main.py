from common.path_tracking import load_path
path = load_path("path_sine.csv")
print(path.head())
print(path.tail())
print("waypoints:", len(path))
