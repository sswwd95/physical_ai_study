from common.path_tracking import load_path,pure_pursuit_control
path=load_path("path_sine.csv")
result=pure_pursuit_control(path,x=0,y=-.7,yaw=0,speed=.6,lookahead=.8)
print("yaw_rate, steering, nearest, target, alpha, curvature")
print(result)
