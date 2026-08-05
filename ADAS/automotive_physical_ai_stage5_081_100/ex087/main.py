from common.sync_utils import load_stream, nearest_merge
wheel = load_stream("wheel_20hz.csv")
gps = load_stream("gps_2hz.csv")
for tol in [0.05,0.15,0.30]:
    m = nearest_merge(wheel, gps, tolerance=tol)
    print("tolerance", tol, "matched", m["gps_speed_mps"].notna().sum(), "/", len(m))
