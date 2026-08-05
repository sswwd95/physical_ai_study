import time
from common.project_viewer_utils import load_project,set_wheels,body_distance
mujoco,model,data,path=load_project()
base=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"base")
obs=mujoco.mj_name2id(model,mujoco.mjtObj.mjOBJ_BODY,"obstacle_1")
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<16:
        dist=body_distance(data,base,obs)
        speed=8 if dist>2 else 4 if dist>1 else 0
        set_wheels(data,speed,speed)
        mujoco.mj_step(model,data)
        print("distance",round(dist,3),"command",speed)
        viewer.sync(); time.sleep(model.opt.timestep)
