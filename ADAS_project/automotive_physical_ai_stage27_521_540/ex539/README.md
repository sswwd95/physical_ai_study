# 예제 539 — ADAS 이벤트 로그

## 실행
```bat
python ex539\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,pandas as pd` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `mj,m,d=load(scene("ex539.xml",'<body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body>')); rows=[]` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | ` while v.is_running() and d.time<12:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | `  x,y,yaw=pose(d); dist=d.mocap_pos[0][0]-x; event="AEB" if dist<.5 else "LDW" if abs(y)>.45 else "NONE"; cmd=0 if event=="AEB" else 4` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | `  wheels(d,cmd,cmd); rows.append([d.time,x,y,yaw,dist,event,cmd]); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 8 | `p=out("ex539_adas_events.csv"); pd.DataFrame(rows,columns=["time_s","x","y","yaw","distance","event","cmd"]).to_csv(p,index=False); print(p)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
