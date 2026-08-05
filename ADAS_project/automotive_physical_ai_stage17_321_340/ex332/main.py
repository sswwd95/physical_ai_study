import pandas as pd
from common.path_tracking import load_path,stanley_control,simulate_tracker,tracking_metrics,output_path
path=load_path("path_sine.csv"); rows=[]
for gain in [.4,.8,1.2,2.0]:
    def controller(path,x,y,yaw,speed,gain=gain):
        return stanley_control(path,x,y,yaw,speed,gain=gain)
    rows.append({"gain":gain,**tracking_metrics(simulate_tracker(path,controller,.6,23))})
r=pd.DataFrame(rows)
p=output_path("ex332_stanley_gain.csv"); r.to_csv(p,index=False,encoding="utf-8-sig")
print(r)
