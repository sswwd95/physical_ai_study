# 예제 540 — ADAS 통합 Viewer

## 실행
```bat
python ex540\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,pandas as pd` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `mj,m,d=load(scene("ex540.xml",'<geom type="box" pos="3 .6 .01" size="8 .025 .01" rgba="1 1 1 1"/><geom type="box" pos="3 -.6 .01" size="8 .025 .01" rgba="1 1 1 1"/><body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body><body name="blind" mocap="true" pos="-.5 .8 .15"><geom type="box" size=".25 .15 .12" rgba="1 .4 .1 1"/></body>')); rows=[]; interventions=0` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `base=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base")` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | ` v.cam.type=mj.mjtCamera.mjCAMERA_TRACKING; v.cam.trackbodyid=base; v.cam.distance=2` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | ` while v.is_running() and d.time<18:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 8 | `  x,y,yaw=pose(d); distance=d.mocap_pos[0][0]-x; dx=d.mocap_pos[1][0]-x; dy=d.mocap_pos[1][1]-y` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 9 | `  blind=(-1.2<dx<.5 and abs(dy)<1); attention=max(0,1-d.time/25); event="NORMAL"; left=right=4` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 10 | `  if distance<.45:event="AEB"; left=right=0` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 11 | `  elif blind:event="BSM"` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 12 | `  elif abs(y)>.45:event="LKA"; c=max(-2,min(2,-2*y-1.1*yaw)); left=4-c; right=4+c` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 13 | `  elif attention<.4:event="DAW"; left=right=2` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 14 | `  if event!="NORMAL":interventions+=1` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 15 | `  wheels(d,left,right); rows.append({"time_s":float(d.time),"x":x,"y":y,"distance":distance,"blind":blind,"attention":attention,"event":event})` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 16 | `  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 17 | `csv=out("ex540_adas_integrated.csv"); pd.DataFrame(rows).to_csv(csv,index=False)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 18 | `report={"samples":len(rows),"intervention_samples":interventions,"events":pd.Series([r["event"] for r in rows]).value_counts().to_dict()}` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 19 | `js=save_json(report,"ex540_adas_report.json"); print(report,csv,js)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
