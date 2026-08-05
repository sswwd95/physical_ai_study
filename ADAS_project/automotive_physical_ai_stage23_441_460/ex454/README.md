# 예제 454 — 지오펜스

```bat
python ex454\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `from common.ops import xy,dist` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `b=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"base")` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | ` while v.is_running() and d.time<16:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `  wheels(d,-5,5) if dist(xy(d,b),(2,2))<1.3 else wheels(d,7,8); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
