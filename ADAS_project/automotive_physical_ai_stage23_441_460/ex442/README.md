# 예제 442 — 적재량 변경

```bat
python ex442\main.py
```

| 줄 | 소스 | 설명 |
|---:|---|---|
| 1 | `import time` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 2 | `from common.ops import load,wheels` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 3 | `mj,m,d=load()` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 4 | `pid=mj.mj_name2id(m,mj.mjtObj.mjOBJ_BODY,"payload")` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 5 | `with mj.viewer.launch_passive(m,d) as v:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 6 | ` while v.is_running() and d.time<14:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 7 | `  if d.time>6:` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 8 | `   with v.lock(): m.body_mass[pid]=1.2; mj.mj_setConst(m,d)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
| 9 | `  wheels(d,7,7); mj.mj_step(m,d); v.sync(); time.sleep(m.opt.timestep)` | 디지털 트윈 운영 검증 코드를 실행합니다. |
