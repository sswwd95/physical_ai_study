from common.tb3_burger_utils import load_tb3,realtime_loop,set_wheels
mujoco,model,data,ids=load_tb3()
with mujoco.viewer.launch_passive(model,data) as viewer:
    realtime_loop(mujoco,model,data,viewer,12,lambda m,d:set_wheels(d,4.5,4.5))
