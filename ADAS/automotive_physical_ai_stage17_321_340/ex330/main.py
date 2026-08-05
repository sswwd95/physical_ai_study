from common.path_tracking import load_path,stanley_control
path=load_path("path_sine.csv")
print(stanley_control(path,x=0,y=-.7,yaw=0,speed=.6,gain=1.2))
