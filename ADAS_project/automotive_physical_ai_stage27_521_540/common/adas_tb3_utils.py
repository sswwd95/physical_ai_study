from pathlib import Path
import os,time,math,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
OUTPUTS=ROOT/"outputs"
def repo():
 c=[]
 if os.environ.get("ROBOTIS_MENAGERIE_ROOT"): c.append(Path(os.environ["ROBOTIS_MENAGERIE_ROOT"]))
 c += [ROOT/"vendor/robotis_mujoco_menagerie",Path("C:/work/robotis_mujoco_menagerie"),Path.home()/"robotis_mujoco_menagerie"]
 for r in c:
  if (r/"robotis_tb3/turtlebot3_burger.xml").exists(): return r.resolve()
 raise FileNotFoundError("Run scripts/01_clone_robotis_menagerie.bat or set ROBOTIS_MENAGERIE_ROOT")
def burger_model(): return repo()/"robotis_tb3/turtlebot3_burger.xml"
def scene(name,world=""):
 p=ROOT/"extensions"/name
 p.write_text(f"""<mujoco model="{name}">
 <include file="{burger_model().as_posix()}"/>
 <statistic center="1 0 .4" extent="5"/>
 <visual><headlight diffuse=".7 .7 .7" ambient=".25 .25 .25"/><global azimuth="120" elevation="-22"/></visual>
 <asset><texture type="2d" name="road" builtin="checker" rgb1=".12 .12 .12" rgb2=".18 .18 .18" width="512" height="512"/><material name="roadmat" texture="road" texrepeat="16 16"/></asset>
 <worldbody><light pos="0 0 5" dir="0 0 -1"/><geom type="plane" size="20 10 .05" material="roadmat"/>{world}</worldbody>
 </mujoco>""",encoding="utf-8")
 return p
def load(p):
 import mujoco,mujoco.viewer
 m=mujoco.MjModel.from_xml_path(str(p)); d=mujoco.MjData(m)
 return mujoco,m,d
def wheels(d,l,r):
 d.ctrl[0]=float(np.clip(l,-6.67,6.67)); d.ctrl[1]=float(np.clip(r,-6.67,6.67))
def pose(d):
 q=d.qpos[3:7]; qw,qx,qy,qz=q
 yaw=math.atan2(2*(qw*qz+qx*qy),1-2*(qy*qy+qz*qz))
 return float(d.qpos[0]),float(d.qpos[1]),float(yaw)
def out(name):
 OUTPUTS.mkdir(exist_ok=True); return OUTPUTS/name
def save_json(o,name):
 p=out(name); p.write_text(json.dumps(o,ensure_ascii=False,indent=2),encoding="utf-8"); return p
