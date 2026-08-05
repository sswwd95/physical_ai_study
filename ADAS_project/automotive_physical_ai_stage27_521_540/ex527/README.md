# 예제 527 — RCCW 후측방 경고

## 실행
```bat
python ex527\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,math` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `world='<body name="rear" mocap="true" pos="-1.5 -2 .15"><geom type="box" size=".25 .15 .12" rgba=".9 .1 .6 1"/></body>'` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `mj,m,d=load(scene("ex527.xml",world))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | ` while v.is_running() and d.time<14:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | `  d.mocap_pos[0]=[-1.5,-2+.22*d.time,.15]; x,y,yaw=pose(d); r=math.hypot(d.mocap_pos[0][0]-x,d.mocap_pos[0][1]-y)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 8 | `  print("RCCW" if r<1.2 else "CLEAR"); wheels(d,-3,-3); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
