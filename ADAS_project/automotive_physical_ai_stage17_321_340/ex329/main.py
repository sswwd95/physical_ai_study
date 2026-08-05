import pandas as pd
from common.path_tracking import load_path,pure_pursuit_control,simulate_tracker,tracking_metrics,output_path
path=load_path("path_sine.csv"); rows=[]
for ld in [.35,.6,.9,1.3]:
    def controller(path,x,y,yaw,speed,ld=ld):
        return pure_pursuit_control(path,x,y,yaw,speed,lookahead=ld)
    rows.append({"lookahead_m":ld,**tracking_metrics(simulate_tracker(path,controller,.6,23))})
r=pd.DataFrame(rows)
p=output_path("ex329_lookahead_comparison.csv"); r.to_csv(p,index=False,encoding="utf-8-sig")
print(r)
