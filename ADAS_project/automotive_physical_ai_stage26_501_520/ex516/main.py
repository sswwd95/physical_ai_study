import time
from common.tb3_burger_utils import load_tb3,set_wheels
mujoco,model,data,ids=load_tb3()
command=[0.0,0.0]
def key_callback(keycode):
    if keycode in (ord("W"),ord("w")):command[:]=[4.5,4.5]
    elif keycode in (ord("A"),ord("a")):command[:]=[-3.0,3.0]
    elif keycode in (ord("D"),ord("d")):command[:]=[3.0,-3.0]
    elif keycode in (ord("S"),ord("s")):command[:]=[0.0,0.0]
with mujoco.viewer.launch_passive(model,data,key_callback=key_callback) as viewer:
    while viewer.is_running():
        set_wheels(data,*command)
        mujoco.mj_step(model,data)
        viewer.sync()
        time.sleep(model.opt.timestep)
