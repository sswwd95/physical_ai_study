from common.project_viewer_utils import load_project,realtime_loop
mujoco,model,data,path=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_SITE]=True
    viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_JOINT]=True
    realtime_loop(mujoco,model,data,viewer,10)
