from common.path_tracking import *
path=load_path("path_circle.csv")
def controller(path,x,y,yaw,speed): return pure_pursuit_control(path,x,y,yaw,speed,.7)
df=simulate_tracker(path,controller,.45,42,x0=3,y0=-.6,yaw0=1.57)
p=output_path("ex335_circle_tracking.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(tracking_metrics(df))
