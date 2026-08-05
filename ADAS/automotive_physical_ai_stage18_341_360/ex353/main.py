from common.safety_utils import load_data
df=load_data()
df["avoidance_direction"]=df["obstacle_angle_deg"].map(lambda a:"RIGHT" if a>=0 else "LEFT")
print(df.groupby("avoidance_direction")["distance_m"].agg(["count","mean"]))
