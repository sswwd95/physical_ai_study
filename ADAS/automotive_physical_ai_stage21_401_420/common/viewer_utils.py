from pathlib import Path
import time, numpy as np
ROOT=Path(__file__).resolve().parents[1]
MODEL_PATH=ROOT/"models/viewer_car.xml"
OUTPUTS=ROOT/"outputs"
def load():
 import mujoco, mujoco.viewer
 m=mujoco.MjModel.from_xml_path(str(MODEL_PATH)); d=mujoco.MjData(m)
 return mujoco,m,d
def wheels(d,l,r):
 d.ctrl[0]=float(np.clip(l,-20,20)); d.ctrl[1]=float(np.clip(r,-20,20))
def run(mj,m,d,v,duration=10,control=None):
 start=time.time()
 while v.is_running() and time.time()-start<duration:
  tick=time.time()
  if control: control(m,d)
  mj.mj_step(m,d); v.sync()
  time.sleep(max(0,m.opt.timestep-(time.time()-tick)))
def out(name):
 OUTPUTS.mkdir(exist_ok=True); return OUTPUTS/name
