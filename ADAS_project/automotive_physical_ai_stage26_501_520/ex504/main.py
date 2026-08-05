from common.tb3_burger_utils import load_tb3,realtime_loop
mujoco,model,data,ids=load_tb3()
with mujoco.viewer.launch_passive(model,data) as viewer:
    realtime_loop(mujoco,model,data,viewer,10)
print("simulation time:",data.time)
