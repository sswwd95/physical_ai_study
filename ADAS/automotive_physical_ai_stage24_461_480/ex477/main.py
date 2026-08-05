import time
from common.traffic_utils import load_project,set_ego
mujoco,model,data,plan=load_project()
manual=False
def key(k):
    global manual
    if k in (77,109): manual=not manual
with mujoco.viewer.launch_passive(model,data,key_callback=key) as viewer:
    while viewer.is_running():
        set_ego(data,0,0) if manual else set_ego(data,7,7)
        print("MANUAL" if manual else "AUTO")
        mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
