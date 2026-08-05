import time
from common.dynamics_utils import load_project,set_all
mujoco,model,data,plan=load_project()
left_geoms=[model.geom("left_wheel_geom").id if hasattr(model,"geom") else 0]
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<15:
        if data.time>5:
            with viewer.lock():
                for gid in range(model.ngeom):
                    name=model.geom(gid).name if hasattr(model,"geom") else ""
                    if "left" in name:model.geom_friction[gid,0]=.25
        set_all(data,10); mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
