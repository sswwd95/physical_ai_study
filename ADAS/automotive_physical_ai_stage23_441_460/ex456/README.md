# 예제 456 — 자동 도킹

```bat
python ex456\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `from common.ops import xy,dist` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base"); dock=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"dock")` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | ` while v.is_running() and d.time<20:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  z=dist(xy(d,b),xy(d,dock)); cmd=7 if z>2 else 3 if z>.6 else 0; wheels(d,cmd,cmd); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
