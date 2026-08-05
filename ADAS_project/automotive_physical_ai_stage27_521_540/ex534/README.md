# 예제 534 — DAW 운전자 주의 경고

## 실행
```bat
python ex534\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time,math` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `mj,m,d=load(scene("ex534.xml"))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | ` while v.is_running() and d.time<16:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | `  attention=.5+.5*math.sin(d.time*.5); warning=attention<.4; wheels(d,2,2) if warning else wheels(d,4,4)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | `  print("DAW" if warning else "ATTENTIVE"); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
