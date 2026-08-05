# 예제 537 — 자동주차 조향 보조

## 실행
```bat
python ex537\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `world='<geom type="box" pos="-1.5 .55 .02" size=".8 .03 .02" rgba=".2 .7 1 1"/><geom type="box" pos="-1.5 -.55 .02" size=".8 .03 .02" rgba=".2 .7 1 1"/>'` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `mj,m,d=load(scene("ex537.xml",world))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | ` while v.is_running() and d.time<16:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | `  t=d.time` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 8 | `  if t<4:wheels(d,-3,-3)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 9 | `  elif t<8:wheels(d,-2,-4)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 10 | `  elif t<12:wheels(d,-4,-2)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 11 | `  else:wheels(d,0,0)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 12 | `  mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
