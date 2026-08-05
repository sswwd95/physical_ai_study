from common.path_tracking import *
path=load_path("path_lane_change.csv")
def controller(path,x,y,yaw,speed): return pure_pursuit_control(path,x,y,yaw,speed,.9)
df=simulate_tracker(path,controller,.55,24,x0=0,y0=-.5)
p=output_path("ex334_lane_change_tracking.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(tracking_metrics(df))
