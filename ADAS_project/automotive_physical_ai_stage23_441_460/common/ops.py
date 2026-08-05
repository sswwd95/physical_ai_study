from pathlib import Path
import time,math,json
from collections import deque
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parents[1]
MODEL_PATH=ROOT/"models/digital_twin_operations.xml"
OUTPUTS=ROOT/"outputs"
def load():
 import mujoco,mujoco.viewer
 m=mujoco.MjModel.from_xml_path(str(MODEL_PATH)); d=mujoco.MjData(m)
 return mujoco,m,d
def wheels(d,l,r): d.ctrl[0]=float(np.clip(l,-20,20)); d.ctrl[1]=float(np.clip(r,-20,20))
def out(n): OUTPUTS.mkdir(exist_ok=True); return OUTPUTS/n
def xy(d,b): return float(d.xpos[b][0]),float(d.xpos[b][1])
def dist(a,b): return float(math.hypot(a[0]-b[0],a[1]-b[1]))
class Delay:
 def __init__(self,n): self.q=deque([(0,0)]*(n+1),maxlen=n+1)
 def push(self,c): self.q.append(tuple(c)); return self.q[0]
def save(obj,n): p=out(n); p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)); return p
