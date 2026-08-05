from common.path_tracking import load_path,pure_pursuit_control,simulate_tracker,tracking_metrics,output_path
path=load_path("path_sine.csv")
def controller(path,x,y,yaw,speed):
    return pure_pursuit_control(path,x,y,yaw,speed,lookahead=.8)
df=simulate_tracker(path,controller,speed=.6,duration=23)
p=output_path("ex328_pure_pursuit.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(tracking_metrics(df)); print(p)
