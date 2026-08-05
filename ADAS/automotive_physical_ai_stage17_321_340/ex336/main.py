import numpy as np,pandas as pd
from common.path_tracking import load_path,path_heading,wrap_angle,output_path
path=load_path("path_sine.csv")
headings=np.array([path_heading(path,i) for i in range(len(path))])
ds=np.sqrt(np.diff(path["x_m"],prepend=path["x_m"].iloc[0])**2+np.diff(path["y_m"],prepend=path["y_m"].iloc[0])**2)
curvature=np.abs(np.array([wrap_angle(headings[i]-headings[max(0,i-1)]) for i in range(len(path))]))/np.maximum(ds,.001)
speed=np.clip(.9/(1+4*curvature),.25,.9)
out=path.copy(); out["curvature"]=curvature; out["speed_limit_mps"]=speed
p=output_path("ex336_curvature_speed_limit.csv"); out.to_csv(p,index=False,encoding="utf-8-sig")
print(out.describe())
