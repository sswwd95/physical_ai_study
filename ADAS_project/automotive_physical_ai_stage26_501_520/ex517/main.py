import time
from common.tb3_burger_utils import make_extension_scene,set_wheels
import mujoco,mujoco.viewer
scene=make_extension_scene(
    "ex517_obstacle_scene.xml",
    extra_worldbody='<body name="box_obstacle" pos="1.2 0 .15"><geom type="box" size=".15 .25 .15" rgba=".9 .2 .1 1"/></body>'
)
model=mujoco.MjModel.from_xml_path(str(scene)); data=mujoco.MjData(model)
with mujoco.viewer.launch_passive(model,data) as viewer:
    while viewer.is_running() and data.time<12:
        distance=1.2-float(data.qpos[0])
        set_wheels(data,0,0) if distance<.45 else set_wheels(data,4,4)
        mujoco.mj_step(model,data)
        viewer.sync()
        time.sleep(model.opt.timestep)
