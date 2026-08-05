# 예제 538 — ADAS 경고 우선순위

## 실행
```bat
python ex538\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `mj,m,d=load(scene("ex538.xml",'<body name="lead" mocap="true" pos="2 0 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .2 .1 1"/></body>'))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | ` while v.is_running() and d.time<12:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | `  x,y,yaw=pose(d); dist=d.mocap_pos[0][0]-x; w=[]` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | `  if dist<.5:w.append(("AEB",3))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 8 | `  if abs(y)>.45:w.append(("LDW",2))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 9 | `  if d.time>9:w.append(("DAW",1))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 10 | `  active=max(w,key=lambda z:z[1])[0] if w else "NORMAL"; print(active); wheels(d,0,0) if active=="AEB" else wheels(d,4,4)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 11 | `  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
