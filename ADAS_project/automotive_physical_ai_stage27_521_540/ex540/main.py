import time,pandas as pd
from common.adas_tb3_utils import *
mj,m,d=load(scene("ex540.xml",'<geom type="box" pos="3 .6 .01" size="8 .025 .01" rgba="1 1 1 1"/><geom type="box" pos="3 -.6 .01" size="8 .025 .01" rgba="1 1 1 1"/><body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body><body name="blind" mocap="true" pos="-.5 .8 .15"><geom type="box" size=".25 .15 .12" rgba="1 .4 .1 1"/></body>')); rows=[]; interventions=0
base=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base")
with mj.viewer.launch_passive(m,d) as v:
 v.cam.type=mj.mjtCamera.mjCAMERA_TRACKING; v.cam.trackbodyid=base; v.cam.distance=2
 while v.is_running() and d.time<18:
  x,y,yaw=pose(d); distance=d.mocap_pos[0][0]-x; dx=d.mocap_pos[1][0]-x; dy=d.mocap_pos[1][1]-y
  blind=(-1.2<dx<.5 and abs(dy)<1); attention=max(0,1-d.time/25); event="NORMAL"; left=right=4
  if distance<.45:event="AEB"; left=right=0
  elif blind:event="BSM"
  elif abs(y)>.45:event="LKA"; c=max(-2,min(2,-2*y-1.1*yaw)); left=4-c; right=4+c
  elif attention<.4:event="DAW"; left=right=2
  if event!="NORMAL":interventions+=1
  wheels(d,left,right); rows.append({"time_s":float(d.time),"x":x,"y":y,"distance":distance,"blind":blind,"attention":attention,"event":event})
  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)
csv=out("ex540_adas_integrated.csv"); pd.DataFrame(rows).to_csv(csv,index=False)
report={"samples":len(rows),"intervention_samples":interventions,"events":pd.Series([r["event"] for r in rows]).value_counts().to_dict()}
js=save_json(report,"ex540_adas_report.json"); print(report,csv,js)
