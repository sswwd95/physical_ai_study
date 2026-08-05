from common.sync_utils import load_stream, out
wheel=load_stream("wheel_20hz.csv")
wheel["measurement"]=(wheel["wheel_left_mps"]+wheel["wheel_right_mps"])/2
x=wheel["measurement"].iloc[0]
p=1.0
q=0.02
r=0.10**2
est=[]
for z in wheel["measurement"]:
    p=p+q
    k=p/(p+r)
    x=x+k*(z-x)
    p=(1-k)*p
    est.append(x)
wheel["kalman_speed_mps"]=est
path=out("ex096_kalman_speed.csv")
wheel.to_csv(path,index=False)
print(wheel[["measurement","kalman_speed_mps"]].head())
