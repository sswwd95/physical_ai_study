from common.path_tracking import load_path,stanley_control,simulate_tracker,tracking_metrics,output_path
path=load_path("path_sine.csv")
def controller(path,x,y,yaw,speed):
    return stanley_control(path,x,y,yaw,speed,gain=1.2)
df=simulate_tracker(path,controller,.6,23)
p=output_path("ex331_stanley.csv"); df.to_csv(p,index=False,encoding="utf-8-sig")
print(tracking_metrics(df)); print(p)
