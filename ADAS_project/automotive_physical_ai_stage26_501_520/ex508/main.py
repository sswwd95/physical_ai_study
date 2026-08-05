from common.tb3_burger_utils import load_tb3,realtime_loop,set_wheels
mujoco,model,data,ids=load_tb3()
def mission(model,data):
    t=data.time
    if t<4:set_wheels(data,4,4)
    elif t<7:set_wheels(data,-3,3)
    elif t<11:set_wheels(data,4.5,4.5)
    elif t<14:set_wheels(data,3,-3)
    else:set_wheels(data,0,0)
with mujoco.viewer.launch_passive(model,data) as viewer:
    realtime_loop(mujoco,model,data,viewer,16,mission)
