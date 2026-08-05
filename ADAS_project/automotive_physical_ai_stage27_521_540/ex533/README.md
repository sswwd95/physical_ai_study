# 예제 533 — AHB 오토 하이빔

## 실행
```bat
python ex533\main.py
```

## 주의
이 예제의 ADAS 임계값은 교육용이며 실제 차량 안전 인증값이 아닙니다.

## 라인별 해설
| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 2 | `from common.adas_tb3_utils import *` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 3 | `mj,m,d=load(scene("ex533.xml"))` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 4 | `with mj.viewer.launch_passive(m,d) as v:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 5 | ` while v.is_running() and d.time<14:` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 6 | `  ambient=max(.1,1-d.time/14); high=ambient<.35` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 7 | `  with v.lock(): m.light_diffuse[-1]=[1,1,1] if high else [.35,.35,.35]` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
| 8 | `  print("HIGH_BEAM" if high else "LOW_BEAM"); wheels(d,4,4); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | ADAS 상태·거리·경고·개입 또는 Viewer 동기화를 수행합니다. |
