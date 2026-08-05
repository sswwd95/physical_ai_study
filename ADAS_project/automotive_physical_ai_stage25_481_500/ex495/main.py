import time
from common.dynamics_utils import load_project,set_all
mujoco,model,data,plan=load_project()
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<14:
        if data.time>6:
            with viewer.lock():
                for gid in range(model.ngeom):
                    if model.geom_type[gid]==mujoco.mjtGeom.mjGEOM_CYLINDER:
                        model.geom_size[gid,0]*=.9995
        set_all(data,9); mujoco.mj_step(model,data); viewer.sync(); time.sleep(model.opt.timestep)
