import pandas as pd
from common.path_tracking import *
path=load_path("path_sine.csv")
def pp(path,x,y,yaw,speed): return pure_pursuit_control(path,x,y,yaw,speed,.8)
def st(path,x,y,yaw,speed): return stanley_control(path,x,y,yaw,speed,1.2)
rows=[
{"controller":"pure_pursuit",**tracking_metrics(simulate_tracker(path,pp,.6,23))},
{"controller":"stanley",**tracking_metrics(simulate_tracker(path,st,.6,23))}
]
r=pd.DataFrame(rows)
p=output_path("ex333_controller_comparison.csv"); r.to_csv(p,index=False,encoding="utf-8-sig")
print(r)
