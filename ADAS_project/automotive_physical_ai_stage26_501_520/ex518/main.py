import time
from common.tb3_burger_utils import make_extension_scene,set_wheels
import mujoco,mujoco.viewer
scene=make_extension_scene(
    "ex518_sensor_scene.xml",
    extra_sensor='<framepos name="burger_position" objtype="body" objname="base"/><framequat name="burger_orientation" objtype="body" objname="base"/>'
)
model=mujoco.MjModel.from_xml_path(str(scene)); data=mujoco.MjData(model)
next_print=0
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<10:
        set_wheels(data,4,4); mujoco.mj_step(model,data)
        if data.time>=next_print:
            print(data.sensordata.copy()); next_print+=1
        viewer.sync(); time.sleep(model.opt.timestep)
