# 예제 531 — ISA 지능형 속도 보조

## 실행
```bat
python ex531\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `world='<body name="sign" pos="1.5 .9 .5"><geom type="cylinder" size=".25 .04" euler="90 0 0" rgba="1 1 1 1"/></body>'` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `mj,m,d=load(scene("ex531.xml",world))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | ` while v.is_running() and d.time<12:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | `  x,y,yaw=pose(d); limit=3 if x>1 else 5.5; wheels(d,limit,limit); print("LIMIT",limit)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 8 | `  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
