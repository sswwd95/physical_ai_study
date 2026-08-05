from common.tb3_burger_utils import load_tb3,realtime_loop,set_wheels
mujoco,model,data,ids=load_tb3()
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT]=True
    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTFORCE]=True
    realtime_loop(mujoco,model,data,viewer,12,lambda m,d:set_wheels(d,5.0,5.0))
